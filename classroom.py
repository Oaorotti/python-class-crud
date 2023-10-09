import os
import time
import operations


class ClassRoom:
    def __init__(self, menu):
        self.menu = menu
        self.class_data = {}
        self.class_data = operations.load_data_from_json("data/classes.json")

        if self.class_data is None:
            self.class_data = {}

    def add_class(self):
        try:
            code = int(input("Insira o codigo da turma a ser adicionada: "))
        except ValueError:
            print("Insira um ID valido.")
            return

        str_code = str(code)

        if str_code in self.class_data:
            print("Codigo já atribuido.")
            self.menu.show_options(2)
            return
        else:
            professor_code = int(
                input("Insira o codigo do professor da turma a ser adicionada: "))
            subject_code = int(
                input("Insira o codigo da disciplina a ser adicionado: "))

            if subject_code in self.class_data or professor_code in self.class_data or subject_code in self.class_data:
                print(
                    "Insira um codigo de disciplina / professor que ainda não tenha sido adicionado.")
                self.menu.show_options(2)
                return

            new_dictionary = {"codigo_turma": code,
                              "codigo_professor": professor_code, "codigo_disciplina": subject_code}

            self.class_data[code] = new_dictionary

            operations.save_data_to_json("data/classes.json", self.class_data)
            self.menu.show_options(2)

    def list_class(self):
        if not self.class_data:
            print("não há turmas cadastradas.")
            self.menu.show_options(2)
        else:
            print(f"turmas: {self.class_data}, \n")
            self.menu.show_options(2)

    def delete_class(self):
        try:
            code = int(input("Insira o codigo da turma para ser removida: "))
        except ValueError:
            print("por favor, digite um valor valido.")
            self.menu.show_options(2)
            return

        str_code = str(code)

        if str_code in self.class_data:
            classRoom = self.class_data.pop(str(code))

            print(f"turma {classRoom} removido com sucesso.")

            operations.save_data_to_json("data/classes.json", self.class_data)

            print("Dados da turma atualizados!")
            self.menu.show_options(2)
        else:
            print("codigo de turma não encontrado.")
            self.menu.show_options(2)

    def edit_class(self):
        try:
            code = int(input("Insira o codigo da turma a ser editada: "))
        except ValueError:
            print("por favor, digite um valor valido.")
            self.menu.show_options(2)
            return

        str_code = str(code)

        if str_code in self.class_data:
            classRoom = self.class_data[str(code)]

            try:
                class_code = int(
                    input("Insira o novo codigo da turma para ser atualizado: "))
                professor_code = int(
                    input("Insira o novo codigo de professor para ser atualizado: "))
                subject_code = int(
                    input("Insira o novo codigo de disciplina ser atualizado: "))
            except TypeError:
                print("insira os valores corretos.")
                self.menu.show_options(2)
                return

            classRoom["codigo_turma"] = class_code
            classRoom["codigo_professor"] = professor_code
            classRoom["codigo_disciplina"] = subject_code

            operations.save_data_to_json("data/classes.json", self.class_data)

            print("Dados da turma atualizados!")
            self.menu.show_options(2)
        else:
            print("codigo de turma não encontrado.")
            self.menu.show_options(2)

    def class_menu(self):
        while True:

            try:
                sub_option = int(input("Opção: "))
                os.system("cls")

                if sub_option == 6:
                    break

                if sub_option == 1:
                    self.add_class()
                elif sub_option == 2:
                    self.list_class()
                elif sub_option == 3:
                    self.edit_class()
                elif sub_option == 4:
                    self.delete_class()
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
