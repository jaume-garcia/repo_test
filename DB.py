class DB:
    def __init__(self, name, address, studies="physics"):
        self.name = name
        self.address = address
        self.studies = studies

    def __str__(self):
        return "Name:{}; Address:{}".format(self.name, self.addres)
