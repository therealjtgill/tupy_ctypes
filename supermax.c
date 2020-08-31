
typedef void (*callbackFunc)(int);

void callbackExample(int n, callbackFunc f)
{
   f(n);
}
