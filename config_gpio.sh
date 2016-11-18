#!/bin/bash
# set gpio 17 & 18 as output (and clear) and set gpio 0 as input
for pin in 0 ; do
    echo "Configuring wPi pin $pin as output and clearing"
    gpio write $pin 0
    gpio export $pin out
done
for pin in 8 ; do
    echo "Configuring wPi pin $pin as input"
    gpio export $pin in
done

gpio readall
#echo `gpio readall`
