#!/usr/bin/python
from __future__ import print_function 
import os
import sys
sys.path.insert(0, os.getcwd())
from interface.termAdapter import TermAdapter
from logging.logger import Logger
from netUtils.urlAdapter import UrlAdapter 
from netUtils.pop import Pop
import threading
import yaml

this_termAdapter = None

class Client():
    term_adapter = TermAdapter()
    log = None
    url_adapter = None
    client_id = None
    register = None
    name = None
    Record = None
    command = ""

    def __init__(self, register):
        if self.verify_register(register):
            self.register = register
            self.url_adapter = UrlAdapter(self.register)
            self.log = Logger()
        else:
            raise ValueError("Invalid Register")

    #TODO: actually verify the register
    def verify_register(self, register):
        return True

    def send_message(self, dest_id):
        msg = self.term_adapter.get_text()
        #TODO: implement command tool
        self.command = msg
        print("[Sending message: %s to %s" % (msg, dest_id)) 
        self.url_adapter.send(dest_id, msg)
        

def main():
    this_termAdapter = TermAdapter()
    print("||Please, insert your id:")
    register_in = this_termAdapter.get_text()
    c = Client(register_in)
    while not c.url_adapter.login():
        print("Register not valid. Are you a goddamn hack?")
    dests = c.url_adapter.get_dest_list()
    dest_id = ""
    while dest_id not in dests:
        print("|| Select Destinatary:")
        [print(dest) for dest in dests]
        dest_id = c.term_adapter.get_text()
        if dest_id in dests:
            print("|| Talking to ", dest_id)
        else:
            print("|| Nope")
    income_thread = Pop(c.url_adapter, c.term_adapter, dest_id)
    income_thread.start()
    while(c.command != "!Exit"):
        c.send_message(dest_id)
    income_thread.join() 

if __name__ == "__main__":
    main()
