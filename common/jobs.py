class Job:

    def __init__(self):
        self.title = ''
        self.company = ''
        self.description = []
        self.category = ''
        self.location = ''
        self.responsibilities = []
        self.requirements = []

    def __str__(self):
        s = "Title: " + str(self.title) + "\n"
        s += "Company: " + str(self.company) + " at " + str(self.location) + "\n"
        s += "Category: " + str(self.category) + "\n"
        s += "Description: " + str(self.description) + "\n"
        s += "Responsibilities: \n"
        for r in self.responsibilities:
            s += "- " + str(r) + "\n"
        s += "Requirements:\n"
        for rq in self.requirements:
            s += "- " + str(rq) + "\n"
        return s
