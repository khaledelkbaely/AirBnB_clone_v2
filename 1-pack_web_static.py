#!/usr/bin/python3
""" Generate a .tgz achive from the contents of the web_static folder """
from fabric.api import local
from datetime import datetime
from os.path import isdir


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
