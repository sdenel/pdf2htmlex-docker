# pdf2htmlex inside a Docker container

pdf2htmlex can be bothersome to install. This Dockerfile allows you to use it as a process or as a webservice responding to POST requests.

## Usage
### As a process
```bash
docker build -t pdf2htmlex .
wget http://www.xmlpdf.com/manualfiles/hello-world.pdf
cat hello-world.pdf | docker run -i pdf2htmlex python3 /tmp/process_stdin.py > hello-world.html
```

### As a webservice
Might be to use it from another Docker container.

```bash
docker build -t pdf2htmlex .
docker run -d --name pdf2htmlex pdf2htmlex

wget http://www.xmlpdf.com/manualfiles/hello-world.pdf
PDF2HTMLEX_IP=`docker inspect --format '{{ .NetworkSettings.IPAddress }}' pdf2htmlex`
curl -F "file=@hello-world.pdf;" http://$PDF2HTMLEX_IP/ > hello-world.html
```

# Contributions welcomed!
Still to do: allow usage of pdf2htmlex options.
