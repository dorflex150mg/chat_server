#!/bin/bash
#apache2 -f /etc/apache2/apache2.conf -k stop
#apache2 -f /etc/apache2/apache2.conf -k start
sudo service apache2 start
while true; do sleep 100; done
