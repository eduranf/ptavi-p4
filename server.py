#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
"""
Clase (y programa principal) para un servidor de eco
en UDP simple
"""

import SocketServer


class SIPRegisterHandler(SocketServer.DatagramRequestHandler):
    """
    Echo server class
    """

    dic = {}

    def handle(self):
        # Escribe dirección y puerto del cliente (de tupla client_address)
        self.wfile.write('SIP/2.0 200 OK\r\n\r\n')
        clientIP, clientPort = self.client_address
        print 'client IP: ' + clientIP + ':' + str(clientPort)
        while 1:
            # Leyendo línea a línea lo que nos envía el cliente
            line = self.rfile.read().strip()
            if line[:8] == 'REGISTER':
                self.dic[line.split()[1]] = self.client_address
                print "Dic is: ", self.dic
            if not line:
                break

if __name__ == "__main__":
    # Creamos servidor de eco y escuchamos
    serv = SocketServer.UDPServer(("", 6001), SIPRegisterHandler)
    print "Lanzando servidor UDP de eco..."
    serv.serve_forever()
