from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import json
from src.services.property_service import get_properties

class PropertyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_url = urlparse(self.path)

        if parsed_url.path == "/health":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"status": "ok"}).encode("utf-8"))
            return

        if parsed_url.path == "/properties":
            query_params = parse_qs(parsed_url.query)
            filters = {}

            accepted_filters = {"year", "city", "status"}
            for key in query_params.keys():
                if key not in accepted_filters:
                    self._send_json_error(400, f"Invalid filter: '{key}'")
                    return

            if "year" in query_params:
                try:
                    filters["year"] = int(query_params["year"][0])
                except ValueError:
                    self._send_json_error(400, "Invalid 'year' filter. Must be an integer.")
                    return

            if "city" in query_params:
                filters["city"] = query_params["city"][0]

            if "status" in query_params:
                status = query_params["status"][0]
                allowed_statuses = {"pre_venta", "en_venta", "vendido"}
                if status not in allowed_statuses:
                    self._send_json_error(400, "Invalid 'status'. Must be one of: pre_venta, en_venta, vendido.")
                    return
                filters["status"] = status

            try:
                properties = get_properties(filters)
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(properties, ensure_ascii=False).encode("utf-8"))
            except Exception as e:
                self._send_json_error(500, f"Internal server error: {str(e)}")
        else:
            self._send_json_error(404, "Endpoint not found.")

    def _send_json_error(self, status_code, message):
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps({"error": message}).encode("utf-8"))

def run(server_class=HTTPServer, handler_class=PropertyHandler, port=8080):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"API server running on http://localhost:{port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
