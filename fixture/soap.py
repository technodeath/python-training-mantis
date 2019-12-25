from suds.client import Client
from suds import WebFault
from model.project import Project

class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client("http://localhost/mantisbt-2.23.0/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_project_list_for_user(self, username, password):
        list = []
        client = Client("http://localhost/mantisbt-2.23.0/api/soap/mantisconnect.php?wsdl")
        try:
            projects = client.service.mc_projects_get_user_accessible(username, password)
            for i in range(len(projects)):
                list.append(Project(id=str(projects[i]['id']), name=projects[i]['name'], status=projects[i]['status']['name'],
                                    enabled=projects[i]['enabled'], view_state=projects[i]['view_state']['name'],
                                    description=projects[i]['description']))
        except WebFault:
            return False
        return list
