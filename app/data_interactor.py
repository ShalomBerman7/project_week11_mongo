from pymongo import MongoClient

MONGO_URI = "mongodb://localhost:27017"
DB_NAME = "local"

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db['contact']

class Contact:

    @staticmethod
    def row_to_dict(rows):
        dict_item = {}
        list_of_dict = []
        for row in rows:
            dict_item['id'] = row[0]
            dict_item['first_name'] = row[1]
            dict_item['last_name'] = row[2]
            dict_item['phone_number'] = row[3]
            list_of_dict.append(dict_item)
        return list_of_dict

    @staticmethod
    def get_all_contacts():
        contacts = collection.find({}, {'_id': 0})
        for i in contacts:
            yield i
        return True

    @staticmethod
    def create_contact(first_name, last_name, phone_number):
        new_contact = {'first_name': first_name, 'last_name': last_name, 'phone_number': phone_number}
        collection.insert_one(new_contact)
        return '{massage: created}'


    @staticmethod
    def update_contact(first_name, last_name, phone_number):
        pass

    @staticmethod
    def delete_contact(id):
        pass