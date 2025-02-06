import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:8000")

greeting = "Hello there"
message = proxy.greet(greeting)

print("Message received from server.")
print(message)