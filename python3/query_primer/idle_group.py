n, k = [int(x) for x in input().split()]
members = [input() for _ in range(n)]

for i in range(k):
    datas = input().split()
    if datas[0] == "handshake":
        sorted_members = sorted(members)
        for name in sorted_members:
            print(name)
    elif datas[0] == "leave":
        members.remove(datas[1])
    elif datas[0] == "join":
        members.append(datas[1])

# 解答
# イベントが最大で 100,000 回与えられることを踏まえると、実行時間制限に間に合う目安の計算回数である 10^8 以下に全体の計算量を抑えるためには、各イベントの処理「アイドルの加入」「アイドルの脱退」をO(log N) 程度の計算量で抑える必要があります。
# これらを満たすデータ構造として順序付集合が挙げられます。これは N 要素の集合への要素の追加・削除を O(log N) でおこなうことができ、要素を常にソートされた状態で保持します。
# 各言語によって順序付集合の仕様は異なるので詳しい実装は言語ごとの実装例をみてください。入力に応じた順序付集合の処理を行うことでこの問題を解くことができます。
# N, K = map(int, input().split())
# names = {input() for _ in range(N)}

# for _ in range(K):
#     event = input()

#     if event == "handshake":
#         for name in sorted(names):
#             print(name)
#     else:
#         event, name = event.split()
#         if event == "join":
#             names.add(name)
#         else:
#             names.remove(name)