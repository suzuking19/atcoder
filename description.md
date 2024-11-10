* 参考：https://qiita.com/marogoma/items/c39ee7638c2a3ae7552d

## 各ファイルの使い方
### command.txt
入力サンプルを提出用コードに渡してローカルでコードテストを実行するためのコマンドを記載しておきます。
python3 answer.py < input.txt と入力しておいてください。

### answer.py 
提出用コードをこのファイルに書いていきます。

### input.txt
問題で与えられた入力サンプルをこのファイルにコピペします。

### knowledge.txt → memo.txt(こっちの方が名前が短くて楽)
コンテスト最中や前後に見返すためのメモ置き場です。

## 実際に使ってみる
環境構築は以上となりますので、実際にこれらのファイルを使ってBeginnersSelectionのPracticeAを解いてみます。

### answer.py
下記コードを書きます。
a = int(input())
b,c = map(int,input().split())
s = input()
print(a+b+c, s)

### input.txt
入力例1のサンプルを打ち込みます。
1
2 3
test

### answer.py実行
Control+` でターミナルを起動したら、
command.txtに書いておいたpython3 answer.py < input.txtを実行します。
するとターミナルには6 testと出力されて、これは問題の出力例1の値と一致します。
このサンプルではanswer.pyは題意を満たしていそうです。
※実際のコンテストの前にはターミナル起動とpython3 answer.py < input.txtを１度実行しておくと良いと思います。
(ターミナルで↑かControl+pで過去のコマンドが遡れます)