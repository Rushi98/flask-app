# Usage
## Using [docker](https://www.docker.com/get-started)
```sh
docker-compose up
```

## Virtualenv
### Installation
```sh
python -m venv flask
source flask/bin/activate
pip install --no-cache-dir -r requirements.txt
```
### Running
```sh
cd flask-app
source flask/bin/activate
export FLASK_RUN_PORT=8080
flask run --host=0.0.0.0
```

# References:
1. Flask Quickstart: https://flask.palletsprojects.com/en/2.0.x/quickstart/
2. requirements.txt file format: https://pip.pypa.io/en/stable/reference/requirements-file-format/
3. Dockerfile reference: https://docs.docker.com/engine/reference/builder/
4. docker-compose.yml reference: https://docs.docker.com/compose/
5. Flask templates: https://flask.palletsprojects.com/en/2.0.x/tutorial/templates/
6. "Sending form data" MDN Web Docs: https://developer.mozilla.org/en-US/docs/Learn/Forms/Sending_and_retrieving_form_data
