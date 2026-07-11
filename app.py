from flask import Flask, render_template, request
import firebase_admin
from firebase_admin import credentials, db
from flask import send_file
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet 

app = Flask(__name__)

import os
import json

if "FIREBASE_CREDENTIALS" in os.environ:
    # Running on Render
    cred_dict = json.loads(os.environ["FIREBASE_CREDENTIALS"])
    cred = credentials.Certificate(cred_dict)
else:
    # Running locally
    cred = credentials.Certificate("healthai-51bd6-firebase-adminsdk-fbsvc-735ef6ec25.json")

firebase_admin.initialize_app(cred, {
    "databaseURL": "https://healthai-51bd6-default-rtdb.asia-southeast1.firebasedatabase.app/"
}) 

ref = db.reference("diseases")
DISEASES = ref.get()

latest_report = {} 

@app.route("/", methods=["GET", "POST"])
def home():
    symptoms = sorted({s for d in DISEASES for s in d["symptoms"]})

    if request.method == "POST":

        selected = request.form.getlist("symptoms")
        emergency_symptoms = [
    "chest pain",
    "shortness of breath",
    "coughing blood",
    "unconsciousness",
    "seizure"
]

        emergency = any(symptom in selected for symptom in emergency_symptoms) 
        duration = request.form.get("duration")
        conditions = request.form.getlist("condition")
        severity = request.form.get("severity")

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

                # Improve prediction
                if duration == "more_3_days":
                    score += 5
                elif duration == "more_week":
                    score += 10

                if severity == "moderate":
                    score += 5
                elif severity == "severe":
                    score += 10

                if "elderly" in conditions:
                    score += 5

                if "pregnant" in conditions:
                    score += 5

                score = min(score, 100)

                results.append({
                    "name": d["name"],
                    "score": score
                })

                results.sort(key=lambda x: x["score"], reverse=True)

        global latest_report

        latest_report = {
            "name": name,
            "age": age,
            "gender": gender,
            "symptoms": selected,
            "results": results[:3],
            "emergency": emergency
        } 
        

        history_ref = db.reference("patient_history")

        history_ref.child(name).push({
            "age": age,
            "gender": gender,
            "symptoms": selected,
            "duration": duration,
            "conditions": conditions,
            "severity": severity,
            "result": results[0]["name"] if results else "Unknown"
        })

        return render_template(
            "results.html",
            results=results,
            emergency=emergency
        ) 
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

@app.route("/download-report")
def download_report():

    pdf = SimpleDocTemplate("HealthAI_Report.pdf")
    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph("<b>HealthAI</b>", styles["Title"]))
    story.append(Paragraph("AI Disease Prediction Report", styles["Heading2"]))
    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph("<b>Patient Information</b>", styles["Heading2"]))
    story.append(Paragraph(f"Name: {latest_report['name']}", styles["Normal"]))
    story.append(Paragraph(f"Age: {latest_report['age']}", styles["Normal"]))
    story.append(Paragraph(f"Gender: {latest_report['gender']}", styles["Normal"]))
    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph("<b>Symptoms Selected</b>", styles["Heading2"]))

    for symptom in latest_report["symptoms"]:
        story.append(Paragraph(f"• {symptom}", styles["Normal"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph("<b>Top 3 Predictions</b>", styles["Heading2"]))

    for result in latest_report["results"]:
        story.append(
            Paragraph(
                f"{result['name']} - {result['score']}%",
                styles["Normal"]
            )
        )

    story.append(Paragraph("<br/>", styles["Normal"]))

    if latest_report["emergency"]:
        story.append(
            Paragraph(
                "<font color='red'><b>EMERGENCY WARNING</b></font>",
                styles["Heading2"]
            )
        )
        story.append(
            Paragraph(
                "Seek immediate medical attention.",
                styles["Normal"]
            )
        )

    story.append(Paragraph("<br/>", styles["Normal"]))
    story.append(
        Paragraph(
            "This report is generated for educational purposes only.",
            styles["Italic"]
        )
    )

    pdf.build(story)

    return send_file(
        "HealthAI_Report.pdf",
        as_attachment=True
    )

if __name__ == "__main__":
    app.run(debug=True)