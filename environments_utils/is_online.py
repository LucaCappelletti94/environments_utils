import socket


def is_online() -> bool:
    """Returns whether the system is currently online."""
    try:
        socket.create_connection(
            (
                socket.gethostbyname("1.1.1.1"),
                80
            ),
            2
        ).close()
        return True
    except Exception:
        return False
