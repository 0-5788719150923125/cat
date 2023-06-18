FROM opencog/learn:latest

RUN apt-get update && apt-get install -y python3-pip nodejs npm

RUN echo "progress=false" > .npmrc

RUN npm i -g nodemon

WORKDIR /app

COPY ./requirements.txt src ./

RUN pip3 install -r requirements.txt

CMD ["python3", "-u", "src/main.py"]