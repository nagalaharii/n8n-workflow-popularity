# n8n Workflow Popularity Analysis

## 📌 Project Overview

This project analyzes the popularity of **n8n workflows** by collecting data from:

- YouTube (views, likes, comments)
- Google Trends (search interest)

The goal is to understand which n8n workflows are trending and in demand.

---

## 🏗️ Project Architecture

YouTube API / Google Trends  
 ↓  
Data Fetchers (Python)  
 ↓  
ETL Pipeline  
 ↓  
SQLite Database  
 ↓  
Future: FastAPI / Dashboard

---

## 📁 Project Structure

n8n_popularity_project/
│
├── src/
│ ├── database.py # DB connection
│ ├── models.py # SQLAlchemy models
│ ├── youtube_fetcher.py # YouTube data fetcher
│ ├── google_trends_fetcher.py # Google Trends fetcher
│ ├── pipeline.py # Main pipeline runner
│
├── .env # Environment variables
├── requirements.txt
├── README.md

---

## ⚙️ Technologies Used

- Python
- YouTube Data API
- Google Trends (pytrends)
- SQLAlchemy
- SQLite
- VS Code

---

## 🔐 Environment Variables

Create a `.env` file and add:

```env
YOUTUBE_API_KEY=AIzaSyCtSojNpXBdFc44wvGRm7mpaV7dc3kwnMk
DATABASE_URL=sqlite:///workflows.db

```
