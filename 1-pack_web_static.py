#!/usr/bin/python3
""" Script to create .tgz archive
"""
from fabric.api import run


def do_pack():
    """Function to create tgz archive and store all the archives in 
    versions folder"""
    run('mkdir -p versions/web_static$(date +%Y%M%D%H%M%S).tgz')
    run('tar file_name web_static')
    if (packing successful):
        return (file_path to archive)
    return None

