#!/usr/bin/python3
""" a fabric script that generates a .tgz archive from the web_static content
    folder in the AirBnB_clone repo, using the function do_pack"""
from fabric.api  import local
from datetime import datetime

def do_pack():
    """a function that creates an archive for a directory

    Returns:
        tgz file: the archive path if the archive has been correctly generated 
    """
    try:
        current_time = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_path = "versions/web_static_{}.tgz".format(current_time)
        #create the folder versions if not exists
        local("mkdir -p versions")
        #create the archive
        local("tar -czvf {} web_static".format(archive_path))
        return archive_path
    except:
        return None

