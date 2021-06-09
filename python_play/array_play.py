'''heros=['spider man','thor','hulk','iron man','captain america']

print("The length of list is",len(heros))
heros.append("black panther")
print("After adding 'black panther', the list is",heros)
heros.remove('black panther')
print("After removing 'black panther', the list is",heros)
heros.insert(3,'black panther')
print("adding 'black panther' after 'hulk'",heros)
heros[1:3] = ['doctor strange']
print("adding some changes",heros)
print("sorting heros in alpha order",sorted(heros))'''

def generate_odd(max_num):
    '''odd_nums = []
    for i in range(max_num+1):
        if (i%2 !=0):
            odd_nums.append(i)
    print(odd_nums)'''

print([i for i in range(max_num+1) if(i%2!=0)])
user_input = input("Enter the max odd number : ")
if(isinstance(int(user_input),int)):
    generate_odd(int(user_input))




