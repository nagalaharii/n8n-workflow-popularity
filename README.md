# n8n Workflow Popularity System

## 📌 Overview
This project builds a **production-ready system** to identify the **most popular n8n workflows** across multiple platforms using clear and verifiable popularity evidence.

The system collects data, computes engagement metrics, stores results in a database, and exposes them via a **REST API**, ready for automation using cron jobs.

---

## 🎯 Objective
Analyze and rank n8n workflows based on real-world popularity signals such as:
- Views, likes, and comments
- Engagement ratios
- Search interest trends  
Segmented by **platform** and **country (US, IN)**.

---

## 📊 Data Sources & Popularity Metrics

### 1️⃣ YouTube (n8n workflow videos)
Metrics collected:
- Views
- Likes
- Comments
- like_to_view_ratio = likes / views
- comment_to_view_ratio = comments / views

**Data Source:** YouTube Data API v3

---

### 2️⃣ Google Search (Trends)
Metrics collected:
- Relative search interest
- Trend strength over time

**Data Source:** Google Trends (pytrends)

---

## 🏗️ System Architecture

External APIs  
↓  
Python Data Fetchers  
↓  
ETL Pipeline  
↓  
SQLite Database  
↓  
FastAPI REST API  

---

## 📁 Project Structure

