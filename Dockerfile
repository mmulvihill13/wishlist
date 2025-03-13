ARG PYTHON_VERSION=3.12-slim

FROM python:${PYTHON_VERSION}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update && \
    apt-get install -y libpq-dev gcc apache2-dev && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /code

# Copy and install dependencies
COPY requirements.txt /code/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of the application
COPY . /code/

# Collect static files
RUN python manage.py collectstatic --noinput || echo "collectstatic failed, continuing..."

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "2", "wishlist.wsgi"]
