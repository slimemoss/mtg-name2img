FROM python:3.12.2-alpine

COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY ./ /app
WORKDIR /app
ENV FLASK_APP='/app/run.py'
CMD ["python", "-u", "-m", "flask", "run", "--host", "0.0.0.0", "--port", "80"]
