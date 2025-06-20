FROM python:3.12-slim

WORKDIR /app
COPY main.py .
COPY templates/ ./templates/
RUN pip install Flask 
EXPOSE 5000

CMD ["python", "main.py"]