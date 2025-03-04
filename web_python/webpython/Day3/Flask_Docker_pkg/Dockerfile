from python:alpine3.7
copy ./app
workdir /app
run pip install -r requirements.txt
expose 5010
entrypoint ["python"]
cmd ["mymicroservice.py"]
