# 🔗 QRBot — Telegram URL Shortener Bot

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![python-telegram-bot](https://img.shields.io/badge/Telegram%20Bot-13.11-0088cc?logo=telegram&logoColor=white)
![pyshorteners](https://img.shields.io/badge/pyshorteners-1.0.1-purple)
![License](https://img.shields.io/badge/license-MIT-green)
![Platform](https://img.shields.io/badge/platform-Serverless-orange)

A lightweight Telegram bot that shortens URLs on the fly. Send a long link and get a short one back instantly — powered by the `ttm.sh` shortener service.

---

## ✨ Features

- 🔗 **Instant URL Shortening** — Send any URL, get a shortened link back
- 🧠 **Smart URL Extraction** — Regex-based parser extracts URLs from plain text
- ⚡ **Serverless Ready** — Designed for Google Cloud Functions / similar platforms
- 🤖 **Minimal Footprint** — Zero bloat, single-file bot logic

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| **Python 3** | Core runtime |
| **python-telegram-bot** | Telegram Bot API |
| **pyshorteners** | URL shortening via `ttm.sh` |
| **Google Cloud Functions** | Serverless deployment (webhook mode) |

---

## 📦 Installation

### Prerequisites

- Python 3.8+
- A Telegram Bot token from [@BotFather](https://t.me/BotFather)

### Steps

```bash
# Clone the repo
git clone https://github.com/Fahad-BA/QRBot.git
cd QRBot

# Install dependencies
pip install -r requirements.txt

# Set your bot token
# Edit main.py and replace the TelegramBot variable with your token

# Deploy as a Cloud Function or run locally with a webhook
```

---

## 🚀 Usage

### How It Works

1. Send any message containing a URL to the bot
2. The bot extracts the URL using regex
3. The URL is shortened via `ttm.sh`
4. The shortened link is sent back instantly

### Deploy as a Cloud Function

The bot uses a `webhook` function entry point, compatible with Google Cloud Functions:

```bash
gcloud functions deploy qrbot \
  --runtime python39 \
  --trigger-http \
  --entry-point webhook
```

Set the Telegram webhook to point to your Cloud Function URL:

```
https://api.telegram.org/bot<TOKEN>/setWebhook?url=<YOUR_FUNCTION_URL>
```

---

## 📁 Project Structure

```
QRBot/
├── main.py             # Bot logic (URL extraction + shortening)
├── requirements.txt    # Python dependencies
├── Procfile            # Worker declaration
└── .gitignore
```

---

## 📝 License

This project is licensed under the MIT License.
