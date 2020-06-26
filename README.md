# serpico-results-compute
per-stage results computation module

Python | Flask | Gunicorn | Docker

## Creating the virtual environement
If you want to test it without launcing with docker, you must install the virtual environement, with doing following : 
Create a `venv` folder

```
 $ python3.7 -m venv venv
```
Activate the environment (it should be shown in your shell if you use zsh for example)

    $ . venv/bin/activate

Install all the requirements in the virtual env.
```
$ pip install -r requirements.txt
```
## Deployement
This app is deployed with  [docker](https://docs.docker.com/) and docker-compose
### Local deployment
To deploy localy, go in the root of the project.
#### Build the container
The container must  be rebuilt after modifications in the sources files. To rebuild the container image, do : 
```
$ docker-compose build
```
It will take some times (one or two minutes), and should dipslay someting like : 
```
redis uses an image, skipping
Building web
Step 1/9 : FROM python:3.7-alpine
 ---> 6a5ca85ed89b
Step 2/9 : WORKDIR /app
 ---> Using cache
 ---> b1064f77a3d3
Step 3/9 : ENV FLASK_APP "app:create_app()"
 ---> Using cache
 ---> a133cf7430e0
Step 4/9 : ENV FLASK_RUN_HOST 0.0.0.0
 ---> Using cache
 ---> 659d65ab52f6
Step 5/9 : RUN apk add --no-cache gcc musl-dev linux-headers
 ---> Using cache
 ---> 45aa80ff3881
Step 6/9 : COPY requirements.txt requirements.txt
 ---> Using cache
 ---> e813e0834dac
Step 7/9 : RUN pip install -r requirements.txt
 ---> Using cache
 ---> a5a1bdd652fe
Step 8/9 : COPY . .
 ---> 391d236e4bfb
Step 9/9 : CMD ["flask", "run"]
 ---> Running in 94e3f2426a16
Removing intermediate container 94e3f2426a16
 ---> 69d4d7d0c604
Successfully built 69d4d7d0c604
Successfully tagged serpico_calculation_framework_web:latest
```
#### Run the container :
```
$ docker-compose up
```

It will display something like : 
```
***
redis_1  | 1:M 22 Jun 2020 12:24:20.457 * Loading RDB produced by version 6.0.5
redis_1  | 1:M 22 Jun 2020 12:24:20.457 * RDB age 233365 seconds
redis_1  | 1:M 22 Jun 2020 12:24:20.457 * RDB memory usage when created 0.77 Mb
redis_1  | 1:M 22 Jun 2020 12:24:20.457 * DB loaded from disk: 0.001 seconds
redis_1  | 1:M 22 Jun 2020 12:24:20.457 * Ready to accept connections
web_1    |  * Serving Flask app "app:create_app()"
web_1    |  * Environment: production
web_1    |    WARNING: This is a development server. Do not use it in a production deployment.
web_1    |    Use a production WSGI server instead.
web_1    |  * Debug mode: off
web_1    |  * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
```
To check your container is running, go on [hello world](http://0.0.0.0:5000/), you should see 
```
Hello World! I have been seen x times.
```
(x increment)


## Deployment
sur ta machine
docker login 

docker build -t docker_account_name/tag .

docker push name.tag

sur le serveur
docker pull docker_account_name/tag
docker pull redis
docker ps -a (affiche les container, utile pour faire du ménage)
 docker container rm container_id -f (efface container)
docker run -d -h redis -p 6379 redis 
 docker run -d -p 5000:5000 gdbdg/serpico_compute_result
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

