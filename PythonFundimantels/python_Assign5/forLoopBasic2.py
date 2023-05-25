
def Biggie_Size(list):
    for i in range(len(list)):
        if list[i]>0:
            list[i]='big'
    return list
print(Biggie_Size([-1, 3, 5, -5]))



def count_positives(list):
    count = 0
    for val in list:
        if val > 0:
            count += 1
    list[len(list)-1] = count
    return list
print([1,6,-4,-2,-7,-2])
print(count_positives([1,6,-4,-2,-7,-2]))


def sum_total(list):
    sum = 0
    for i in list:
        sum += i
    return sum
print(sum_total([1,2,3,4]))
print(sum_total([6,3,-2]))




def Average(list):
    sum = 0
    for i in list:
        sum += i
    return (sum/len(list))
print(Average([1,2,3,4]))




def length(list):
    return len(list)
print(length([37,2,1,-9]))
print(length([]))



def min(list):
    if len(list)<0:
        return False
    minInt = list[0]
    for i in list:
        if i<minInt:
            minInt = i
    return minInt
print(min([37,2,1,-9]))



def Max(list):
    if len(list)<0:
        return False
    MaxInt = list[0]
    for i in list:
        if i>MaxInt:
            MaxInt = i
    return MaxInt
print(Max([37,2,1,-9]))



def Ultimate_Analysis(list):
    dictionary = {'sumTotal': 0, 'average': 0, 'minimum': list[0], 'maximun': list[0], 'length': len(list)}
    for i in list:
        if dictionary['minimum']<i:
            dictionary['minimum'] = i
        if dictionary['maximun']>i:
            dictionary['maximun'] = i
        dictionary['sumTotal']+= i
        dictionary['average']=dictionary['sumTotal']/len(list)
    return dictionary
print(Ultimate_Analysis([37,2,1,-9]))



def Reverse_List(list):
    for i in range(0, (len(list)-1)//2):
        temp = list[i]
        list[i] = list[len(list)-1-i]
        list[len(list)-1-i] = temp
    return list
print(Reverse_List([37,2,1,-9]))