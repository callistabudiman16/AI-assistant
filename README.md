# 🎙️ AI Interviewer Generator

An AI-powered web application that generates **structured, company-tailored interview responses** using **Google’s Gemini 2.5 Flash API**.  

---

## 📘 Overview

The **AI Interviewer Generator** helps job seekers and students **simulate realistic interview scenarios**.  
Users input a company, role, product domain, and interview category, and the app generates:

- A relevant, realistic interview question  
- A JSON-formatted answer structured by recognized frameworks (e.g., 5C-PRD, ICE-R, 3E, MVM)  
- Key metrics, pacing guidance, and red-flag insights  

This project demonstrates how **prompt engineering** transforms raw AI output into **consistent, high-quality, and professional responses** aligned with company values and frameworks.

---

## 🎯 Problem Statement

Interview preparation is often **unstructured, time-consuming, and generic**.  
Most online tools provide repetitive question lists that fail to reflect the **company context**, **role expectations**, or **domain complexity**.

**Goal:**  
Create a tool that generates **authentic, framework-based interview responses** customized to each company’s mission, values, and product domain — using **prompt engineering techniques** to optimize AI behavior.

---

## 💡 Solution

The **AI Interviewer Generator** solves this by:
- Using **prompt templates** tailored to company, role, and category  
- Structuring responses into industry frameworks (like **5C-PRD**, **ICE-R**, **3E**)  
- Returning **clean, parseable JSON** for consistent display  
- Applying **prompt engineering patterns** (Persona, Few-Shot, Iterative Refinement) to ensure accuracy, tone, and realism  

---

## 🧠 Prompt Engineering Techniques

This project applies **two prompt engineering patterns** to achieve optimal AI behavior.

---

### 🧍 Persona Prompt Pattern
**Technique:**  
The AI is instructed to *act as a senior interviewer* representing a specific company and role.

```text
You are a senior interviewer. Generate a concise answer that returns ONLY valid JSON (no prose, no backticks).
Audience: {company} interview panel.
Role: {role}.
Domain: {product_domain}.
Duration to speak: {duration_minutes} minutes.

Mission: {mission}
Top values: {values_csv}

Category: {category}
Allowed categories: ["Product Sense", "Execution", "Leadership & Collaboration", "Analytical & Impact", "System Design", "Coding & Algorithms", "Technical Architecture", "Problem Solving", "Data Structures", "Database Design", "API Design", "Security & Scalability", "Code Review & Testing"]
...
```

---

### ✍️ Few-Shot Prompt Pattern

**Technique:**  
This pattern involves providing a **series of examples as context**, which the AI uses to understand the format, tone, and type of response expected.  
After the examples, a new prompt is given, the AI then generates a similar type of output by learning from those examples.




