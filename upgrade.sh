git checkout main
git pull
podman build -f Dockerfile.gunicorn -t piweb
podman play kube gunicorn.yml --replace
