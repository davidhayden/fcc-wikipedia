# Wikipedia Viewer for freeCodeCamp

freeCodeCamp is a website/organization that helps developers learn and become better developers. In addition to training resources, they have a number of projects that developers can complete to receive certificates. One of the projects for the front-end certification is a Wikipedia Viewer.

This repository is a spin-off of the Wikipedia Viewer project. Rather than using static HTML and hosting the project on CodePen, I built it as a Python Flask application and deployed it to Heroku.

![freeCodeCamp Wikipedia Viewer](/assets/wikipedia-viewer-david-hayden.png)

## Getting Started

The best way to run the project locally is to clone the github repository. Once you clone the repository, it is best to create a virtual environment and `pip install` the requirements. At that point you can run the website via Flask or Gunicorn.

### Step 1: Clone the Repository

```
$ git clone https://github.com/davidhayden/fcc-wikipedia.git
```

### Step 2: Create Virtual Environment and Install Requirements

Change into the project directory, create a virtual environment, and `pip install` the requirements in the `requirements.txt` file.

```
$ cd fcc-wikipedia

$ python -m venv env
$ source env/bin/activate
$ (env) pip install -r requirements.txt
```

### Step 3: Run via Flask

You can now run the website via Flask.

```
$ (env) export FLASK_APP=wiki.py
$ (env) export FLASK_DEBUG=1
$ (env) flask run

 * Serving Flask app "wiki"
 * Forcing debug mode on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 181-621-853
```

You can browse to localhost on port 5000 to view the Wikipedia Viewer app.

### Step 3: Run via Gunicorn

If you're running on Mac or Linux, pip installed Gunicorn, which is used to run the website on Heroku. You can optionally run the website using Gunicorn.

```
$ (env) gunicorn wiki:app

[18992] [INFO] Starting gunicorn 19.7.1
[18992] [INFO] Listening at: http://127.0.0.1:8000 (18992)
[18992] [INFO] Using worker: sync
[18995] [INFO] Booting worker with pid: 18995
```

You can browse to localhost on port 8000 to view the Wikipedia Viewer app.

### Step 4: Quit Web Server and Deactivate Virtual Environment

When you're done viewing the Wikipedia Viewer, you can press `CTRL+C` to exit the running Flask or Gunicorn web server.

You can then type `deactivate` to leave the virtual environment.

```
CRTL+C

$ (env) deactivate
$ 
```

## Deploying to Heroku

The project includes a `Procfile` that tells Heroku this is a web app and to run the application using Gunicorn.

```
web gunicorn wiki:app
```

Make sure you are in the project directory. You can deploy to Heroku using the familiar set of commands.

```
$ heroku create
$ git push heroku master
$ heroku ps:scale web=1
$ heroku open
```

Delete the Heroku application after you are done viewing it.

## Road map

There are no plans to add any additional features to the code.

## License
This code is made available under the [MIT License](http://www.opensource.org/licenses/mit-license.php).

## Credits
Created and maintained by David Hayden.
