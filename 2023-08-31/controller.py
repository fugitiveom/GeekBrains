import lang
from model import PhonebookModel
from view import PhonebookView
import sys

class PhoneBookController:
    def __init__(self, model: PhonebookModel, view: PhonebookView) -> None:
        self.model = model
        self.view = view
        self.lang = lang.ru
    
    def run(self):
        while True:
            user_choice = self.view.get_user_choise(self.lang['main_menu'], self.lang['enter'])
            self.handle_user_input(user_choice)
    
    def handle_user_input(self, cmd):
        if cmd == 'exit':
            sys.exit()
        if cmd == 'show_phonebook':
            self.model.show_phonebook(self.lang['record'])
        if cmd == 'add_record':
            record_data = {}
            for key, val in self.lang['record'].items():
                record_data[key] = self.view.get_user_input(val, self.lang['enter'])
            self.model.add_record(record_data)
        if cmd == 'search_for_record':
            request = self.view.get_user_input(self.lang['search'])
            self.model.search_for_record(request, self.lang['record'])
