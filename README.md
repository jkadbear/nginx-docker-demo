# Nginx Docker demo

This demo shows how to use dockerized ` Nginx`.

- Auto indexer (with custom [nginx-indexer](https://github.com/nervo/nginx-indexer))
- Reverse proxy for web app
- [HTTPS with Let's Encrypt ](https://cloud.google.com/community/tutorials/nginx-reverse-proxy-docker)

### Nginx proxy

```bash
docker run -d --name nginx-proxy --rm -p 80:80 \
    -v /var/run/docker.sock:/tmp/docker.sock:ro \
    jwilder/nginx-proxy
```

### Static file service

```bash
docker run -d --name download --rm \
    -v $PWD/nginx.conf:/etc/nginx/nginx.conf \
    -v $PWD/download:/usr/share/nginx/html \
    -e VIRTUAL_HOST=download.lpwan-thu.top nginx
```

open `http://download.lpwan-thu.top`

### Nodejs App

```bash
cd nodeapp
docker build -t jkadbear/jura .
docker run -d --name nodeapp --rm \
    -e VIRTUAL_HOST=nodeapp.lpwan-thu.top jkadbear/nodeapp
```

open `http://nodeapp.lpwan-thu.top`

### SpringBoot App

```bash
cd SimpleSpringBoot
./mvnw clean package -DskipTests
docker build -t jkadbear/jura .
docker run -d --name jura --rm \
    -e VIRTUAL_HOST=jura.lpwan-thu.top jkadbear/jura
```

open `http://jura.lpwan-thu.top`

### IP Report

```bash
cd ip-reporter
docker build -t jkadbear/ip-reporter .
docker run -d --name ip --rm -p PORT:5000 jkadbear/ip-reporter
```

open `http://lpwan-thu.top:PORT/ip`

### SSH proxy

```bash
docker run -d --name nginx-ssh --rm -p ANOTHERPORT:ANOTHERPORT:
    -v $PWD/nginx-ssh.conf:/etc/nginx/nginx.conf nginx
```

