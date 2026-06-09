def score_severity(severity: str, ioc_count: int) -> int:
    """
    Generate a risk score based on severity + number of IOCs.
    """
    base_scores = {
        "Low": 20,
        "Medium": 50,
        "High": 75,
        "Critical": 95
    }

    base = base_scores.get(severity, 20)

    # IOC impact increases risk score
    bonus = min(ioc_count * 3, 15)

    return min(base + bonus, 100)
