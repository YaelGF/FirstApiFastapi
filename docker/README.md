# Config Ubuntu 20.04 and Python with FastAPI

## 1. Dockefile 
```
FROM ubuntu:18.04

LABEL description = "Description"

RUN apt update
RUN apt upgrade -y
RUN apt install -y python3
RUN apt install -y python3-pip
RUN pip3 install web.py
```

## 2. Build Docker image
```
docker build -t fastapi:v1 .
```

## 3. Create docker container
nota:regresar a la carpeta principal
```
cd ..
```

```
docker run -it -v $(pwd)/PaginaFastapi:/PaginaFastAPI --net host --name webpy -h python fastapi:v1
```

## 4. Run Web Page

```
$cd /PythonWeb
$python3 app.py
```