from datetime import datetime
from firebase import firebase

config = {
  'apiKey': "AIzaSyB6b-lvRKq4LrOXIUF3wuGaL6Hpv0GX1Yo",
  'authDomain': "sekirite-3d2a7.firebaseapp.com",
  'databaseURL': "https://sekirite-3d2a7-default-rtdb.firebaseio.com",
  'projectId': "sekirite-3d2a7",
  'storageBucket': "sekirite-3d2a7.firebasestorage.app",
  'messagingSenderId': "867537729571",
  'appId': "1:867537729571:web:7063340fac31e2ce591996",
  'measurementId': "G-X8N4GP3KMX"
  }

firebase_app = firebase.FirebaseApplication(config['databaseURL'], None)

db = firebase_app

def insert_report(data):
    new_ref = db.post('/reports', {
        'location': data['location'],
        'type': data['type'],
        'message': data.get('message', ''),
        'created_at': datetime.utcnow().isoformat()
    })
    # new_ref is like {'name': '-Mx7...'} — the generated key
    report_id = new_ref.get('name')

    # Fetch inserted data back
    inserted_doc = db.get(f'/reports/{report_id}', None)
    if inserted_doc is None:
        raise Exception("Failed to fetch inserted report")
    inserted_doc['id'] = report_id
    return inserted_doc


def get_all_reports():
    reports = db.get('/reports', None)
    if not reports:
        return []

    reports_list = []
    for key, val in reports.items():
        val['id'] = key
        reports_list.append(val)

    # Sort by created_at descending
    reports_list.sort(key=lambda x: x.get('created_at', ''), reverse=True)
    return reports_list

