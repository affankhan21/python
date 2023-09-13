
print('Enter correct username password combo to continue')



count=0
while count<4:
  username=input('Enter username: ')
  password=input('Enter password: ')
if(username="abc") and (password="123"): 
    print('Access granted.')
    break
else:
    print('Incorrect.Try again.') 
    count+=1
 