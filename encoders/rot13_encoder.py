def rot13_encode(data: str) -> str:
    return data.translate(
        str.maketrans(
            "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
            "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"
        )
    )

def rot13_decode(data: str) -> str:
    # ROT13 encoding is symmetrical, so decode is same as encode
    return rot13_encode(data)
