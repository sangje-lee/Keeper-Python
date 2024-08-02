class Note:
    def __init__(self, new_id, new_title, new_content):
        # initialise instance variables
        self.the_id = new_id
        self.the_title = new_title
        self.the_content = new_content

    # Editing the title of the note
    def edit_note_title(self, new_title):
        self.the_title = new_title

    # Editing the content of the note
    def edit_note_content(self, new_content):
        self.the_content = new_content

    # Return the title of the note in string form
    def return_title(self):
        return self.the_title

    # Return the content of the note in string form
    def return_content(self):
        return self.the_content

    # Return the ID (key) of the note in integer
    def return_id(self):
        return self.the_id