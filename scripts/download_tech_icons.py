import os
import urllib.request
import urllib.error

TECH_DIR = r"C:\GitHub\AbhayDw\assets\technology"
ICONS_DIR = r"C:\GitHub\AbhayDw\assets\icons"
os.makedirs(TECH_DIR, exist_ok=True)
os.makedirs(ICONS_DIR, exist_ok=True)

# Official Simple Icons / Devicon raw SVG URLs
TECH_URLS = {
    "python.svg": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg",
    "sql.svg": "https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/sqlite.svg",
    "numpy.svg": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/numpy/numpy-original.svg",
    "pandas.svg": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg",
    "matplotlib.svg": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/matplotlib/matplotlib-original.svg",
    "seaborn.svg": "https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/seaborn.svg",
    "scikitlearn.svg": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/scikitlearn/scikitlearn-original.svg",
    "langchain.svg": "https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/langchain.svg",
    "gemini.svg": "https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/googlegemini.svg",
    "mysql.svg": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original.svg",
    "postgresql.svg": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg",
    "powerbi.svg": "https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/powerbi.svg",
    "excel.svg": "https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/microsoftexcel.svg",
    "git.svg": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg",
    "github.svg": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg",
    "vscode.svg": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original.svg",
    "jupyter.svg": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/jupyter/jupyter-original.svg",
}

SOCIAL_URLS = {
    "linkedin.svg": "https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/linkedin.svg",
    "github.svg": "https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/github.svg",
    "portfolio.svg": "https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/vercel.svg",
    "email.svg": "https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/gmail.svg",
    "location.svg": "https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/googlemaps.svg"
}

headers = {"User-Agent": "Mozilla/5.0"}

def download_all():
    print("Downloading tech SVGs...")
    for filename, url in TECH_URLS.items():
        dest = os.path.join(TECH_DIR, filename)
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=10) as r:
                data = r.read()
                with open(dest, "wb") as f:
                    f.write(data)
                print(f"[OK] {filename} ({len(data)} bytes)")
        except Exception as e:
            print(f"[FAIL] {filename}: {e}")

    print("\nDownloading social SVGs...")
    for filename, url in SOCIAL_URLS.items():
        dest = os.path.join(ICONS_DIR, filename)
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=10) as r:
                data = r.read()
                with open(dest, "wb") as f:
                    f.write(data)
                print(f"[OK] {filename} ({len(data)} bytes)")
        except Exception as e:
            print(f"[FAIL] {filename}: {e}")

if __name__ == "__main__":
    download_all()
