# -*- coding: utf-8 -*-
from data.project import testdata
from model.project import Project
import random


def test_add_project_testcase(app, db):
    old_projects = db.get_project_list()
    app.project.go_to_projects_page()
    app.project.press_add_new_project_button()
    app.project.fill_and_submit_new_project(testdata)
    new_projects = db.get_project_list()
    assert len(old_projects)+1 == len(new_projects)
    old_projects.append(testdata)
    assert old_projects == new_projects