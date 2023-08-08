import json
from types import SimpleNamespace
from datetime import datetime
import Note

class DataStoremanager:
    @staticmethod
    def saveData(notes):
        with open("data.json", "w") as outfile:
            json = "["
            for value in notes.values():
                json = json + value.toJson() + ","
            json = json[:-1]
            json += "]"
            outfile.write(json)

    @staticmethod
    def loadData():
        loaded = {}
        with open("data.json", "r") as infile:
            data = json.load(infile,object_hook=lambda d: SimpleNamespace(**d))
            for dataLine in data:
                note = Note.Note(dataLine.header, dataLine.body, datetime.fromisoformat(dataLine.lastModified) )
                loaded.update({f'{note.id}':note})
        return loaded
    
    