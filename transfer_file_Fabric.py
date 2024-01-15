#!/usr/bin/python3
"""A Python script to upload files to the servers"""
from fabric.api import env, put, task, run

env.hosts = ['server_usr1@ip1', 'server_usr2@ip2']

@task
def upload_and_run_script():
    local_file_path = '0-setup_web_static.sh'
    remote_path = "~/"

    try:
        # Upload the file to each server
        for host in env.hosts:
            put(local_file_path, remote_path, use_sudo=True)
            print(f'File uploaded to {host}:{remote_path}')

            # Run the script on the remote server
            remote_script_path = f"{remote_path}/0-setup_web_static.sh"
            run(f"chmod +x {remote_script_path} && {remote_script_path}")

            print(f'Script executed on {host}')

    except Exception as e:
        print(f"Error: {e}")