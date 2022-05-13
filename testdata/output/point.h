typedef struct {
  int x;
  int y;
} Point;

struct Point__public__def {
  Point * (new*)(void);
  Point * (newXY*)(int,int);
  const char * (toString*)(Point*);
  void (free*)(Point*);
} Point__impl;