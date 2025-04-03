collection = {1,2,2,2,3,"hello","strii","strii"} #sets ignores duplicate values
print(collection)
print(type(collection))
print(len(collection))#length also ignores duplicate values
collection_1=set()
collection_1.add(1)
collection_1.add(2)
collection_1.add(3)
collection_1.remove(2)
print(collection_1)
idk = {"hi","bye","see you","good bye","vamos"}
print(idk.pop())
print(idk.pop())
print(collection_1.union(idk))
set_1={1,2,4,3,5,5,7,8,13}
set_2={2,3,6,9,10,11,12,14}
print(set_1.union(set_2))
set_3={15,13,1,14,13,13,2,3,5,6,7,8,18,9}
set_4={11,2,15,3,4,6,13,14,6,5,4,7,4,9,7,5}
print(set_3.intersection(set_4))
