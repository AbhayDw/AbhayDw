import http.server
import socketserver
import os
import sys

DEFAULT_PORT = 8080
DIRECTORY = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en" data-color-mode="dark" data-dark-theme="dark_dimmed">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Abhay Dwivedi — GitHub Profile Preview</title>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.5.1/github-markdown.min.css">
  <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
  <style>
    body {
      background-color: #0d1117;
      color: #e6edf3;
      margin: 0;
      padding: 30px 15px;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Noto Sans", Helvetica, Arial, sans-serif;
    }
    .container {
      max-width: 960px;
      margin: 0 auto;
      background: #161b22;
      border: 1px solid #30363d;
      border-radius: 8px;
      padding: 36px 44px;
      box-shadow: 0 8px 24px rgba(0,0,0,0.4);
    }
    .top-bar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 24px;
      padding-bottom: 12px;
      border-bottom: 1px solid #30363d;
      font-size: 13px;
      color: #8b949e;
    }
    .top-bar a {
      color: #58a6ff;
      text-decoration: none;
    }
    .badge-status {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: #1f2937;
      border: 1px solid #374151;
      padding: 4px 10px;
      border-radius: 12px;
      color: #38bdf8;
      font-weight: 500;
    }
    .status-dot {
      width: 8px;
      height: 8px;
      background: #10b981;
      border-radius: 50%;
      box-shadow: 0 0 8px #10b981;
    }
    .markdown-body {
      box-sizing: border-box;
      min-width: 200px;
      max-width: 100%;
      background-color: transparent !important;
      color: #c9d1d9 !important;
    }
    .markdown-body table {
      display: table !important;
      width: 100% !important;
    }
    .markdown-body table tr {
      background-color: #161b22 !important;
      border-top: 1px solid #21262d !important;
    }
    .markdown-body table td, .markdown-body table th {
      border: 1px solid #30363d !important;
      padding: 12px 14px !important;
    }
    .theme-toggle-btn {
      background: #21262d;
      border: 1px solid #363b42;
      color: #c9d1d9;
      padding: 4px 10px;
      border-radius: 6px;
      cursor: pointer;
      font-size: 12px;
    }
    .theme-toggle-btn:hover {
      background: #30363d;
    }
  </style>
</head>
<body>
  <div class="container">
    <div class="top-bar">
      <div>
        <strong>Previewing:</strong> <code>AbhayDw / README.md</code>
      </div>
      <div style="display: flex; gap: 12px; align-items: center;">
        <button class="theme-toggle-btn" onclick="toggleTheme()">🌓 Switch Theme</button>
        <div class="badge-status">
          <span class="status-dot"></span> Live Localhost Active
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
      const html = document.documentElement;
      const container = document.querySelector('.container');
      const body = document.body;
      if (isDark) {
        body.style.backgroundColor = '#0d1117';
        container.style.backgroundColor = '#161b22';
        container.style.borderColor = '#30363d';
        html.setAttribute('data-color-mode', 'dark');
        html.setAttribute('data-dark-theme', 'dark_dimmed');
      } else {
        body.style.backgroundColor = '#f6f8fa';
        container.style.backgroundColor = '#ffffff';
        container.style.borderColor = '#d0d7de';
        html.setAttribute('data-color-mode', 'light');
        html.setAttribute('data-light-theme', 'light');
      }
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
    print(f"  ABHAY DWIVEDI — GITHUB PROFILE LOCAL PREVIEW SERVER")
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
