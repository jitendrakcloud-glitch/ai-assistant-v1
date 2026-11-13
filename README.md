# My AI Personal Assistant — Version 1

This is a beginner-friendly local AI chat app built with Python and Streamlit.

## Before you start

- Windows 10 or 11
- Python 3.10 or newer
- An OpenAI API key
- Internet access

**Important:** ChatGPT subscriptions and API billing are separate. API usage may incur charges. Never share your API key or upload your `.env` file.

## 1. Install Python

Download Python from https://www.python.org/downloads/ .
During installation, tick **Add Python to PATH**.

Open Command Prompt and check:

```bat
python --version
```

## 2. Open this project folder in Command Prompt

Change directory to the folder where you extracted this ZIP. Example:

```bat
cd %USERPROFILE%\Desktop\my_ai_personal_assistant
```

## 3. Create a virtual environment

```bat
python -m venv .venv
.venv\Scripts\activate
```

## 4. Install the packages

```bat
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## 5. Add your API key securely

1. Make a copy of `.env.example`.
2. Rename the copy to `.env` (make sure it is not named `.env.txt`).
3. Open `.env` in Notepad.
4. Replace `put_your_api_key_here` with your API key.
5. Save the file.

Create/manage API keys at https://platform.openai.com/api-keys .

Do not paste your key into chat, source code, screenshots, or public repositories.

## 6. Run the app

```bat
streamlit run app.py
```

A browser tab should open with your assistant. If it does not, copy the local URL shown in Command Prompt (usually http://localhost:8501) into your browser.

## 7. First tests

Try:
- "Help me plan my day."
- "Explain Python variables to a beginner."
- "Draft a polite email requesting a meeting."

## Troubleshooting

- If `python` is not recognized, reinstall Python and tick **Add Python to PATH**, then reopen Command Prompt.
- If `streamlit` is not recognized, activate `.venv` and run `python -m pip install -r requirements.txt`.
- If the app reports an API error, verify the key, API account billing/limits, internet access, and model availability.
- Keep `.env` private. The app runs locally on your computer by default.

## What Version 1 includes

- AI chat interface
- Multi-message conversation during the current browser session
- Clear conversation button
- API key loaded from a local `.env` file

Chat history is not yet saved permanently. We will add local storage, tasks, reminders, PDF and Excel tools in later versions.
