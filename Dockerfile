FROM python:3.12-slim

# prevent python buffering
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# copy project
COPY . .

# collect static
RUN python manage.py collectstatic --noinput

# run server
CMD ["gunicorn", "portfolio_site.wsgi:application", "--bind", "0.0.0.0:8000"]