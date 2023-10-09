import time
import os
import operations


class Professor:
    def __init__(self, menu):
        self.menu = menu
        self.professors_data = {}
        self.professors_data = operations.load_data_from_json(
            "data/professors.json")

        if self.professors_data is None:
            self.professors_data = {}

    def add_professor(self):
        try:
            data_code = int(
                input("Insira o codigo do professor a ser adicionado: "))
        except ValueError:
            print("Insira um ID valido.")
            return

        str_code = str(data_code)

        if str_code in self.professors_data:
            print("Codigo ja atribuido.")
            self.menu.show_options(2)
            return
        else:
            professor_name = input(
                "Insira o nome do professor a ser adicionado: ")
            professor_cpf = input(
                "Insira o CPF do professor a ser adicionado: ")

            new_dictionary = {"codigo": data_code,
                              "nome": professor_name, "cpf": professor_cpf}

            self.professors_data[data_code] = new_dictionary
            operations.save_data_to_json(
                "data/professors.json", self.professors_data)

            self.menu.show_options(2)

    def edit_professor(self):
        try:
            code = int(input("Insira o codigo do professor para ser editado: "))
        except ValueError:
            print("por favor, digite um valor valido.")
            self.menu.show_options(2)
            return

        str_code = str(code)

        if str_code in self.professors_data:
            professor = self.professors_data[str(code)]

            try:
                new_name = input(
                    "Insira o novo nome do professor para ser atualizado: ")
                new_cpf = input(
                    "Insira o novo cpf do professor para ser atualizado: ")
            except TypeError:
                print("insira os valores corretos.")
                self.menu.show_options(2)
                return

            professor["nome"] = new_name
            professor["cpf"] = new_cpf

            operations.save_data_to_json(
                "data/professors.json", self.professors_data)

            print("Dados do professor atualizados!")
            self.menu.show_options(2)
        else:
            print("codigo de professor não encontrado.")
            self.menu.show_options(2)

    def list_professor(self):
        if not self.professors_data:
            print("não há professores cadastrados.")
            self.menu.show_options(2)
        else:
            print(f"professores: {self.professors_data}, \n")
            self.menu.show_options(2)

    def delete_professor(self):
        try:
            code = int(
                input("Insira o codigo do professor para ser removido: "))
        except ValueError:
            print("por favor, digite um valor valido.")
            self.menu.show_options(2)
            return

        if str(code) in self.professors_data:
            professor = self.professors_data.pop(str(code))

            print(f"professor {professor} removido com sucesso.")

            operations.save_data_to_json(
                "data/professors.json", self.professors_data)

            print("Dados do professor atualizados!")
            self.menu.show_options(2)
        else:
            print("codigo de professor não encontrado.")
            self.menu.show_options(2)

    def professor_menu(self):
        while True:

            try:
                sub_option = int(input("Opção: "))
                os.system("cls")

                if sub_option == 6:
                    break

                if sub_option == 1:
                    self.add_professor()
                elif sub_option == 2:
                    self.list_professor()
                elif sub_option == 3:
                    self.edit_professor()
                elif sub_option == 4:
                    self.delete_professor()
                elif sub_option == 5:
                    self.menu.show_options(1)
                    break
                else:
                    print("Opção invalida!")
                    self.menu.show_options(2)

            except ValueError:
                print("Digite uma opção valida")
                time.sleep(3)
                os.system("cls")
                self.menu.show_options(2)
                continue
