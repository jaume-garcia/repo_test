class DB:
    def __init__(self, name, address, studies="physics"):
        self.name = name
        self.address = address
        self.studies = studies

    def __str__(self):
<<<<<<< HEAD
        return "Name:{}; Address:{}".format(self.name, self.addres)

=======
        return "Name:{}; Address:{}".format(self.name, self.address)
>>>>>>> parent of afa5339 (Added a bug in __str__ in DB.py)
