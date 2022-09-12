#!/usr/bin/env python

class Hello_World:

    def __init__(self):
        self.message = 'Welcome to python scripting'

    def PrintMessage(self):
        print(self.message)

if __name__ == '__main__':
    obj_hello = Hello_World()
    obj_hello.PrintMessage()
