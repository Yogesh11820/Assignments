# from collections  import Counter
def count(list):
    cnt = 0
    for i in list:
        cnt+=1
     
    yield cnt


list=['a',6,8,'h','y',7,4]
for i in count(list):
    print(i)    