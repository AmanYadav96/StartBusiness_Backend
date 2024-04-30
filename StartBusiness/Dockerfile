FROM python:3.9

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Command to run the Django application
CMD ["python", "StartBusiness/wsgi.py"]


# Use the official Python image as the base image
# FROM python:3.9

# # Set environment variables for Python
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

# # Set the working directory in the container
# WORKDIR /app

# # Copy the dependencies file to the working directory
# COPY requirements.txt /app/

# # Install dependencies
# RUN pip install --upgrade pip
# RUN pip install -r requirements.txt

# # Copy the current directory contents into the container at /app
# COPY . /app/

# # Expose the port the app runs on
# EXPOSE 8000
# WORKDIR /app/StartBusiness

# # Command to run the Django application
# CMD ["StartBusiness/wsgi.py"]
