FROM python:3.9-slim

WORKDIR /app

# Install dependencies first (better layer caching)
COPY . /app
COPY ./shared /app/shared
COPY ./database /app/database
COPY ./requirements.txt /app/requirements.txt

COPY ./app.py /app/app.py
COPY ./stocks_routes.py /app/routes.py
COPY ./capital_gains_routes.py /app/routes.py
COPY ./validators.py /app/validators.py
COPY ./models /app/models
COPY ./utils /app/utils

ENV FLASK_APP=app.py

RUN pip install --no-cache-dir -r requirements.txt

# Expose the application port
EXPOSE 8080

# Run the application
CMD ["python", "app.py"]
