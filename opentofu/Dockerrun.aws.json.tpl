{
  "AWSEBDockerrunVersion": "1",
  "Image": {
    "Name": "${image_name}",
    "Update": "true"
  },
  "Entrypoint": "gunicorn",
  "Command": "--bind 0.0.0.0:8000 --workers 3 website.wsgi"
}
