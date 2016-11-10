class Job:

    def __init__(self):
        self.title = ''
        self.company = ''
        self.description = []
        self.category = ''
        self.location = ''
        self.responsibilities = []
        self.requirements = []
        self.preferred_requirements = []
        self.posting_link = ''

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

        if self.preferred_requirements:
            s += "Preferred Requirements:\n"
            for prq in self.preferred_requirements:
                s += "- " + str(prq) + "\n"

        s += "Link: " + str(self.posting_link) + "\n"

        return s
