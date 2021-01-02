import math
def isPointInSquare(x:float, y:float)->bool:
      N, x0, y0 = 5, 5, 5
      return (N**2 >= x**2) and (N**2 >= y**2), math.sqrt(x ** 2 + y ** 2) <= N, math.sqrt((x-x0)**2 + (y-y0)**2) <= N

points = [
{'x': 2, 'y': 0, 'inRegion': 'unknown'},
{'x': -3, 'y': 4, 'inRegion': 'unknown'},
{'x': 5, 'y': 3, 'inRegion': 'unknown'},
{'x': 0, 'y': 7, 'inRegion': 'unknown'},
{'x': -6, 'y': 0, 'inRegion': 'unknown'}
]
print ('N, r, h, x0, y0 = 5!')
print('A)')
i = 0
while i < 5:
      circle, square, random_square = isPointInSquare(points[i]['x'], points[i]['y'])
      if circle == True:
        points[i]['inRegion'] = 'YES'
      else:
         points[i]['inRegion'] = 'NO'    
      i += 1
print(points)

print('B)')
i = 0
while i < 5:
      circle, square, random_square = isPointInSquare(points[i]['x'], points[i]['y'])
      if square == True:
        points[i]['inRegion'] = 'YES'
      else:
         points[i]['inRegion'] = 'NO'    
      i += 1
print(points)

print('C)')
i = 0
while i < 5:
      circle, square, random_square = isPointInSquare(points[i]['x'], points[i]['y'])
      if random_square == True:
        points[i]['inRegion'] = 'YES'
      else:
         points[i]['inRegion'] = 'NO'    
      i += 1
print(points)

