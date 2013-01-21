from fabric.api import task, prompt, local
from fabric.colors import green, red, blue
from functools import partial
from textwrap import dedent
import oopen
import sys
import os
import re
import subprocess
import datetime
local = partial(local, capture=True)
EDITOR = 'subl'


def ensure_in_sync():
    if local('git describe --dirty') == oopen.__version__:
        return True


@task
def update_version():
    current_version = oopen.__version__
    major, minor, patch = [int(n) for n in current_version.split('.')]

    v_selection = prompt("Do you want to update the:\n(1) Major version: {0}\n(2) Minor version: {1}\n(3) Patch version: {2}\n=>".format(green(major), green(minor), green(patch)), default="3", validate=r'[0-9]')
    v_selection = int(v_selection)

    v_selection -= 1
    version = [major, minor, patch]
    version[v_selection] += 1

    #reset [minor], patch versions when updating major or minor
    while v_selection < 2:
        v_selection += 1
        version[v_selection] = 0

    version = ".".join([str(n) for n in version])
    accept = prompt(
        "\nPlease confirm; do you want to update the version \nfrom {0}\nto   {1}\nyes/[no]: ".format(blue(current_version), red(version)))
    if accept != "yes":
        sys.exit(1)

    changes = local('git log --oneline --no-color {}..HEAD'.format(current_version))
    local(r'''sed -i "~" /^__version/s/\'.*\'/\\\'{}\\\'/ oopen/__init__.py'''.format(version))

    change_log = re.sub(r'^[0-9a-z]*?\ ', '- ', changes)
    # subprocess.check_output(popenargs, kwargs)
    subproc = subprocess.Popen(['subl', '-n', '-w', '-'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    retdata = subproc.communicate(change_log)[0]

    # subproc.stdin.write(change_log)
    # retdata = subproc.stdout.read()
    hist = open('HISTORY.rst', 'r')
    line = ''
    header = ''
    #Set the position of the file
    while line != 'History\n':
        line = hist.readline()
        header += line
    header += hist.readline()

    entry_header = dedent('''\

        {0} ({1})
        ++++++++++++++++++\n\n'''.format(version, str(datetime.date.today())))

    new_hist = header + entry_header + retdata + "\n" + hist.read()
    hist.close()
    hist = open('HISTORY.rst', 'w').write(new_hist)
    return version


@task
def clean():
    if os.path.isdir('dist'):
        local('rm -rf dist/')
    if os.path.isdir('oopen.egg-info'):
        local('rm -rf oopen.egg-info')


@task
def readme():
    local('cat INFO.rst INSTALL.rst HISTORY.rst LICENSE.rst > README.rst')


@task
def publish():
    if not ensure_in_sync():
        print red('Your git tag does not match your version (or working tree)')
        return False
    local('python setup.py register')
    local('python setup.py publish')


@task
def push():
    if not ensure_in_sync():
        print red('Your git tag does not match your version (or working tree)')
        return False
    local('git push')
    local('git push --tags')


@task
def new_release():

    ans = local('git status --porcelain')
    if ans != '':
        print 'Please commit your code and run again.'
        return

    ans = prompt('Do you want to increment the version?', default='no', validate=r'(yes|no)')
    if ans == 'yes':
        version = update_version()
        readme()
        local('git add oopen/__init__.py')
        local('git add README.rst')
        local('git commit -m "Incrementing version to {}"'.format(version))

    ans = prompt('Do you want to tag this version?', default='no', validate=r'(yes|no)')
    if ans == 'yes':
        local('git tag -s {}'.format(version))

    ans = prompt('Do you want to push to github?', default='no', validate=r'(yes|no)')
    if ans == 'yes':
        push()

    ans = prompt('Do you want to publish to PYPI?', default='no', validate=r'(yes|no)')
    if ans == 'yes':
        publish()
