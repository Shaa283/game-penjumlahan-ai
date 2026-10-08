from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler

HOST = "127.0.0.1"
PORT = 8000

class Handler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

if __name__ == "__main__":
    server = ThreadingHTTPServer((HOST, PORT), Handler)
    print("========================================")
    print(" Game Penjumlahan - Server Lokal")
    print("========================================")
    print(f"Server aktif di: http://localhost:{PORT}")
    print("Buka alamat tersebut secara manual di Chrome/Edge.")
    print("Jangan tutup terminal selama game digunakan.")
    print("Tekan CTRL+C untuk menghentikan server.")
    print("========================================")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer dihentikan.")
    finally:
        server.server_close()
