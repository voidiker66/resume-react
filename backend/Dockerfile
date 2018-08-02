#Use an official Python runtime as a parent image
FROM python:3

# Set the working directory to /index
WORKDIR /index

# Copy the current directory contents into the container at /index
#ADD . /index
COPY . /index

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 50 for backend
EXPOSE 5000

# Define environment variable
#ENV NAME World

# Run app.py when the container launches
CMD ["python", "index.py"]