# Parash GPT

Parash GPT is a lightweight Django chatbot API built to demonstrate a branded chatbot experience. It provides a minimal chat backend powered by the Groq chat API, and it responds to identity questions with: "I am Parash GPT made by Parash."

## Project structure

- `chatbot/` — Django project root and settings
- `chatbot/bot/` — chatbot app with API views and URLs
- `Frontend/` — static demo UI for local browser testing
- `.env` — local environment variables (kept out of source control)
- `.gitignore` — ignores virtualenvs, `.env`, database files, and editor artifacts

## Features

- `POST /api/chatbot/` JSON API endpoint
- Direct identity response for questions like "who are you" or "what is your name"
- CORS-friendly local frontend support
- Environment-based secret management via `.env`
- Basic production-ready settings with secrets outside source code
- `python-dotenv` support for local development

## Prerequisites

- Python 3.11+ installed
- `pip` available
- Optional: a virtual environment tool such as `venv`

## Setup

1. Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\activate
```

2. Install the required packages:

```powershell
pip install -r requirements.txt
```

3. Create a local `.env` file.

```powershell
copy .env.example .env
```

4. Edit `.env` and add your own values:

```env
DJANGO_SECRET_KEY=your-secret-key
DJANGO_DEBUG=True
GROQ_API_KEY=your-groq-api-key
```

5. Run the database migrations:

```powershell
python manage.py migrate
```

6. Start the server:

```powershell
python manage.py runserver
```

## API Usage

Send a POST request to:

```text
http://127.0.0.1:8000/api/chatbot/
```

Example request body:

```json
{
  "message": "Hello Parash GPT"
}
```

Example response body:

```json
{
  "reply": "Your bot response here"
}
```

## Frontend Demo

Open `Frontend/chatbot.html` directly in your browser after starting the Django server. The demo calls the backend API and displays the chat conversation.

## Environment variables

The project reads secrets from `.env` using `python-dotenv`:

- `DJANGO_SECRET_KEY` — Django secret key
- `DJANGO_DEBUG` — set `True` for development, `False` for production
- `GROQ_API_KEY` — the API key used by the Groq client

## Security

- Do not commit `.env` to source control.
- Keep your API keys and Django secret key private.
- Use a proper WSGI/ASGI server in production.

## Testing

Run Django tests with:

```powershell
python manage.py test
```

## Notes

This project is intended as a local development demo. For production deployment, use a production-grade server, configure allowed hosts, secure TLS, and store secrets in a safe secret manager.
