import firebase_admin
from firebase_admin import credentials
from firebase_admin.firestore import client

from src.infra.db.firebase.account import firebase_helper
from src.main.config import create_app

try:
    # Use a service account.
    cred = credentials.Certificate('google_credentials.json')
    firebase_admin.initialize_app(cred)
    firebase_helper.connect(client())
    app = create_app()
except Exception as e:
    print(e)
