#Servidor                   #Cliente
"""
socket()                    socket()
   |                            |
bind()                          |
   |                            |
listen()                        |
   |                            |
accept()                        |
   |                            |
   |                            |
   |        <---------       connect()
   |                            |
recv()        <-----         send()
   |                            |
send()       -------->       recv()
"""