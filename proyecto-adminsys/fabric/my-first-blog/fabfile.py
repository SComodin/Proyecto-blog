from fabric.api import run
from fabric.api import cd
from fabric.api import env
from fabric.contrib.files import exists

env.hosts = ['3.15.38.15']

PROJECT_NAME = "my_first_blog"
PROJECT_PATH = f"/tmp/new_dp{PROJECT_NAME}"
REPO_URL = "https://github.com/scomodin/my_first_blog.git"
VENV_PYTHON = f'{PROJECT_PATH}/.venv/bin/python'
VENV_PIP = f'{PROJECT_PATH}/.venv/bin/pip'


def clone():
    print(f"clone repo {REPO_URL}...")

    if exists(PROJECT_PATH):
        print("project already exists")
    else:
        run(f"git clone {REPO_URL} {PROJECT_PATH}")


def create_venv():

    print("creating venv....")

    with cd(PROJECT_PATH):
        run("python3 -m venv .venv")


def install_requirements():

    print("installing requirements.txt...")

    with cd(PROJECT_PATH):
        run(f"{VENV_PIP} install -r requirements.txt ")


def django_migrate():

    print("executing django migrations...")

    with cd(PROJECT_PATH):
        run(f"{VENV_PYTHON} manage.py migrate ")


def django_loaddata():

    print("loading initial data...")

    with cd(PROJECT_PATH):
        run(f"{VENV_PYTHON} manage.py loaddata db.json ")


def django_runserver():

    print("runing server...")

    with cd(PROJECT_PATH):
        run(f"{VENV_PYTHON} manage.py runserver")


def deploy():
    clone()
    create_venv()
    install_requirements()
    django_migrate()
    django_loaddata()
    django_runserver()
