"""A class which holds the commands to be executed."""

class EditFile:
    def __init__(self):
        self.fileContent= ""
        self.filepath = ""

    def findAllTextFiles(self, dirpath):
        import os

        def findAll(filepath):
            for dir in os.listdir(filepath):
                if dir.find(".") != -1:
                    if dir.find(".txt") != -1:
                        print("  "+dir)
                else:
                    print(f"\nIn sub-directory {dir} (path {os.path.join(filepath, dir)}), the following was found\n")
                    findAll(os.path.join(filepath, dir))
                    print(f"\n(end of files found in {dir} and sub-directories)\n")

        print(f"The following was found in the directory at {dirpath} and it's sub-directories:\n")

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

        self.fileContent = ""
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

        print("the opened file's contents are:\n\n" + self.fileContent)



 