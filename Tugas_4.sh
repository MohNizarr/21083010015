#!/bin/bash
echo "Input : "
a=0
read input

until [ ! $input -gt $a ]
do
  echo $input
  input=$((input - 2)) #bilangan yg diinput dikurangi 2
done

# -gt : Memeriksa apakah nilai operan kiri lebih besar daripada operan kanan (>)
