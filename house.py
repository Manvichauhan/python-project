def Stolen(val, n):
    if n == 0:
        return 0
    if n == 1:
        return val[0]
    if n == 2:
        return max(val[0], val[1])
    dp = [0]*n
    dp[0] = val[0]
    dp[1] = max(val[0], val[1])
    for i in range(2, n):
        dp[i] = max(val[i]+dp[i-2], dp[i-1])
 
    return dp[-1]
def main():
    val = [6, 7, 1, 3, 8, 2, 5]
    n = len(val)
    print("Maximum Stolen value : {}".
        format(Stolen(val, n)))
 
# if __name__ == '__main__':
#     main()