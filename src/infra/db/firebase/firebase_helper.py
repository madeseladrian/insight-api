from dataclasses import dataclass
from typing import Any

from firebase_admin.firestore import client


@dataclass
class FirebaseHelper:
    client_firebase: Any = None

    def connect(self, client_firebase: client) -> None:
        self.client_firebase = client_firebase

    def get_collection(self, collection: str) -> Any:
        return self.client_firebase.collection(collection)

    def get_document(self, collection: str) -> Any:
        return self.get_collection(collection).document()

firebase_helper = FirebaseHelper()
