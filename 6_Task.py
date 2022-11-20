random_list = []
n = int(input())
for i in range(0, n):
            the_num = int(input())
            random_list.append(the_num)
print(random_list)
random_list = list(filter(lambda x: all(x%i != 0 for i in range(2,int(x**0.5)+1)), random_list))
print(random_list)