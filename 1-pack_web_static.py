#!/usr/bin/python3
""" Generate a .tgz achive from the contents of the web_static folder """
from fabric.api import local
from datetime import datetime


def do_pack():
    """ Generate a .tgz achive from the contents of the web_static folder """
    local("[ ! -d versions ] && mkdir versions")

    curr_time = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = "web_static_{}.tgz".format(curr_time)

    try:
        local("tar -cvzf {} web_static".format(archive_name))
        return archive_name
    except Exception:
        return None
