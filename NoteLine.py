from datetime import datetime

class Note:
    def __init__(self, id_note, title, body, created_at=None, edited_at=None):
        self.id = id_note
        self.title = title
        self.body = body
        self.created_at = created_at or datetime.now()
        self.edited_at = edited_at or datetime.now()

    def __str__(self):
        return f"Note ID: {self.id} - title:  {self.title} | Description: {self.body} | Created: {self.created_at} | Edited: {self.edited_at}"

    def edit(self, title, body):
        self.title = title
        self.body = body
        self.edited_at = datetime.now()