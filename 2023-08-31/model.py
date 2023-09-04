import json

class PhonebookModel:
    def __init__(self):
        self.contacts = {}

    def add_record(self, user_data: dict):
        data = {}
        data[f"{user_data['name']} {user_data['surname']}"] = user_data
        self.contacts.update(data)

    def remove_record(self, name_surname: str):
        pass

    def search_for_record(self, request: str) -> dict:
        found = {}
        for key, value in self.contacts.items():
            if request in key:
                found[key] = value
        return found

    def edit_records(self, record: dict, new_data: dict):
        for key, value in record.items():
            for sub_key, _ in value.items():
                if new_data[sub_key] != '':
                    record[key][sub_key] = new_data[sub_key]
    
    def export_to_file(self, path):
        with open(path, 'w') as file:
            json.dump(self.contacts, file, indent=4)

    def import_from_file(self, path):
        with open(path, 'r') as file:
            self.contacts = json.load(file)