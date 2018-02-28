FROM python:3.6
ENV PYTHONUNBUFFERED 1

ADD requirements.txt /app/
RUN pip install -r /app/requirements.txt

ADD . /app
WORKDIR /app

EXPOSE 5000

# Run api.py when the container launches
CMD ["python", "api.py"]