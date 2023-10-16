Objective: Deploy Python and PostgreSQL using Docker and create a script to ingest data from an API into a PostgreSQL database.

1. Docker Setup: Install Docker on your machine.

2. Docker Compose and Dockerfile:
- Create a "docker-compose.yml" file to define two services: "web" (Python) and "database" (PostgreSQL).
- Create a "Dockerfile" to build the Python image, copy necessary files, and specify the command to run the data ingestion script.

3. Data Ingestion Script:
- Write a Python script named "data_ingestion_script.py" to fetch data from an API from our previous exercise.
- Insert the fetched data into the PostgreSQL database.


Submission Guidelines:

- Submit the Docker project directory using github project link.
- Include any necessary documentation or instructions.