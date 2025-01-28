s1 = {3,1,9,7,6}
s2 = {2,4,5,6,8}
print(s1)
print(s2)
union = s1.union(s2)
intersection = s1.intersection(s2)
diff1 = s1.difference(s2)
diff2 = s2.difference(s1)
print("union is ", union)
print("intersection is ", intersection)
print("difference between set one and two is ", diff1)
print("difference between set two and one is ", diff2)
print('ADDING AND REMOVING A NUMBER')

s1.add(4)
print('added 4 to set 1', s1)
s2.remove(4)
print('removed 4 from set 2', s2)

sort = sorted(s1)
print('sorted set is', sort)