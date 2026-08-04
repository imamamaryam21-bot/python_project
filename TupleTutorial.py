#How to create a tuple
student=("Imama","Hashir","Shameer","Imama")
#when we make a tuple which contain only one element then we should add a comma at last
student2=("Mariyam",)
#print(student)
#how to access its elements or entities,by using index
#print(student[-3])
'''if "Hashir" in student:
    print("Yes, he is in the student tuple.")
else:
    print("No,there is no similar name in the tuple.") '''   
#how to update a tuple
'''student_list=list(student)
student_list[1]="Muhammad"
student=tuple(student_list)
print(student)
#one thing more we cannot update or change the tuple
#we can only change the list,so first we make the tuple a list and then change its elements'''

#now add the tuples
#student += student2
#print(student)

#for n in student:
#    print(n)
i=0
while i<len(student):
    print(student[i])
    i+=1