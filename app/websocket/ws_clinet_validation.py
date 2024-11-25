async def validate_client_ip(client_info):
    """Validate the client's information."""
    if isinstance(client_info, tuple) and len(client_info) == 2:
        client_ip, client_port = client_info
        if client_ip and client_port:
            print(f"Client {client_ip}:{client_port} is valid.")
            return f"{client_ip}:{client_port}"
    print("Invalid client IP. Closing the connection.")
    return None
