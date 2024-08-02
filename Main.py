from App import App

NoteInItem = App()

itemLoopable = True
while (itemLoopable == True) :
    print("Welcome to command version of Things to do")
    print("1. Add")       # Add a note
    print("2. Edit")      # Edit a note (Content only)
    print("3. Remove")    # Remove a note
    print("4. View")      # View a note
    print("5. Exit")      # Exit the Code
    userChoice = input("") # Read userChoice in String format
    if (userChoice == "5"):
        break
    elif (userChoice == "1"):
        # Add a note to the ArrayList created
        userTitle = input("Enter the Title: ")
        userComment = input("Enter the content: ")
        NoteInItem.addNote(userTitle, userComment) # Add a new Note to ArrayList
        # break
    elif (userChoice == "2"): # userChoice is "2"
        # Edit the specific note to the ArrayList, based on the key/ID
        if (NoteInItem.totalLength() == 0):
            # If the ArrayList (App class) is empty then
            # Alert user to add the new note first
            print()
            print("Enter the data before proceed")
        else:
            # If the ArrayList has at least one note then
            # First display all the notes inside the ArrayList
            for i in range(NoteInItem.totalLength()) :
                testItem = NoteInItem.viewNote(i)
                print(str(i) + " " + testItem[1] + " " + testItem[2])
            # Then ask user to which section note to edit
            userColumn = int(input("Enter the number to edit: ")) # Read userColumn in integer format
            if (userColumn < NoteInItem.totalLength()) and (userColumn >= 0) :

                # If the proper range (key/ID) is selected then
                # Display specific key of the note (Content only)
                testItem = NoteInItem.viewNote(userColumn)
                print(str(userColumn) + " " + testItem[2])
                print()
                print("Only the content can be edited")
                # Ask user to prompt new Content
                newUserComment = input("Enter the new content: ")
                if (newUserComment == "") :
                    # If user give blank then
                    # Assume the note will not be edited.
                    # newUserComment = testItem[2];
                    newUserComment = testItem[2]
                    print("No change occurs")
                else:
                    # If user state a new Content then
                    # Replace old Content into new Content
                    newNote = NoteInItem.viewNote(userColumn)
                    NoteInItem.editNote(userColumn, newNote[1], newUserComment)
            else:
                # If the proper range (key/ID) is not selected then
                # Indicate that there's no note contain in that range Key/ID
                print()
                print("Invalid ID number, try again!")
    elif (userChoice == "3"): # line is "3"
        # Delete the specific note to the ArrayList, based on the key/ID
        if (NoteInItem.totalLength() == 0) :
            # If the ArrayList (App class) is empty then
            # Alert user to add the new note first
            print()
            print("Enter the data before proceed")
        else:
            # If the ArrayList has at least one note then
            # First display all the notes inside the ArrayList
            for i in range(NoteInItem.totalLength()) :
                testItem = NoteInItem.viewNote(i)
                print(str(i) + " " + testItem[1] + " " + testItem[2])
            # Then ask user to which section note to remove/delete
            userColumn = int(input("Enter the number to delete: "))
            if (userColumn < NoteInItem.totalLength()) and (userColumn >= 0) :
                NoteInItem.deleteNote(userColumn)
            else:
                print()
                print("Invalid ID number, try again!")
    elif (userChoice == "4"):
        # Display all the notes inside the Arraylist
        # The note will display,
        # Location of the Arraylist, Key code, Title, then Content
        for i in range(NoteInItem.totalLength()):
            testItem = NoteInItem.viewNote(i)
            print(str(i) + " " + testItem[0] + " " + testItem[1] + " " + testItem[2])
    else:
        print("Invalid Code, try again.")
    print()