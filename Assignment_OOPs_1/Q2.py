import statistics
from statistics import mean

class arithmetic(): 
    def __init__(self,data):
        self.data = data


    def avg(self):
        n = len(self.data)
        return sum(self.data) 
    
    def Mean(self):
        return  (mean(self.data))
    def Mode(self):
        return statistics.mode(self.data)
    def Standard_deviation(self):
        return statistics.stdev(self.data)
data = [5,7,6,7,4,5,7,46,3]
data_p = arithmetic(data)
#data_p.set_element(data)

print("The average of list is ",data_p.avg())
print("The average of list is ",data_p.Mean())
print("The average of list is ",data_p.Mode())
print("The average of list is ",data_p.Standard_deviation())       