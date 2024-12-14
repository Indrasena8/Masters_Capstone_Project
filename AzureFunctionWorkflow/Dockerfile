# Use the official Azure Functions Python image
FROM mcr.microsoft.com/azure-functions/python:4-python3.11

# Set the working directory for the Azure Functions runtime
WORKDIR /home/site/wwwroot

# Copy all the application files to the working directory
COPY . /home/site/wwwroot

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt
