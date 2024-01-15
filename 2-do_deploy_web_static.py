#!/usr/bin/python3
"""a scripy that deploys the web_static content to the servers and
decompresses it using  tar -xzvf"""
from fabric.api import *
from datetime import datetime
import os.path
# connecting to the servres
env.hosts = ['107.23.156.230', '54.146.92.28']


def deploy(archive_path):
    """a function that deploys files to servers
    """
    if not os.path.isfile("archive_path"):
        return False
    try:
        # uploding the ARCHIVE to the remote servers at /tmp/
        put(archive_path, '/tmp/')
        # extcrating the file name only without tzg ext
        archive_name = archive_path.split('/')[-1]  # includes .tgz
        file_name = archive_name.split('.')[0]  # without .tgz
        # making the directory where it need be to stored
        path_toCreate = f"/data/web_static/releases/{file_name}"
        run(f'mkdir -p {path_toCreate}')
        # uncompress the archive into the directory above
        run(f"tar -xzf /tmp/{archive_name} -C {path_toCreate}")
        # Remove the aechuve from the web server
        run(f"rm /tmp/{archive_name}")
        # delets the current symbplic link from the servers and
        # creates a new one each time we deployed an archived one
        curr_Symbolink = "/data/web_static/current"
        run(f"rm {curr_Symbolink}")
        run(f"ln -s {curr_Symbolink} {path_toCreate}")

        for host in env.hosts:
            print(f" Deployment to the server with the IP : {host} is Done")

        return True
    except Exception:
        return False
