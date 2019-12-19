# -*- coding: utf-8 -*-
from data.project import testdata
from model.project import Project
import random


def test_random_project_testcase(app, db):
    if len(db.get_project_list()) == 0:
        app.project.go_to_projects_page()
        app.project.press_add_new_project_button()
        app.project.fill_and_submit_new_project(testdata)
    old_projects = db.get_project_list()
    random_project = random.choice(old_projects)
    app.project.go_to_projects_page()
    app.project.delete_project_by_name(random_project.name)
    new_projects = db.get_project_list()
    assert len(old_projects)-1 == len(new_projects)
    old_projects.remove(random_project)
    assert old_projects == new_projects