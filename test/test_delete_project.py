from model.details import Details
import random
import string


def randomString(stringLength):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


def test_delete_first_project(app):
    app.session.login("administrator", "root")
    if len(app.project.get_project_list()) == 0:
        app.project.create(Details(projectname=randomString(8), description=randomString(15)))
    old_list = app.project.get_project_list()
    app.project.delete_first_project()
    new_list = app.project.get_project_list()
    assert len(new_list) == len(old_list) -1
