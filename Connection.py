import msgpack
import struct
import socket
import pickle

# update_info_list = [character_id, GameAction]
#


class Connection(object):
    def __init__(self, sock):
        self.sock = sock

    def send_packed(self, msg):
        msg = msgpack.packb(msg)
        msg = struct.pack(">I", len(msg)) + msg
        self.sock.sendall(msg)

    def receive_packed(self):
        msg_len = self.sock.recv(4)
        if msg_len:
            msg_len = struct.unpack(">I", msg_len)[0]
            msg = self.sock.recv(msg_len)
            msg = msgpack.unpackb(msg, encoding="utf-8")
            return msg

    def send_byte(self, msg):
        msg_to_send = bytes([msg])
        self.sock.sendall(msg_to_send)

    def receive_byte(self):
        received_msg = self.sock.recv(1)
        if not received_msg:
            return
        return ord(received_msg.decode())

    def send_object(self, object_to_send):
        pickled_object = pickle.dumps(object_to_send)
        print(len(pickled_object))
        print(len(struct.pack(">I", len(pickled_object))))
        msg = struct.pack(">I", len(pickled_object)) + pickled_object
        self.sock.sendall(msg)

    def receive_object(self):
        msg_len = self.sock.recv(4)
        if msg_len:
            msg_len = struct.unpack(">I", msg_len)[0]
            msg = self.sock.recv(msg_len)
            print(msg)
            msg = pickle.loads(msg)
            return msg
