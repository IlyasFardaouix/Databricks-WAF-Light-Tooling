# 🔍 Databricks WAF Light Tooling

[![Documentation](https://img.shields.io/badge/docs-GitHub%20Pages-blue?style=flat-square)](https://abhidatabricks.github.io/Databricks-WAF-Light-Tooling/)

> 📖 **Full documentation & live demo video:** [abhidatabricks.github.io/Databricks-WAF-Light-Tooling](https://abhidatabricks.github.io/Databricks-WAF-Light-Tooling/)

---

## 🚀 Overview

**Databricks WAF Light Tooling** is a lightweight, automated assessment tool built to evaluate Databricks Lakehouse implementations against the **Well-Architected Framework (WAF)** principles. It analyzes system tables, logs, and metadata to generate real-time scores and actionable recommendations that drive better governance, security, performance, and cost-efficiency.

---

## ❗ Problem Statement

Building a secure, efficient, and well-governed Databricks Lakehouse requires continuous adherence to WAF principles. However, the assessments generally suffer from:

- ⏱️ Time-consuming processes  
- 🔁 Inconsistencies in evaluation  
- ⚙️ Lack of automation  

---

## 🌟 Opportunity Statement

A **WAF Tool** can solve these pain points by offering:

- ✅ Automated WAF assessments  
- 📊 Real-time scoring  
- 🛠 Actionable insights  

…empowering customers to continuously optimize their Databricks environments with minimal effort.

---

## 💡 Proposed Solution

Develop a **lightweight WAF assessment tool** that:

- Automates analysis using **System Tables**, **audit logs**, and **workspace metadata**  
- Provides **real-time scoring** against WAF pillars  
- Highlights **gaps and improvement opportunities**  
- Offers **low-friction deployment** for both internal teams and customers  

---

## 🛠 Existing Alternatives

- Many teams build **custom dashboards** for monitoring.
- These are often:
  - ❌ Manually maintained  
  - ❌ Inconsistent across customers  
  - ❌ Hard to scale or reuse  

**Databricks WAF Light Tooling** offers a reusable, scalable, and automated alternative.

---

## 👥 End Users

### 1. **Databricks Field Engineering**
- Solution Architects, Customer Success Engineers, and Pre-sales teams
- Use the tool to assess customer environments and recommend WAF-aligned improvements

### 2. **Databricks Customers**
- Data Engineers, Platform Admins, and Architects
- Self-assess their environments and improve governance, security, and cost efficiency

---

## 🎬 Demo

<video width="100%" controls>
  <source src="https://abhidatabricks.github.io/Databricks-WAF-Light-Tooling/WAF2.0Demo.mp4" type="video/mp4">
</video>

---

## 📦 Getting Started

### ⚙️ Installation

The WAF Assessment Tool can be installed in your Databricks workspace with a single notebook execution. The installation process automatically:

1. **Deploys the WAF Assessment Dashboard** - Creates a Lakeview dashboard with real-time WAF scores
2. **Publishes the Dashboard** - Configures it with a SQL warehouse for data queries
3. **Configures Embedding** - Sets up embedding domains for the Databricks App
4. **Deploys the Databricks App** - The central hub with embedded dashboard, Recommendations, Progress, Reload, and Genie access
5. **Updates Configuration** - Automatically configures dashboard IDs and workspace settings

#### Permissions Required by the Installer

Before running `install.ipynb`, ensure the person running it has:

| Permission | Why |
|---|---|
| **Workspace Admin** or **Apps Admin** | Required to deploy Databricks Apps |
| **CREATE CATALOG** on the metastore | Only needed if the target catalog does not exist yet |
| **CREATE SCHEMA** on the target catalog | To create the `waf_cache` schema |
| **SELECT on `system.*`** | WAF queries read `system.billing`, `system.compute`, `system.access`, etc. |
| **An existing SQL Warehouse** | Installer attaches it to publish the dashboard |
| **Workspace files access** | To upload app source files via Workspace API |

#### Quick Start

1. **Add the Repo to Databricks**
   - Go to **Workspace → Repos → Add Repo**
   - URL: `https://github.com/AbhiDatabricks/Databricks-WAF-Light-Tooling.git`
   - Branch: `main`

2. **Run `install.ipynb`**
   - Open `install.ipynb` from the repo
   - **Edit Cell 1**: set `catalog = "<your_catalog_name>"` (e.g. `"main"` or `"platform_shared"`)
   - **Run All Cells**
   - At the end you will see a full summary with ✅/❌ per step and direct links to the app, dashboard, Genie Space, and reload job

3. **Share Access** — see [Grant Access to Other Users](#-grant-access-to-other-users) below

#### Installation Options

- **Full Installation** (`install.ipynb`): Complete setup including dashboard, app, Genie Space, and reload job

**WAF Assessment App — main dashboard view:**

![WAF Assessment App Dashboard](assets/waf-app-dashboard.png?raw=true)

**WAF Recommendations (Not Met) — failing controls with actionable fixes:**

![WAF Recommendations Not Met](assets/waf-recommendations.png?raw=true)

![WAF Recommendations Detail](assets/waf-recommendations-detail.png?raw=true)

**WAF Assessment Progress — score trend over time:**

![WAF Assessment Progress](assets/waf-progress.png?raw=true)

### 🎯 What You Get

After installation, you'll have access to:

1. **WAF Assessment Dashboard** - Real-time scoring across 4 WAF pillars:
   - 🛡️ **Reliability** - System resilience and recovery
   - ⚖️ **Governance** - Data governance and compliance
   - 💰 **Cost Optimization** - Resource efficiency
   - ⚡ **Performance Efficiency** - Compute and query performance
   - 📊 **Summary** - Aggregated scores across all pillars
   - 🤖 **AI Assistant tab** - Genie Space embedded directly in the dashboard

2. **Databricks App** *(central hub)* - The single URL your team needs, featuring:
   - Embedded dashboard visualization
   - **WAF Recommendations (Not Met)** page — every failing control with score, threshold gap, and actionable fix
   - **Reload Data** button — triggers the background reload job on demand
   - **Genie** button — deep-links to the AI assistant for natural-language WAF queries
   - Comprehensive WAF Guide sidebar with score calculation explanations, thresholds, and code examples

3. **Genie Space** - AI assistant pre-loaded with all 15 WAF tables and detailed instructions:
   - Ask questions like *"Which controls are failing and what should I do?"*
   - Pre-built SQL examples for every pillar
   - Linked as an AI Assistant tab inside the dashboard

4. **WAF Reload Job** - Background Databricks Job that refreshes all WAF cache tables:
   - Triggered automatically at the end of install
   - Invokable on demand from the app's Reload button
   - Runs with full service principal permissions on `waf_cache`

---

## 📚 Documentation

📖 **[Full Documentation Site](https://abhidatabricks.github.io/Databricks-WAF-Light-Tooling/)** — includes demo video, feature overview, and getting started guide.

### For Users

- **Installation Guide**: See [Getting Started](#-getting-started) section above
- **Dashboard Guide**: Interactive WAF Guide is available in the Databricks App sidebar
- **Architecture Diagrams**: See `architecture/` folder for visual documentation

### For Developers

- **[Developer Documentation](DEVELOPER_DOC.md)**: Complete guide to dataset architecture, relationships, and data flow
- **[Architecture Diagrams](architecture/)**: 
  - System Architecture Overview
  - Data Flow Diagrams
  - User Flow - Complete Journey
  - User Interaction Flow
  - Deployment Architecture
  - And more (see `architecture/README.md` for full list)

### Architecture Documentation

The `architecture/` folder contains:
- **Mermaid diagram source files** (`.mmd`) for all architecture diagrams
- **`render_diagrams.html`** - Browser-based diagram renderer for easy viewing
- **Documentation files** explaining each diagram
- **Quick start guide** for generating diagram images

See `architecture/README.md` for details on viewing and generating diagrams.

---

## 🏗️ Project Structure

```
Databricks-WAF-Light-Tooling/
├── install.ipynb                          # Main installation notebook
├── README.md
├── LICENSE
│
├── dashboards/
│   └── WAF_ASSESSMENTv1.7.1.lvdash.json  # Lakeview dashboard template
│
├── streamlit-waf-automation/              # Databricks App source
│   ├── app.py                            # Databricks App (central hub)
│   ├── app.yaml                          # App config (catalog, job_id, warehouse_id, genie_url)
│   ├── waf_reload.py                     # Notebook: refreshes all waf_cache tables
│   ├── dashboard_queries.yaml            # All WAF SQL queries (source