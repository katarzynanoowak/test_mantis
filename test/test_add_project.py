from fixture.project import Project
from model.details import Details
import random
import string


def randomString(stringLength):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


def test_add_new_project(app):
    app.session.login("administrator", "root")
    old_list = app.project.get_project_list()
    app.project.create(Details(projectname=randomString(8), description=randomString(15)))
    new_list = app.project.get_project_list()
    assert len(new_list) == len(old_list) + 1

