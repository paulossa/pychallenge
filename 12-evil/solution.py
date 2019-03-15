# Dealing evil 
# Image has some sort of index and following it leads to the file evil2.gfx

data = open("evil2.gfx", "rb").read()

for i in range(5):
    open('%d.jpg' % i ,'wb').write(data[i::5])