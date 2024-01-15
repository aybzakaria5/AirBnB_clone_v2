#!/usr/bin/python3
"""A script that deploys the web_static content to the servers and
decompresses it using tar -xzvf"""
from fabric.api import *
from datetime import datetime
import os.path

# Connecting to the servers
env.hosts = ['54.146.92.28']

def do_deploy(archive_path):
    """A function that deploys files to servers
    """
    if not os.path.exists(archive_path):
        return False
    try:
        # Uploading the ARCHIVE to the remote servers at /tmp/
        put(archive_path, '/tmp/')
        
        # Extracting the file name only without tzg extension
        archive_name = archive_path.split('/')[-1]  # includes .tgz
        file_name = archive_name.split('.')[0]  # without .tgz
        
        # Creating the directory to store the extracted contents
        path_to_create = f"/data/web_static/releases/{file_name}"
        run(f'sudo mkdir -p {path_to_create}')
        
        # Uncompress the archive into the directory created above
        run(f"sudo tar -xzf /tmp/{archive_name} -C {path_to_create} --strip-components=1")
        # Remove the archive from the web server
        run(f"sudo rm /tmp/{archive_name}")
        
        # Deleting the current symbolic link from the servers
        run(f"sudo rm -f /data/web_static/current")
        
        # Creating a new symbolic link pointing to the extracted contents
        run(f"sudo ln -s {path_to_create} /data/web_static/current")

        for host in env.hosts:
            print(f"Deployment to the server with the IP: {host} is Done")

        return True
    except Exception as e:
        print(f"Deployment failed: {e}")
        return False
