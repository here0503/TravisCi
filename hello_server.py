import http.server
import socketserver

# Configuración del puerto y dirección
port = 8000
handler = http.server.SimpleHTTPRequestHandler

# Crear un servidor web
with socketserver.TCPServer(("", port), handler) as httpd:
    print(f"Servidor web en el puerto {port}")
    # Iniciar el servidor
    httpd.serve_forever()