# -*- coding: utf-8 -*-
from data.project import testdata
from model.project import Project
import random


def test_random_project_testcase(app, db):
    if len(app.soap.get_project_list_for_user('administrator', 'root')) == 0:
        app.project.go_to_projects_page()
        app.project.press_add_new_project_button()
        app.project.fill_and_submit_new_project(testdata)
    old_projects = app.soap.get_project_list_for_user('administrator', 'root')
    random_project = random.choice(old_projects)
    app.project.go_to_projects_page()
    app.project.delete_project_by_name(random_project.name)
    new_projects = app.soap.get_project_list_for_user('administrator', 'root')
    assert len(old_projects)-1 == len(new_projects)
    old_projects.remove(random_project)
    assert old_projects == new_projects