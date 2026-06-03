# SentinelAI 🛡️🤖  
**AI-Powered SOC Automation with Microsoft Sentinel + ChatGPT**

SentinelAI is a security operations automation project that integrates Microsoft Sentinel (SIEM/SOAR) with AI (ChatGPT / Azure OpenAI) to automate incident triage, enrichment, and response recommendations.

It simulates a modern Security Operations Center (SOC) workflow where security incidents are automatically analyzed, summarized, and enriched with actionable intelligence.

---

## 🚀 What This Project Does

When a security incident is triggered in Microsoft Sentinel:

- Microsoft Sentinel detects suspicious activity using analytics rules  
- An automation rule triggers a Logic App playbook  
- Incident data is sent to an AI model (ChatGPT / Azure OpenAI)  
- AI analyzes the incident and returns:
  - Attack type classification  
  - Suspicious IPs and domains  
  - Threat summary  
  - Recommended investigation steps  
- The AI response is written back into the Sentinel incident as a comment  

---

## 🧠 Key Features

- Automated SOC incident triage  
- AI-powered incident summarization  
- IOC (Indicators of Compromise) extraction  
- Security recommendations generation  
- Microsoft Sentinel automation rules integration  
- Azure Logic Apps (Playbooks) orchestration  
- Extensible SOC automation architecture  

---

## 🏗️ Architecture Overview

Sentinel Alert  
↓  
Analytics Rule (KQL Detection)  
↓  
Automation Rule Trigger  
↓  
Logic App Playbook  
↓  
Azure OpenAI / ChatGPT  
↓  
AI Analysis Output  
↓  
Sentinel Incident Comment Update  

---

## 📁 Project Structure

SentinelAI/
│
├── playbooks/              # Logic App workflow templates (SOC automation + AI playbooks)
├── automation/             # Microsoft Sentinel automation rules (trigger logic + conditions)
├── analytics/              # KQL detection rules for incident generation
├── scripts/                # Helper scripts for incident parsing, enrichment, and analysis
├── docs/                   # Architecture diagrams and SOC workflow documentation
├── .env.example            # Environment variables template (API keys, workspace IDs, etc.)
└── README.md               # Project documentation and setup guide

---

## ⚙️ Setup Instructions

### 1. Enable Microsoft Sentinel
Enable Microsoft Sentinel on an Azure Log Analytics Workspace.

---

### 2. Import Analytics Rules
Deploy the KQL detection rules located in:

/analytics/sentinel-analytics-rule.json


---

### 3. Configure Automation Rule
Import the automation rule from:

/automation/sentinel-automation-rule.json


Make sure it is enabled and linked to the correct playbook.

---

### 4. Deploy Logic App Playbook
Deploy the Logic App using:

/playbooks/chatgpt-incident-playbook.json


Configure:
- Azure OpenAI endpoint OR OpenAI API key  
- Sentinel incident permissions (RBAC)  
- HTTP connectors for API calls  

---

### 5. Configure Environment Variables

Copy `.env.example` and fill in your values:

OPENAI_API_KEY=your_api_key_here
SENTINEL_WORKSPACE_ID=your_workspace_id
AZURE_TENANT_ID=your_tenant_id
AZURE_SUBSCRIPTION_ID=your_subscription_id
LOGIC_APP_URL=your_logic_app_url


---

## 🔐 Security Considerations

- Do NOT send production incident data to public LLM APIs  
- Prefer Azure OpenAI for enterprise deployments  
- Store secrets in Azure Key Vault instead of `.env` in production  
- Apply RBAC restrictions to Logic Apps and Sentinel workspace  
- Audit all API calls for compliance  

---

## 📊 Example AI Output

**Incident Summary:**  
Multiple failed login attempts detected from external IP addresses.

**Indicators of Compromise (IOCs):**
- IP: 185.xxx.xxx.xxx  
- IP: 91.xxx.xxx.xxx  
- Domain: suspicious-login-site[.]com  

**Attack Type:**  
Credential Brute Force / Unauthorized Access Attempt  

**Recommended Actions:**
- Block offending IP addresses at firewall level  
- Reset affected user credentials  
- Enforce MFA for impacted accounts  
- Investigate lateral movement activity  

---

## 🎯 Skills Demonstrated

This project demonstrates practical experience in:

- Microsoft Sentinel (SIEM engineering)  
- SOC automation (SOAR workflows)  
- KQL detection engineering  
- Azure Logic Apps integration  
- AI-driven security analysis  
- API integration with OpenAI / Azure OpenAI  
- Incident response automation pipelines  
- Cloud security architecture design  

---

## 💼 Resume Impact

This project is designed to demonstrate job-ready SOC engineering skills, including:

- Automating Tier 1 SOC analyst workflows  
- Reducing incident response time using AI  
- Building scalable security automation pipelines  
- Integrating AI into enterprise security operations  
- Working with real-world SIEM/SOAR systems  

---

## 📌 Future Improvements

- MITRE ATT&CK framework mapping integration  
- Real-time streaming with Azure Event Hub  
- Microsoft Defender for Cloud integration  
- Multi-tenant SOC automation support  
- Threat intelligence enrichment feeds  
- Advanced correlation engine for incidents  

---

## 🧠 Inspiration

Built from enterprise SOC engineering practices using:

- Microsoft Sentinel  
- Azure Logic Apps  
- AI-assisted security operations workflows  
- Modern SOC automation principles  

---

## 📜 License

MIT License — for educational and portfolio use
