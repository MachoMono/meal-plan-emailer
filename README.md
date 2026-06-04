# Meal Plan Prompt Emailer

Every two weeks, this app emails you a ready-to-paste prompt that tells Claude (in your browser) to build a themed 2-week dinner + snack + dessert plan and add all the ingredients to your HEB cart — without checking out, so you can review before anything is purchased.

## Setup

1. Fork or clone this repo to your own GitHub account.
2. Add three repository secrets under **Settings → Secrets and variables → Actions**:
   - `RESEND_API_KEY` — from your [Resend](https://resend.com) dashboard
   - `RESEND_FROM_ADDRESS` — a verified sender address in Resend (e.g. `onboarding@resend.dev` for testing, then your own domain)
   - `RECIPIENT_EMAIL` — where you want the prompt delivered
3. Enable Actions on the repo (Actions tab → enable if prompted).
4. Done. The workflow runs every Sunday at 8 am Central and emails you on even ISO weeks (~every 2 weeks).

## Testing locally

```bash
cp .env.example .env
# Fill in real values in .env, then:
export $(grep -v '^#' .env | xargs)
python src/main.py --dry-run --force
```

`--dry-run` prints the email to stdout without sending or touching `history.json`.  
`--force` bypasses the even-week gate.

## Manual trigger

Go to **Actions → Biweekly meal-plan emailer → Run workflow**. Check "force" to run regardless of week parity.

## Editing

| What to change | Where |
|---|---|
| Cuisine themes | Top of `src/themes.py` — edit the `THEMES` list |
| Prompt body (dietary prefs, budget, pantry) | `src/prompt_template.md` |
| Send schedule | `cron:` line in `.github/workflows/biweekly.yml` |

## Troubleshooting

If no email arrives after a scheduled run, open the **Actions** tab, click the workflow run, and read the logs. Common causes: expired/wrong secret, unverified Resend sender domain, or an off-week run without `--force`.
