import os
import re
from text import MIN_LENGTH, SYMBOLS

_lower_re = re.compile(r"[a-z]")
_upper_re = re.compile(r"[A-Z]")
_digit_re = re.compile(r"\d")
_symbol_re = re.compile("[" + re.escape(SYMBOLS) + "]")
_repeat_re = re.compile(r"(.)\1{2,}")  # 3+ repeated same chars, e.g. 'aaa'
_seq_re = re.compile(r"(?:0123|1234|2345|3456|4567|5678|6789|abcd|bcde|cdef|defg|qwerty)")

def load_common_passwords(path: str) -> set[str]:
    if not os.path.exists(path):
        return set()
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return {line.strip() for line in f if line.strip()}

def requirements_check(pw: str) -> dict:
    return {
        "length": len(pw) >= MIN_LENGTH,
        "lower": bool(_lower_re.search(pw)),
        "upper": bool(_upper_re.search(pw)),
        "digit": bool(_digit_re.search(pw)),
        "symbol": bool(_symbol_re.search(pw)),
    }

def unmet_requirements(checks: dict) -> list[str]:
    names = {
        "length": f"Length < {MIN_LENGTH}",
        "lower": "No lowercase letter",
        "upper": "No uppercase letter",
        "digit": "No digit",
        "symbol": "No symbol",
    }
    return [names[k] for k, ok in checks.items() if not ok]

def score_password(pw: str, common_set: set[str]) -> tuple[int, list[str]]:
    """
    Return (score 0-100, issues list)
    """
    issues = []

    # Immediately fail if it's a known common password
    if pw.lower() in common_set:
        return 0, ["Password is in the top 1000 most common list"]

    checks = requirements_check(pw)
    issues.extend(unmet_requirements(checks))

    # Start scoring
    score = 0

    # Length: up to 40 pts (8->10, 12->20, 16->30, 20+->40)
    L = len(pw)
    if L >= 20:
        score += 40
    elif L >= 16:
        score += 30
    elif L >= 12:
        score += 20
    elif L >= 8:
        score += 10
    else:
        score += 0  # too short

    # Variety: up to 40 pts (10 each)
    for ok in checks.values():
        # we only want lower/upper/digit/symbol (length already counted)
        pass
    variety = sum([
        checks["lower"], checks["upper"], checks["digit"], checks["symbol"]
    ]) * 10
    score += variety

    # Repeats / sequences penalties: up to -20
    if _repeat_re.search(pw):
        score -= 10
        issues.append("Contains 3+ repeated characters in a row")
    if _seq_re.search(pw.lower()):
        score -= 10
        issues.append("Contains an obvious sequence (e.g., '1234', 'abcd', 'qwerty')")

    # Bonus for longer truly varied passwords: up to +20
    if L >= 12 and variety >= 30:
        score += min(20, (L - 12) * 2)

    # Clamp 0..100
    score = max(0, min(100, score))

    # If any core requirement is missing, cap at 40 to discourage weak structure
    if not all(checks.values()):
        score = min(score, 40)

    return score, issues

def label_for_score(score: int, labels) -> str:
    chosen = labels[0][1]
    for threshold, name in labels:
        if score >= threshold:
            chosen = name
        else:
            break
    return chosen