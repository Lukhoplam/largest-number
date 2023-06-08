# created a function 
#assigned i to the value 0
def large(list_, i=0):
    #checks whether the element at the current index is equal to number in the list
    if list_[i] == max(list_):
        return list_[i]
    return large(list_, i+1)
results= large([1,4,6,3,2,45,5])
print(results)

