# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# JWinslow,11-12-2022,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection
strTask = "" # capture the user input
strPriority = "" # capture the user input


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# TODO: Add Code Here

# Open the file
objFile = open("ToDoList.txt.rtf", "r")  # had the name "ToDoList.txt" instead of objFile...did not work

# pull data from the list
for row in objFile:
    strData = row.split(",")
    dicRow = {"Task": strData[0].strip(), "Priority": strData[1].strip()}
# use the data to build a dictionary
    lstTable.append(dicRow)
# close the file when done
objFile.close()
# -- Input/Output -- #
print(lstTable)

# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current ToDo List
    2) Add a new Task.
    3) Remove an existing Task.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks


    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        # TODO: Add Code Here
        print("The current ToDo List items are: ", "\n")
        for row in lstTable:
            print(row["Task"] + " | " + row["Priority"] + " | ")
        continue # to show the menu again

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        # TODO: Add Code Here
        strTask = str(input("What is the New Task? -")).strip() # case sensitive for str instead of Str, and 2nd " missing
        strPriority = str(input("What is the Priority of this Task? [high|low] -")).strip()
        dicRow = {"Task": strTask, "Priority": strPriority}
        lstTable.append(dicRow)
        print("Current ToDo List:")
        #Show the current items in the table
        print("The Current items ToDo are:", "\n")
        for row in lstTable:
            print(row["Task"] + "|" + row["Priority"] + "|")
        continue # to show the menu again


    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        # TODO: Add Code Here
        strKeyToRemove = input("Which Task would you like to remove? -")
        blnItemRemoved = False # use this to verify that the data was found and removed
        intRowNumber = 0
        for row in lstTable:
            task, priority = dict().values()
            if task == strKeyToRemove:
                del lstTable[intRowNumber]
                blnItemRemoved = True
            intRowNumber += 1
        # Update user on the status
        if blnItemRemoved == True:
            print("The task was removed.")
        else:
            print("I'm sorry, I could not finish the request.")

        # Show the current items in the table
        print(" The current items ToDo are: ")
        continue # show the menu again

    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        # TODO: Add Code Here

        # Show the current items in the table
        print("The current items ToDo are: ")
        for row in lstTable:
            print(row["Task"] + "|" + row["Priority"] + "|")

        # Ask the user if the data is to be saved
        if "y" == str(input("Save this data to file? (y/n) - ")).strip().lower():
            objFile = open("ToDoList.txt.rtf", "w")
            for dicRow in lstTable:
                objFile.write(dicRow["Task"] + "," + dicRow["Priority"] + "\n")
            objFile.close()
            input("Data saved to file! Press the [Enter] key to return to the menu.")
        else:
            input("New data was Not Saved, however, the previous data still exists! Press the [Enter] key to return to the menu.")
        continue # show the menu again

    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        # TODO: Add Code Here
        exit()
        break  # and Exit the program
