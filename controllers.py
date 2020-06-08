import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


cred = credentials.Certificate('key.json')
firebase_admin.initialize_app(cred)

db = firestore.client()


def get_manga():
    doc_ref = db.collection(u'mangas').document(u'Life So Happy')
    doc = doc_ref.get()
    if doc.exists:
        return doc.to_dict()
