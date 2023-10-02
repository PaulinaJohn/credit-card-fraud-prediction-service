# Using a slim base image for the final production image
FROM python:3.9-slim AS production

# Setting working directory
WORKDIR /app

# Copying .dockerignore file first
COPY .dockerignore /app/.dockerignore

# Copying only necessary files based on .dockerignore
COPY ./requirements.txt /app/requirements.txt

# Installing dependencies
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Copying in the code
COPY . /app

# Exposing port and defining the entry point
EXPOSE 30131
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "30131"]