s=input()
op= ""
k=int(input())
for i in range(len(s)):
    if ord(s[i])>=65 and ord(s[i])<=90:
        if ((ord(s[i])+(k%26))>90):
            op+=chr(64+((ord(s[i])+(k%26))-90))
        else:
            op+=chr(ord(s[i])+(k % 26))

    elif ord(s[i])>=97 and ord(s[i])<= 122:
        if (ord(s[i]) + (k % 26)) > 122:
            op+=chr(96+((ord(s[i])+(k % 26))-122))
        else:
            op+= chr(ord(s[i]) + (k % 26))

    elif (ord(s[i])>= 48 and ord(s[i])<= 57):
        if ((ord(s[i])+ (k % 10)) > 57):

            op+= chr(47 + ((ord(s[i]) + (k % 10)) - 57))
        else:

            op+= chr(ord(s[i]) + (k % 10))
    else:
        op+=chr(ord(s[i]))

print(op)


