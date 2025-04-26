# https://leetcode.com/problems/coin-change/submissions/1618576449/
class Solution:
    def coinChange(self, coins, amount):
        '''
        START
        1   3   6   8
        1+1, 1+3, 1+6, 1+8, 3+6, 3+8, 6+8
        1+1+1, 1+3+1, 1+6+1, etc.

        DFS to start with to find highest tree level (gets you least coins used)
        Then we make it fast using memoization 
        '''

        '''
        stack = []
        minIterations = amount + 1 #coins must be at least 1, so we can use amount + 1 as local min instead of inf
        for coin in coins:
            stack.append([coin, 1])

        while stack:
            val, iteration = stack.pop()
            for coin in coins:
                if val + coin == amount:
                    minIterations = min(iteration + 1, minIterations)
                if val + coin < amount:
                    stack.append([val + coin, iteration + 1])
        if minIterations == amount + 1:
            return -1
        return minIterations
        '''

        # Problem above is we are repeatedly calculating the same values - what I mean by this is for a target of 6 we are going through the options of 6, 3+3, 1+1+1+1+1+1, 3+1+1+1
        # Idea of memoization if we find the optimal amount for each value that is possible with the given coins leading up to the amount;
        if amount == 0:
            return 0
        if amount < 0:
            return -1

        memo = [-1] * amount
        for coin in coins:
            if coin == amount:
                return 1
            if coin > amount:
                continue
            memo[coin - 1] = 1
        print(memo)
        for i in range(amount + 1):
            if i in coins:
                continue
            minCoins = amount + 1
            for coin in coins:
                if i - coin >= 0:
                    if memo[i - coin - 1] != -1:
                        minCoins = min(minCoins, memo[i - coin - 1] + 1)
            if minCoins == amount + 1:
                memo[i - 1] = -1
            else:
                memo[i - 1] = minCoins
        return memo[amount - 1]
        
sol = Solution()
coins = [1, 3, 6, 8]
amount = 18
print(sol.coinChange(coins, amount))
