# Compile to an object file
gcc -Wall -Wextra -pedantic -c -fPIC simple.c -o simple.o
# Compile to a shared object file (library)
gcc -shared simple.o -o simple.so

# Compile to an object file
gcc -Wall -Wextra -pedantic -c -fPIC less_simple.c -o less_simple.o
# Compile to a shared object file (library)
gcc -shared less_simple.o -o less_simple.so

# Compile to an object file
gcc -Wall -Wextra -pedantic -c -fPIC maximum.c -o maximum.o
# Compile to a shared object file (library)
gcc -shared maximum.o -o maximum.so

# Compile to an object file
gcc -Wall -Wextra -pedantic -c -fPIC supermax.c -o supermax.o
# Compile to a shared object file (library)
gcc -shared supermax.o -o supermax.so