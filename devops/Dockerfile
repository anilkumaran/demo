# # Use an official Python runtime as a parent image
# FROM python:3.9-slim

# # Set the working directory in the container
# WORKDIR /app

# # Copy the current directory contents into the container at /app
# COPY . /app

# RUN ls devops/

# # Install any needed packages specified in requirements.txt
# RUN pip install --no-cache-dir -r employee_mgmt/requirements.txt

# # Make port 5000 available to the world outside this container
# EXPOSE 5000

# # Define environment variable
# ENV FLASK_APP=app.py
# ENV FLASK_RUN_HOST=0.0.0.0

# # Run app.py when the container launches
# CMD ["flask", "run"]


FROM python:3.9-slim-buster
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r employee_mgmt/requirements.txt
EXPOSE 5000
CMD ["python", "employee_mgmt/app.py"]