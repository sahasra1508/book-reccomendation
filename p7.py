def lists(file):
    list=[]
    for line in file:
        line=line.strip()
        list.append(line)
    return list
def new():
    file=open('p.txt','r')
    list=lists(file)
    n=len(list)
    us=list[n-1]
    num=int(us[0:4])
    num += 1
    r=str(num)
    userid=r
    file.close()
    text=r+'.txt'
    file=open(text, 'w')
    name=input('Enter your name:')
    email=input('Enter your E-mail Id:')
    print('Please note down your UserID:',userid)
    str1=name+'\n'+email
    file.write(str1)
    file.close()
    file=open(text, 'r')
    read=lists(file)
    file.close()
    file=open('p.txt','a')
    file.write('\n')
    file.write(r)
    file.close()
    return userid,read,text  
def present(userid):
    text=userid+'.txt'
    file=open(text, 'r')
    read=lists(file)
    return read,text