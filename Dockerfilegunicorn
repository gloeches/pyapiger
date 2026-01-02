# Use an official Python 3.7 runtime as a parent image
FROM python:3.7-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --upgrade pip

# Copy the rest of the application code into the container at /app
COPY . .

# Make port 8000 available to the world outside this container (Gunicorn's default)
EXPOSE 8000

# Define the command to run your app with Gunicorn
# "flask-api:app" assumes your Flask app instance is named 'app' in flask-api.py
# -b 0.0.0.0:8000 binds Gunicorn to all network interfaces on port 8000
CMD ["gunicorn", "flask-api:app", "-b", "0.0.0.0:8000"]