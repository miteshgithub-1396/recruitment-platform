# Use an official Python runtime as the base image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt


# Define environment variable
ENV NAME World

# Run the Gunicorn server
CMD ["gunicorn", "--bind", "0.0.0.0:80", "app:app"]
