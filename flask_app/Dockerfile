FROM python:3.10-slim

WORKDIR /app
COPY . .

RUN pip install -r requirements.
EXPOSE 3000
CMD ["python", "app.py", "0.0.0.0:3000"]

