FROM python:3.12-slim

WORKDIR /app
COPY main.py .
COPY util.py .
RUN pip install Flask Flask-JWT-extended pyjwt
EXPOSE 5000

CMD ["python", "main.py"]