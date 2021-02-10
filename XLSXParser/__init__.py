import pylightxl as xl

class Parser:
    def __init__(self, db_name):
        self.sheet = xl.readxl(fn=db_name).ws_names[0]
        self.db = xl.readxl(fn=db_name)

    def readName(self):
        return self.db.ws(self.sheet).address(address="A2") + self.db.ws(self.sheet).address(address="B2") + self.db.ws(self.sheet).address(address="C2")

    def readAnswers(self):
        return
