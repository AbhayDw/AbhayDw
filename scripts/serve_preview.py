import http.server
import socketserver
import os
import sys

PORT = 8080
DIRECTORY = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en" data-color-mode="dark" data-dark-theme="dark_dimmed">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Abhay Dwivedi — GitHub Profile Preview</title>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.5.1/github-markdown-dark.min.css">
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
      max-width: 940px;
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
  </style>
</head>
<body>
  <div class="container">
    <div class="top-bar">
      <div>
        <strong>Previewing:</strong> <code>AbhayDw / README.md</code> (Local Server)
      </div>
      <div class="badge-status">
        <span class="status-dot"></span> Local Host Active (Port 8080)
      </div>
    </div>
    <div id="content" class="markdown-body">
      Loading README.md...
    </div>
  </div>

  <script>
    fetch('/README.md')
      .then(response => response.text())
      .then(markdown => {
        // Set marked options
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
    with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
        print(f"[PREVIEW SERVER] Serving GitHub profile preview at http://localhost:{PORT}")
        print(f"[PREVIEW SERVER] Root directory: {DIRECTORY}")
        sys.stdout.flush()
        httpd.serve_forever()

if __name__ == "__main__":
    run()

