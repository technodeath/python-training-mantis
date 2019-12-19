from model.project import Project
import string
import random


def random_name(maxlen=15):
    symbols = string.ascii_letters + " "*15
    return "".join(random.choice(symbols) for i in range(maxlen))

testdata = Project(name=random_name(), status="development", view_state="public", description="project_description_1")
