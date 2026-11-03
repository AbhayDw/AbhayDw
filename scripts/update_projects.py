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

# Curated verified projects (top 4 showcased prominently)
CURATED_PROJECTS = [
    {
        "name": "AI Powered Car Price Prediction",
        "description": "End-to-end regression modeling and feature engineering pipeline to predict pre-owned vehicle valuations with cross-validated evaluation.",
        "language": "Python, Scikit-learn",
        "repo_url": "https://github.com/AbhayDw/AI-Powered-Car-Price-Prediction",
        "demo_url": "https://abhay-portfolio-pi-tan.vercel.app/"
    },
    {
        "name": "Emergency Patient Priority Prediction",
        "description": "Clinical triage prioritization system utilizing multi-class predictive classification to assess patient acuity and support hospital admissions.",
        "language": "Python, Machine Learning",
        "repo_url": "https://github.com/AbhayDw/Emergency-Patient-Priority-Prediction",
        "demo_url": "https://abhay-portfolio-pi-tan.vercel.app/"
    },
    {
        "name": "Breast Cancer Detection",
        "description": "Diagnostic classification pipeline evaluating cellular biopsy metrics with precision/recall threshold optimization and ROC-AUC validation.",
        "language": "Python, Scikit-learn",
        "repo_url": "https://github.com/AbhayDw/Breast-Cancer-Detection",
        "demo_url": "https://abhay-portfolio-pi-tan.vercel.app/"
    },
    {
        "name": "California Housing Price Prediction",
        "description": "Geospatial housing valuation regression model implementing spatial clustering, automated imputation, and hyperparameter tuning.",
        "language": "Python, Scikit-learn",
        "repo_url": "https://github.com/AbhayDw/California-Housing-Price-Prediction",
        "demo_url": "https://abhay-portfolio-pi-tan.vercel.app/"
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
        print(f"[SYNC] Notice: Unable to query live GitHub API ({e}). Using curated verified portfolio.")
        return []

    portfolio_repos = []
    seen = set()
    for repo in data:
        if repo.get("fork") or repo.get("archived"):
            continue

        topics = [t.lower() for t in repo.get("topics", [])]
        name = repo.get("name", "")
        if "portfolio" in topics and name not in seen:
            seen.add(name)
            portfolio_repos.append({
                "name": name.replace("-", " ").title(),
                "description": repo.get("description") or "Production engineering project and implementation repository.",
                "language": repo.get("language") or "Python",
                "repo_url": repo.get("html_url"),
                "demo_url": repo.get("homepage") or "https://abhay-portfolio-pi-tan.vercel.app/"
            })

    return portfolio_repos

def generate_markdown(projects):
    """Formats projects into a restrained, clean editorial table."""
    lines = [
        "| Project | Focus & Technical Overview | Stack & Links |",
        "| :--- | :--- | :--- |"
    ]
    
    # Prominently show top 4 projects
    for p in projects[:4]:
        name = p["name"]
        desc = p["description"]
        lang = p["language"]
        repo = p["repo_url"]
        demo = p.get("demo_url", "")

        demo_link = f" &nbsp;·&nbsp; [Live Demo ↗]({demo})" if demo else ""
        repo_link = f"[Repository ↗]({repo}){demo_link}"

        # Clean cell text without unescaped pipes
        clean_desc = desc.replace("|", "/")
        lines.append(f"| **[{name}]({repo})** | {clean_desc} | `{lang}`<br/>{repo_link} |")

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

    print(f"[SYNC] Formatting {min(len(projects), 4)} featured projects...")
    projects_md = generate_markdown(projects)

    pattern = re.compile(f"{re.escape(START_TAG)}.*?{re.escape(END_TAG)}", re.DOTALL)
    replacement = f"{START_TAG}\n{projects_md}\n{END_TAG}"

    new_content = pattern.sub(replacement, content)

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(new_content)

    print("[SYNC] Successfully updated README.md projects section.")

if __name__ == "__main__":
    update_readme()
