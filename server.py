from xmlrpc.server import SimpleXMLRPCServer

def greet(greeting):
      return f"{greeting}. This message is from the server."

server = SimpleXMLRPCServer(("localhost", 8000))
print("Server running on port 8000...")

server.register_function(greet, "greet")
server.serve_forever()
