# import the python base image
FROM python:3.11

# inside the container set the working directory as app
WORKDIR /app

# copy your code
COPY . /app/

# install requirements .txt
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["python", "run.py"]