import struct

def send_msg(sock, msg):
    try:
        data = msg.serialize()
        length = struct.pack('>I', len(data))
        sock.sendall(length + data)
    except Exception as e:
        raise ConnectionError(f"Send failed: {e}")


def recv_msg(sock):
    try:
        raw_len = recvall(sock, 4)
        if not raw_len:
            return None
        length = struct.unpack('>I', raw_len)[0]
        return recvall(sock, length)
    except Exception:
        return None


def recvall(sock, n):
    data = b''
    while len(data) < n:
        packet = sock.recv(n - len(data))
        if not packet:
            return None
        data += packet
    return data
