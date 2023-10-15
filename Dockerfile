# Use Python 3.11 as the base image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install any required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container
COPY app/ .

# Optionally, expose a port if your app needs it
EXPOSE 80

# Set the command to run your application
CMD ["python", "main.py"]