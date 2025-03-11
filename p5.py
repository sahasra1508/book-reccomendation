from book import book4 as b
from coder import p6 as filter
import p7 as user
filt_book=b.books
list=[]
print("\n%38s"%('*****Welcome*****'))
print("%48s"%('To Find Book: Books You Like To Read'))
print('------------------------------------------------------------')
string=input('\nDo you have a UserID?\n').lower()
if string=="yes":
    userid=input('Enter your UserID:')
    read,text=user.present(userid)
else:
    print('Create a new User profile')
    userid,read,text=user.new()
print('\n')
print('------------------------------------------------------------')
print('Hello! user %s :- %s \n '%(userid ,read[0]))
print('Enter the order of priority')
print('1 for Genre\n2 for Rating\n3 for Author\n0 to end\n')
i=0
while i<10:
    list.append(int(input('')))
    if list[i]==0:
        break
    i += 1
print('\n')
print('------------------------------------------------------------')
for i in list:
    if i==1:
        filt_book=filter.genre(filt_book)
    if i==2:
        filt_book=filter.rating(filt_book)
    if i==3:
        filt_book=filter.author(filt_book)
print('\nBooks recomended for you:')
print('\nBookID',end='   ')
print('Read',end='   ')
print('Title',end='                                   ')
print('Author\n')
for i in filt_book:
    for key in i:
        if key=='bookid':
            print('%-9s'% i[key],end='')
            if i[key] in read:
                print('yes',end='    ')
            else:
                print('NO',end='     ')
        if key=='title ':
            print("%-40s"% i[key],end='')
        if key=='author':
            print('%-23s\n'%i[key])
print('\nWe hope that these books will match your expectation.')
see=input('Did you read any book from above?\n').lower()
add=open(text,'a')
if see=='yes':
   a=input('Please, Enter the bookID of the book.')
   add.write('\n')
   add.write(a)
add.close()
print('\n*Thank you for your reseponse')