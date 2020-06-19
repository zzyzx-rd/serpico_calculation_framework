# serpico-results-compute
per-stage results computation module

Python | Flask | Gunicorn | Docker

## Installation
After pulling, in **project root** do the following:
Create a `venv` folder
```
$ python3.7 -m venv venv
```
$ Activate the environment (it should be shown in your shell)
```
$ . venv/bin/activate
```
Install all the requirements
```
$ pip install -r requirements.txt
```
## Deployement
### Local tests
This app is deployed with [gunicorn](https://docs.gunicorn.org/en/latest/index.html), and [docker](https://docs.docker.com/)
To deploy localy, go in the root of the project.
#### Build the image: 
```
$ docker build --tag nameimage:1.0 .
```
(```nameimage```is case sensitive, and must be lowercase). It can be waht you want.
It should display something like
```
Sending build context to Docker daemon  25.56MB
...
Successfully built 51cb3ac30e9c
Successfully tagged nameimage:1.0
```
#### Run the image
```
$ docker run --publish 5000:8080 --detach --name containername nameimage:1.0
```
It should display something like : 
```
43ae85f092d5a7d2b5b898b2cc9bbb78e7e74ec2978fb9faaf6be0ac2b666bd5
```
To check every thing works correctly, go on [hello world](http://localhost:5000/hello). 

#### Kill the contener
To stop and delete the container, just run :
```
$ docker rm --force contenername 
```
It should display :
```
contenername
```
## Flask help
### Launch the app (in dev mode, for local tests)
Commands to launch the app.
```
$ export FLASK_APP=gradesCalculator
$ export FLASK_ENV=development
$ flask run
```
It should display something like
```
 * Serving Flask gradesCalculator "gradesCalculator" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 295-924-858
```

### Add external users
**Warning** Don't do this on debbuging mode (other users can run any code they want on your machine)
Disable the debbugong mode, or trust the users, and run :
```
$ flask run --host=0.0.0.0
 ```

### debbug mode
``` 
$ export FLASK_ENV=development 
 ```