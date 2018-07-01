FROM python:3.6.1
MAINTAINER jkadbear "jkadbear@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install flask
EXPOSE 5000
CMD ["python", "report.py"]
