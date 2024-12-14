# Use the official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install any necessary packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Flask is running on
EXPOSE 5001

# Define environment variable
ENV FLASK_APP=app.py

# Run the application
CMD ["flask", "run", "--host=0.0.0.0", "--port=5001"]
