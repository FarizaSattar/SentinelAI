import re

IP_REGEX = r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b"
DOMAIN_REGEX = r"\b(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}\b"
HASH_REGEX = r"\b[a-fA-F0-9]{32,64}\b"


def extract_iocs(text: str) -> dict:
    """
    Extract Indicators of Compromise (IOCs) from incident text.
    """
    ips = re.findall(IP_REGEX, text)
    domains = re.findall(DOMAIN_REGEX, text)
    hashes = re.findall(HASH_REGEX, text)

    # Remove false positives (IPs inside domain matches)
    domains = [d for d in domains if not re.match(IP_REGEX, d)]

    return {
        "ips": sorted(set(ips)),
        "domains": sorted(set(domains)),
        "hashes": sorted(set(hashes))
    }
