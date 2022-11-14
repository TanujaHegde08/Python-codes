import sys as s
def disarium():
    print("Disarium number:")
    for i in range(1,100):
        arr =[int(num) for num in str(i)]
        sum=0
        for j,n in enumerate(arr):
            sum+=n**(j+1)
        if sum==int(i):
            print(sum)

def ceaser(var):
    print("Ceaser Cipher")
    text=var
    cipher=" "
    for char in text:
        var=ord(char)+3
        if(text.isupper() and var > ord('Z'))or(text.islower() and var>ord('z')):
            var=var-26
        cipher+=chr(var)
    print(cipher)

def program():
    print("1.Finding disarium Number\n2.Finding Cipher text\n3.exit")
    ch=int(input("Enter Your Choice..."))
    if ch==1:
        disarium()
    elif ch==2:
        plaintext=input("Enter any string to encrypt\n")
        ceaser(plaintext)
    elif ch==3:
        s.exit()
    else:
        print ("Invalid")

program()