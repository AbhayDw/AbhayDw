import http.server
import socketserver
import os
import sys

DEFAULT_PORT = 8080
DIRECTORY = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Abhay Dwivedi — Professional GitHub Profile</title>
  <link id="theme-css" rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.5.1/github-markdown-dark.min.css">
  <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
  <style>
    body {
      background-color: #080D16;
      color: #F3F0E8;
      margin: 0;
      padding: 30px 15px;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Noto Sans", Helvetica, Arial, sans-serif;
      transition: background-color 0.2s ease;
    }
    body.light {
      background-color: #f6f8fa;
      color: #1f2328;
    }
    .container {
      max-width: 980px;
      margin: 0 auto;
      background: #0D1424;
      border: 1px solid #303A49;
      border-radius: 12px;
      padding: 40px 48px;
      box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
      transition: all 0.2s ease;
    }
    body.light .container {
      background: #ffffff;
      border-color: #d0d7de;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.06);
    }
    .top-bar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 24px;
      padding-bottom: 14px;
      border-bottom: 1px solid #303A49;
      font-size: 13px;
      color: #AAB3BF;
    }
    body.light .top-bar {
      border-color: #e1e4e8;
      color: #656d76;
    }
    .top-bar a {
      color: #D2AD68;
      text-decoration: none;
      font-weight: 600;
    }
    .badge-status {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: rgba(210, 173, 104, 0.12);
      border: 1px solid #D2AD68;
      padding: 4px 12px;
      border-radius: 14px;
      color: #D2AD68;
      font-weight: 600;
      font-size: 12px;
    }
    .status-dot {
      width: 8px;
      height: 8px;
      background: #F59E0B;
      border-radius: 50%;
      box-shadow: 0 0 6px #F59E0B;
    }
    .theme-btn {
      background: #111927;
      border: 1px solid #303A49;
      color: #F3F0E8;
      padding: 5px 12px;
      border-radius: 6px;
      font-size: 12px;
      cursor: pointer;
      font-weight: 600;
    }
    body.light .theme-btn {
      background: #f6f8fa;
      border-color: #d0d7de;
      color: #1f2328;
    }
    .markdown-body {
      box-sizing: border-box;
      min-width: 200px;
      max-width: 100%;
      background-color: transparent !important;
    }
    .markdown-body table {
      display: table !important;
      width: 100% !important;
    }
    .markdown-body table tr {
      background-color: #0D1424 !important;
      border-top: 1px solid #303A49 !important;
    }
    body.light .markdown-body table tr {
      background-color: #ffffff !important;
      border-top: 1px solid #d0d7de !important;
    }
    .markdown-body table tr:nth-child(2n) {
      background-color: #111927 !important;
    }
    body.light .markdown-body table tr:nth-child(2n) {
      background-color: #f6f8fa !important;
    }
    .markdown-body table td, .markdown-body table th {
      border: 1px solid #303A49 !important;
      padding: 12px 14px !important;
    }
    body.light .markdown-body table td, body.light .markdown-body table th {
      border-color: #d0d7de !important;
    }
  </style>
</head>
<body>
  <div class="container">
    <div class="top-bar">
      <div>
        <strong>Live Preview:</strong> <code>AbhayDw / README.md</code>
        &nbsp;&bull;&nbsp;
        <a href="/previews/">View Header Gallery ↗</a>
      </div>
      <div style="display: flex; gap: 12px; align-items: center;">
        <button class="theme-btn" onclick="toggleTheme()">🌓 Switch Theme</button>
        <div class="badge-status">
          <span class="status-dot"></span> Concept 2: Cinematic Horizon Live
        </div>
      </div>
    </div>
    <div id="content" class="markdown-body">
      Loading README.md...
    </div>
  </div>

  <script>
    let isDark = true;
    function toggleTheme() {
      isDark = !isDark;
      document.body.className = isDark ? '' : 'light';
      document.getElementById('theme-css').href = isDark 
        ? 'https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.5.1/github-markdown-dark.min.css'
        : 'https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.5.1/github-markdown-light.min.css';
    }

    fetch('/README.md?t=' + Date.now())
      .then(response => response.text())
      .then(markdown => {
        marked.setOptions({
          gfm: true,
          breaks: true
        });
        document.getElementById('content').innerHTML = marked.parse(markdown);
      })
      .catch(err => {
        document.getElementById('content').innerHTML = '<p style="color:red">Error loading README.md: ' + err + '</p>';
      });
  </script>
</body>
</html>
"""

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_GET(self):
        if self.path in ("/", "/index.html", "/preview"):
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.send_header("Cache-Control", "no-cache")
            self.end_headers()
            self.wfile.write(HTML_TEMPLATE.encode("utf-8"))
        else:
            return super().do_GET()

def run():
    os.chdir(DIRECTORY)
    socketserver.TCPServer.allow_reuse_address = True
    port = DEFAULT_PORT

    for attempt_port in [8080, 8000, 8081, 8888, 3000]:
        try:
            httpd = socketserver.TCPServer(("", attempt_port), CustomHandler)
            port = attempt_port
            break
        except OSError:
            continue

    print("=" * 65)
    print(f"  ABHAY DWIVEDI — PROFESSIONAL GITHUB PROFILE PREVIEW")
    print(f"  Live URL:   http://localhost:{port}")
    print(f"  Directory:  {DIRECTORY}")
    print("=" * 65)
    print("  Press Ctrl+C in this terminal to stop the server.\n")
    sys.stdout.flush()

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[PREVIEW SERVER] Server stopped.")

if __name__ == "__main__":
    run()
