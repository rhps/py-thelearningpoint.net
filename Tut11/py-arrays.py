array = []
array.append(1)
array.append(2)
array.append(4)
array.append(8)

print "array" , array
print "array 3 = ", array[3]

secondArray = [1, 2, 3]
print "print array + secondArray = ", array + secondArray

thirdArray = [10,98,1,2,4,2,0]
print "print thirdArray = ", thirdArray
thirdArray.sort()
print "print thirdArray sorting  = ", thirdArray

if 2 in thirdArray: print "found 2"

array2DTest = []
array2DTest += [[1,2,3]] 
print "print first 2D array",array2DTest
array2DTest += [[1,4,6]]
print "print next 2D array",array2DTest
print array2DTest[0]
print array2DTest[1]
print array2DTest[1][2]
print array2DTest[0][0]
print zip([1,2,3,4],[5,6,7,8],[9,10,11,12])

