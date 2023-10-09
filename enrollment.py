import json
import os
import time

import operations


class Enrollment:
    def __init__(self, menu):
        self.menu = menu
        self.enrollment_data = {}
        self.enrollment_data = operations.load_data_from_json(
            "data/enrollments.json")

        if self.enrollment_data is None:
            self.enrollment_data = {}

    def add_enrollment(self):
        try:
            code = int(input("Insira o codigo da turma a ser adicionada: "))
        except ValueError:
            print("Insira um ID valido.")
            return

        str_code = str(code)

        if str_code in self.enrollment_data:
            print("Codigo já atribuido.")
            self.menu.show_options(2)
            return
        else:
            class_code = int(
                input("Insira o codigo da turma a ser adicionada: "))
            student_code = int(
                input("Insira o codigo de estudante a ser adicionado: "))

            if class_code in self.enrollment_data or student_code in self.enrollment_data:
                print(
                    "Insira um codigo de turma / estudante que ainda não tenha sido adicionado.")
                self.menu.show_options(2)
                return

            new_dictionary = {"codigo_turma": code,
                              "codigo_estudante": student_code}

            self.enrollment_data[code] = new_dictionary

            operations.save_data_to_json(
                "data/enrollments.json", self.enrollment_data)
            self.menu.show_options(2)

    def list_enrollment(self):
        if not self.enrollment_data:
            print("não há turmas cadastradas.")
            self.menu.show_options(2)
        else:
            print(f"turmas: {self.enrollment_data}, \n")
            self.menu.show_options(2)

    def delete_enrollment(self):
        try:
            code = int(
                input("Insira o codigo da matricula para ser removida: "))
        except ValueError:
            print("por favor, digite um valor valido.")
            self.menu.show_options(2)
            return

        str_code = str(code)

        if str_code in self.enrollment_data:
            classRoom = self.enrollment_data.pop(str(code))

            print(f"matricula {classRoom} removido com sucesso.")

            operations.save_data_to_json(
                "data/enrollments.json", self.enrollment_data)

            print("Dados da matricula atualizados!")
            self.menu.show_options(2)
        else:
            print("codigo de matricula não encontrado.")
            self.menu.show_options(2)

    def edit_enrollment(self):
        try:
            code = int(input("Insira o codigo da matricula a ser editada: "))
        except ValueError:
            print("por favor, digite um valor valido.")
            self.menu.show_options(2)
            return

        str_code = str(code)

        if str_code in self.enrollment_data:
            classRoom = self.enrollment_data[str(code)]

            try:
                class_code = int(
                    input("Insira o novo codigo da turma para ser atualizado: "))
                student_code = int(
                    input("Insira o novo codigo de aluno para ser atualizado: "))
            except TypeError:
                print("insira os valores corretos.")
                self.menu.show_options(2)
                return

            classRoom["codigo_turma"] = class_code
            classRoom["codigo_estudante"] = student_code

            operations.save_data_to_json(
                "data/enrollments.json", self.enrollment_data)

            print("Dados da matricula atualizados!")
            self.menu.show_options(2)
        else:
            print("codigo de matricula não encontrado.")
            self.menu.show_options(2)

    def enrollment_menu(self):
        while True:

            try:
                sub_option = int(input("Opção: "))
                os.system("cls")

                if sub_option == 6:
                    break

                if sub_option == 1:
                    self.add_enrollment()
                elif sub_option == 2:
                    self.list_enrollment()
                elif sub_option == 3:
                    self.edit_enrollment()
                elif sub_option == 4:
                    self.delete_enrollment()
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
