#!/usr/bin/python3
""" Script that creates and distributes an archive
to web servers """


from fabric.api import *
from datetime import datetime
from os.path import exists


env.hosts = ['54.161.255.140', '34.207.156.215']


def do_pack():
    """function and store the path of the created archive
    """
    local("sudo mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    file = "versions/web_static_{}.tgz".format(date)
    result = local("sudo tar -cvzf {} web_static".format(file))
    if result.succeeded:
        return file
    else:
        return None


def do_deploy(archive_path):
    """ distributes an archive to my web servers
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
    except Exception:
        return False


def deploy():
    """ function, using the new path of the new archive
    """
    new_path = do_pack()
    if exists(new_path) is False:
        return False
    result = do_deploy(new_path)
    return result
