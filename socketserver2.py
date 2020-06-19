#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @File  : socketserver2.py
# python3 socket TCP ������ һ�Զ�ת����Ϣ
# @Author: ����ɭ
# @Date  : 2018/8/29
# @Desc  :


import socket
import select


# ����һ����
class ChatServer:
    # ��ʼ�� ��������˿ڼ���
    def __init__(self, port):
        self.port = port
        # ���ò���
        self.srvsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.srvsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.srvsock.bind(("", port))
        self.srvsock.listen(10)  # ���ü�������
        # ������߷�����
        self.descripors = [self.srvsock]
        print("Server started!")

    # ���м�������
    def run(self):
        while True:
            # ��ȡ �µ���������
            (sread, swrite, sexc) = select.select(self.descripors, [], [])
            # �� �Ի�ȡ��������
            for sock in sread:
                # �ж��Ƿ����µ�����
                if sock == self.srvsock:
                    self.accept_new_connection()
                else:
                    # �����յ�����Ϣ
                    str_send = sock.recv(1024).decode('gbk')   # ����������С1024
                    # ����Ƿ�Ͽ�����
                    host, port = sock.getpeername()
                    if str_send == '':
                        str_send = 'Client left %s:%s\r\n' % (host, port)
                        self.broadcast_str(str_send, sock)
                        sock.close
                        self.descripors.remove(sock)
                    else:
                        newstr = '[%s:%s] %s' % (host, port, str_send)
                        self.broadcast_str(newstr, sock)

    # ����һ���µ����ӿͻ���
    def accept_new_connection(self):
        # ��������
        newsock, (remhost, remport) = self.srvsock.accept()
        # �������
        self.descripors.append(newsock)
        newsock.send("You are Connected\r\n".encode('utf8'))
        str_send = 'Client joined %s:%s' % (remhost, remport)
        self.broadcast_str(str_send, newsock)

    # �㲥����
    def broadcast_str(self, str_send, my_sock):
        # ������������
        for sock in self.descripors:
            if sock != self.srvsock and sock != my_sock:
                sock.send(str_send.encode('utf8'))
        print("ת������:"+str_send+"        --- ���ͳɹ���")


# ʵ��������������
ChatServer(1010).run()