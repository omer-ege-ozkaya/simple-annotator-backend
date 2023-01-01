# Simple Annotator Backend

Author: Omer Ege Ozkaya

This projects simply handles http requests with Annotation JSON-LD bodies and inserts them in MongoDB.
"ID" field is manipulated by this backend for the annotation to refer to itself.


annotation-model.js is from https://github.com/goodmansasha/annotation-model.

## How to use?
Setting up the backend and the database:
```
# Create and start mongodb container.
docker compose up

# Activate venv
source venv/bin/activate

# Run backend server (Python 3.11.1)
python run.py
```
Open `testpage.html` from a browser. Select a text. Annotate.

You might watch the logs from "Developer Tools Console" of the browser. You might also keep an eye on the logs of the run.py and MongoDB logs.

Note: This project still have missing functionality!
