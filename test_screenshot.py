import subprocess
import os

html = """
<!DOCTYPE html>
<html>
<head>
<style>
  * { margin:0; padding:0; box-sizing: border-box; }
  body { width: 1200px; height: 800px; background: linear-gradient(135deg, #0f172a, #1e3a8a); color: white; display: flex; align-items: center; justify-content: center; font-family: sans-serif; }
  h1 { font-size: 48px; }
</style>
</head>
<body>
  <h1>Test Banner 1200x800</h1>
</body>
</html>
"""

with open("test_b.html", "w", encoding="utf-8") as f:
    f.write(html)

html_path = os.path.abspath("test_b.html")
png_path = os.path.abspath("test_b.png")
edge = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
cmd = [edge, "--headless", "--disable-gpu", "--hide-scrollbars", "--window-size=1200,800", f"--screenshot={png_path}", "file:///" + html_path.replace("\\", "/")]

subprocess.run(cmd, check=True)
print("PNG Exists:", os.path.exists(png_path))
if os.path.exists(png_path):
    print("PNG Size:", os.path.getsize(png_path))
    os.remove(png_path)
os.remove("test_b.html")

