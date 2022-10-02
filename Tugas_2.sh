#!/bin/bash

read -p "Masukkan nilai A : " nilaiA;
read -p "Masukkan nilai B : " nilaiB;

if [ $nilaiA -gt $nilaiB ]
then
 echo "Nilai A > Nilai B"
elif [ $nilaiA -lt $nilaiB ]
then
 echo "Nilai A < Nilai B"
else
 echo "Nilai A == Nilai B"
fi

#-
