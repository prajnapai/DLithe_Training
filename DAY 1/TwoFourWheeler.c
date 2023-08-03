#include <stdio.h>

int main(){
    int twoWheeler,fourWheeler,noVehicles,noWheels;
    scanf("%d%d",&noVehicles,&noWheels);
    fourWheeler = (noWheels - 2*noVehicles)/2;
    twoWheeler = noVehicles - fourWheeler;
    printf("TW=%d FW=%d",twoWheeler, fourWheeler);

    return 0;
}