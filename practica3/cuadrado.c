#include <stdio.h>

int main()
{
    printf("Hello World\n");
    
    int cuadrado(int num1){
        
        int cuadrado = num1 * num1;
        return cuadrado;
    }
    
    printf("%d", cuadrado(9));

    return 0;
}
