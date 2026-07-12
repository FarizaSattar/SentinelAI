# 🛡️ SentinelAI
### An AI-powered assistant for security teams, built on Microsoft Sentinel + Azure OpenAI

## 👋 What is this?

Imagine you're a security analyst, and every day hundreds (sometimes thousands) of alerts show up in your queue — most of them harmless, but a few might be a real attacker trying to break in. Investigating each one by hand is slow, repetitive, and exhausting. That exhaustion has a name in the industry: **alert fatigue**.

SentinelAI is my attempt to help with that. It connects **Microsoft Sentinel** (a security monitoring platform) with **Azure OpenAI**, so that the moment a suspicious incident is created, an AI assistant automatically investigates it — pulling together the relevant details, identifying attack patterns, and writing up a clear, structured summary — all before a human analyst even opens the ticket.

**Important:** SentinelAI doesn't replace analysts or make decisions on its own. Think of it as a very fast, very thorough assistant that hands you a head start, while a person stays in control of what actually happens next.

## ❓ Why I built this

Security teams face a tough balancing act: attacks need fast responses, but experienced analysts are limited and every incident takes real time to investigate properly. I wanted to see whether AI could take on the repetitive first-pass work — gathering context, mapping techniques, summarizing risk — so analysts could spend their time on judgment calls instead of data-gathering.

## 🚀 What it actually does

When Microsoft Sentinel flags something suspicious, here's what happens automatically, with zero manual steps:

1. **An incident is created** — say, a possible brute-force login attempt.
2. **Azure Logic Apps kicks off the investigation** — gathering the alert details: who, what IP, what device, when, and which rule triggered.
3. **That context is sent to Azure OpenAI**, which analyzes it and generates:
   - A plain-English executive summary
   - What kind of attack this looks like
   - How severe it is
   - Which MITRE ATT&CK techniques are involved (a standard framework for classifying attacker behavior)
   - Indicators of Compromise (IOCs) — the technical fingerprints of the attack
   - Recommended next steps
4. **All of this gets posted right back into the Sentinel incident**, ready for a human to review.

From there, the analyst just decides: close it, escalate it, block an IP, reset a password — whatever the situation calls for.

## 📈 Why it matters — a quick example

Picture someone trying to brute-force their way into a privileged account.

**Without SentinelAI:** an analyst opens the alert, digs through logs, tracks down the source IP, researches the attack pattern, manually maps it to MITRE ATT&CK, writes it all up, and recommends next steps. That's realistically **15–30 minutes**, per incident, all day long.

**With SentinelAI:** by the time the analyst opens the incident, the AI has already done all of that — attack classification, IOCs, risk level, and recommendations are sitting right there. Investigation time drops to just a few minutes.

## 👥 Who this is for

Whether you're deep in security operations or just curious how AI fits into cybersecurity, there's something here for you:

- SOC analysts and security engineers looking to speed up triage
- Cloud security folks working in Azure environments
- Cybersecurity students who want a real example of SIEM + SOAR + AI working together
- Anyone curious how "AI in cybersecurity" actually works under the hood, beyond the buzzwords

## 🛠️ What you'll need to try it

**Azure services:**
Microsoft Sentinel · Log Analytics Workspace · Logic Apps · Azure OpenAI Service · a Resource Group and Subscription

**Permissions:**
Enough access to create Sentinel rules, deploy Logic Apps, call Azure OpenAI, and read/update incidents.

**Helpful (not required) background:**
Microsoft Sentinel, Kusto Query Language (KQL), Logic Apps, and general incident response concepts. If those are new to you, the docs folder walks through deployment step by step.

## 💡 How it works, visually

```
Suspicious Login Attempt
        │
        ▼
Sentinel Detection Rule Fires
        │
        ▼
Incident Created
        │
        ▼
Logic App Automatically Triggers
        │
        ▼
Azure OpenAI Analyzes the Incident
        │
        ▼
AI Writes Up Findings & Recommendations
        │
        ▼
Analyst Reviews & Decides Next Steps
        │
        ▼
Contained / Resolved
```

## 🧰 Built with

Python · Microsoft Sentinel · Azure Logic Apps · Azure OpenAI · KQL
