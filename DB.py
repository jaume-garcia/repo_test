class DB:
    def __init__(self, name, address, studies="physics",degree="physics):
        self.name = name
        self.address = address
        self.studies = studies
        self.degree = degree

    def __str__(self):
        return "Name:{}; Address:{}".format(self.name, self.address)
