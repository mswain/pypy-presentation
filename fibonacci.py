import argparse
from datetime import datetime

def get_args():
    parser = argparse.ArgumentParser(description='Calculate Nth Fibonacci Number.')
    parser.add_argument("n", type=int, help="Nth Fibonacci number")
    return parser.parse_args()

def F(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return F(n-1)+F(n-2)

args = get_args()
start_time = datetime.now()
solution = F(args.n)
end_time = datetime.now()

print "{0} fibonacci number is: {1} found in {2}s ".format(args.n, solution, (end_time-start_time).total_seconds())

