import xmlrpc.server

from product import ProductImpl

HOST = "127.0.0.1"
PORT = 9000


class Server:
    def __init__(self):
        self.products = {
            "laptop": ProductImpl("Laptop", "Lenovo laptop", 800000.0),
            "ram": ProductImpl("Mobile", "MI 9 mobile", 24000.0),
            "bag": ProductImpl("Bag", "Branded bag", 800.0),
            "charger": ProductImpl("Charger", "MI Charger", 230.0),
        }

    def get_product(self, key):
        if key not in self.products:
            raise KeyError(f"Product '{key}' not found")
        return self.products[key].to_dict()


if __name__ == "__main__":
    print("Server is booting....")
    server = xmlrpc.server.SimpleXMLRPCServer((HOST, PORT), allow_none=True)
    server.register_introspection_functions()
    server.register_instance(Server(), allow_dotted_names=True)
    print(f"XML-RPC server running on http://{HOST}:{PORT}")
    server.serve_forever()
