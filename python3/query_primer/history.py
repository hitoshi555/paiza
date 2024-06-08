# 解答
# 入力が複数個与えられているのでこの問題も入力ごとに処理をおこなうクエリの問題に見えますが、結論から言うとこの問題はクエリの問題ではありません（ひっかけです、すみません）
# よくよく問題文を見ると、この問題は「全ての歴史の出来事をソートしたのち、各出来事に対応した人の名前を順に出力する」ことで解くことができます。
# 処理を入力のたびにおこなうことも大切ですが、まとめて処理できるものはいったん全て入力を受け取ってから処理をするということも大切になります。
# 問題ごとに、どのタイミングで入力を受け取り、どのタイミングで処理するのかを意識することが大切です。
# 歴史の出来事と担当をペアとしてまとめて保持してそれらを年の順に並べたり、歴史の出来事と担当を関連付けてから、出来事をソートしたのち対応する担当を出力することでこの問題を解くことができます。

N, K = map(int, input().split())
names = [input() for _ in range(N)]

histories = [None] * K
for i in range(K):
    year, charge = input().split()
    # タップル を利用して行っている
    histories[i] = (int(year), charge)

for year, name in sorted(histories):
    print(name)