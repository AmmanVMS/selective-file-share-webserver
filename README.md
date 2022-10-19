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
SOURCE=./test py3/bin/gunicorn -w 4 -b "0.0.0.0:5000" app:app
```

Then, you can head over to [localhost:5000](http://localhost:5000) to see it!


This runs the app with all options set:

```
export APP_DEBUG=false
export PORT=5000
export APP_SHARED_PATH=shared
export SOURCE=./test
SOURCE=./test
py3/bin/gunicorn -w 4 -b "0.0.0.0:5000" app:app
```

## Update

Run this to update the app to the latest version:

```
cd selective-file-share-webserver
git pull
venv/bin/pip install --upgrade -r requirements.txt
```

## Development

To run the development version of the app, use this:

```
SOURCE=./test venv/bin/python3 app.py
```


