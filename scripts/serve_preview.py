import http.server
import socketserver
import os
import sys

DEFAULT_PORT = 8080
DIRECTORY = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en" data-color-mode="light" data-light-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Abhay Dwivedi — Professional GitHub Profile</title>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.5.1/github-markdown-light.min.css">
  <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
  <style>
    body {
      background-color: #f6f8fa;
      color: #1f2328;
      margin: 0;
      padding: 30px 15px;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Noto Sans", Helvetica, Arial, sans-serif;
    }
    .container {
      max-width: 980px;
      margin: 0 auto;
      background: #ffffff;
      border: 1px solid #d0d7de;
      border-radius: 12px;
      padding: 40px 48px;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.06);
    }
    .top-bar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 24px;
      padding-bottom: 14px;
      border-bottom: 1px solid #e1e4e8;
      font-size: 13px;
      color: #656d76;
    }
    .top-bar a {
      color: #0969da;
      text-decoration: none;
      font-weight: 600;
    }
    .badge-status {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: #f0fdf4;
      border: 1px solid #bbf7d0;
      padding: 4px 12px;
      border-radius: 14px;
      color: #15803d;
      font-weight: 600;
      font-size: 12px;
    }
    .status-dot {
      width: 8px;
      height: 8px;
      background: #16a34a;
      border-radius: 50%;
      box-shadow: 0 0 6px #22c55e;
    }
    .markdown-body {
      box-sizing: border-box;
      min-width: 200px;
      max-width: 100%;
      background-color: transparent !important;
      color: #1f2328 !important;
    }
    .markdown-body table {
      display: table !important;
      width: 100% !important;
    }
    .markdown-body table tr {
      background-color: #ffffff !important;
      border-top: 1px solid #d0d7de !important;
    }
    .markdown-body table tr:nth-child(2n) {
      background-color: #f6f8fa !important;
    }
    .markdown-body table td, .markdown-body table th {
      border: 1px solid #d0d7de !important;
      padding: 12px 14px !important;
    }
  </style>
</head>
<body>
  <div class="container">
    <div class="top-bar">
      <div>
        <strong>Previewing Live:</strong> <code>AbhayDw / README.md</code>
      </div>
      <div class="badge-status">
        <span class="status-dot"></span> Clean Light Canvas Live (Port 8080)
      </div>
    </div>
    <div id="content" class="markdown-body">
      Loading README.md...
    </div>
  </div>

  <script>
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
