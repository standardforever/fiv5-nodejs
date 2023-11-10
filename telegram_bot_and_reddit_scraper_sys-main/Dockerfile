FROM python:3.10-slim-bullseye

# Set the working directory to /app
WORKDIR /src

# Update package lists and install any needed system packages
RUN apt-get update && apt-get install -y git

COPY . ./

RUN pip install --no-cache-dir -r ./app/requirements.txt

#EXPOSE 8502
#EXPOSE 8502

LABEL authors="ACTRegTech"

#CMD ["python", "./app/main.py", "--server.port=8502", "--server.address=0.0.0.0"]
CMD ["python", "./app/main.py"]
