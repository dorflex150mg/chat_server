from __future__ import print_function
import sys


prompt = ">>"
incoming = "-- "

class TermAdapter:

    def get_text(self):
        print(prompt, end='')
        msg = raw_input()
        return msg

    def insert(self, dest_id, msg):
        print(incoming, dest_id, ": ", msg)
