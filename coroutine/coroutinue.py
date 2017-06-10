def consumer():
    print('start generator')
    r='first r'
    while True:
        print('*')
        n=yield r
        print('consumer %s'% n)
        r='200 ok' 


def producer(c):
    c.send(None)
    for n in range(5):
        print('produce %s'% n)
        r=c.send(n)
        print('consumer code %s'%r)

c=consumer()
producer(c)