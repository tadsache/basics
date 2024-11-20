FROM python:3.10-slim
LABEL authors="het2dr"
# Set the working directory within the container
WORKDIR /api-flask

COPY api.py /api-flask/
COPY requirements.txt  /api-flask/

# Upgrade pip and install Python dependencies
RUN pip3 install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Expose Port
EXPOSE 42069

# Define the command to run the Flask application using Gunicorn
CMD [ "python3", "api.py"]
21