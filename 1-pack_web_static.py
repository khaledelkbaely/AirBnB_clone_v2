#!/usr/bin/python3
""" Generate a .tgz achive from the contents of the web_static folder """
from fabric.api import local
from datetime import datetime
import os


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
