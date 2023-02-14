FROM python:3.11-slim-buster

RUN apt-get update && apt-get install -y gcc python3-dev g++

# Set the working directory to /app
WORKDIR /app

RUN python -m venv /app/venv
SHELL ["/bin/bash", "-c"]
RUN source /app/venv/bin/activate

RUN pip install --upgrade pip

COPY ./requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
RUN python -m pip install Pillow

COPY . .

RUN python manage.py migrate && python manage.py collectstatic --noinput

EXPOSE 8000

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]