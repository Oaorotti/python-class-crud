import os
import time
import operations


class Student:
    def __init__(self, menu):
        self.menu = menu
        self.students_data = {}
        self.students_data = operations.load_data_from_json(
            "data/students.json")

        if self.students_data is None:
            self.students_data = {}

    def add_student(self):
        try:
            data_code = input(
                "Insira o codigo do estudante a ser adicionado: ")
        except ValueError:
            print("Insira um ID valido.")
            return

        str_code = str(data_code)

        if str_code in self.students_data:
            print("Codigo ja atribuido.")
            self.menu.show_options(2)
            return
        else:
            student_name = input(
                "Insira o nome do estudante a ser adicionado: ")
            student_cpf = input("Insira o CPF do estudante a ser adicionado: ")

            new_dictionary = {"codigo": int(data_code),
                              "nome": student_name, "cpf": student_cpf}

            self.students_data[data_code] = new_dictionary
            operations.save_data_to_json(
                "data/students.json", self.students_data)

            self.menu.show_options(2)

    def edit_student(self):
        try:
            code = int(input("Insira o codigo do estudante para ser editado: "))
        except ValueError:
            print("por favor, digite um valor valido.")
            self.menu.show_options(2)
            return

        str_code = str(code)

        if str_code in self.students_data:
            student = self.students_data[str(code)]

            try:
                new_name = input(
                    "Insira o novo nome do estudante para ser atualizado: ")
                new_cpf = input(
                    "Insira o novo cpf do estudante para ser atualizado: ")
            except TypeError:
                print("insira os valores corretos.")
                self.menu.show_options(2)
                return

            student["nome"] = new_name
            student["cpf"] = new_cpf

            operations.save_data_to_json(
                "data/students.json", self.students_data)

            print("Dados do estudante atualizados!")
            self.menu.show_options(2)
        else:
            print("codigo de estudante não encontrado.")
            self.menu.show_options(2)

    def list_student(self):
        if not self.students_data:
            print("não há estudantes cadastrados.")
            self.menu.show_options(2)
        else:
            print(f"Estudantes: {self.students_data}, \n")
            self.menu.show_options(2)

    def delete_student(self):
        try:
            code = int(
                input("Insira o codigo do estudante para ser removido: "))
        except ValueError:
            print("por favor, digite um valor valido.")
            self.menu.show_options(2)
            return

        str_code = str(code)

        if str_code in self.students_data:
            student = self.students_data.pop(str(code))

            print(f"Estudante {student} removido com sucesso.")

            operations.save_data_to_json(
                "data/students.json", self.students_data)

            print("Dados do estudante atualizados!")
            self.menu.show_options(2)
        else:
            print("codigo de estudante não encontrado.")
            self.menu.show_options(2)

    def students_menu(self):
        while True:

            try:
                sub_option = int(input("Opção: "))
                os.system("cls")

                if sub_option == 6:
                    break

                if sub_option == 1:
                    self.add_student()
                elif sub_option == 2:
                    self.list_student()
                elif sub_option == 3:
                    self.edit_student()
                elif sub_option == 4:
                    self.delete_student()
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
