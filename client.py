import xmlrpc.client

HOST = "http://127.0.0.1:9000"


if __name__ == "__main__":
    try:
        proxy = xmlrpc.client.ServerProxy(HOST)
        laptop = proxy.get_product("laptop")

        print("Name:", laptop["name"])
        print("Description:", laptop["description"])
        print("Price:", laptop["price"])
    except Exception as exc:
        print("Exception in client side:", exc)
