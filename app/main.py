from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from data_interactor import Contact

app = FastAPI()


class Items(BaseModel):
    first_name: str
    last_name: str
    phone_number: str


@app.get("/contacts")
def get_contacts():
    try:
        contacts = Contact.get_all_contacts()
        return contacts
    except:
        return "get error"


@app.post("/contacts")
def create_contact(contacts: Items):
    try:
        contact = Contact.create_contact(contacts.first_name, contacts.last_name, contacts.phone_number)
        return contact
    except:
        return "post error"


@app.put("/contacts/{id}")
def update_contact(contacts: Items):
    try:
        contact = Contact.update_contact(contacts.first_name, contacts.last_name, contacts.phone_number)
        return contact
    except:
        return "put error"


@app.delete("/contacts/{id}")
def delete_contact(id):
    try:
        contact = Contact.delete_contact(id)
        return contact
    except:
        return "delete error"


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
