# Architecture Overview

## Flow Diagram

Sentinel Alert
   ↓
Analytics Rule
   ↓
Automation Rule Trigger
   ↓
Logic App Playbook
   ↓
Azure OpenAI / GPT Model
   ↓
AI Response (JSON)
   ↓
Sentinel Incident Comment Update

---

## Components

### Microsoft Sentinel
- Detects threats using KQL analytics rules

### Automation Rules
- Trigger playbooks automatically

### Logic Apps (Playbooks)
- Orchestrate data flow
- Call AI endpoint
- Format response

### AI Layer
- Extracts:
  - IPs
  - Domains
  - Threat type
  - MITRE mapping (optional)

---

## Output Example

- Incident summary
- Recommended actions
- IOC list
- Attack classification
