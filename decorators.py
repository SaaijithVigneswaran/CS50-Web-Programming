def announce(f):
    def wrapper():
        print("about to run dunction ..")
        f()
        print("done with function ")
    return wrapper
    

@announce
def hello():
    print ("helloworld")

hello()