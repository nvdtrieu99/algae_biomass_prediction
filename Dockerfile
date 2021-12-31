FROM python:3.8
WORKDIR ./
ADD requirements.txt requirements.txt
ADD api.py api.py
RUN pip install -r requirements.txt
ADD app
EXPOSE 8080
CMD ["python", "api.py"]