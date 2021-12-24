from os import environ
from unittest.mock import Mock

import google.auth.credentials
from google.cloud import firestore

def get_db() -> firestore.Client:
    if environ.get("FIRESTORE_EMULATOR_HOST"):
        print("Connecting to emulator")
        return firestore.Client(
            project="proj",
            credentials=Mock(spec=google.auth.credentials.Credentials),
        )
    else:
        print("Connecting to live environment")
        return firestore.Client()


db = get_db()

# Add a new document
print("Creating document")
doc_ref = db.collection(u'users').document(u'devops')
doc_ref.set({  # Crash
    u'first': u'one',
    u'last': u'two',
    u'born': 2021
})

# Then query for documents
print("Reading documents")
users_ref = db.collection(u'users')

for doc in users_ref.stream():
    print(u'{} => {}'.format(doc.id, doc.to_dict()))

col = db.collection(u'test')
for doc in col.stream():
     print(u'{} => {}'.format(doc.id, doc.to_dict()))
