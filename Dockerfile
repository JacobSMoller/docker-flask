FROM python:3.6-alpine

WORKDIR /usr/src/app

COPY setup.py ./
COPY README.md ./
RUN pip install --no-cache-dir .

COPY . .

CMD ["gunicorn", "-b", "0.0.0.0:5000", "wsgi:app"]
