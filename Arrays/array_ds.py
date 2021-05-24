#importing array for array operations
import array as arr


#initializing array with array values
a = arr.array('i', [1,2,3])

#printing original array
print("This is the new array",end=" ")
for i in range(0,3):
	print(a[i],end=" ")

print("\n")

#adding an element in the end
a.append(4)
print(a)

#adding an element at a specific position insert(position,element)
a.insert(2,5)
print(a)
print("\n")

#removing an element from a position and return the value pop(position)
print(a.pop(2))
print(a)
print("\n")

#removing the first occurence of the value remove(value)
a.remove(1)
print(a)

#print the index of first occurrence of value
print(a.index(2))

#reverse of array, the function does not return the array it only changes the values in the indexes
a.reverse()
print(a)
