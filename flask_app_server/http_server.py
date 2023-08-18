import http.server 
import socketserver 


#specify port 
PORT = 8000
#path to html files
directory = "C:/Users/dylan/flask_app/templates"


class SimpleHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    pass 




#start server
with socketserver.TCPServer(("", PORT), SimpleHTTPRequestHandler) as httpd:
    print(f"Server running at port {PORT}")
    #serve indefinitely
    httpd.serve_forever()
    