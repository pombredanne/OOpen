from fabric.api import task, prompt, local, run, sudo
from fabric.colors import green, red, yellow
import oopen
import sys


@task
def update_version():
    current_version = oopen.__version__
    major, minor, patch = [int(n) for n in current_version.split('.')]

    v_selection = prompt(green("Do you want to update the:\n(1) Major version\n(2) Minor version\n(3) Patch version\n[3]: "))
    # if (v_selection != 1 and v_selection != 2):
    #     v_selection = 3
    v_selection = int(v_selection)

    print v_selection
    #after all is ok:
    v_selection -= 1
    version = [major, minor, patch]
    version[v_selection] += 1

    #reset [minor], patch versions when updating major or minor
    while v_selection < 2:
        v_selection += 1
        version[v_selection] = 0

    version = ".".join([str(n) for n in version])
    accept = prompt(green(
        "\nPlease confirm; do you want to update the version from {0} to {1}\nyes/[no]: ").format(current_version, version))
    if accept != "yes":
        sys.exit(1)




    # tag_selection = prompt(green("Do you want to issue a git tag -s ? [y]: ")).lower()
    # tag_selection = True if tag_selection == 'y' else False
