function impares{
param([Parameter()] [int] $num)
$cont = 0
$suma = 0
for($i=0 ; $i-le $num ; $i++){

    $m = ($i % 2)
    if($m -ne 0){

        Write-Host "Numero aceptado: "$i

        $cont = ($cont + 1)
        $suma = ($suma + $i)   
    }
}

Write-Host "Cantidad de Impares sumados: " $cont
Write-Host "Valor de los numeros sumados: " $suma

}
pares -num 100


