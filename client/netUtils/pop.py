from netUtils.urlAdapter import UrlAdapter
import time
import os
import threading
import yaml


class Pop(threading.Thread):
    
   def __init__(self, url_adapter, term_adapter, dest_id):
       threading.Thread.__init__(self)
       self.current_dest_id = dest_id
       self.url_adapter = url_adapter
       self.term_adapter = term_adapter

   def set_dest_id(self, dest_id):
       self.dest_id = dest_id
   
   def run(self):
       while True:
           in_msg = self.url_adapter.read(self.current_dest_id)
           if in_msg == "404":
               pass
           elif in_msg == "200":
               pass
           else:
               reply_list = eval(in_msg)
               msg = reply_list['msg']
               index = reply_list['index']
               ''.join(msg)
               if index < self.url_adapter.get_last(current_dest_id):
                   self.term_adapter.insert(self.current_dest_id, msg)
                   self.url_adapter.increment(current_dest_id)
           time.sleep(1)
