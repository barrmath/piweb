# piweb
Petit site internet sur Raspberry Pi<br>
<br>
Prérequis : Podman<br>
<br>
Construction du container :

```bash
podman build .
```

<br>
chargement du container :<br>

```bash
podman run -p 5000:5000 web_app:latest -d   
```