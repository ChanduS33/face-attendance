import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendancesystem-dd4b6-default-rtdb.asia-southeast1.firebasedatabase.app/"
})

ref = db.reference('Students')

data = {
    "1207":
        {
            "Name": "Dhoni",
            "Branch": "Civil",
            "total_attendance": 12,
            "last_attendance_time": "2024-5-11 00:54:34"
        },
    "1209":
        {
            "Name": "Koushik",
            "Branch": "MECH",
            "total_attendance": 12,
            "last_attendance_time": "2024-5-11 00:54:34"
        },
    "1268":
        {
            "Name": "Abel",
            "Branch": "MECH",
            "total_attendance": 12,
            "last_attendance_time": "2024-5-11 00:54:34"
        },
    "1271":
        {
            "Name": "Ruchita",
            "Branch": "IT",
            "total_attendance": 12,
            "last_attendance_time": "2024-5-11 00:54:34"
        },
    "1278":
        {
            "Name": "Keerthi",
            "Branch": "CSE",
            "total_attendance": 7,
            "last_attendance_time": "2024-5-11 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)
