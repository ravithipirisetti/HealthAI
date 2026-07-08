import firebase_admin
from firebase_admin import credentials, db

from diseases import DISEASES

cred = credentials.Certificate("healthai-51bd6-firebase-adminsdk-fbsvc-735ef6ec25.json")

firebase_admin.initialize_app(cred, {
    "databaseURL": "https://healthai-51bd6-default-rtdb.asia-southeast1.firebasedatabase.app/"
})

ref = db.reference("diseases")

ref.set(DISEASES)

print(f"✅ Successfully uploaded {len(DISEASES)} diseases to Firebase!")