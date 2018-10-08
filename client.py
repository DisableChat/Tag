import socket
import sys
import charGrid as cg
import curses
from curses import wrapper

##
# MagikarpUsedFly
##

##
# Description: Client for game
# yikes
##


MIN_BOUNDS = 0
MAX_BOUNDS = 10


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def close_socket(sock):
    print('closing socket')
    sock.close()

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

def main(stdscr):
    try:
        # Hide Cursor
        curses.curs_set(0)

        # Starting Possition
        Y_Cor = 2
        X_Cor = 0

        # Loop to continually update Y_Cor and X_Cor, then clear the screen and
        # print the ascii symobl in correct location.
        while True:
            stdscr.addstr(0, 0, 'Y_Cor:{} X_Cor:{}'.format(Y_Cor, X_Cor))
            stdscr.addch(Y_Cor, X_Cor, '+', curses.A_UNDERLINE)
            Y_Cor, X_Cor = cg.get_directional_input(Y_Cor, X_Cor, stdscr.getkey())

            cordinate_package = 'Player1-Cordinates:(y:{}, x:{})'.format(Y_Cor, X_Cor)
            cordinate_package = cordinate_package.encode('utf-8')

            # Send data
            print('sending {!r}'.format(cordinate_package))
            sock.sendall(cordinate_package)


            # Look for the response
            amount_received = 0
            amount_expected = len(cordinate_package)

            while amount_received < amount_expected:
                data = sock.recv(1024)
                amount_received += len(data)
                print('received {!r}'.format(data))
            stdscr.clear()
            stdscr.refresh()
    except KeyboardInterrupt:
        sys.exit("Keyboard Interrupt, Quitting...")


wrapper(main)
print('hiiiii')
close_socket(sock)
