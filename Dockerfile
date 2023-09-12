# Use the official Python 3.8 image
FROM python:3.8-slim

 

# Set the working directory inside the container
WORKDIR /app

 

# Copy the requirements file into the container
COPY requirements.txt .

 

# Install Flask using pip
RUN pip install --no-cache-dir -r requirements.txt

 

# Copy the rest of the application files into the container
COPY . .

 

# Specify the command to run on container start
CMD ["python", "app.py"]

 

# Expose port 80
EXPOSE 80