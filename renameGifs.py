import os

#print (os.listdir("Gifs/"))
os.chdir("Gifs/")


def Start():
    TempRename()
    FinalRename()
    os.chdir('..')

def TempRename():
    i = 1
    for f in os.listdir():
        #print(f'Renaming file {i}')
        f_name, f_ext = os.path.splitext(f)
        f_name = "" + str(i)
        #increment()
        i += 1

        new_name = f'{f_name}.temp{f_ext}'
        os.rename(f, new_name)

def FinalRename():
    i = 1
    for f in os.listdir():
        #print(f'Renaming file {i}')
        f_name, f_ext = os.path.splitext(f)
        f_name = "" + str(i)
        #increment()
        i += 1

        new_name = f'{f_name}{f_ext}'
        os.rename(f, new_name)

Start()
