FROM python:2.7-slim

# Set the working directory to app
WORKDIR /tomer-app/

# Copy the current directory contents into the container at /app
COPY . /tomer-app/

# 
RUN pip install flask

#
CMD ["python", "tomer-app.py"]
