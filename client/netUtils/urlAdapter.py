from logging.logger import Logger
import os
import socket
import urllib
import urllib2
import yaml


class UrlAdapter():
    log = Logger()
    relative_conf_path = "config/"
    conf_filename = ""
    path = "/"
    SLASH = "/"

    def __init__(self, client_register):
       self.dest_list_last = {}
       self.client_register = client_register
       cur_dir = os.getcwd()
       self.conf_filename = os.getenv("conf") 
       self.relative_conf_path += self.conf_filename
       conf_path = cur_dir + self.SLASH + self.relative_conf_path
       print("conf path: ", conf_path)
       with open(conf_path, "r") as conf_file:
           conf_data = yaml.load(conf_file, Loader=yaml.Loader)
           self.server_list = conf_data["server_list"]
           self.dest_list = conf_data["dest_list"]
           self.read_endpoint = conf_data["endpoints"]["read"]
           self.send_endpoint = conf_data["endpoints"]["send"]
           self.login_endpoint = conf_data["endpoints"]["login"]
       for dest_id in self.dest_list:
           self.dest_list_last[dest_id] = 0 

    def get_dest_list(self):
        if len(self.dest_list) > 0:
            return self.dest_list
        else:
            raise ValueError("No dests")
            
    def get_server(self):
        if len(self.server_list) > 0:
            return self.server_list[0]
        else:
            raise ValueError("No servers")

    def login(self):
        ip = socket.gethostname()
        dict_data = {"register": self.client_register}
        data = urllib.urlencode(dict_data)
        url = self.get_server() + self.login_endpoint + "?" + data
        print "[INFO] calling server at %s" % url
        response = urllib2.urlopen(url)
        accepted = response.read()
        print "[INFO] server replied with %s" % accepted
        if accepted == "401":
            return False
        elif accepted == "200":
            return True
        else:
            print str(accepted)
            raise ValueError("Unexpected Response")
        
    def read(self, dest_id):
        dict_data = {"dest_id": dest_id, "register": self.client_register}
        data = urllib.urlencode(dict_data)
        url = self.get_server() + self.read_endpoint + "?" + data
        response = urllib2.urlopen(url)
        updates = response.read()
        if type(eval(updates)) == list:
            (self.log.update(dest_id, update, income=True) for update in updates)
        return updates

    def send(self, dest_id, msg):
        url = self.get_server() + self.send_endpoint
        dict_data = {"dest_id": dest_id, "source_id": self.client_register,  "msg": msg, "last": dest_id_last[dest_id]}
        data = urllib.urlencode(dict_data)
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        req = urllib2.Request(url, headers=headers, data=data)
        self.log.update(dest_id, msg)
	reply = urllib2.urlopen(req)
        content = reply.read()
        self.log.log_reply(msg, dest_id, content)
        print("Finished sending")
    
    def get_last(dest_id):
        return self.dest_list_last[dest_id]
