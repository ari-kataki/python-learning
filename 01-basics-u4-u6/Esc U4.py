#esc 4
print ("\nesc 4")
L = [1, 2, 3, 4, 5]
print(L)
R = []
R.append(L.pop(4))
R.append(L.pop(3))
R.append(L.pop(2))
R.append(L.pop(1))
R.append(L.pop(0))
print(L)
print(R)

#esc 5
print ("\nesc 5")
D = {"apple": 0.67, "banana": 0.34, "orange": 0.50}
print(D)
print ("apple")

#esc 6
print ("\nesc 6")
D = {"mario": 67, "luca": 34, "francesco": 50}
print(D)
avg = sum(list(D.values())) / len(D)
print("Average:", avg)

#esc 7
print ("\nesc 7")
lRiga1 = [10,100,-3]
lRiga2 = [4,-1,0]
lRiga3 = [65,7,258]
lTabella = [lRiga1, lRiga2, lRiga3]
print(f"the sum of the 1st column is:, {sum(lRiga1)}")
print(f"the sum of the 2nd column is:, {sum(lRiga2)}")
print(f"the sum of the 3rd column is:, {sum(lRiga3)}")

print(f"the sum of the 1st column is:, {sum(lRiga1)}")
print(f"the sum of the 2nd column is:, {sum(lRiga2)}")
print(f"the sum of the 3rd column is:, {sum(lRiga3)}")

#esc 8
print ("\nesc 8")
l = [0,1,2,3,4,5,6,7,8,9]
print (l)
x = 7
y = 9
print (f"x is not present in L? {x in l}")
print (f"y is NOT present in L? {y not in l}")
