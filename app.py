#!/usr/bin/python3
"""Run this app to share files of a folder that contain a certain string.


python3 app.py /path/to/folder

All files that are in /path/to/folder and sub directories are shared if they contain the SHARED_FILE

environment configuration:
- SHARED_FILE=.shared
  a string that must be in the path (case insensitive) so it is shared

"""
from flask import Flask, render_template, redirect, send_from_directory
import os
import sys
from pprint import pprint

if len(sys.argv) < 1:
    print(__doc__)

# configuration
DEBUG = os.environ.get("APP_DEBUG", "true").lower() == "true"
PORT = int(os.environ.get("PORT", "5000"))
SOURCE_DIRECTORY = sys.argv[1] # ends with /
if not SOURCE_DIRECTORY or SOURCE_DIRECTORY[-1] not in ("/", "\\"):
    SOURCE_DIRECTORY+= "/"
SHARE_STRING = os.environ.get("APP_SHARED_PATH", ".shared").lower()

# constants
HERE = os.path.dirname(__file__) or "."
TEMPLATES = os.path.join(HERE, "templates")


app = Flask(__name__, template_folder=TEMPLATES)

def is_shared(path):
    """Shortcut to test if a path is shared."""
    return SHARE_STRING in path.lower()

def get_beautiful_file_name(path):
    """Return a file name that is more nice for people."""
    return get_file_id(path).replace(SHARE_STRING, "")

__PATH_TO_ID = {}
__ID_TO_PATH = {}
def get_file_id(path):
    """Return the id for the downloads."""
    if path in __PATH_TO_ID:
        return __PATH_TO_ID[path]
    path = path.replace("\\", "/").lower()
    i1 = path.find(SHARE_STRING)
    i2 = path[:i1].rfind("/")
    _id = path[i2 + 1:]
    __PATH_TO_ID[path] = _id
    __ID_TO_PATH[_id] = path
    return _id


def get_path_from_id(_id):
    """Return a path beloning to the id"""
    if _id in __ID_TO_PATH:
        return __ID_TO_PATH[_id]
    for file in get_all_files():
        if get_file_id(file) == _id:
            return file
    raise FileNotFoundError(f"Could not find the file with id {_id} - maybe it was removed?")


def get_all_files():
    """Return a list of all files that are shared."""
    result = []
    for dirpath, dirnames, filenames in os.walk(SOURCE_DIRECTORY):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            if is_shared(filepath):
                result.append(filepath[len(SOURCE_DIRECTORY):])
    result.sort()
    return result

@app.route("/")
def list_directory():
    return render_template("directory.html",
        files=get_all_files(),
        directory=SOURCE_DIRECTORY,
        get_beautiful_file_name=get_beautiful_file_name,
        get_file_id=get_file_id,
        sorted=sorted)

@app.route("/download/<path:_id>")
def download(_id):
    assert not ".." in _id, "The path should be valid!"
    path = get_path_from_id(_id)
    return send_from_directory(SOURCE_DIRECTORY, path)



if __name__ == "__main__":
    pprint(get_all_files())
    app.run(debug=DEBUG, host="0.0.0.0", port=PORT)