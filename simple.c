#include <stdio.h>

void count(int n)
{
   for (int i = 0; i < n; ++i)
   {
      printf("Counting to %d, currently on %d\n", n, i);
   }
}
