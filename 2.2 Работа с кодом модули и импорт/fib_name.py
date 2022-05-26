def fib_name(k):
    if k == 0 or k == 1:
        return 1
    else:
        return fib_name(k - 1) + fib_name(k -2)

if __name__=="__main__":
    print(__name__)
    print(fib_name(31))