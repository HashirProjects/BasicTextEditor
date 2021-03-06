"""A class which holds the commands to be executed."""

class EditFile:
    def __init__(self):
        self.fileContent= ""
        self.filepath = ""

    def findAllTextFiles(self, dirpath):
        import os

        def findAll(filepath, indentLvl = 1):
            for dir in os.listdir(filepath):
                try:
                    if dir.find(".") != -1:
                        print("    "*(indentLvl)+dir)
                    else:
                        print("    "*indentLvl + f"In sub-directory {dir} (path {os.path.join(filepath, dir)}), the following was found\n")
                        findAll(os.path.join(filepath, dir), indentLvl + 1)
                except:
                    pass

        print(f"\nThe following was found in the directory at {dirpath} and it's sub-directories:\n")

        findAll(dirpath)

    def open(self, filepath):

        if self.fileContent != "":
            print ("A file is already open.")
            return

        try:
            with open(filepath, "r") as f:
                self.fileContent= f.read()
            
            print(f"Opened file. Path: {filepath} ")

            self.filepath = filepath
        except:
            print("That filepath was not valid.")

    def close(self):
        
        if self.fileContent == "":
            print("No file is currently open.")
            return

        with open(self.filepath, "w") as f:
            f.write(self.fileContent)

        self.fileContent = ""
        self.filepath = ""
        print("Closed File.")


    def move(self, newFilePath):
        
        if self.fileContent == "":
            print("No file is currently open.")
            return

        self.filepath = newFilePath

        with open(newFilePath, "w") as f:
            f.write(self.fileContent)

    def display(self):
        if self.fileContent == "":
            print("No file is currently open.")
            return

        print("the opened file's contents are:\n\n")

        fileByLine = self.fileContent.split("\n")

        for i in range(len(fileByLine)):
            print(f"{i}) {fileByLine[i]}")

    def editLine(self, lineNumber):
        if self.fileContent == "":
            print("No file is currently open.")
            return

        fileByLine = self.fileContent.split("\n")

        fileByLine[lineNumber] = input("Write the new contents of the line below:\n")

        self.fileContent = "\n".join(fileByLine)



 