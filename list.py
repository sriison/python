mylist = ["1","apple","3.4"]
print(len(mylist))
mylist=["one","two","three"]
print(mylist[0])
anotherlist = ["four","five","six","sevens"]
newlist = mylist + anotherlist
print(newlist)
newlist[0] = "ONE ALL CAPS"
print(newlist)

newlist.append("seven")
print(newlist)

print(newlist.pop())
print(newlist)

testlist = ["a","z","j","d","c","m","t","r"]
numlist = [10,4,3,5,345,343,2365,234,342,321,243,133,32.232]
numlist.sort()
testlist.sort()
print(testlist)
print(numlist)
numlist.reverse()
testlist.reverse()
print(testlist)
print(numlist)
    