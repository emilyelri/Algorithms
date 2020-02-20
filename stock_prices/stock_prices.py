#!/usr/bin/python

import argparse

def find_max_profit(prices):
  profit = 0
  minimum = prices[0]
  maximum = max(prices)

  if prices.index(maximum) == 0:
    lossMin = max(prices[1:])
    return lossMin-maximum
  else:
    for i in range(0, len(prices)):
      if prices[i] < minimum:
        minimum = prices[i]
      if prices[i] - minimum > profit:
        profit = prices[i] - minimum

  return profit


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))