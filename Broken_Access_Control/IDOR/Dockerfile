# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files to the working directory
COPY . .

# Expose the port on which the application will run
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
