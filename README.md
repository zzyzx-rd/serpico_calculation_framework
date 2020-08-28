# serpico-results-compute
per-stage results computation module

Python | Flask | Gunicorn | Docker
## Deployement
This app is deployed with  [docker](https://docs.docker.com/) and docker-compose
### Local deployment
* To deploy localy, go in the root of the project.
    > cd serpico_compute_result
* Build the container : 
The container must  be rebuilt after modifications in the sources files. To rebuild the container image, do : 

    > docker-compose build

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
* Run the container :

    > docker-compose up


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


## Deployment sur le serveur
Sur le serveur ```serpico```, aller dans ```/var/www/serpico_calculation_framework```.
* Pour mettre le code à jour, il suffit de pull.
    > git pull   
* Pour vérifier les containers présents sur le serveur (et faire du ménage si besoins): 
    > docker ps -a 

Cà devrait afficher quelquechose comme: 

    ```
    CONTAINER ID        IMAGE                             COMMAND                  CREATED             STATUS                          PORTS               NAMES
    5e077a11f79d        serpicocalculationframework_web   "gunicorn --bind 0.0…"   2 minutes ago       Exited (0) About a minute ago   
    ```
* Pour supprimer des containers inutiles (ou shut down des containers en  cours), faire : 
    > docker container rm *container_id* -f 

Remarque : il est possible de mettre autant d'ID de container que souhaité.
* Pour rebuild le container (après un pull)
    >docker-compose build                                                                               
* Pour lancer le service, il suffit de faire comme sur votre machine personnelle, soit :
    > docker-compose up

* Enfin, pour appeler ce service, il faut utiliser l'une des 3 url suivantes : 
    * http://51.15.121.241:5000/ : page du hello world, utile pour tester la disponibilité du serice sans passer par Serpico
    * http://51.15.121.241:5000/main/criteriaComputation : url de computation des criterias
    * http://51.15.121.241:5000/main/stageComputation : url de computation des stages ou activity. 

## Faire du ménage avec docker
Si jamais vous installez docker sur votre machine, vous risquez d'avoir plein de trucs qui trainent.
Pour faire du ménage.
* Effacer les images mortes (peut occuper des dizaines de Gi) :
    > docker image prune
* Effacer les containers:
    > docker container prune
    