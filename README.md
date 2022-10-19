# selective file share webserver

This webserver shares files in a directory only if the path contains a certain string such as `.shared`.

## Installation

You need
- git
- Python3
- virtualenv


1. Clone the repository:
    ```
    git clone https://github.com/AmmanVMS/selective-file-share-webserver
    cd selective-file-share-webserver
    ```
2. Create a virtual environment:
    ```
    virtualenv -p python3 venv
    venv/bin/pip install -r requirements.txt
    ```

## Running the app

You can run the app for a specific folder, e.g. `./test`:

```
venv/bin/python3 app.py ./test
```

Then, you can head over to [localhost:5000](http://localhost:5000) to see it!


This runs the app with all options set:

```
export APP_DEBUG=false
export PORT=5000
export APP_SHARED_PATH=shared
venv/bin/python3 app.py /path/to/folder/to/share
```

## Update

Run this to update the app to the latest version:

```
cd selective-file-share-webserver
git pull
venv/bin/pip install -r requirements.txt
```