# layer 1 
# fetching image for python version 3.9.6 slim from docker liberary
# FROM python:3.9.6-slim
# decided to fatch the newest docker image (from dockerhub - ON LINUX:AMD64) :
FROM python:alpine3.15

#declaring the maintainer name  REMOVED - now using label instead - who did it 
LABEL key="Itamar_Atid"  
# layer 2
# copy app content to docker image
COPY ./ /app/

# copy requirments to docker image  - not needed becuase of copying all the directory 
#COPY ./requirements.txt /app

# setting the working directory to run the command 
WORKDIR /app

# layer 3
# run the requirments for service
RUN pip3 install -r requirements.txt

# expose the desired port for srevice to run - get all its information required during the runtime from a specified Port
EXPOSE 8000

# layer 4
# run the service
# ( can use entry point also but decided to run CMD [array])
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]