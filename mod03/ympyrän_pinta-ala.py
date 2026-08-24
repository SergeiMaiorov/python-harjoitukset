import math


## Pyydä ympyrän säde ja talle
circle_radius_input = input("Anna ympyrän pituus senttimetreinä: ")
radius_float = float(circle_radius_input)


## lasken ympyrän pinta-alan 
## pi * säde potenssiin kaksi
area = math.pi * radius_float**2


## tulosta ympyrän pinta-alan 
print(f"Ympyrän pinta-ala on: {area}")