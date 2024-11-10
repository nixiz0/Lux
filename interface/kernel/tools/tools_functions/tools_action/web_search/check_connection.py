import socket


def is_connected():
    try:
        # if connected it's reachable
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False