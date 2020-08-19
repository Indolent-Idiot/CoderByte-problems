#Find Intersection
#Have the function FindIntersection(strArr) read the array of strings stored in strArr which will contain 2 elements:
#the first element will represent a list of comma-separated numbers sorted in ascending order,
#the second element will represent a second list of comma-separated numbers (also sorted) 
#Your goal is to return a comma-separated string containing the numbers that occur in elements of strArr in sorted order. If there is no intersection, return the string false.
#Sample ExampleS
#Input: ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]
#Output: 1,4,13
#Input: ["1, 3, 9, 10, 17, 18", "1, 4, 9, 10"]
#Output: 1,9,10


def FindIntersection(strArr):


 lst=str()  # Create an empty string
 a=strArr[0]
 b=strArr[1]
 #split indiudual strings 
 c=a.split(", ")
 d=b.split(", ")
 for nums in c:
    for num in d:
       if (num==nums):
          lst=lst+num+","

       else:
         continue
 l=len(lst)
 if l < 1:
   return False
 else : 

  ls=lst[0:l-1]       
  return ls.rstrip()

# keep this function call here 
print FindIntersection(raw_input())
