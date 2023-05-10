import os


class Globals:

    def __init__(self):
        self.scriptPath = os.path.abspath(__file__)
        self.srcPath = os.path.dirname(self.scriptPath)
        self.parentPath = os.path.dirname(self.srcPath)

        self.dataPath = os.path.join(self.parentPath, "data")
        self.databasePath = os.path.join(self.dataPath, "database.db")
        self.credentialsPath = os.path.join(self.dataPath, "credentials.json")


GLOBALS = Globals()
