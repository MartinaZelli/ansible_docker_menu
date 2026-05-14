from http.server import HTTPServer, BaseHTTPRequestHandler

class BasicHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Risponde a tutte le richieste con la pagina configurata
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        content = """
<!DOCTYPE html>
<html>
<head>
<style>
    body {
        background-color: #E6E6FA;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        margin: 0;
    }
    .card {
        background: rgba(255, 255, 255, 0.6);
        padding: 40px;
        border-radius: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        text-align: center;
    }
    h1 { color: #2c3e50; margin: 0; }
</style>
</head>
<body>
    <div class="card">
        <h1>servizio 1 attivo</h1>
        <p>In ascolto sulla porta: 7111</p>
    </div>
</body>
</html>
"""
        self.wfile.write(content.encode('utf-8'))

if __name__ == "__main__":
    PORT = 7111
    server = HTTPServer(('0.0.0.0', PORT), BasicHandler)
    print(f"Server 'Servizio 1' avviato correttamente.")
    print(f"Indirizzo locale: http://localhost:{PORT}")
    server.serve_forever()
