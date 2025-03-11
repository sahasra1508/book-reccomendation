from book import p2 as p2
gen=input('Enter the genre of the book:')
try:
    rat=float(input('Enter the minimum rating of the book:'))
except:
    rat=0.00
aut=input('Enter the author name:')
filt_book = [row for row in p2.books if row['author']==aut or gen in row['genre'] and row['rating']>rat]
for i in filt_book:
    for key in i:
        if key=='title':
            print('Book :',i[key],end='  ')
        if key=='author':
            print('Author :',i[key])