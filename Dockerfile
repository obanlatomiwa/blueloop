# Base Image
FROM python:3

# current directory for the container
WORKDIR /usr/src/app

# We copy just the requirements.txt first to leverage Docker cache from source current dir to  destination
COPY requirements.txt ./

# Install requirements
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONUNBUFFERED 1

EXPOSE 8085

ENTRYPOINT ["python"]

CMD ["manage.py", "runserver", "0.0.0.0:8085"]