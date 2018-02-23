msg = "Hello World"
print(msg)

def foo():
    print('foo')

def bar():
    foo()

def main():
    print("main invoke bar")
    bar()

if __name__ == '__main__':
    main()