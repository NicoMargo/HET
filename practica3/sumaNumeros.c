#include <stdio.h>

int main()
{
    printf("Hello World\n");
    
    int suma(int num1, int num2, int num3){
        
        int resultado = num1 + num2;
        resultado = resultado + num3;
        return resultado;
    }
    
    printf("%d", suma(1,2,3));

    return 0;
}
