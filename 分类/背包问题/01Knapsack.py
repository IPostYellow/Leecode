"""
给定一组N个权值的数组，我们要将这些物品放入容量为C的背包。我们要获取总权重最大的背包物品。每个物品被选择就要全部放进去，否则就不放进去。
Items: { Apple, Orange, Banana, Melon }
Weights: { 2, 3, 1, 4 }
Profits: { 4, 5, 3, 7 }
Knapsack capacity: 5
Apple + Orange (total weight 5) => 9 profit
Apple + Banana (total weight 3) => 7 profit
Orange + Banana (total weight 4) => 8 profit
Banana + Melon (total weight 5) => 10 profit
"""
def knapsack_recursive(profits,weights,capacity,currentIndex):
    if capacity<=0 or currentIndex>=len(profits):
        return 0
    profit1=0
    if weights[currentIndex]<=capacity: # 如果当前物品容量够的话
        profit1=profits[currentIndex]+knapsack_recursive(profits,weights,capacity-weights[currentIndex],currentIndex+1) #拿这个物品
    profit2=knapsack_recursive(profits,weights,capacity,currentIndex+1)#不拿这个物品

    return max(profit1,profit2)

def solve_knapsack(profits,weights,capacity):
    return knapsack_recursive(profits,weights,capacity,0)

print(solve_knapsack([1,6,10,16],[1,2,3,5],7))
print(solve_knapsack([1,6,10,16],[1,2,3,5],6))
