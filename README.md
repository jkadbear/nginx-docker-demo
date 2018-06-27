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

```
docker run -d --name download --rm \
    -v $PWD/nginx.conf:/etc/nginx/nginx.conf \
    -v $PWD/download:/usr/share/nginx/html \
    -e VIRTUAL_HOST=download.lpwan-thu.top nginx
```

open `http://download.lpwan-thu.top`

### Web App

```
cd app
docker build -t jkadbear/jura
docker run -d --name jura --rm \
    -e 'VIRTUAL_HOST=jura.lpwan-thu.top' jkadbear/jura
```

open `http://jura.lpwan-thu.top`

### Ip Report

```
cd ip-reporter
docker build -t jkadbear/ip-reporter
docker run -d --name ip --rm -p 7777:5000 jkadbear/ip-reporter
```

open `http://lpwan-thu.top:7777/ip`

### SSH proxy

```
docker run -d --name nginx-ssh --rm -p ANOTHERPORT:ANOTHERPORT:
    -v $PWD/nginx-ssh.conf:/etc/nginx/nginx.conf nginx
```

