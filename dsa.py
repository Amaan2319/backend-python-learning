# two sum problem
from dataclasses import dataclass
from collections import defaultdict


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

# composition
# a class composed of different class ke objects
@dataclass
class Screen:
    type: str
@dataclass
class Battery:
    capacity: int
@dataclass
class Processor:
    cores: int

@dataclass
class Smartphone:
    _battery: Battery
    _screen: Screen
    _processor: Processor
    model: str

phone1 = Smartphone(model="Poco X6 Neo", _battery=Battery(5000), _screen=Screen("AMOLED"), _processor=Processor(8))
print(phone1.model)

@dataclass 
class Subscription:
    plan: str
    price: float
    is_active: bool = field(default=True)


@dataclass
class Address:
    street: str
    city: str
    zip_code: str


@dataclass
class User:
    name: str
    subscription: Subscription
    address: Address

    @property
    def subscription_info(self):
        return f"Plan: {self.subscription.plan}, Price: {self.subscription.price}, Active: {self.subscription.is_active}"
    

h_address = Address(street="Vatva", city="Ahmedabad", zip_code="382445")
premium_plan = Subscription(plan="Premium", price=9.99, is_active=True)

amaan = User(name="Amaan", subscription=premium_plan, address=h_address)
print(amaan.subscription_info)  # Output: Plan: Premium, Price: 9.

# first class functions

def greet(name):
    return f"Hello{name} "

greet_amaan = greet("amaan")
print(greet_amaan)

def welcome(name):
    return f"Welcome {name}"

funcs = [greet, welcome]

for func in funcs:
    print(func("charlie"))


def greet_(word):
    def hello(name):
        return f"{word} {name}!"
    return hello
xy = greet_("salam")
print(xy("bob"))

# decorators again
import time 
def time_logger(func):
    def wrapper(*args,**kwargs):
        start_time = time.time()

        result = func(*args,**kwargs)
        end_time = time.time()
        exec_Time = end_time - start_time
        print(f"Function {func.__name__} took {exec_Time:.6f} seconds to run")
        return result
    return wrapper

@time_logger
def test():
    print("test function")

test() 

# anagram program
def isAnagram(s,t):
    if len(s)!=len(t):
        return False
    count_s, count_t = {},{}
    for i in range(len(s)):
        count_s[s[i]] = 1 + count_s.get(s[i],0)
        count_t[t[i]] = 1 + count_t.get(t[i],0)
    return count_t == count_s

# palindrom check
def isPalindrome(s):
    if len(s) ==1:
        return True
    r = []
    for item in s[::-1]:
        r.append(item)

    return s == "".join(r)

# first unique number
def firstUnique(s: str):
    count = defaultdict(int)

    for char in s:
        count[char] += 1

    for i, char in enumerate(s):
        if s[char]==1:
            return i

    return -1