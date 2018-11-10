# Use an official Python runtime as a parent image
FROM python:3.7

# Set the working directory for the container
WORKDIR /usr/local/jsonio

# Copy requirements.txt to the container
ADD ./requirements.txt ./

# Install packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Copy the rest of the contents into the container
ADD . ./

# Install source code (without dependencies)
RUN pip install --trusted-host pypi.python.org --no-deps ./
