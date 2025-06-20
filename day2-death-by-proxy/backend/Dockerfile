FROM python:3.12-slim

WORKDIR /app
COPY main.py .
RUN pip install Flask
EXPOSE 15000

CMD ["python", "main.py"]