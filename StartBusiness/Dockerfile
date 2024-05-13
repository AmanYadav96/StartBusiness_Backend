# Use the official Python image as the base image
FROM python:3.12.1

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt /app/

# Install dependencies
RUN pip install --upgrade pip
RUN ["pip" ,"install","Django==5.0.6" ]
RUN ["pip" ,"install","djongo==1.3.6" ]
RUN ["pip" ,"install","sqlparse==0.5.0" ]
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/

# Expose the port the app runs on

EXPOSE 9090


# Command to run the Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
