import os
import json
import time

import operations
import enrollment
import classroom
import professor
import subject
import student

class Menu:
    def __init__(self):
        self.students = student.Student(self)
        self.professors = professor.Professor(self)
        self.subjects = subject.Subjects(self)
        self.classRooms = classroom.ClassRoom(self)
        self.enrollments = enrollment.Enrollment(self)

    def show_options(self, option):
        if option == 1:
            print("1 - Estudante, 2 - Disciplina, 3 - Professor, 4 - Turma, - 5 Matricula, 6 - Sair")
        elif option == 2:
            print("1 - Incluir, 2 - Listar, 3 - Atualizar, 4 - Excluir, 5 - Voltar ao menu principal, 6 - Sair")

    def main_menu(self):
        self.show_options(1)

        while True:

            try:
                select_option = int(input("Opção: "))

                os.system("cls")

            except ValueError:
                print("digite uma opção que seja valida")
                time.sleep(1)
                os.system("cls")
                self.show_options(1)
                continue

            self.show_options(2)

            # sub menus options
            if select_option == 1:
                self.students.students_menu()
                
            elif select_option == 2:
                self.subjects.subject_menu()
                
            elif select_option == 3:
                self.professors.professor_menu()
                
            elif select_option == 4:
                self.classRooms.class_menu()
                
            elif select_option == 5:
                self.enrollments.enrollment_menu()

            elif select_option == 6:
                break
            
menu = Menu()

menu.main_menu()