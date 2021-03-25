#!/bin/bash


sumatoria(){
echo "Este programa suma y cuenta cuantos numeros impares hay en un rango de 0 a 100"

for((i=0;i<=$1;i++))
do
if((($i%2) != 0));then
echo "$i"
cont=$(($cont + 1))
suma=$(($suma + $i))
fi
done
echo "ls suma total es: " $suma
echo  "la cantidad de numeros sumados es: " $cont
}

sumatoria 100
