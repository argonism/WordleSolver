# Wordle Solver

wordleを解けるやつです。

平均約3.9028回の回答で答えを当てることができます。

平均情報量が一番大きい単語を毎回選択します。

平均情報量の計算はxclocheさんの以下の記事を参考にしました。
https://xcloche.hateblo.jp/entry/2022/01/24/212558

ソルバーとしては、毎回答ごとに、現在まで得られたヒントを満たすような単語集合の中から、最も平均情報量が高い単語を回答として提出する、貪欲な方法を取っています。

なお、Wordleの回答を自動化するものではありません。

語彙はWordleから直接抜き取りましたが、念のため公開しません。