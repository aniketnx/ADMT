A = 10
B = 20
C = 30
D = 40

com1= A*B + A*B*C + A*B*C*D
print("Cost of ((A*B)*C)*D)",com1)
com2= B*C + A*B*C + A*B*C*D
print("Cost of (A*(B*C)*D)",com2)
com3= C*D + B*C*D + A*B*C*D
print("Cost of (A*B*(C*D))",com3)
com4= A*C + A*C*D + A*B*C*D
print("Cost of ((A*C)*D*B)",com4)
com5= A*D + A*D*B + A*B*C*D
print("Cost of ((A*D)*B*C)",com5)

if (com1 < com2) and (com1 < com3) and (com1 < com4) and (com1 < com5):
   minimum = com1
elif (com2 < com1) and (com2 < com3) and (com2 < com4) and (com2 < com5):
   minimum = com2
elif (com3 < com1) and (com3 < com2) and (com3 < com4) and (com3 < com5):
   minimum = com3
elif (com4 < com1) and (com4 < com2) and (com4 < com3) and (com4 < com5):
   minimum = com4
else:
   minimum = com5



print("The minimum cost is ",minimum)