MITRE_MAP = {
    "brute force": {
        "technique": "T1110",
        "tactic": "Credential Access"
    },
    "password spray": {
        "technique": "T1110.003",
        "tactic": "Credential Access"
    },
    "phishing": {
        "technique": "T1566",
        "tactic": "Initial Access"
    },
    "impossible travel": {
        "technique": "T1078",
        "tactic": "Valid Accounts"
    },
    "malware": {
        "technique": "T1204",
        "tactic": "Execution"
    },
    "suspicious login": {
        "technique": "T1078",
        "tactic": "Credential Access"
    }
}


def map_mitre(text: str) -> dict:
    """
    Map incident text to MITRE ATT&CK technique and tactic.
    """
    text = text.lower()

    for keyword, mapping in MITRE_MAP.items():
        if keyword in text:
            return mapping

    return {
        "technique": "Unknown",
        "tactic": "Unknown"
    }
