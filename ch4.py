a = str(input("Input:　"))
lengh = len(a)
output = "Yes,this is a palindrome"
for i in range(lengh//2):
    if a[i] != a[lengh-1-i]:
        output = "Not a palindrome"
print(output)

