import asyncio
import time
import sys

storage = {}
class ConnectionError(Exception):
    pass

class ClientServerProtocol(asyncio.Protocol):
    def __init__(self):
        self.transport = None

    def connection_made(self, transport):
        self.transport = transport
        if self.transport is None:
            raise ConnectionError("Connection failed")

    def data_received(self, data):
        cmd, info_n = data.decode("utf-8").split(" ", 1)
        info = info_n.rstrip("\n").split(" ")
        if cmd == "put":
            if len(info) != 3:
                answ = "error\nwrong command\n\n"
                self.transport.write(answ.encode("utf-8"))
                return
            answ = self._put(info)
            # ok\n\n
        elif cmd == "get":
            if len(info) != 1:
                answ = "error\nwrong command\n\n"
                self.transport.write(answ.encode("utf-8"))
                return
            answ = self._get(info)
            # ok\npalm.cpu 10.5 1501864247\neardrum.cpu 15.3 1501864259\n\n OR ok\n\n
        else:
            answ = "error\nwrong command\n\n"
        self.transport.write(answ.encode("utf-8"))

    def _put(self, info):
        # info = <key> <value> <timestamp>\n
        key, value, ts = info[0], info[1], info[2]
        if key not in storage:
            storage[key] = list()
        storage[key].append((int(ts), float(value)))
        return "ok\n\n"

    def _get(self, info):
        # info = <key>\n
        request = info[0]
        answ = "ok\n"
        if request == "*":
            for k, v in storage.items():
                new_list = []
                for item in v:
                    if item not in new_list:
                        new_list.append(item)
                storage[k] = new_list
            for key, values in storage.items():
                for val in values:
                    answ += str(key) + " " + str(val[1]) + " " + str(val[0]) + "\n"
        else:
            if request in storage:
                for key, val in storage[request]:
                    answ += str(request) + " " + str(val) + " " + str(key) + "\n"
        answ += "\n"
        return answ

def run_server(host, port):
    loop = asyncio.get_event_loop()
    coro = loop.create_server(ClientServerProtocol, host, int(port))
    server = loop.run_until_complete(coro)
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()

#run_server("127.0.0.1", 8888)