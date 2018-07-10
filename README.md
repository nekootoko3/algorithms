# algorithms

[algorithms and data structure for programming contest](https://www.amazon.co.jp/dp/B00U5MVXZO/ref=dp-kindle-redirect?_encoding=UTF8&btkr=1)  
All scripts are written in python3

## sort

### insertion_sort

- O(N²)
  - minimum computational comlexity is O(N)
- stable sort
- insertion_sort.py が正しい挿入ソートのアルゴリズム(最小の計算量がO(N))
    - insertion_sort_2.py は最初の配列の並び順によらず計算量が(O(N²))
- http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_1_A

### bubble_sort

- O(N²)
- stable sort
- http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_2_A

### selection_sort

- O(N²)
- unstable sort
- http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_2_B

### stable_sort

- http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_2_C

### shell_sort

- http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_2_D
- 最大の計算量O(Nの1.5乗)

## data_structure

### stack

- http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_3_A

### queue

- http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_3_B
- queue.py は処理対象を配列から取り出さずインデックスを動かすことで処理対象を変えている。  
  処理対象の必要処理時間を超えたら削除、その時インデックスを詰める必要があるのでインデックスが小さい場合には処理に時間がかかる  
  連結リストならもっと早くなるのかもしれない
- queue_2.py はpython3の[collections](https://docs.python.jp/3/library/collections.html#collections.deque)を使った実装
- queue_3.py はcollectionsを使わずにqueueを実装。queueの大きさは要素数+1

## search

### linear_search

- O(N)
- http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_4_A
- python の 配列内にある値が存在するかを確認する`x in list`という構文は、内部的には線形探索を使っている

### binary_search

- O(logN)
  - 一度探索するごとに範囲が半分になるので
- http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_4_B
- 1はfor文を使って再帰的に関数実行、2が分かり易いwhile文、3はpythonのsetを利用

### dictionary

- O(1) (衝突がなければ)
- http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_4_C
- 1はpythonの辞書を使わずに配列で実装。時間足りなかった。2はpythonの辞書を使っている、早い。

## Recursion / Divede and Conquer

### exhaustive_search

- O(2のN乗)
- http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_5_A
- 1、2は各対象となる値と組み合わせた値が等しいかを比較している(時間切れ)
  - 対象となる値が少ない場合には問題ないが、増えた場合には同じ計算が何度も行われるので先に全通りの組み合わせの各和をハッシュで持つ3の方法がよい
- 3は先に全ての組み合わせの各和をハッシュに入れて、各対象となる値がハッシュに存在しているかを確認する方式(時間内に終わる)
- 4,5は組み合わせの作り方が異なる。各配列の値を使う場合、使わない場合それぞれを選択する再帰関数となっている
  - 4,5のやり方が綺麗。


## Tree

### rooted_trees

- http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_7_A
- 1,2ともに左子右兄弟表現だが、1の場合メモリエラーになる。