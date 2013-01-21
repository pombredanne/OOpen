from fabric.api import task, prompt, local
from fabric.colors import green, red, blue
from functools import partial
import oopen
import sys
import os

local = partial(local, capture=True)


def ensure_in_sync():
    if local('git describe --dirty') == oopen.__version__:
        return True


@task
def update_version():
    current_version = oopen.__version__
    major, minor, patch = [int(n) for n in current_version.split('.')]

    v_selection = prompt("Do you want to update the:\n(1) Major version: {0}\n(2) Minor version: {1}\n(3) Patch version: {2}\n=>".format(green(major), green(minor), green(minor)), default=3, validate='[0-9]')
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

    local(r'''sed -i "~" /^__version/s/\'.*\'/\\\'{}\\\'/ oopen/__init__.py'''.format(version))


    # tag_selection = prompt(green("Do you want to issue a git tag -s ? [y]: ")).lower()
    # tag_selection = True if tag_selection == 'y' else False


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
        return
    local('python setup.py register')
    local('python setup.py publish')
