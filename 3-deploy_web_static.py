#!/usr/bin/python3
"""
Fabric script (based on the file 2-do_deploy_web_static.py) that creates and
distributes an archive to your web servers, using the function deploy
"""
from fabric.api import local, env, run, put, hosts
from datetime import datetime
import os

env.hosts = ['3.236.115.48', '107.22.146.197']


def do_pack():
    """
    create the archive file with the contents of the web_static folder
    and return the archive path if the archive has been correctly generated
    otherwise return None
    """
    datetime_str = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = "web_static_{}.tgz".format(datetime_str)
    try:
        local('mkdir -p versions')
        local('tar -cvzf versions/{} web_static'.format(file_name))
        return "versions/{}".format(file_name)
    except:
        return None


def do_deploy(archive_path):
    """
    upload the archive to the /tmp/ directory of the web server
    uncompress the archive
    delete the archive from the web server
    handle symbolic links
    return True is all operations went well, False otherwise
    """
    if not os.path.exists(archive_path):
        return False
    try:
        put(archive_path, '/tmp/')
        file_name = archive_path.split('/')[-1]
        file_name_noext = file_name.split('.')[0]
        new_folder = '/data/web_static/releases/' + file_name_noext + '/'
        run('sudo mkdir -p {}'.format(new_folder))
        run('sudo tar -xzf /tmp/{} -C {}'.format(file_name, new_folder))
        run('sudo rm /tmp/{}'.format(file_name))
        run('sudo mv {}web_static/* {}'.format(new_folder, new_folder))
        run('sudo rm -rf {}web_static'.format(new_folder))
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -s {} /data/web_static/current'.format(new_folder))
        return True
    except:
        return False


def deploy():
    """calls do_pack() and do_deploy()"""
    try:
        archive_path = do_pack()
        status = do_deploy(archive_path)
        return status
    except:
        return False
