#!/usr/bin/python3
"""python Fabric script that generates a .tgz archive
   from the contents of the web_static folder of your
   AirBnB Clone repo, using the function do_pack
"""
from fabric.api import *
from datetime import datetime

def do_pack():
    local("sudo mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    file = "versions/web_static_{}.tgz".format(date)
    result = local("sudo tar -cvzf {} web_static".format(file))
    if result.succeeded:
        return file
    else:
        return None
