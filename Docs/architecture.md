# 📄 Docs/architecture.md

# 🏗️ Architecture Overview

## 🔄 High-Level Flow

Sentinel Alert  
↓  
Analytics Rule (KQL Detection)  
↓  
Automation Rule Trigger  
↓  
Azure Logic App Playbook  
↓  
Azure OpenAI / GPT Model  
↓  
AI Response (Structured JSON)  
↓  
Sentinel Incident Update  
↓  
SOC Analyst Review  

---

## 🧩 Core Components

### 🛡️ Microsoft Sentinel (SIEM)
- Central security monitoring platform
- Ingests logs from Azure AD, endpoints, cloud services
- Executes KQL analytics rules
- Generates security incidents

---

### ⚙️ Analytics Rules
- KQL-based detection logic
- Identifies suspicious authentication patterns
- Triggers incidents based on thresholds

---

### 🤖 Automation Rules (SOAR Layer)
- Routes incidents to playbooks
- Applies tagging and severity-based routing
- Reduces manual SOC workload

---

### 🔗 Logic Apps (Playbooks)
- Orchestrates incident workflow
- Sends data to Azure OpenAI
- Processes AI response
- Updates Sentinel incident

---

### 🧠 AI Layer (Azure OpenAI)
- Classifies attack type
- Extracts IOCs (IPs, domains)
- Maps MITRE ATT&CK techniques
- Generates remediation steps

---

## 📊 Output Structure

AI returns structured security intelligence:

- Incident summary  
- Threat classification  
- IOC list  
- MITRE ATT&CK mapping  
- Recommended actions  
- Risk scoring  

---

## 🎯 Key Design Principles

- Event-driven architecture  
- Serverless-first design  
- API-driven orchestration  
- Scalable SOC automation  
- AI-assisted triage (human-in-the-loop)  
