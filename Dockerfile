# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install FastAPI and Uvicorn
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000 to the outside world
EXPOSE 8000

# Define environment variable to make sure the output is logged correctly
ENV PYTHONUNBUFFERED=1

# Command to run the FastAPI app using Uvicorn server
CMD ["fastapi", "run", "--host", "0.0.0.0", "--port", "8000"]
