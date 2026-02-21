"""
Docstring for blind-75.best_time_to_buy_and_sell_stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.



Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
"""


# This solution will not work for prices [3,3]
def main(prices):
    left = 0
    right = 1
    profit = 0

    while right < len(prices):
        if prices[right] < prices[left]:
            left = right
        elif prices[right] > prices[left]:
            profit = max(profit, prices[right] - prices[left])
        right += 1

    print(profit)


def main2(prices):
    max_profit = 0
    min_price = float("inf")

    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price

    print(max_profit)


if __name__ == "__main__":
    main([7, 1, 5, 3, 6, 4])
    main([7, 6, 4, 3, 1])
    main([3, 3])

    main2([7, 1, 5, 3, 6, 4])
    main2([7, 6, 4, 3, 1])
    main2([3, 3])
