#!/usr/bin/python3
"""a script that archive a folder locally using fabric 
so it can be deployed later on the servers 
-> USAGE: fab -f 1-pack_web_static.py do_pack
"""
import os
from datetime import datetime
from fabric.api import local

def do_pack():
    """packing the web static files to deploys them in the srevres 
    """
    dt = datetime.now()
    # sets the file aparrence 
    file = "versions/web_static_{}.tgz".format(dt.strftime("%Y%m%d%H%M%S"))
    # checks if the directory is ther , if not it should skip
    if os.path.exists("versions"):
        print("there's already a directory that does this")
        return None
    # creating the directory
    local("mkdir versions")
    # creating the .tgz archive from the directory
    local(f"tar -czvf {file} /web_static")
    return file
