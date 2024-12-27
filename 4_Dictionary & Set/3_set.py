# collection = {1, 2, 3, 4, "hello", "world"}
# # dset is unorder and dublicate items store 1 times
# print(collection)
# print(type(collection))

collection = set() #empty set ; syntax
# set is mutable  but element are imutable
collection.add(1)
collection.add(2)
collection.add(2)
collection.add("apnacollage")
collection.add((1, 2, 3))
#collection.add([1, 2, 3]) # error list not use un hashable jiska value aage change ho jaye


collection.remove(1)
collection.clear() # all value set()

print(collection)

#***********************************

set1 = {1,2,3}
set2 = {3,4,5}
print(set1.union(set2))
print(set1.intersection(set2))