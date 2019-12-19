import pymysql.cursors
from model.project import Project


class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host,
                             user=user,
                             password=password,
                             db=name, autocommit=True)

    def get_project_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, name, status, enabled, view_state, description from bugtracker.mantis_project_mantis")
            for row in cursor:
                (id, name, status, enabled, view_state, description) = row
                list.append(Project(id=str(id), name=name, status=status, enabled=enabled, view_state=view_state,
                                    description=description))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()
