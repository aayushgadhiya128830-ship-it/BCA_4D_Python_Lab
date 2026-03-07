def outer():
    a = "Hello"
    def inner():
        nonlocal a

        print("Inside Funcation",a)
        a = "abc"

    inner()
    print("outside function",a)

outer()
