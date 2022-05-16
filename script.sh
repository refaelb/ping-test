# for i in `kubectl get ns | awk '{print $1}'`; 
# do
    echo $i
    echo abc

    for x in ` kubectl -n abc top pods | grep -v Running | awk '{print $3}' ` ;
    do
        if [ "2" = $x ]
        then
            echo "m"
        
            # kubectl -n abc exec $x -- sh -c "echo abc"
        fi
        # echo $x
        # kubectl -n abc exec $x -- ping -c 3
    done
