def xor_encode(data: str, key: str) -> str:
    """
    XOR encodes a string using the given key.
    Returns hex string of encoded bytes.
    """
    key_bytes = key.encode()
    data_bytes = data.encode()
    encoded_bytes = bytearray()

    for i in range(len(data_bytes)):
        encoded_bytes.append(data_bytes[i] ^ key_bytes[i % len(key_bytes)])

    return encoded_bytes.hex()

def xor_decode(encoded_hex: str, key: str) -> str:
    """
    Decodes a hex string XOR encoded with the given key.
    Returns decoded string.
    """
    encoded_bytes = bytes.fromhex(encoded_hex)
    key_bytes = key.encode()
    decoded_bytes = bytearray()

    for i in range(len(encoded_bytes)):
        decoded_bytes.append(encoded_bytes[i] ^ key_bytes[i % len(key_bytes)])

    return decoded_bytes.decode('utf-8')
