import random

THEMES = [
    "Mediterranean",
    "Tex-Mex",
    "Japanese",
    "Italian",
    "Thai",
    "Korean",
    "Indian",
    "French bistro",
    "BBQ Southern",
    "Vietnamese",
    "Middle Eastern",
    "Cajun",
    "Greek",
    "Chinese (Sichuan or Cantonese)",
    "Spanish tapas",
    "Moroccan",
    "Filipino",
    "Peruvian",
]


def pick_themes(history: list[str]) -> tuple[str, str]:
    for exclusion_window in (6, 4, 2, 0):
        excluded = set(history[-exclusion_window:]) if exclusion_window else set()
        available = [t for t in THEMES if t not in excluded]
        if len(available) >= 2:
            chosen = random.sample(available, 2)
            history += chosen
            del history[:-12]
            return chosen[0], chosen[1]
    raise RuntimeError("Cannot pick 2 distinct themes from available list")
