def send_msg(sock, msg):
    data = msg.serialize()
    length = len(data).to_bytes(4, 'big')
    sock.sendall(length + data)


def recv_msg(sock):
    try:
        raw_len = sock.recv(4)
        if not raw_len:
            return None
        length = int.from_bytes(raw_len, 'big')
        data = b''
        while len(data) < length:
            chunk = sock.recv(length - len(data))
            if not chunk:
                return None
            data += chunk
        return data
    except:
        return None
