#!/bin/bash
# configure all pins as input then re-configure several as output
for pin in 0 1 2 3 4 5 6 7 8 9 ; do
    echo "Configuring BCM pin $pin as input with pull-down"
    gpio export $pin in
done
for pin in 10 11 12 13 14 15 16 17 18 19 ; do
    echo "Configuring BCM pin $pin as input"
    gpio export $pin in
done
for pin in 20 21 22 23 24 25 26 27 ; do
    echo "Configuring BCM pin $pin as input"
    gpio export $pin in
done

for pin in 6 13 19 26 ; do
    echo "Configuring BCM pin $pin as output and clearing"
    gpio export $pin out
    gpio -g write $pin 0
done

gpio readall
