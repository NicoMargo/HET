#include <stdio.h>

int suma(int num1, int num2, int num3){
        
        int resultado = num1 + num2;
        resultado = resultado + num3;
        return resultado;
}

int main()
{
    int resultado = suma(1,2,3);

    printf("%d", resultado);
    return 0;
}
