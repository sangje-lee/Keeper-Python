from Note import Note

class App:

    def __init__(self):
        self.theNotes = []  # Create new empty list
        self.x = 0

    def addNote(self, newTitle, newContent):
        self.theNotes.append(Note(self.x, newTitle, newContent))
        self.x += 1  # Used for generate key, once added, add one from x.

    def deleteNote(self, key):
        del self.theNotes[key]

    def editNote(self, key, newTitle, newContent):
        item = self.theNotes[key]
        item.edit_note_title(newTitle)
        item.edit_note_content(newContent)

    def totalLength(self):
        return len(self.theNotes)

    def viewId(self, key):
        item = self.theNotes[key]
        return item.return_id()

    def viewKey(self, id):
        for i, item in enumerate(self.theNotes):
            if id == item.return_id():
                return i
        return -1  # Return -1 if not found

    def viewNote(self, key):
        item = self.theNotes[key]
        return [str(item.return_id()), item.return_title(), item.return_content()]