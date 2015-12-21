from fabric.api import local



def hello(name, surname, treat='Sr'):
    print(u'Hello %s %s %s' % (treat, name, surname))

def call_it():
    local('python ./test.py')
