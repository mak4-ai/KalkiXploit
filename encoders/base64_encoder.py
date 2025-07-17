import base64

def base64_encode(data: str) -> str:
    encoded_bytes = base64.b64encode(data.encode('utf-8'))
    return encoded_bytes.decode('utf-8')

def base64_decode(data: str) -> str:
    decoded_bytes = base64.b64decode(data.encode('utf-8'))
    return decoded_bytes.decode('utf-8')
