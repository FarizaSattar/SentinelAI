import json

def extract_iocs(text):
    iocs = {
        "ips": [],
        "domains": []
    }

    for word in text.split():
        if word.count(".") == 3:
            iocs["ips"].append(word)
        if "." in word and len(word) > 4:
            iocs["domains"].append(word)

    return iocs


def format_incident(incident_json):
    summary = f"""
SOC INCIDENT SUMMARY
--------------------
Title: {incident_json.get('title')}
Severity: {incident_json.get('severity')}
Description: {incident_json.get('description')}
"""
    return summary


if __name__ == "__main__":
    sample = {
        "title": "Suspicious Login",
        "severity": "High",
        "description": "Multiple failed logins from foreign IP"
    }

    print(format_incident(sample))
    print(extract_iocs(sample["description"]))
