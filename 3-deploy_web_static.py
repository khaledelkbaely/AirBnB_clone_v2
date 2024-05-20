#!/usr/bin/python3
""" disributes an archive to your web servers """
from fabric.api import env, local, put, run
from datetime import datetime
from os.path import exists, isdir

env.hosts = ['54.234.82.159', '100.26.167.203']
created_path = None


def do_pack():
    """ Generate a .tgz achive from the contents of the web_static folder """
    try:
        curr_time = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        archive_name = "versions/web_static_{}.tgz".format(curr_time)
        local("tar -cvzf {} web_static".format(archive_name))
        return archive_name
    except Exception:
        return None


def do_deploy(archive_path):
    """ disributes an archive to your web servers """
    if exists(archive_path) is False:
        return False

    try:
        archive_name = archive_path.split('/')[-1]
        folder = archive_name.split('.')[0]
        path_for_folder = '/data/web_static/releases/'

        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path_for_folder, folder))
        run('tar -xzf /tmp/{} -C {}{}/'.format(
            archive_name, path_for_folder, folder))
        run('rm -rf /tmp/{}'.format(archive_name))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path_for_folder, folder))
        run('rm -rf {}{}/web_static'.format(path_for_folder, folder))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(
            path_for_folder, folder))
        return True
    except Exception:
        return False


def deploy():
    """ create and disributes an archive to web servers """
    global created_path
    if created_path is None:
        created_path = do_pack()
    if not created_path:
        return False
    return do_deploy(created_path)
