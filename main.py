import gitlab
import subprocess
import os

gl = gitlab.Gitlab(url='', private_token='')
rootdir = 'repo'
depth = 1

group_id = <add your group_id>

def download_repo():
    group = gl.groups.get(group_id)
    subprocess.run('rm -rf repo/*', shell=True)
    os.chdir("repo")
    print(os.getcwd())
    for project in group.projects.list(iterator=True):
        print(project.name + " " + project.ssh_url_to_repo)
        subprocess.call(['git', 'clone', project.ssh_url_to_repo])
    os.chdir("..")


def upload_repo():
    for subdir, dirs, files in os.walk(rootdir):
        if subdir[len(rootdir):].count(os.sep) == depth:
            # print(subdir)
            os.chdir(subdir)
            print(os.getcwd())
            subprocess.run('git revert HEAD~0', shell=True)
            subprocess.run('git push', shell=True)
            os.chdir('../..')
            print(os.getcwd())


download_repo()
upload_repo()
