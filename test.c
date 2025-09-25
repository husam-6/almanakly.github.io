#include <stdio.h>
int main() {
    int a = 10;
    switch (a) {
        case 100:
            printf("Equals 100!\n"); 
            break;
        case 5: 
            printf("Equals 5\n"); 
            break;
        default:
            printf("Matched none!\n");
    }

    int b = a > 5 ? a < 5 : -100;
    // if (a > 5) {
    //  b = 40; 
    // } else {
    //  b = -100; 
    // }
    printf("%d\n", b);
}
