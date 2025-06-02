#include <stdio.h>

int main() {
    int A[5], B[5];
    int num;

// Entrada dos elementos do vetor A
    printf("Digite 5 elementos do Vetor A:\n");
    for (num = 0; num < 5; num++) {
        printf("Elemento %d: ", num + 1);
        scanf("%d", &A[num]);
    }

// Cálculo do vetor B
    for (num = 0; num < 5; num++) {
        B[num] = A[num] * 3;
    }

// Exibição do vetor B
    printf("\n Os elementos do Vetor B são:\n");
    for (num = 0; num < 5; num++) {
        printf("B[%d] = %d\n", num, B[num]); 
        
// Exibe cada elemento em uma linha
    }
    
    return 0;
}
