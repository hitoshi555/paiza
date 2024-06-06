n, x, p = [int(x) for x in input().split()]
roster = []

for i in range(n):
    s = int(input())
    roster.append(s)

roster.append(p)

for _ in range(x):
    s = input().split()
    if s[0] == "join":
        roster.append(int(s[1]))
    elif s[0] == "sorting":
        newlist = sorted(roster)
        print(newlist.index(p) + 1)

# 解答
# イベントが最大で 100,000 回起こるということは、実行時間を考えるとイベント 1 つあたりおおよそ 1,000 回程度のループで処理を行わなければいけません。要素数 N の配列のソートには O(N log N) かかりますから、sorting が与えられるたびにソートをしていては間に合いません。
# そこで、効率の良いデータの持ち方を考えてみましょう。転校生がやってくることで paiza 君が前から何番目に並ぶかが変化するのは、転校生の身長が paiza 君よりも小さいときのみです。
# 元からクラスにいる人の中で身長が paiza 君よりも小さい人の数を数えておき、転校生が来るたびに身長が paiza 君より小さいかどうかを判定し、小さい場合は答えを +1 することで、いちいちソートをせずにこの問題を解くことができます。
# N, K, P = map(int, input().split())
# A = [int(input()) for _ in range(N)]

# A.append(P)
# ans = sorted(A).index(P) + 1

# for _ in range(K):
#     event = input()

#     if event == "sorting":
#         print(ans)
#         continue

#     x = int(event.split()[1])
#     if x < P:
#         ans += 1
