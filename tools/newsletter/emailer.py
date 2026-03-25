"""Send the daily newsletter via Gmail SMTP."""
from __future__ import annotations

import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path

CONFIG_PATH = Path(__file__).parent / "config.json"


def load_config() -> dict[str, str]:
    if not CONFIG_PATH.exists():
        raise FileNotFoundError(
            f"Email config not found at {CONFIG_PATH}\n"
            "Copy config.example.json → config.json and fill in your credentials."
        )
    return json.loads(CONFIG_PATH.read_text(encoding="utf-8"))


def send(subject: str, html_body: str) -> None:
    """Send an HTML email using the credentials in config.json."""
    cfg = load_config()

    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = cfg["from_email"]
    msg["To"] = cfg["to_email"]
    msg.attach(MIMEText(html_body, "html", "utf-8"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(cfg["from_email"], cfg["app_password"])
        server.sendmail(cfg["from_email"], cfg["to_email"], msg.as_string())

    print(f"✓ Newsletter sent to {cfg['to_email']}")
