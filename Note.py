import uuid
from datetime import datetime

class Note:
    def __init__(self, header, body, lastModified):
        self.id = f'{uuid.uuid4()}'
        self.header = header
        self.body = body
        self.lastModified = lastModified

    def toJson(n):
        if isinstance(n, Note):
            json = f'{{"id":"{n.id}","header": "{n.header}","body": "{n.body}","lastModified": "{n.lastModified.isoformat()}"}}'
            return json
        else:
            type_name = n.__class__.__name__
            raise TypeError("Unexpected type {0}".format(type_name))
    