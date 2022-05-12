#!/bin/bash
VMLIST=( 0.0.0.0 127.0.0.1 8.8.8.8 )
while true; do
    count=0
    for vm in ${VMLIST[@]}
    do
        echo -e "\n" test ping pacage loss in vm $vm ... 
        testping=$(ping $vm -c 3 | grep -oP '\d+(?=% packet loss)')
        if  [ $testping != '0' ] 
        then
            echo "ping $vm failed "
            curl --location --request POST 'http://52.170.32.128:9000/status/0' --header 'service: '$vm
        else
            count=$((count+1))
        fi
    done
    if [ $count == ${#VMLIST[@]} ]
    then
        curl --location --request POST 'http://52.170.32.128:9000/status/1' --header 'service: ok'
    fi
done