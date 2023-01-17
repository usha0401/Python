'''Indian army is going to do a surprise attack on one of its enemies country. The President of India, the Supreme Commander of the Indian Army will be sending an alert message to all its commanding centers. As enemy would be monitoring the message, Indian army is going to encrypt(cipher) the message using basic encryption technique. A decoding key 'K' (number) would be sent secretly.

You are assigned to develop a cipher program to encrypt the message. Your cipher must rotate every character in the message by a fixed number making it unreadable by enemies.

Given a single line of string 'S' containing alpha, numeric and symbols, followed by a number '0<=N<=1000'. Encrypt and print the resulting string.

Note: The cipher only encrypts Alpha and Numeric. (A-Z, a-z, and 0-9) . All Symbols, such as - , ; %, remain unencrypted.'''


s=input()
k=int(input())
op=''
for i in s:
    if i.isalpha():
        if ord(i)>=65 and ord(i)<=90:

            if ((ord(i)+(k%26))>90):
                op+=chr(64+((ord(i)+(k%26))-90))
            else:
                op+=chr(ord(i)+(k % 26))

        elif ord(i)>=97 and ord(i)<= 122:
            if (ord(i) + (k % 26)) > 122:
                op+=chr(96+((ord(i)+(k % 26))-122))
            else:
                op+= chr(ord(i) + (k % 26))

    elif i.isdigit():
        if((ord(i)+ (k % 10)) > 57):
            op+=chr(47 + ((ord(i) + (k % 10)) - 57))
        else:
            op+=chr(ord(i) + (k % 10))
    else:
        op+=i
print(op)