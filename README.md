# 🎯 Project Overview

Every day, organizations generate thousands of security events from endpoints, firewalls, cloud services, identity providers, and applications. A Security Information and Event Management (SIEM) platform such as Microsoft Sentinel collects these logs and creates alerts when suspicious activity is detected.

The challenge is that not every alert represents a real attack. Security analysts must manually investigate each incident, determine its severity, gather additional context, and decide on the appropriate response. This process is repetitive, time-consuming, and often leads to alert fatigue—especially in environments that produce hundreds or thousands of alerts per day.

**SentinelAI** automates this investigation process by combining Microsoft Sentinel, Azure Logic Apps, and Azure OpenAI into an intelligent SOC automation platform.

Instead of requiring an analyst to manually review every incident, SentinelAI automatically gathers relevant incident details, sends them to an AI analysis engine, enriches the investigation with additional context, and generates actionable recommendations directly within Microsoft Sentinel.

Rather than replacing security analysts, SentinelAI acts as an AI-powered assistant that accelerates investigations, standardizes incident triage, and reduces the time required to respond to potential threats.

---

# ❓ Why SentinelAI?

Traditional Security Operations Centers face several challenges:

* Large numbers of security alerts every day
* Limited availability of experienced SOC analysts
* Slow manual investigations
* Inconsistent incident documentation
* High operational costs
* Alert fatigue caused by repetitive investigations

SentinelAI addresses these challenges by automating the repetitive parts of incident response while keeping security analysts in control of remediation decisions.

The result is:

* Faster incident investigations
* Better incident documentation
* Consistent security recommendations
* Reduced analyst workload
* Improved response times
* Scalable cloud-native automation

---

# 👥 Who Is This Project For?

SentinelAI is designed for anyone interested in modern Security Operations Center (SOC) workflows, including:

* SOC Analysts
* Security Engineers
* Cloud Security Engineers
* Cybersecurity Students
* Microsoft Sentinel Administrators
* DevSecOps Engineers
* Managed Security Service Providers (MSSPs)

The project also serves as a practical portfolio demonstrating SIEM, SOAR, cloud automation, and AI integration within Azure.

---

# 🚀 What Does SentinelAI Do?

Once deployed, SentinelAI continuously monitors incidents created inside Microsoft Sentinel.

Whenever a detection rule generates a new incident, the automation pipeline performs the following actions automatically:

1. Microsoft Sentinel creates a security incident.
2. An Automation Rule detects the new incident.
3. Azure Logic Apps launches the investigation workflow.
4. Incident details are collected, including:

   * Alert title
   * Severity
   * User accounts
   * Source IP addresses
   * Host information
   * Event timestamps
   * Detection rule metadata
5. The incident context is securely sent to Azure OpenAI.
6. AI analyzes the incident and generates:

   * Executive summary
   * Attack classification
   * Threat severity assessment
   * MITRE ATT&CK techniques
   * Indicators of Compromise (IOCs)
   * Recommended investigation steps
   * Suggested remediation actions
7. The AI-generated analysis is automatically posted back into the Sentinel incident as comments or enrichment.
8. Security analysts review the recommendations and determine whether additional investigation or containment actions are required.

This process reduces the amount of manual work required for every security incident while providing analysts with consistent, structured intelligence.

---

# 🛠️ Prerequisites

Before deploying SentinelAI, you will need access to the following Azure resources:

### Required Azure Services

* Microsoft Sentinel
* Azure Log Analytics Workspace
* Azure Logic Apps
* Azure OpenAI Service
* Azure Resource Group
* Azure Subscription

### Required Permissions

Your Azure account should have permissions to:

* Create Microsoft Sentinel Analytics Rules
* Create Automation Rules
* Deploy Logic Apps
* Access Azure OpenAI
* Create Managed Identities (optional)
* Read and update Sentinel incidents

### Recommended Knowledge

While not required, familiarity with the following technologies will make deployment easier:

* Microsoft Sentinel
* Kusto Query Language (KQL)
* Azure Portal
* Azure Logic Apps
* Azure OpenAI
* Incident Response
* Basic Cybersecurity Concepts

---

# 💡 How to Use SentinelAI

After deployment, no manual interaction is required during normal operation.

The platform works automatically whenever Microsoft Sentinel generates a new security incident.

A typical workflow looks like this:

```
User Authentication Event
           │
           ▼
Microsoft Sentinel Detection Rule
           │
           ▼
Security Incident Created
           │
           ▼
Automation Rule Triggered
           │
           ▼
Logic App Executes
           │
           ▼
Azure OpenAI Analysis
           │
           ▼
AI Generates Investigation Report
           │
           ▼
Incident Updated
           │
           ▼
SOC Analyst Reviews Results
           │
           ▼
Containment / Remediation
```

From the analyst's perspective, the only interaction required is reviewing the AI-generated analysis and deciding whether to:

* Close the incident
* Escalate the incident
* Investigate further
* Block malicious IPs
* Reset compromised accounts
* Trigger additional response actions

---

# 📈 Example Scenario

Imagine an attacker attempts to brute-force a privileged account.

Without SentinelAI:

* Alert appears in Sentinel.
* Analyst opens the incident.
* Analyst reviews logs.
* Analyst identifies source IP.
* Analyst researches attack pattern.
* Analyst maps MITRE ATT&CK techniques.
* Analyst documents findings.
* Analyst recommends remediation.

This process may take **15–30 minutes** per incident.

With SentinelAI:

* Alert appears.
* AI immediately analyzes the incident.
* MITRE ATT&CK techniques are identified.
* Indicators of Compromise are extracted.
* Risk level is assessed.
* Recommendations are generated.
* Findings are posted directly into the incident.

The analyst can begin investigating immediately with much of the repetitive analysis already completed, reducing investigation time to just a few minutes.


