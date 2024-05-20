#!/usr/bin/python3
""" disributes an archive to your web servers """
from fabric.api import put, run, env
from os.path import exists

env.hosts = ['54.234.82.159', '100.26.167.203']


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
