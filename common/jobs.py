class Job:

    def __init__(self):
        self.title = ''
        self.company = ''
        self.description = ''
        self.location = ''
        self.responsibilities = []
        self.requirements = []

    def __str__(self):
        s = "Title: " + str(self.title) + "\n"
        s += "Company: " + str(self.company) + " at " + str(self.location) + "\n"
        s += "Description: " + str(self.description) + "\n"
        s += "Responsibilities: " + str(self.responsibilities) + "\n"
        s += "Requirements: " + str(self.requirements)
        return s
