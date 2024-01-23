import http.server
import socketserver

PORT=8080

class FakeRedirect(http.server.SimpleHTTPRequestHandler):
   def do_GET(self):
       uri='http://localhost:8081'
       i = self.path.index ( "?" ) + 1
       params = [ tuple ( p.split("=") ) for p in self.path[i:].split ( "&" ) ]
       for k,v in params:
         if k=='uri':
            uri=v
       self.send_response(301)
       new_path = '%s%s'%(uri, self.path)
       self.send_header('Location', new_path)
       self.end_headers()

socketserver.TCPServer(("", PORT), FakeRedirect).serve_forever()
