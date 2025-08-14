import time

def a():
    aga = 0
    while aga < 100:
        aga += 1
        time.sleep(1)
        print(aga)

def aa():
    h = 50
    while h < 100:
        h += 1
        time.sleep(1)
        print(h)

def aaa():
    agua = 10
    while agua > 0:
        print(agua)
        agua -= 1
        time.sleep(1)
    print('Fogo!')
    

aaa()