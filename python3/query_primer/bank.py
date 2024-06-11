# 解答
# 会社による預金の引き出しは最大で 100,000 回行われるため、実行時間制限に間に合う目安の計算回数である 10^8 以下に全体の計算量を抑えるためには、預金の引き出し 1 回あたりの処理を O(log N) 程度でおこなう必要が出てきます。
# 初めに与えられる情報と、引き出し時に与えられる情報のうち共通しているものは会社名であり、暗証番号のチェックや預金残高の計算には時間はかからないことから、次のような処理が O(log N) 程度でできれば良いことがわかります。
#   「会社名から、その会社の暗証番号を取得する」
#   「会社名から、その会社の預金残高を取得する」
  
# 決まった値から関連した値を取り出したい時には連想配列を使うと便利です。
# 連想配列では、上の 2 つの処理と要素の追加をいずれも O(log N) でおこなうことができるので、連想配列を用いることでこの問題を解くことができます。
# 最後に、与えられた順で会社の残高を出力する必要があるので、与えられた順に会社の名前を保持しておく必要があることに注意しましょう。
N, K = map(int, input().split())

data = {}
for _ in range(N):
    c, p, d = input().split()
    data[c] = (p, int(d))

for _ in range(K):
    g, m, w = input().split()

    pin, save = data[g]
    if pin != m:
        continue

    data[g] = (pin, save - int(w))

for name, d in data.items():
    print(name, d[1])