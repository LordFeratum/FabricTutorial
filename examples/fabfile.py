from fabric.api import env, local, run
from fabric.operations import put

env.hosts = ['doble.me']
env.user  = 'lordferatum'


def hello(name, surname, treat='Sr'):
    print(u'Hello %s %s %s' % (treat, name, surname))

def call_it():
    local('python ./test.py')

def do_lluc():
    run('uname -a')

def deploy_lluc():
    project_folder = '/home/lordferatum'
    put('test.py', project_folder)
    run('python %s/test.py' % project_folder)
