# 🚀 Deployment Guide 

## 🧾 Prerequisites

Before deploying SentinelAI, ensure you have:

- Azure Subscription  
- Microsoft Sentinel enabled  
- Log Analytics Workspace  
- Azure OpenAI resource  
- Azure Logic Apps access  
- Contributor / Security Admin permissions  

---

## 🛡️ Step 1: Enable Microsoft Sentinel

1. Go to Azure Portal  
2. Open Log Analytics Workspace  
3. Enable Microsoft Sentinel  
4. Connect data sources (Azure AD, SignInLogs, etc.)  

---

## 📡 Step 2: Deploy Analytics Rules

Import KQL rules from:

```
/Analytics/
```

Deploy:
- suspicious-signin-rule.json  
- impossible-travel-rule.json  
- brute-force-detection-rule.json  

---

## ⚙️ Step 3: Configure Automation Rules

Import rules from:

```
/Automation/
```

Enable:
- Incident triggering rules  
- Severity-based escalation rules  

---

## 🤖 Step 4: Deploy Logic Apps (Playbooks)

Import:

```
/Playbooks/
```

Configure:
- Azure OpenAI endpoint  
- API keys  
- Sentinel incident permissions  
- HTTP connectors  

---

## 🔐 Step 5: Configure Environment Variables

Create `.env` from `.env.example`:

```env
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_KEY=
SENTINEL_WORKSPACE_ID=
AZURE_SUBSCRIPTION_ID=
AZURE_TENANT_ID=
LOGIC_APP_URL=
```

---

## 🧪 Step 6: Testing the System

1. Trigger failed login attempts  
2. Verify Sentinel incident creation  
3. Check automation rule execution  
4. Confirm AI enrichment response  
5. Validate incident update in Sentinel  

---

## 📊 Success Criteria

- Incident auto-created in Sentinel  
- Playbook executes successfully  
- AI returns structured response  
- IOC + MITRE mapping generated  
- Incident enriched automatically  
```
