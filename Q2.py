import time 

def retry(fun):
    for x in range(0,3):
        def inner():
          print("Runnig",x+1)
          time.sleep(3)
        inner()
    return inner
          
@retry   
def fun():
    print("fun is called")
