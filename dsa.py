# two sum problem
from dataclasses import dataclass


def twoSum(arr,target):
    seen = {}
    for i in range(0,len(arr)):
        num = arr[i]
        compliment = target-num
        if compliment in seen:
            return [seen[compliment],i]
        else:
            seen[num]=i

print(twoSum([2,7,1,3,9],9))


# best time to buy and sell stock
def maxProfit(self, prices):
        min_price =float('inf')
        max_profit=0
        for price in prices:
            if price<min_price:
                min_price=price
            elif price-min_price>max_profit:
                max_profit=price-max_profit   
        return max_profit

from abc import ABC, abstractmethod
from dataclasses import dataclass, field

@dataclass
class Parent(ABC):
    name: str
    age: int
    
    def getName(self):
        return self.name
    @abstractmethod
    def getAge(self):
        pass

class Child(Parent):
    def getAge(self):
        return self.age

c = Child(name="Amaan", age=21)

print(c.getAge())