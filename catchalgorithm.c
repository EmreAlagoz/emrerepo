#include <stdio.h>
#include <stdlib.h>
int main(){
	//oyuncunun konumu//
	int oyuncu[2]={32,67};
	//canavarin konumu//
	int canavar[2]={0,0};
	int dogrulama=1;
	//X ekseninde yaklasma icin [0] degerlerini aliyoruz//
	while(dogrulama)
	{
	if(canavar[0] > oyuncu[0])
		canavar[0]--;
	else if(canavar[0] < oyuncu[0])
		canavar[0]++;
	else
	dogrulama =-1;
	printf("Canavar ve oyuncu ayni x ekseninde\n");
	break;
	// x ekseninde ayni konumdalar
	}
	//Y ekseninde yaklasma icin [1] degerlerini aliyoruz//
	while(dogrulama)
	{
	if(canavar[1] > oyuncu[1])
		canavar[1]--;
	else if(canavar[1] < oyuncu[1])
		canavar[1]++;
	else
	dogrulama =-1;
	printf("Canavar ve oyuncu ayni y ekseninde\n");
	break;
	}
	// y ekseninde ayni konumdalar
	return 0;
}
