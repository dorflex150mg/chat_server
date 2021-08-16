#!/bin/bash
usage () {
    echo -e "Usage:"
    echo -e "\tBuilds the chat client container and runs it"
    echo -e "\twith a certain id"
    echo -e "\t./run.sh id"
    echo -e "\t* id: 0 for fren and 1 for other_fren"
}
if [ -z "$1" ]
then
    usage
    exit
fi
if [ $# -gt 2 ]
then
    usage
    exit
fi
docker build -t chat_client . 
docker run -it --env "conf"=$1 chat_client
