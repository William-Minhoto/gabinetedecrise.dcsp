
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import json, os, webbrowser, threading, time

ROOT=Path(__file__).resolve().parent
os.chdir(ROOT)
DATA=ROOT/"data"/"gabinete.json"

class H(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith("/api/dados"):
            try:
                raw=DATA.read_bytes()
                self.send_response(200); self.send_header("Content-Type","application/json; charset=utf-8")
                self.send_header("Cache-Control","no-store"); self.end_headers(); self.wfile.write(raw)
            except Exception as e: self.send_error(500,str(e))
            return
        super().do_GET()
    def do_POST(self):
        if self.path != "/api/dados": return self.send_error(404)
        n=int(self.headers.get("Content-Length","0"))
        try:
            obj=json.loads(self.rfile.read(n).decode("utf-8"))
            DATA.write_text(json.dumps(obj,ensure_ascii=False,indent=2),encoding="utf-8")
            self.send_response(204); self.end_headers()
        except Exception as e: self.send_error(400,str(e))

if __name__=="__main__":
    port=8791
    url=f"http://127.0.0.1:{port}"
    threading.Thread(target=lambda:(time.sleep(.7),webbrowser.open(url)),daemon=True).start()
    print("Gabinete:",url)
    ThreadingHTTPServer(("127.0.0.1",port),H).serve_forever()
