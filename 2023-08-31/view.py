class PhonebookView:
    def get_user_choise(self, prompt: dict, preprint: str = '') -> str:
        while True:
            print(preprint)
            for cmd, desc in prompt.items():
                print(cmd, desc)
            user_choise = input(': ')
            if user_choise in prompt.keys():
                return user_choise
    
    def get_user_input(self, text: str, preprint: str = '') -> str:
        return input(f'{preprint} {text}: ')
    
    def show_records(self, records: dict, lang: dict, preprint: str = ''):
        print(preprint)
        for key, value in records.items():
            print(key, ':')
            for sub_key, sub_value in value.items():
                print('\t', lang[sub_key], sub_value)

    def show_message(self, message):
        print(message)
