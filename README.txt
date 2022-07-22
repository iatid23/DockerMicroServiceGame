## running the app - docker-compose up only 

explain work flow steps:
------------------------

this assignment has 3 parts :
1. auth (python api) (microservice) port:8000 - every microservice will need its own container
2. game (python api) (microservice) port:8001 - every microservice will need its own container
3. ui (react ui) - will need is own container also

-becuase of the multipule containers we will use one compose file to run all of them together
############################

stages to do the assignment:
----------------------------

1 - check every service locally without docker  - 
* while checking i sew there is a problem in the auth service using decode('utf-8')
* solution was to remove it
2 - make dokerfile for every service and check at least one locally (checked auth)
3. - make composefile for running all 
4. add comments inside the docker and comsoe files to explain stages of work 
5. playing !!! (checking spretlly the api on localhost (ports 8000/8001), playing on localhost://3000
6. what i learned (new things)

stage 1 (over venv to prevent confilcts in istalled packesges)
###############################################
trying it locally without docker:
###############################################
1. Auth Service
---------------
has two endpoint:
1. login
2. signup

setup and run
-------------

1. setup venv
2. activate venv
3. copy/Create requirements.txt file 
4. run requirements.txt file install packages
5. run python manage.py runserver 0.0.0.0:8000
################################################
###############################################
trying it locally without docker:
2.Game Service
-------------
has 9 functions (endpoints):
1. validate_and_get_email_from_jwt
2. start_new_game
3. is_have_active_game
4. get_game_state
5. checkWinnerCord
6. checkWinner
7. isAllBoardFull
8. player_move
9. cpu_player_worker 

setup and run
-------------

1. setup venv
2. activate venv
3. copy/Create requirements.txt file (if needed)
4. run requirements.txt file install packages
5. run python manage.py runserver 0.0.0.0:8001
################################################
################################################

trying it locally without docker:
3. ui (React)
-------------

setup and run
-------------

1. npm install
2. npm start
################################################


after checking locally has a problem with body_unicode = request.body.decode('utf-8') in Auth Service 
i Changed it to body_unicode = request.body - now it works
##################################################
stage 2 - making dockerfiles for each service and checking at least one
########################################################################
1. makle dockerfile
2. check docker locally (no compose)
########################################################################
stage 3
########################################################################
1. make docker-compose.ymal file
2. run docker-compose file by - "docker-compose up" command


--rm		Automatically remove the container when it exits
-d          Run container in background and print container ID
--publish , -p		Publish a container's port(s) to the host

#############################################
stage 4 - comments - will comments on docker and compose files (inside)
################################################

#############################################
stage 5 - playing !!! (and checking)
################################################
1. checking auth api on localhost://8000
2. checking game api on localhost://3000
3. playing game on localhost://3000
################################################


stage 6 - what i learned (new things)
################################################
1. compose file - concept and sytax
2. docker file layers and syntax
2. run django
3. microservice conept
4. binding them
################################################

##  docker-compose up  - closing running containers


thanks!!