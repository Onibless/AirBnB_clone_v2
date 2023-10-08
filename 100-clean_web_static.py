#!/usr/bin/python3
""" script that deletes out-of-date archives,
using the function do_clean
"""
import os
from fabric.api import *

env.hosts = ['54.161.255.140', '34.207.156.215']


def do_clean(number=0):
    """Function that delete outdated archives.
    Args:
        number (int): The number of archives to keep.
    """
    number = 1 if int(number) == 0 else int(number)

    u_arch = sorted(os.listdir("versions"))
    [u_arch.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in u_arch]

    with cd("/data/web_static/releases"):
        u_arch = run("ls -tr").split()
        u_arch = [a for a in u_arch if "web_static_" in a]
        [u_arch.pop() for i in range(number)]
        [run("rm -rf ./{}".format(i)) for i in u_arch]
