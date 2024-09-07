from NotesApplication import NotesApp


class Menu:
    def __init__(self):
        self.notes_app = NotesApp("notes.csv")

    def show(self):
        while True:
            print("Выберите действие:")
            print("1. Добавить новую заметку")
            print("2. Показать все заметки")
            print("3. Заголовок или описание заметки")
            print("4. Удалить заметку")
            print("5. Найти заметку")
            print("6. Выход")
            choice = input("Выберите от 1 до 6): ")
            if choice == "1":
                title = input("Введите название новой заметки: ")
                body = input("Описание: ")
                self.notes_app.add_note(title, body)
            elif choice == "2":
                self.notes_app.show_notes()
            elif choice == "3":
                id_note = input("Введите номер заметки, которую вы хотите изменить: ")
                if self.notes_app.find_note_by_id(id_note):                 
                    title = input("Введите новый заголовок: ")
                    body = input("Введите новое описание: ")
                    self.notes_app.edit_note_by_id(id_note, title, body)
                else: print(f"{id_note} заметка не найдена")
            elif choice == "4":
                id_note = input("Введите номер заметки которую хотите удалить: ")
                self.notes_app.delete_note_by_id(id_note)
            elif choice == "5":
                print("1. Найти заметку по номеру")
                print("2. Найти по заголовку или описанию")
                find_choice = input()
                if find_choice == "1":
                    id_note = input("Номер строки для поиска: ")
                    result = self.notes_app.find_note_by_id(id_note)
                    if result: print(result)
                    else: print("Не найдено")
                elif find_choice == "2":
                    text = input("Введите текст, который хотите найти ")
                    result = self.notes_app.find_note_by_text(text)
                    if result:
                        print(*result, sep="\n")
                    else: print("Ничего не найдено")
                else: print("Неправильный ввод, вы вернулись в главное меню")


            elif choice == "6":
                break
            else:
                print("Неккоректный ввод.")