import sys
sys.setrecursionlimit(100000)
def f(n):
    if n < 5:
        return n
    if n >= 5:
        return 2*n*f(n-4)
#print(f(13766)-9*f(13762))/f(13758)на пальцах...
print(2*13766*2*13762-9*2*13762)