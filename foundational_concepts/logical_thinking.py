def task1(n):
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print()
        
def task2(n):
    for i in range(n):
        for j in range(i+1):
            print("*", end=" ")
        print()


def task3(n):
    for i in range(n + 1):
        for j in range(i):
            print(j + 1, end=" ")
        print()
        
def task4(n):
    for i in range(1, n+1):
        for j in range(i):
            print(i, end=" ")
        print()

def task5(n):
    for i in range(n + 1, -1, -1):
        for j in range(i):
            print("*", end=" ")
        print()
        
def task6(n):
    for i in range(n, -1, -1):
        for j in range(i):
            print(j + 1, end=" ")
        print()

def task7(n):
    for i in range(n):
        for j in range(n-i-1):
            print(" ", end=" ")
                
        for j in range((2*i)+1):
            print("*", end=" ")
            
        for j in range(n-i-1):
            print(" ", end=" ")
        print()

        
def task8(n):
    for i in range(n, -1, -1):
        for j in range(n-i):
            print(" ", end=" ")
                
        for j in range((2*i)-1):
            print("*", end=" ")
            
        for j in range(n-i):
            print(" ", end=" ")
        print()
        
def task9(n):
    task7(n)
    task8(n)
        
def task10(n):
    for i in range((n * 2)-1):
        if i < (n * 2)//2:
            for j in range(i+1):
                print("*", end=" ")
        else:
            for j in range((n*2) - i - 1):
                print("*", end=" ")
        
        print()
        
n = 5
print('Printing Task 1: ')
task1(n)
print("-"*(n + 1))
print('Printing Task 2: ')
task2(n)
print("-"*(n + 1))
print('Printing Task 3: ')
task3(n)
print("-"*(n + 1))
print('Printing Task 3: ')
task4(n)
print("-"*(n + 1))
print('Printing Task 5: ')
task5(n)
print("-"*(n + 1))
print('Printing Task 6: ')
task6(n)
print("-"*(n + 1))
print('Printing Task 7: ')
task7(n)
print("-"*((n*2) + 1))
print('Printing Task 8: ')
task8(n)
print("-"*((n*2) + 1))
print('Printing Task 9: ')
task9(n)
print("-"*((n*2) + 1))
print('Printing Task 10: ')
task10(n)
print("-"*((n*2) + 1))