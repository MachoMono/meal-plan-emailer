import os
import smtplib
import sys
from email.mime.text import MIMEText

import requests


def send_email(subject: str, body: str) -> None:
    provider = os.environ.get("EMAIL_PROVIDER", "resend").lower()
    recipient = os.environ["RECIPIENT_EMAIL"]

    if provider == "smtp":
        _send_smtp(subject, body, recipient)
    else:
        _send_resend(subject, body, recipient)


def _send_resend(subject: str, body: str, recipient: str) -> None:
    api_key = os.environ["RESEND_API_KEY"]
    from_address = os.environ["RESEND_FROM_ADDRESS"]

    response = requests.post(
        "https://api.resend.com/emails",
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
        json={"from": from_address, "to": recipient, "subject": subject, "text": body},
        timeout=15,
    )

    if not response.ok:
        print(f"Resend error {response.status_code}: {response.text}", file=sys.stderr)
        sys.exit(1)

    print(f"Email sent via Resend to {recipient}")


# Gmail SMTP fallback — set EMAIL_PROVIDER=smtp to use
def _send_smtp(subject: str, body: str, recipient: str) -> None:
    user = os.environ["SMTP_USER"]
    password = os.environ["SMTP_PASS"]

    msg = MIMEText(body, "plain")
    msg["Subject"] = subject
    msg["From"] = user
    msg["To"] = recipient

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(user, password)
        server.sendmail(user, recipient, msg.as_string())

    print(f"Email sent via SMTP to {recipient}")
