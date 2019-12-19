from model.project import Project
from selenium.webdriver.support.ui import Select
from data.project import testdata


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    project_cache = None

    def go_to_projects_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//span[@class="menu-text" and text() = " Manage "]').click()
        wd.find_element_by_xpath('//a[text() = "Manage Projects"]').click()

    def press_add_new_project_button(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//button[text() = "Create New Project"]').click()

    def delete_project_by_name(self, name):
        wd = self.app.wd
        self.select_project_by_name(name)
        wd.find_element_by_css_selector('input[value="Delete Project"]').click()
        wd.find_element_by_css_selector('input[value="Delete Project"]').click()

    def select_project_by_name(self, name):
        wd = self.app.wd
        wd.find_element_by_xpath("//a[text()='%s']" % name).click()

    def fill_and_submit_new_project(self, new_project_data):
        wd = self.app.wd
        self.fill_project_text(new_project_data)
        self.fill_project_dropdowns(new_project_data)
        self.fill_project_checkbox()
        wd.find_element_by_css_selector('input[type="submit"]').click()
        self.go_to_projects_page()

    def fill_and_submit_edit_group(self, new_group_data):
        # fill the group form and update
        wd = self.app.wd
        self.fill_group_form(new_group_data)
        wd.find_element_by_name("update").click()
        self.go_to_groups_page()
        self.group_cache = None

    def fill_project_text(self, project):
        wd = self.app.wd
        self.change_text_value("#project-name", project.name)
        self.change_text_value("#project-description", project.description)

    def fill_project_dropdowns(self, project):
        wd = self.app.wd
        self.change_dropdown_value("#project-status", project.status)
        self.change_dropdown_value("#project-view-state", project.view_state)

    def fill_project_checkbox(self):
        wd = self.app.wd
        self.change_checkbox_value()

    def change_checkbox_value(self):
        wd = self.app.wd
        wd.find_element_by_css_selector(".lbl").click()

    def change_text_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_css_selector(field_name).click()
            wd.find_element_by_css_selector(field_name).clear()
            wd.find_element_by_css_selector(field_name).send_keys(text)

    def change_dropdown_value(self, field_name, value):
        wd = self.app.wd
        if value is not None:
            wd.find_element_by_css_selector(field_name).click()
            Select(wd.find_element_by_css_selector(field_name)).select_by_visible_text(value)
            wd.find_element_by_css_selector(field_name).click()