from dataclasses import dataclass
from typing import Any
import uuid

from firebase_admin.firestore import client


@dataclass
class FirebaseHelper:
    client_firebase: Any = None

    def connect(self, client_firebase: client) -> None:
        self.client_firebase = client_firebase

    def get_collection(self) -> Any:
        return self.client_firebase.collection('users')

    def get_document(self) -> Any:
        return self.get_collection().document(str(uuid.uuid4()))

firebase_helper = FirebaseHelper()
