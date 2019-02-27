import socket as sk

class ClientError(Exception):
    pass
    
class ClientSocketError(ClientError):
    """Исключение, выбрасываемое клиентом при сетевой ошибке"""
    pass


class ClientProtocolError(ClientError):
    """Исключение, выбрасываемое клиентом при ошибке протокола"""
    pass
    
class Client:
    def __init__(self, ip, port, timeout = None):
        self.ip = ip
        self.port = port
        self.timeout = timeout

    def _comm(self, command):
        with sk.create_connection((self.ip, self.port), self.timeout) as s:
            s.sendall(command.encode("utf-8"))
            answ = s.recv(1024).decode("utf-8")
            if answ.split("\n")[0] != "ok":
                raise ClientError()
            return answ.split("\n")[1:-2]

    def get(self, key):
        res = {}
        answ = self._comm("get " + key + "\n")
        for l in answ:
            key, val, ts = l.split()
            if key not in res:
                res[key] = list()
            res[key].append((int(ts), float(val)))
        return res

    def put(self, key, val, timestamp = None):
        if not timestamp:
            timestamp = str(int(time.time()))
        command = "put " + str(key) + " " + str(val) + " " + str(timestamp) + "\n"
        self._comm(command)