#!/usr/bin/python3
""" script that distributes an archive to web servers,
using the function do_deploy
"""


from fabric.api import *
from datetime import datetime
from os.path import exists

env.hosts = ['54.161.255.140', '34.207.156.215']


def do_deploy(archive_path):
    """ distributes an archive to your web servers
    """
    if exists(archive_path) is False:
        return False
    file = archive_path.split('/')[-1]
    extract_tgz = '/data/web_static/releases/'\
        + "{}".format(file.split('.')[0])
    tmp = "/tmp/" + file

    try:
        put(archive_path, "/tmp/")
        run("mkdir -p {}/".format(extract_tgz))
        run("tar -xzf {} -C {}/".format(tmp, extract_tgz))
        run("rm {}".format(tmp))
        run("mv {}/web_static/* {}/".format(extract_tgz, extract_tgz))
        run("rm -rf {}/web_static".format(extract_tgz))
        run("rm -rf /data/web_static/current")
        run("ln -s {}/ /data/web_static/current".format(extract_tgz))
        return True
    except _:
        return False
