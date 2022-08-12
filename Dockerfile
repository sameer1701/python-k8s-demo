FROM python:3.6

# Creating Application Source Code Directory
RUN mkdir -p /sourceCode/src
# Setting Home Directory for containers
WORKDIR /sourceCode/src
# Installing python dependencies
COPY requirements.txt /sourceCode/src
RUN pip3 install — no-cache-dir -r requirements.txt
# Copying src code to Container
COPY . /sourceCode/src/app
# Application Environment variables
ENV APP_ENV development
# Exposing Ports
EXPOSE 5000
# Running Python Application
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]