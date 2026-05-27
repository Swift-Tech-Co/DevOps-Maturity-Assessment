"""
DevOps Maturity Self-Assessment
Swift Tech Co. — https://swifttechco.com

Scores DevOps maturity across 7 dimensions and identifies top improvement areas.
Each question is scored 0 (basic), 1 (developing), or 2 (advanced).
"""

QUESTIONS = [
    {
        "id":   "cicd",
        "label": "CI/CD pipeline",
        "options": [
            "No CI/CD: manual deploys",
            "Partial: some automation",
            "Full CI/CD: auto-deploy on merge",
        ],
    },
    {
        "id":   "iac",
        "label": "Infrastructure as Code",
        "options": [
            "Manual server config",
            "Partial IaC (some scripts)",
            "Full IaC (Terraform/Pulumi)",
        ],
    },
    {
        "id":   "mon",
        "label": "Monitoring & alerting",
        "options": [
            "No monitoring",
            "Basic uptime checks",
            "Full observability (logs + metrics + traces)",
        ],
    },
    {
        "id":   "dep",
        "label": "Deployment time",
        "options": [
            "> 30 min or manual",
            "5 to 30 minutes",
            "< 5 minutes (automated)",
        ],
    },
    {
        "id":   "test",
        "label": "Automated test coverage",
        "options": [
            "No automated tests",
            "< 50% coverage",
            "> 80% coverage",
        ],
    },
    {
        "id":   "env",
        "label": "Environment setup",
        "options": [
            "Production only",
            "Dev + Production",
            "Dev + Staging + Production",
        ],
    },
    {
        "id":   "dr",
        "label": "Disaster recovery",
        "options": [
            "No plan",
            "Documented but untested",
            "Documented + tested regularly",
        ],
    },
]


def calculate(answers: dict) -> dict:
    """
    Args:
        answers: dict mapping question id to answer index (0, 1, or 2).
                 E.g. {"cicd": 2, "iac": 1, "mon": 0, "dep": 1, "test": 1, "env": 2, "dr": 0}

    Returns:
        dict with keys: score, pct, level, gaps
    """
    required = {q["id"] for q in QUESTIONS}
    missing  = required - set(answers.keys())
    if missing:
        raise ValueError(f"Missing answers for: {', '.join(sorted(missing))}")

    score = sum(answers.get(q["id"], 0) for q in QUESTIONS)
    pct   = round(score / (len(QUESTIONS) * 2) * 100)

    if pct <= 25:
        level = "Basic"
    elif pct <= 50:
        level = "Developing"
    elif pct <= 75:
        level = "Advanced"
    else:
        level = "Elite"

    gaps = [q["label"] for q in QUESTIONS if answers.get(q["id"], 0) < 2]

    return {
        "score": score,
        "pct":   pct,
        "level": level,
        "gaps":  gaps,
    }
