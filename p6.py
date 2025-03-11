def genre(filt):
    gen=input('Enter the genre :')
    filt1=[row for row in filt if gen in row['genre']]
    return filt1