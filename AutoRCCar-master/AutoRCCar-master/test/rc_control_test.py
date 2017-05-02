__author__ = 'zhengwang'

import serial
import pygame
from pygame.locals import *


class RCTest(object):

    def __init__(self):
        pygame.init()
        pygame.display.set_mode((100, 100))
        self.ser = serial.Serial("COM3", 115200, timeout=1)  # open serial port at 115200 with 1s timeout
        self.send_inst = True     # command to send or it terminates later with pygame
        self.steer()

    def steer(self):

        while self.send_inst:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    key_input = pygame.key.get_pressed()

                    # complex orders
                    if key_input[pygame.K_UP] and key_input[pygame.K_RIGHT]:
                        print("Forward Right")
                        self.ser.write(chr(6))   # write a 6 to the arduino connected at serial port 115200
                    #
                    # elif key_input[pygame.K_UP] and key_input[pygame.K_LEFT]:
                    #     print("Forward Left")
                    #     self.ser.write(chr(7))
                    #
                    # elif key_input[pygame.K_DOWN] and key_input[pygame.K_RIGHT]:
                    #     print("Reverse Right")
                    #     self.ser.write(chr(8))
                    #
                    # elif key_input[pygame.K_DOWN] and key_input[pygame.K_LEFT]:
                    #     print("Reverse Left")
                    #     self.ser.write(chr(9))

                    # simple orders
                    elif key_input[pygame.K_UP]:
                        print("Forward")
                        self.ser.write(chr(1))

                    elif key_input[pygame.K_DOWN]:
                        print"Reverse %d", chr(2)
                        self.ser.write(chr(2))

                    elif key_input[pygame.K_RIGHT]:
                        print("Right")
                        self.ser.write(chr(3))

                    elif key_input[pygame.K_LEFT]:
                        print("Left")
                        self.ser.write(chr(4))


                    # exit
                    elif key_input[pygame.K_x] or key_input[pygame.K_q]:
                        print 'Exit'
                        self.send_inst = False
                        self.ser.write(chr(0))
                        self.ser.close()
                        break

                elif event.type == pygame.KEYUP:
                    self.ser.write(chr(0))

if __name__ == '__main__':
    RCTest()

