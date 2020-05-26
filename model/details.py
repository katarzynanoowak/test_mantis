from sys import maxsize


class Details:

    def __init__(self, projectname=None, description=None, id=None):
        self.projectname = projectname
        self.description = description
        self.id = id

    def __repr__(self):
        return "$s:%s;%s" % (self.projectname, self.description)
