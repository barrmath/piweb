# piweb
Petit site internet sur Raspberry Pi<br>
<br>
Prérequis : Podman<br>
<br>
Construction du container :

```bash
podman build -f Dockerfile.gunicorn -t web_app 
```

<br>
chargement du container :<br>

```bash
podman run -d -p 5000:5000 web_app:latest    
```