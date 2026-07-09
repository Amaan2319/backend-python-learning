# two sum problem
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
def maxProfit(self, prices: List[int]) -> int:
        min_price =float('inf')
        max_profit=0
        for price in prices:
            if price<min_price:
                min_price=price
            elif price-min_price>max_profit:
                max_profit=price-max_profit   
        return max_profit