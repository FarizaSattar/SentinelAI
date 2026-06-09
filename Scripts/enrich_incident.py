import json

from ioc_extractor import extract_iocs
from mitre_mapper import map_mitre
from severity_scorer import score_severity


def enrich_incident(incident: dict) -> dict:
    """
    Enrich Sentinel incident with:
    - IOC extraction
    - MITRE mapping
    - Risk scoring
    - Response recommendations
    """

    description = incident.get("description", "")
    severity = incident.get("severity", "Low")

    iocs = extract_iocs(description)
    mitre = map_mitre(description)

    ioc_count = len(iocs["ips"]) + len(iocs["domains"]) + len(iocs["hashes"])

    risk_score = score_severity(severity, ioc_count)

    return {
        "title": incident.get("title"),
        "severity": severity,
        "risk_score": risk_score,
        "summary": description,
        "iocs": iocs,
        "mitre": mitre,
        "recommendations": [
            "Review authentication logs",
            "Check source IP reputation",
            "Block malicious indicators",
            "Reset compromised credentials if needed",
            "Enforce MFA",
            "Investigate lateral movement"
        ]
    }


if __name__ == "__main__":
    sample = {
        "title": "Suspicious Login Activity",
        "severity": "High",
        "description": "Multiple failed logins from 185.34.22.11 targeting login.microsoftonline.com"
    }

    result = enrich_incident(sample)
    print(json.dumps(result, indent=2))
