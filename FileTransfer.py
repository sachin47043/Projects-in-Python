import http.server
import socketserver

PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as http:
    print(f"Server running on port {PORT}")
    http.serve_forever()