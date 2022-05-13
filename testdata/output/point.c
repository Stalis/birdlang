#include <stdlib.h>
#include <stdio.h>

#include "point.h"

static Point * Point__new();
static Point * Point__newXY(int x, int y);
static const char * Point__toString(Point *);
static void Point__free(Point *);

struct Point__public__def Point__impl = {
    .new = & Point__new,
    .newXY = & Point__newXY,
    .free = & Point__free
};

static Point * Point__alloc() {
    return malloc(sizeof(Point));
}

static Point * Point__new() {
    return Point__newXY(0, 0);
}

static Point * Point__newXY(int x, int y) {
    Point * res = Point__alloc();
    res->x = x;
    res->y = y;
    return res;
}

static const char * Point__toString(Point * p) {
    char * str = calloc(10, sizeof(char));
    snprintf(str, 10, "{%d;%d}", p->x, p->y);
    return str;
}

static void Point__finalize(Point * p) {
}

static void Point__dispose(Point * p) {
    free(p);
}

static void Point__free(Point * p) {
    Point__finalize(p);
    Point__dispose(p);
}