#!/usr/bin/python3
""" disributes an archive to your web servers """
from fabric.api import *
from fabric.operations import put, run, sudo, local
from datetime import datetime
import os

env.hosts = ['54.234.82.159', '100.26.167.203']


def do_pack():
    """ Generate a .tgz achive from the contents of the web_static folder """
    if not os.path.exists('versions'):
        os.mkdir('versions')

    curr_time = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = "versions/web_static_{}.tgz".format(curr_time)

    try:
        local("tar -cvzf {} web_static".format(archive_name))
        return archive_name
    except Exception:
        return None


def do_deploy(archive_path):
    """ disributes an archive to your web servers """
    if not os.path.isfile(archive_path):
        return False

    try:
        archive_name = archive_path.split('/')[-1]
        path_for_folder = '/data/web_static/releases'

        put(archive_path, '/tmp/{}'.format(archive_name))
        folder = archive_name.split('.')[0]
        run('mkdir -p {}/{}/'.format(path_for_folder, folder))
        run('tar -xzf /tmp/{} -C {}/{}/'.format(
            archive_name, path_for_folder, folder))
        run('rm -rf /tmp/{}'.format(archive_name))
        run('mv {}/{}/web_static/* {}/{}/'.format(
            path_for_folder, folder, path_for_folder, folder))
        run('rm -rf {}/{}/web_static'.format(path_for_folder, folder))
        run('rm -rf /data/web_static/current')
        run('ln -s {}/{} /data/web_static/current'.format(
            path_for_folder, folder))
        return True
    except Exception:
        return False


def deploy():
    """ create and disributes an archive to web servers """
    path_to_archive = do_pack()
    if not path_to_archive:
        return False
    return do_deploy(path_to_archive)
