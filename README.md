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
