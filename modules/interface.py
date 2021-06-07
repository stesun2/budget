from modules.budget import Budget

class Interface:
    def run(self):
        while True:
            self.print_menu():
            option = int(input("Select Option: "))
            if option == '1':
                