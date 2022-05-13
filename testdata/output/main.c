#include <stdio.h>
#include "point.h"

int main(int argc, char ** argv) {
//    Point* p = Point__impl.new();
    p->x = 10;
    p->y = 12;
    printf("%s", Point__impl.toString(p));
    printf("Hello, World!\n");
    return 0;
}
