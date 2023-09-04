import sys
import os
import lang
from model import PhonebookModel
from view import PhonebookView

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
            self._cmd_show_phonebook()
        if cmd == 'add_record':
            self._cmd_add_record()
        if cmd == 'search_for_record':
            self._cmd_search_for_record()
        if cmd == 'edit_record':
            self._cmd_edit_record()
        if cmd == 'export_to_file':
            self._cmd_export_to_file()
        if cmd == 'import_from_file':
            self._cmd_import_from_file()
    
    def _cmd_show_phonebook(self):
        found_records = self.model.search_for_record('')
        self.view.show_records(found_records, self.lang['record'])

    def _cmd_add_record(self):
        record_data = {}
        for key, val in self.lang['record'].items():
            record_data[key] = self.view.get_user_input(val, self.lang['enter'])
        self.model.add_record(record_data)

    def _cmd_search_for_record(self):
        found_records = self._call_search()
        self.view.show_records(found_records, self.lang['record'], self.lang['search']['found_records'])

    def _cmd_edit_record(self):
        found_record: dict = self._call_search()
        self.view.show_records(found_record, self.lang['record'], self.lang['search']['found_records'])
        record_data = {}
        while len(found_record.keys()) > 1:
            if len(found_record.keys()) > 1:
                self.view.show_message(self.lang['error']['too_many_records'])
                found_record: dict = self._call_search()
                self.view.show_records(found_record, self.lang['record'], self.lang['search']['found_records'])
        for key, value in self.lang['record'].items():
            record_data[key] = self.view.get_user_input(value, self.lang['enter'])
        self.model.edit_records(found_record, record_data)

    def _cmd_export_to_file(self):
        file_name = self.view.get_user_input(self.lang['file']['export'], self.lang['enter'])
        path = os.path.join('.', file_name)
        self.model.export_to_file(path)

    def _cmd_import_from_file(self):
        file_name = self.view.get_user_input(self.lang['file']['import'], self.lang['enter'])
        path = os.path.join('.', file_name)
        self.model.import_from_file(path)

    def _call_search(self):
        request = self.view.get_user_input(self.lang['search']['type_request'])
        found_records = self.model.search_for_record(request)
        return found_records
