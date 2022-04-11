# coding: utf-8
# Your code here!
import math;

MIN_DEGREE = 0;
MAX_DEGREE = 360;
DEGREE_INTERVAL = 15;
# 以下は有効桁数
SIGNIFICANT_DIGITS = 4;

for d in range(MIN_DEGREE,MAX_DEGREE,DEGREE_INTERVAL):
    radian = math.radians(d);
    
    print(f'sin{d}°の値は{round(math.sin(radian),SIGNIFICANT_DIGITS)}');
    print(f'cos{d}°の値は{round(math.cos(radian),SIGNIFICANT_DIGITS)}');
    if d in [90,270]:
        print(f'tan{d}°の値は定義されていません。');
    else:
        print(f'tan{d}°の値は{round(math.tan(radian),SIGNIFICANT_DIGITS)}');
