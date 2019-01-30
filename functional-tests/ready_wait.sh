#!/bin/sh
while : ; do
    sleep 5
    curl -f http://nginx:10920/ > /dev/null
    [ "$?" != "0" ] || break
done

echo "App is ready"
