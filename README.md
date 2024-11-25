# Simple TTS API

This is a simple barebone API for an app to convert text to speech.

### Installing Python requirements

```bash
pip install -r requirements.txt
```

### Database

Setup a local PostgreSQL database and update the `.env` file with the correct credentials.

### How to run

* Create `.env` file: `touch .env`
.env example

```
DB_NAME=tts
DB_USER=tts
DB_PASSWORD=tts
DB_HOST=localhost
DB_PORT=5432
SECRET_KEY=your-secret-key-here
```

Run migrations: `python manage.py migrate`

Run the server: `python manage.py runserver`

### Formatting

This project uses `black` for formatting.
flake8 is used for linting.
isort is used for sorting imports.

### Testing

Run tests: `python manage.py test`

For basic API tests