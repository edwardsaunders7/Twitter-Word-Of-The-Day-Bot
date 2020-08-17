import os

os.chdir("img/")
print(os.getcwd())
COUNT = 1

def increment():
    global COUNT
    COUNT = COUNT + 1

for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)
    f_name = "gif" + str(COUNT)
    increment()

    new_name = f'{f_name}{f_ext}'
    os.rename(f, new_name)
