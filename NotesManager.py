import DataStoreManager
from datetime import datetime
import Note
import json

class NotesManager:

    def __init__(self):
        self.notes = {}

    
    def addNote(self,header, body):
        note = Note.Note(header,body,datetime.now())
        self.notes.update({note.id:note})
    
    def getNoteById(self,id):
        for key, value in self.notes.items():
            if key == id:
                return value
            
    def getAllRecords(self):
        return self.notes
    
    def removeNote(self,uuidString):
        del self.notes[uuidString]
    
    def updateNote(self, note):
        note.lastModified = datetime.now()
        self.notes.update({note.id:note})

    def load(self):
        self.notes = DataStoreManager.DataStoremanager.loadData()
    
    def save(self):
        DataStoreManager.DataStoremanager.saveData(self.notes)
