char *hari[] =
{"Kamis", "Jum'at", "Sabtu", "Minggu", "Senin", "Selasa", "Rabu"};
char *weton[] =
{"Wage", "Kliwon", "Legi", "Paing", "Pon"};
int hb[] = {0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365};

int jmlhari(int d, int m, int y) {
int ht = (y - 1970) * 365 - 1;

int hs = hb[m - 1] + d;

int kab = 0;

int i;

if(y % 4 == 0) {
if(m > 2) {
hs++;
}
}

for(i = 1970; i < y; i++) {
if(i % 4 == 0) {
kab++;
}
}
return (ht + hs + kab);
}


#include <stdio.h>

int main(void) {
int tg, bl, th, idxhari, idxweton;

printf("\n-- MENGHITUNG WETON --\n");
printf(" tanggal [d m y]: ");
scanf("%d%d%d", &tg, &bl, &th);

idxhari = jmlhari(tg, bl, th) % 7;
idxweton = jmlhari(tg, bl, th) % 5;
printf(" hasil: %s %s\n", hari[idxhari], weton[idxweton]);
return 0;
}