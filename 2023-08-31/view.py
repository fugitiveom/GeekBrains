class PhonebookView:
    def get_user_choise(self, prompt: dict, preprint: str = ''):
        while True:
            print(preprint)
            for cmd, desc in prompt.items():
                print(cmd, desc)
            user_choise = input(': ')
            if user_choise in prompt.keys():
                return user_choise
    
    def get_user_input(self, text: str, preprint: str = ''):
        return input(f'{preprint} {text}: ')
    
    def show_records(self, records: dict):
        pass
