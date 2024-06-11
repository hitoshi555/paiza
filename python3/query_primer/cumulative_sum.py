# 書いた下記コードはタイムオーバーを起こした
# n, k = [int(x) for x in input().split()]

# numbers = [int(input()) for _ in range(n)]

# for i in range(k):
#     num = int(input())
#     ans = 0
#     for j in range(num):
#         ans += numbers[j]
#     print(ans) 

# 解答
# 各 Q_i (1 ≦ i ≦ K) について A_1 ... A_{Q_i} の和をいちいち計算すると、最悪ケースのとき、プログラム全体でループが K × N 回回るため実行時間に間に合いません。
# では実行時間に間に合わせるためにはどうしたら良いでしょうか。
# A_1 から A_i までの和を sum[i] とすると、sum[i] = sum[i-1] + A[i] という関係が成り立つことを用いて、すべての i について sum[i] を計算しておくことで、この問題を実行時間内に解くことができます。
# 今回の問題で求めた区間の和 を 累積和 といい、計算量を落とす際にしばしば用いられます。
N, K = map(int, input().split())
A = [int(input()) for _ in range(N)]

# A[:]はストライド?
ans = [0] + A[:] # value が0から始まる数字の配列を作成
for i in range(1, N + 1):
    ans[i] += ans[i - 1] # ans[2]が74 に ans[1] の45 を足す
    # 2週目はans[3]の-94 に ans[2]の119を足す
    # これをn+1回行うとansにそれぞれの累積和が入る

for _ in range(K):
    q = int(input())
    print(ans[q])