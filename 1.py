delta=int(input("Введите значение разницы:"))
N=int(input("Введите число:"))
array=[0]*N 
print("Введите", N, "элементов массива:") 
count=0
for i in range(N):
    array[i] = int(input())
for i in range(N):
    if (array[i]-delta)==min(array):
        count+=1
    else:
        count+=0
print(array)
print("Количество элементов=", count)