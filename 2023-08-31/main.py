from model import PhonebookModel
from view import PhonebookView
from controller import PhoneBookController

if __name__ == "__main__":
    model = PhonebookModel()
    view = PhonebookView()
    controller = PhoneBookController(model, view)
    controller.run()
