import os
import time
import operations


class Subjects:
    def __init__(self, menu):
        self.menu = menu
        self.subjects_data = {}
        self.subjects_data = operations.load_data_from_json(
            "data/subjects.json")

        if self.subjects_data is None:
            self.subjects_data = {}

    def add_subject(self):
        try:
            code = int(
                input("Insira o codigo da disciplina a ser adicionada: "))
        except ValueError:
            print("Insira um ID valido.")
            return

        str_code = str(code)

        if str_code in self.subjects_data:
            print("Codigo já atribuido.")
            self.menu.show_options(2)
            return
        else:
            subject_name = input(
                "Insira o nome da disciplina a ser adicionada: ")

            new_dictionary = {"codigo": code,
                              "nome": subject_name}

            self.subjects_data[code] = new_dictionary

            operations.save_data_to_json(
                "data/subjects.json", self.subjects_data)
            self.menu.show_options(2)

    def edit_subject(self):
        try:
            code = int(input("Insira o codigo da disciplina a ser editada: "))
        except ValueError:
            print("por favor, digite um valor valido.")
            self.menu.show_options(2)
            return

        str_code = str(code)

        if str_code in self.subjects_data:
            subject = self.subjects_data[str_code]

            try:
                new_name = input(
                    "Insira o novo nome da disciplina para ser atualizado: ")
            except TypeError:
                print("insira os valores corretos.")
                self.menu.show_options(2)
                return

            subject["nome"] = new_name

            operations.save_data_to_json(
                "data/subjects.json", self.subjects_data)

            print("Dados da disciplina atualizados!")
            self.menu.show_options(2)
        else:
            print("codigo de disciplina não encontrado.")
            self.menu.show_options(2)

    def list_subject(self):
        if not self.subjects_data:
            print("não há disciplinas cadastradas.")
            self.menu.show_options(2)
        else:
            print(f"disciplinas: {self.subjects_data}, \n")
            self.menu.show_options(2)

    def delete_subject(self):
        try:
            code = int(
                input("Insira o codigo da disciplina para ser removida: "))
        except ValueError:
            print("por favor, digite um valor valido.")
            self.menu.show_options(2)
            return

        str_code = str(code)

        if str_code in self.subjects_data:
            subject = self.subjects_data.pop(str(code))

            print(f"disciplina {subject} removido com sucesso.")

            operations.save_data_to_json(
                "data/subjects.json", self.subjects_data)

            print("Dados da disciplina atualizados!")
            self.menu.show_options(2)
        else:
            print("codigo de disciplina não encontrado.")
            self.menu.show_options(2)

    def subject_menu(self):
        while True:

            try:
                sub_option = int(input("Opção: "))
                os.system("cls")

                if sub_option == 6:
                    break

                if sub_option == 1:
                    self.add_subject()
                elif sub_option == 2:
                    self.list_subject()
                elif sub_option == 3:
                    self.edit_subject()
                elif sub_option == 4:
                    self.delete_subject()
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
