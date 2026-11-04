import os

TECH_DIR = r"C:\GitHub\AbhayDw\assets\technology"
ICONS_DIR = r"C:\GitHub\AbhayDw\assets\icons"
ASSETS_DIR = r"C:\GitHub\AbhayDw\assets"
os.makedirs(TECH_DIR, exist_ok=True)
os.makedirs(ICONS_DIR, exist_ok=True)

# Exact official SVGs with brand colors and standard 24x24 / 128x128 viewboxes
SVGS = {
    # ---------------- TECHNOLOGY ----------------
    os.path.join(TECH_DIR, "python.svg"): '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128" width="24" height="24">
  <path fill="#3776AB" d="M63.5 6.7c-26.6 0-25 11.5-25 11.5l.03 11.9h25.4v3.6H28.7S13 32 13 58.7c0 26.6 13.8 25.7 13.8 25.7h8.2v-11.6s-.4-13.8 13.6-13.8h25.2s13.1.2 13.1-12.8V20.4s1.8-13.7-23.4-13.7zm-13.7 7.4c2.5 0 4.5 2 4.5 4.5s-2 4.5-4.5 4.5-4.5-2-4.5-4.5 2-4.5 4.5-4.5z"/>
  <path fill="#FFD43B" d="M64.5 121.3c26.6 0 25-11.5 25-11.5l-.03-11.9H64.1v-3.6h35.2s15.7 1.7 15.7-25c0-26.6-13.8-25.7-13.8-25.7h-8.2v11.6s.4 13.8-13.6 13.8H34.2S21.1 69 21.1 82v15.8s-1.8 13.7 23.4 13.7zm13.7-7.4c-2.5 0-4.5-2-4.5-4.5s2-4.5 4.5-4.5 4.5 2 4.5 4.5-2 4.5-4.5 4.5z"/>
</svg>''',

    os.path.join(TECH_DIR, "sql.svg"): '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="#D2AD68" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <ellipse cx="12" cy="5" rx="9" ry="3"/>
  <path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3"/>
  <path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"/>
</svg>''',

    os.path.join(TECH_DIR, "numpy.svg"): '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24">
  <path fill="#4DABCF" d="M2.5 4.2h3.8L12 14.8V4.2h3.5v15.6h-3.8L6 9.2v10.6H2.5V4.2zm15.2 0H21v15.6h-3.3V4.2z"/>
</svg>''',

    os.path.join(TECH_DIR, "pandas.svg"): '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24">
  <path fill="#130754" d="M4 3h3v18H4V3zm5 4h3v14H9V7zm5-2h3v16h-3V5zm5 5h3v11h-3V10z"/>
  <path fill="#E70488" d="M4 17h3v4H4v-4zm5-6h3v4H9v-4zm5-2h3v4h-3V9zm5 6h3v4h-3v-4z"/>
</svg>''',

    os.path.join(TECH_DIR, "matplotlib.svg"): '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24" fill="none">
  <rect width="24" height="24" rx="4" fill="#11557C"/>
  <path d="M4 18h16M7 15l3-6 4 4 4-8" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
  <circle cx="7" cy="15" r="1.5" fill="#D2AD68"/>
  <circle cx="10" cy="9" r="1.5" fill="#D2AD68"/>
  <circle cx="14" cy="13" r="1.5" fill="#D2AD68"/>
  <circle cx="18" cy="5" r="1.5" fill="#D2AD68"/>
</svg>''',

    os.path.join(TECH_DIR, "seaborn.svg"): '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24">
  <path fill="#3776AB" d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 17.93c-3.95-.49-7-3.85-7-7.93 0-.62.08-1.21.21-1.79L9 15v1c0 1.1.9 2 2 2v1.93zm6.9-2.54c-.26-.81-1-1.39-1.9-1.39h-1v-3c0-.55-.45-1-1-1H8v-2h2c.55 0 1-.45 1-1V7h2c1.1 0 2-.9 2-2v-.41c2.93 1.19 5 4.06 5 7.41 0 2.08-.8 3.97-2.1 5.39z"/>
</svg>''',

    os.path.join(TECH_DIR, "scikitlearn.svg"): '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24">
  <path fill="#F7931E" d="M12 2L3 7v10l9 5 9-5V7l-9-5zm0 2.3l6.5 3.6-6.5 3.6L5.5 7.9 12 4.3zM5 9.4l6 3.3v6.9l-6-3.3V9.4zm8 10.2v-6.9l6-3.3v6.9l-6 3.3z"/>
</svg>''',

    os.path.join(TECH_DIR, "langchain.svg"): '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24" fill="none">
  <rect width="24" height="24" rx="4" fill="#1C3C3C"/>
  <path d="M7 12a5 5 0 0 1 5-5h2a5 5 0 0 1 0 10h-2a5 5 0 0 1-5-5z" stroke="#34D399" stroke-width="2"/>
  <path d="M17 12a5 5 0 0 1-5 5h-2a5 5 0 0 1 0-10h2a5 5 0 0 1 5 5z" stroke="#FDE68A" stroke-width="2"/>
</svg>''',

    os.path.join(TECH_DIR, "gemini.svg"): '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24">
  <path fill="#1A73E8" d="M12 2C12 7.52 7.52 12 2 12c5.48 0 10 4.48 10 10 0-5.52 4.48-10 10-10-5.52 0-10-4.48-10-10z"/>
</svg>''',

    os.path.join(TECH_DIR, "mysql.svg"): '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24">
  <path fill="#4479A1" d="M12.4 3.2c-3.1 0-5.8 1.5-7.3 3.8l1.7 1.1c1.2-1.9 3.3-3.1 5.6-3.1 3.7 0 6.7 3 6.7 6.7 0 3.7-3 6.7-6.7 6.7-2.3 0-4.4-1.2-5.6-3.1L5.1 16.4c1.5 2.3 4.2 3.8 7.3 3.8 4.8 0 8.7-3.9 8.7-8.7s-3.9-8.3-8.7-8.3z"/>
  <path fill="#F29111" d="M6.2 12c0-.7.1-1.3.4-1.9L4.8 9C4.3 9.9 4 10.9 4 12s.3 2.1.8 3l1.8-1.1c-.3-.6-.4-1.2-.4-1.9z"/>
</svg>''',

    os.path.join(TECH_DIR, "postgresql.svg"): '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24">
  <path fill="#336791" d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 3c2.76 0 5 2.24 5 5 0 1.28-.48 2.45-1.28 3.34l-1.42-1.42c.43-.56.7-1.26.7-2.02 0-1.71-1.39-3.1-3.1-3.1s-3.1 1.39-3.1 3.1c0 .76.27 1.46.7 2.02l-1.42 1.42C8.48 12.45 8 11.28 8 10c0-2.76 2.24-5 5-5z"/>
</svg>''',

    os.path.join(TECH_DIR, "powerbi.svg"): '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24">
  <rect x="4" y="11" width="3.5" height="9" rx="1" fill="#F2C811"/>
  <rect x="10.25" y="7" width="3.5" height="13" rx="1" fill="#E8B20B"/>
  <rect x="16.5" y="4" width="3.5" height="16" rx="1" fill="#D39B07"/>
</svg>''',

    os.path.join(TECH_DIR, "excel.svg"): '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24">
  <rect width="24" height="24" rx="4" fill="#107C41"/>
  <path d="M7 6l4.5 6L7 18h2.5l3-4.5 3 4.5H18l-4.5-6L18 6h-2.5l-3 4.5L9.5 6H7z" fill="#FFFFFF"/>
</svg>''',

    os.path.join(TECH_DIR, "git.svg"): '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24">
  <path fill="#F05032" d="M21.6 10.9L13.1 2.4c-.6-.6-1.5-.6-2.1 0L8.9 4.5l2.7 2.7c.6-.2 1.4 0 1.9.5.5.5.7 1.3.5 1.9l2.6 2.6c.6-.2 1.4 0 1.9.5.7.7.7 1.9 0 2.6-.7.7-1.9.7-2.6 0-.6-.6-.7-1.4-.4-2.1L12.9 10v4.7c.2.1.4.3.6.5.7.7.7 1.9 0 2.6-.7.7-1.9.7-2.6 0-.7-.7-.7-1.9 0-2.6.2-.2.4-.4.6-.5V9.8c-.2-.1-.4-.3-.6-.5-.6-.6-.7-1.4-.4-2.1L7.8 4.5 2.4 9.9c-.6.6-.6 1.5 0 2.1l8.5 8.5c.6.6 1.5.6 2.1 0l8.6-8.5c.6-.6.6-1.5 0-2.1z"/>
</svg>''',

    os.path.join(TECH_DIR, "github.svg"): '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24" fill="#F3F0E8">
  <path d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.53 1.032 1.53 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z"/>
</svg>''',

    os.path.join(TECH_DIR, "vscode.svg"): '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24">
  <path fill="#007ACC" d="M17.6 2.2l-9.8 8.8L4.2 8.1 2 9.5l4.5 3.5L2 16.5l2.2 1.4 3.6-2.9 9.8 8.8 4.4-2.1V4.3l-4.4-2.1zm0 5.4v10.8l-6-5.4 6-5.4z"/>
</svg>''',

    os.path.join(TECH_DIR, "jupyter.svg"): '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24">
  <path fill="#F37626" d="M12 4.5c4.1 0 7.5 1.8 7.5 4s-3.4 4-7.5 4-7.5-1.8-7.5-4 3.4-4 7.5-4z"/>
  <path fill="#767677" d="M12 11.5c4.1 0 7.5 1.8 7.5 4s-3.4 4-7.5 4-7.5-1.8-7.5-4 3.4-4 7.5-4z"/>
  <circle cx="18" cy="5" r="1.5" fill="#E86222"/>
  <circle cx="6" cy="19" r="1.5" fill="#5F5F5F"/>
</svg>''',

    # ---------------- SOCIAL / CONTACT ICONS ----------------
    os.path.join(ICONS_DIR, "linkedin.svg"): '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="18" height="18" fill="#D2AD68">
  <path d="M19 3a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h14m-.5 15.5v-5.3a3.26 3.26 0 0 0-3.26-3.26c-.85 0-1.84.52-2.28 1.3v-1.11h-2.79v8.37h2.79v-4.93c0-.77.62-1.4 1.39-1.4a1.4 1.4 0 0 1 1.4 1.4v4.93h2.75M6.46 10.9h2.8v8.37h-2.8v-8.37M7.86 6.2a1.63 1.63 0 1 0 0 3.26 1.63 1.63 0 0 0 0-3.26z"/>
</svg>''',

    os.path.join(ICONS_DIR, "github.svg"): '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="18" height="18" fill="#D2AD68">
  <path d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.53 1.032 1.53 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z"/>
</svg>''',

    os.path.join(ICONS_DIR, "portfolio.svg"): '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="#D2AD68" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <circle cx="12" cy="12" r="10"/>
  <line x1="2" y1="12" x2="22" y2="12"/>
  <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>
</svg>''',

    os.path.join(ICONS_DIR, "email.svg"): '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="#D2AD68" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <rect x="2" y="4" width="20" height="16" rx="2"/>
  <path d="M22 6l-10 7L2 6"/>
</svg>''',

    os.path.join(ICONS_DIR, "location.svg"): '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="#D2AD68" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/>
  <circle cx="12" cy="10" r="3"/>
</svg>''',

    # ---------------- ELEGANT HORIZON DIVIDER ----------------
    os.path.join(ASSETS_DIR, "gold-divider.svg"): '''<svg width="100%" height="16" viewBox="0 0 960 16" fill="none" xmlns="http://www.w3.org/2000/svg">
  <line x1="0" y1="8" x2="960" y2="8" stroke="#303A49" stroke-width="1"/>
  <line x1="40" y1="8" x2="160" y2="8" stroke="#D2AD68" stroke-width="2"/>
  <circle cx="40" cy="8" r="2.5" fill="#D2AD68"/>
</svg>'''
}

for path, content in SVGS.items():
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip())
    print(f"Created {os.path.basename(path)}")

print("All official SVGs successfully created.")
