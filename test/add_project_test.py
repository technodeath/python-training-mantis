# -*- coding: utf-8 -*-
from data.project import testdata
from model.project import Project
import random


def test_add_project_testcase(app, db):
    old_projects = app.soap.get_project_list_for_user('administrator', 'root')
    print(old_projects)
    app.project.go_to_projects_page()
    app.project.press_add_new_project_button()
    app.project.fill_and_submit_new_project(testdata)
    new_projects = app.soap.get_project_list_for_user('administrator', 'root')
    assert len(old_projects)+1 == len(new_projects)
    old_projects.append(testdata)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)