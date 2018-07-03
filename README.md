# Nginx Docker demo

This demo shows how to use dockerized ` Nginx`.

- Auto indexer (with custom [nginx-indexer](https://github.com/nervo/nginx-indexer))
- Reverse proxy for web app
- Docker Registry

Before staring these services, run `export DOMAIN=xxx` to set  your base domain, or create `.env` file under relevant directory. For `ssh-proxy`, `SSHPORT` should be set. For `ip-report`, `REPORTPORT` should be set.

In order to proxy the nginx-proxy container and the web app container must be on the same Docker network.

When you run a multi-container web app with `docker-compose`, Docker attaches the containers to a default network. The default network is different from the bridge network that containers run with the docker run command attach to.

To resolve this, create a new Docker network.

```bash
docker network create --driver bridge proxy-network
```


### Nginx Proxy with Simpole Static file service

```bash
cd nginx-proxy
docker-compose up -d
```

open `http://download.$DOMAIN`

### Docker Registry

1. create certificate and set HTTPS

   https://docs.docker.com/registry/insecure/#use-self-signed-certificates

   ```bash
   openssl req \
     -newkey rsa:4096 -nodes -sha256 -keyout certs/hub.$DOMAIN.key \
     -x509 -days 365 -out certs/hub.$DOMAIN.crt
   ```

   https://docs.docker.com/docker-for-mac/#add-tls-certificates

   e.g. for Mac users:

   ```bash
   security add-trusted-cert -d -r trustRoot -k ~/Library/Keychains/login.keychain ca.crt
   ```

   **NOTE**: You need to restart Docker for Mac after making any changes to the keychain or to the ~/.docker/certs.d directory in order for the changes to take effect.

2. apply access control

   ```bash
   cd docker-registry
   mkdir auth
   docker run --rm \
   --entrypoint htpasswd \
   registry:2 -Bbn testuser testpasswd > auth/htpasswd
   ```

3. run

   ```bash
   docker-compose up -d
   ```

try `docker login hub.$DOMAIN`

### Nodejs App

```bash
cd nodeapp
docker-compose up -d
```

open `http://nodeapp.$DOMAIN`

### SpringBoot App

```bash
cd SimpleSpringBoot
./mvnw clean package -DskipTests
docker build -t jkadbear/jura .
docker run -d --name jura --rm \
    -e VIRTUAL_HOST=jura.$DOMAIN jkadbear/jura
```

open `http://jura.DOMAIN`

### IP Report

```bash
cd ip-report
docker-compose up -d
```

open `http://$DOMAIN:$REPORTPORT/ip`

### SSH proxy

```bash
cd ssh-proxy
cp nginx.conf.example nginx.conf # edit IP and SSHPORT
docker-compose up -d
```

try `ssh -p $SSHPORT USER@$DOMAIN`

