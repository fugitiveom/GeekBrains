class PhonebookModel:
    def __init__(self):
        self.contacts = {}

    def show_phonebook(self, lang: dict):
        for key, value in self.contacts.items():
            print(key, ':')
            for key, value in value.items():
                print('\t', lang[key], value)

    def add_record(self, user_data: dict):
        data = {}
        data[f"{user_data['name']} {user_data['surname']}"] = user_data
        self.contacts.update(data)

    def remove_record(self, name_surname: str):
        pass

    def search_for_record(self, request: str, lang: dict):
        found = {}
        for key, value in self.contacts.items():
            if request in key:
                print(key, ':')
                found.update(f'{key}: {value}')
                for key, value in value.items():
                    print('\t', lang[key], value)
        return found

    def edit_record(self):
        print('Working edit record')