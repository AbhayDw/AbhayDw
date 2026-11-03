#!/usr/bin/env python3
"""
Abhay Dwivedi — GitHub Profile Project Synchronization Script
Fetches public repositories tagged with 'portfolio', sorts by recent activity,
and cleanly updates the projects section in README.md without touching other content.
"""

import os
import re
import sys
import json
import urllib.request
import urllib.error

GITHUB_USER = "AbhayDw"
API_URL = f"https://api.github.com/users/{GITHUB_USER}/repos?per_page=100&sort=pushed&direction=desc"
README_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "README.md")

START_TAG = "<!-- START_SECTION:PROJECTS -->"
END_TAG = "<!-- END_SECTION:PROJECTS -->"

# Curated fallback projects (aligned with professional portfolio requirements)
CURATED_PROJECTS = [
    {
        "name": "AI Powered Car Price Prediction",
        "description": "End-to-end regression modeling and feature engineering pipeline predicting pre-owned vehicle valuations with cross-validated evaluation.",
        "language": "Python / Scikit-learn",
        "repo_url": "https://github.com/AbhayDw/AI-Powered-Car-Price-Prediction",
        "demo_url": "https://abhay-portfolio-pi-tan.vercel.app/",
        "topics": ["machine-learning", "regression", "scikit-learn"]
    },
    {
        "name": "Emergency Patient Priority Prediction",
        "description": "Clinical triage prioritization system utilizing multi-class predictive modeling to categorize patient acuity and assist hospital admissions.",
        "language": "Python / ML",
        "repo_url": "https://github.com/AbhayDw/Emergency-Patient-Priority-Prediction",
        "demo_url": "https://abhay-portfolio-pi-tan.vercel.app/",
        "topics": ["healthcare-ai", "classification", "data-analytics"]
    },
    {
        "name": "Breast Cancer Detection",
        "description": "Diagnostic classification pipeline evaluating cellular biopsy metrics with precision/recall threshold optimization and ROC-AUC validation.",
        "language": "Python / Scikit-learn",
        "repo_url": "https://github.com/AbhayDw/Breast-Cancer-Detection",
        "demo_url": "https://abhay-portfolio-pi-tan.vercel.app/",
        "topics": ["biomedical", "classification", "diagnostics"]
    },
    {
        "name": "Titanic Survival Prediction",
        "description": "Rigorous exploratory data analysis (EDA), probabilistic feature engineering, and ensemble classification on demographic survival factors.",
        "language": "Python / Pandas / ML",
        "repo_url": "https://github.com/AbhayDw/Titanic-Survival-Prediction",
        "demo_url": "https://abhay-portfolio-pi-tan.vercel.app/",
        "topics": ["eda", "classification", "statistics"]
    },
    {
        "name": "California Housing Price Prediction",
        "description": "Geospatial housing valuation regression model implementing spatial clustering, automated imputation, and hyperparameter tuning.",
        "language": "Python / Scikit-learn",
        "repo_url": "https://github.com/AbhayDw/California-Housing-Price-Prediction",
        "demo_url": "https://abhay-portfolio-pi-tan.vercel.app/",
        "topics": ["regression", "geospatial", "feature-engineering"]
    },
    {
        "name": "Movie Recommendation System",
        "description": "Hybrid content-based and collaborative filtering recommendation engine utilizing cosine similarity and vector space representations.",
        "language": "Python / NLP / Vectors",
        "repo_url": "https://github.com/AbhayDw/Movie-Recommendation-System",
        "demo_url": "https://abhay-portfolio-pi-tan.vercel.app/",
        "topics": ["recommender-system", "nlp", "vector-similarity"]
    }
]

def fetch_portfolio_repos():
    """Fetches repositories from GitHub API and filters by portfolio topic."""
    token = os.environ.get("GITHUB_TOKEN")
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "AbhayDw-Portfolio-Sync"
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"

    req = urllib.request.Request(API_URL, headers=headers)
    
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        print(f"[SYNC] Notice: Unable to query live GitHub API ({e}). Using curated project portfolio.")
        return []

    portfolio_repos = []
    for repo in data:
        if repo.get("fork") or repo.get("archived"):
            continue

        topics = [t.lower() for t in repo.get("topics", [])]
        if "portfolio" in topics:
            portfolio_repos.append({
                "name": repo.get("name", "").replace("-", " ").title(),
                "description": repo.get("description") or "Production engineering project and implementation repository.",
                "language": repo.get("language") or "Python",
                "repo_url": repo.get("html_url"),
                "demo_url": repo.get("homepage") or "https://abhay-portfolio-pi-tan.vercel.app/",
                "topics": topics,
                "pushed_at": repo.get("pushed_at")
            })

    return portfolio_repos

def format_cell_content(p):
    """Formats project card for standard GitHub Flavored Markdown table."""
    name = p["name"]
    desc = p["description"]
    lang = p["language"]
    repo_url = p["repo_url"]
    demo_url = p.get("demo_url", "")
    
    demo_part = f" • <a href=\"{demo_url}\">Live System Demo ↗</a>" if demo_url else ""
    
    return (
        f"<strong><a href=\"{repo_url}\">{name}</a></strong><br/>"
        f"<em>{desc}</em><br/><br/>"
        f"<strong>Core Stack:</strong> <code>{lang}</code><br/>"
        f"<a href=\"{repo_url}\">Inspect Repository ↗</a>{demo_part}"
    )

def generate_markdown(projects):
    """Formats projects into a robust 2-column Markdown table."""
    lines = [
        "| Architecture & Implementation | Architecture & Implementation |",
        "| :--- | :--- |"
    ]
    
    for i in range(0, len(projects), 2):
        p1 = projects[i]
        p2 = projects[i + 1] if i + 1 < len(projects) else None

        c1 = format_cell_content(p1)
        c2 = format_cell_content(p2) if p2 else "<em>Additional production systems and case studies under active deployment.</em>"

        # Escape pipe symbols if any exist inside cell
        c1 = c1.replace("|", "&#124;")
        c2 = c2.replace("|", "&#124;")

        lines.append(f"| {c1} | {c2} |")

    return "\n".join(lines)

def update_readme():
    """Updates only the section between START_TAG and END_TAG."""
    if not os.path.exists(README_PATH):
        print(f"[SYNC] Error: {README_PATH} not found.")
        sys.exit(1)

    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    if START_TAG not in content or END_TAG not in content:
        print(f"[SYNC] Error: Boundary tags {START_TAG} / {END_TAG} not found in README.md")
        sys.exit(1)

    fetched = fetch_portfolio_repos()
    projects = fetched if fetched else CURATED_PROJECTS

    print(f"[SYNC] Formatting {len(projects)} projects (source: {'GitHub API' if fetched else 'Curated Verified Suite'})...")
    projects_md = generate_markdown(projects)

    pattern = re.compile(f"{re.escape(START_TAG)}.*?{re.escape(END_TAG)}", re.DOTALL)
    replacement = f"{START_TAG}\n{projects_md}\n{END_TAG}"

    new_content = pattern.sub(replacement, content)

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(new_content)

    print("[SYNC] Successfully updated README.md projects section.")

if __name__ == "__main__":
    update_readme()
