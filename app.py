from flask import Flask, render_template, request
import firebase_admin
from firebase_admin import credentials, db

app = Flask(__name__)

cred = credentials.Certificate("healthai-51bd6-firebase-adminsdk-fbsvc-735ef6ec25.json")

firebase_admin.initialize_app(cred, {
    "databaseURL": "https://healthai-51bd6-default-rtdb.asia-southeast1.firebasedatabase.app/"
})

ref = db.reference("diseases")
DISEASES = ref.get()


@app.route("/", methods=["GET", "POST"])
def home():
    symptoms = sorted({s for d in DISEASES for s in d["symptoms"]})

    if request.method == "POST":
        selected = request.form.getlist("symptoms")

        name = request.form["name"]
        age = request.form["age"]
        gender = request.form["gender"]

        results = []

        for d in DISEASES:
            matched = len(set(selected) & set(d["symptoms"]))

            if matched > 0:
                coverage = matched / len(d["symptoms"])
                precision = matched / len(selected) if selected else 0

                score = int(((coverage + precision) / 2) * 100)

                results.append({
                    "name": d["name"],
                    "score": score
                })

        results.sort(key=lambda x: x["score"], reverse=True)

        history_ref = db.reference("patient_history")

        history_ref.child(name).push({
            "age": age,
            "gender": gender,
            "symptoms": selected,
            "result": results[0]["name"] if results else "Unknown"
        })

        return render_template("results.html", results=results)

    return render_template("index.html", symptoms=symptoms)


@app.route("/disease/<name>")
def disease(name):
    for d in DISEASES:
        if d["name"] == name:
            return render_template("disease.html", disease=d)

    return "Disease not found"


@app.route("/prevention/<name>")
def prevention(name):
    for d in DISEASES:
        if d["name"] == name:
            return render_template("prevention.html", disease=d)

    return "Disease not found"


@app.route("/redflags/<name>")
def redflags(name):
    for d in DISEASES:
        if d["name"] == name:
            return render_template("redflags.html", disease=d)

    return "Disease not found"


if __name__ == "__main__":
    app.run(debug=True)