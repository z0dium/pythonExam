import NotesManager
from datetime import datetime
from uuid import uuid4
import os

class View:
    def __init__(self):
        self.notesManager = NotesManager.NotesManager()
           
    def printNote(self,note):
        print("------------------------------------------------------------------------------------")
    
        print(note.header, " : ", note.lastModified.strftime("%m/%d/%Y, %H:%M:%S"), " id - ", f'{note.id}')
        print(note.body) 
        print("------------------------------------------------------------------------------------")

    def mainMenu(self):
        print("Пункты меню:")
        print("1. Загрузить заметки из файла (отменит все несохраненные изменения)")
        print("2. Показать все заметки")
        print("3. Добавить новую заметку")
        print("4. Показать/редактировать заметку по id:")
        print("5. Сохранить изменения в файл")
        print("6. Выйти")
        print()
        num = 0
        while num < 1 or num > 6:
            option = input("Введите номер нужного пункта: ")
            if option.isnumeric():
                num = int(option)
        if num == 1:
            self.loadPreviousSaved()
        if num == 2:
            self.showAllNotes()
        if num == 3:
            self.addNewNote()
        if num == 4:
            self.chooseNoteById()
        if num == 5:
            self.saveChanges()
        if num == 6:
            self.finish()

    def loadPreviousSaved(self):
        self.notesManager.load()
        self.mainMenu()

    def showAllNotes(self):
        for key, value in self.notesManager.getAllRecords().items():
            self.printNote(value)
        print()    
        self.mainMenu()    
        
    def addNewNote(self):
        header = input("Введите заголовок заметки: ")
        body = input("Введите содержимое заметки: ")
        self.notesManager.addNote(header,body)
        print()
        self.mainMenu()

    def chooseNoteById(self):
        print()
        id = input("Введите id заметки: ")
        note = self.notesManager.getNoteById(id)
        while note == None:
            id = input("Указанный id не найден. Введите id заметки: ")
            note = self.notesManager.getNoteById(id)
        stillEditing = True
        while stillEditing:
            os.system('cls')
            self.printNote(note)
            print("1. Изменить заголовок    2. Изменить содержимое      3. Удалить заметку     4. Выйти в главное меню")
            option = 0
            while option < 1 or option > 4:
                option = input("Введите номер нужного пункта: ")
                if option.isnumeric():
                    option = int(option)
            if option == 1:
                note.header = input("Новый заголовок: ")
                self.notesManager.updateNote(note)
                self.printNote(note)
            if option == 2:    
                note.body = input("Новое содержимое: ")
                self.notesManager.updateNote(note)
                self.printNote(note)
            if option == 3:
                self.notesManager.removeNote(f'{note.id}')
                stillEditing = False
            if option == 4:
                stillEditing = False
        self.mainMenu()    

    def saveChanges(self):
        self.notesManager.save()
        self.mainMenu()

    def finish(self):
        print("Сохранить изменения?")
        option = 'g'
        while not (option == 'y' or option == 'n'):
            option = input("(y/n): ")
            if option == 'y':
                self.notesManager.save()
        exit()

