# 🚨 Incident Response Flow

## 🔍 Step 1: Detection
Microsoft Sentinel detects suspicious activity using KQL analytics rules.

---

## 🚨 Step 2: Incident Creation
A security incident is generated automatically in Sentinel.

---

## ⚙️ Step 3: Automation Trigger
Automation rule triggers the Logic App playbook.

---

## 🤖 Step 4: AI Analysis
Incident data is sent to Azure OpenAI for analysis.

AI performs:
- Threat classification  
- IOC extraction  
- Behavior analysis  
- MITRE ATT&CK mapping  

---

## 🧠 Step 5: AI Enrichment Output

AI returns structured output:

- Summary of incident  
- Attack type classification  
- List of IOCs  
- Severity assessment  
- Recommended actions  

---

## 📝 Step 6: Incident Update
Playbook writes AI response back into Sentinel incident as a comment.

---

## 👨‍💻 Step 7: SOC Analyst Review
Analyst:
- Reviews AI output  
- Validates threat  
- Takes containment actions  
- Escalates if necessary  

---

## 🔁 Continuous Improvement Loop

- Analyst feedback improves detection rules  
- KQL queries are refined  
- AI prompts are optimized  
- Automation becomes more accurate over time  
