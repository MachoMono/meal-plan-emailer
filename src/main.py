import argparse
import json
import os
import sys
from datetime import date, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

from emailer import send_email
from themes import pick_themes

HISTORY_FILE = Path(__file__).parent.parent / "history.json"
TEMPLATE_FILE = Path(__file__).parent / "prompt_template.md"


def next_monday(tz_name: str = "America/Chicago") -> date:
    today = date.today()
    days_ahead = (7 - today.weekday()) % 7 or 7  # Monday=0; always next Monday
    return today + timedelta(days=days_ahead)


def load_history() -> list[str]:
    if not HISTORY_FILE.exists():
        return []
    data = json.loads(HISTORY_FILE.read_text())
    return data.get("history", [])


def save_history(history: list[str]) -> None:
    HISTORY_FILE.write_text(json.dumps({"history": history}, indent=2))


def build_body(week1: str, week2: str) -> str:
    template = TEMPLATE_FILE.read_text()
    return template.replace("{{WEEK1_THEME}}", week1).replace("{{WEEK2_THEME}}", week2)


def build_subject(week1: str, week2: str) -> str:
    monday = next_monday()
    mon_str = monday.strftime("%-m/%-d")
    return f"Grocery prompt — {week1} / {week2} (week of {mon_str})"


def is_on_week() -> bool:
    return date.today().isocalendar().week % 2 == 0


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--force", action="store_true", help="Skip schedule gate")
    parser.add_argument("--dry-run", action="store_true", help="Print email, don't send")
    args = parser.parse_args()

    if not args.force and not is_on_week():
        sys.exit(0)

    history = load_history()
    week1, week2 = pick_themes(history)

    subject = build_subject(week1, week2)
    body = build_body(week1, week2)

    if args.dry_run:
        print(f"Subject: {subject}\n")
        print(body)
        return

    send_email(subject, body)
    save_history(history)


if __name__ == "__main__":
    main()
