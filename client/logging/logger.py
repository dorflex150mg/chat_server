import os
import datetime
import hashlib

class Logger():
    log_dir_name = "/log/"
    SEPARATOR = ": "
    INCOME_TAG = "<< "
    OUTGOING_TAG = ">> "
    BREAK = "\n"
    path = "/"
    
    def __init__(self):
        cur_dir = os.getcwd()
        path = cur_dir + self.log_dir_name
        if not (os.path.isdir(path)):
            os.mkdir(path)
        self.path = path

    def update(self, dest_id, msg, income=False):
        time = datetime.datetime.now()
        time_label = time.strftime("%d.%m.%Y - %H:%M:%S")
        msg_id = hashlib.md5(msg).hexdigest()
        with open(self.path + dest_id, "a+") as log_file:
            if income:
               tag = self.INCOME_TAG
            else:
               tag = self.OUTGOING_TAG
            log_file.write(tag + time_label + self.SEPARATOR + msg  +  self.SEPARATOR + msg_id + self.BREAK)

    def log_reply(self, msg, dest_id, reply):
        msg_id = hashlib.md5(msg).hexdigest()
        with open(self.path + dest_id, "a+") as log_file:
             log_file.write(msg_id + self.SEPARATOR + reply + self.BREAK)
 
                
