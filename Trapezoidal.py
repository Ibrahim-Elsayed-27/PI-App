import math
expression=input("Enter the expression:")
start=float(input("Enter the start point:"))
end=float(input("Enter the end point:"))
number_of_segments=int(input("Enter number of segments:"))
unit_segment=(end-start)/number_of_segments
print(unit_segment)
areas=[]
while start<=end:
    x=start
    y_start=eval(expression)
    x=start+unit_segment
    areas.append(round(y_start,4))
    start+=unit_segment

#print(sum(areas[1:len(areas)-1]))
print(areas)
area=(unit_segment/2)*(areas[0]+areas[len(areas)-1]+2*(sum(areas[1:len(areas)-1])))
print(unit_segment/2)
print(areas[0],areas[len(areas)-1],sum(areas[1:len(areas)-1]))
print(f"Answer Is:{round(area,5)}")