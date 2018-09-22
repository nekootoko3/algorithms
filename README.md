# algorithms

[algorithms and data structure for programming contest](https://www.amazon.co.jp/dp/B00U5MVXZO/ref=dp-kindle-redirect?_encoding=UTF8&btkr=1)  
All scripts are written in python3

## section_3 - sort

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

## section_4 - data_structure

### stack

- http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_3_A

### queue

- http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_3_B
- queue.py は処理対象を配列から取り出さずインデックスを動かすことで処理対象を変えている。  
  処理対象の必要処理時間を超えたら削除、その時インデックスを詰める必要があるのでインデックスが小さい場合には処理に時間がかかる  
  連結リストならもっと早くなるのかもしれない
- queue_2.py はpython3の[collections](https://docs.python.jp/3/library/collections.html#collections.deque)を使った実装
- queue_3.py はcollectionsを使わずにqueueを実装。queueの大きさは要素数+1

## section_5 - search

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

## section_6 - Recursion / Divede and Conquer

### exhaustive_search

- O(2のN乗)
- http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_5_A
- 1、2は各対象となる値と組み合わせた値が等しいかを比較している(時間切れ)
  - 対象となる値が少ない場合には問題ないが、増えた場合には同じ計算が何度も行われるので先に全通りの組み合わせの各和をハッシュで持つ3の方法がよい
- 3は先に全ての組み合わせの各和をハッシュに入れて、各対象となる値がハッシュに存在しているかを確認する方式(時間内に終わる)
- 4,5は組み合わせの作り方が異なる。各配列の値を使う場合、使わない場合それぞれを選択する再帰関数となっている
  - 4,5のやり方が綺麗。

## section_7 - sort2

### merge_sort

- O(NlogN)
- 安定なソート
- http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_5_B
- 1は疑似コードをそのままコードにしたものでタイムエラーになる
- 2はマージするときに左右の配列を初期化していた処理を、元の配列のコピーを取るようにした速度改善したもの。

### partition

- O(N)
- http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_6_B

### quick_sort

- O(NlogN)
- 1, 2, 3 は全てquick_sortのやり方は同じ。安定かそうでないかの判定方法だけが違う。

### counting_sort (bucket sort)

- O(n+k)
- http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_6_A

## section_8 - Tree

### rooted_trees

- http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_7_A
- 根付き木では、例えば、各ノードが`親ノード`、`左の子`、`右の子`へのポインタを持っていれば、高さ、深さ、兄弟、ノードの種類などを求めることができる。
- 1,2ともに左子右兄弟表現だが、1の場合メモリエラーになる。

### binary_tree

- http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_7_B
- 二分木では、各ノードが`親ノード`、`左の子`、`右の子`へのポインタを持っていれば、高さ、深さ、兄弟、ノードの種類などを求めることができる。
- 1のポイント
  - 出力に必要な兄弟ノード、次数も各ノードに持たせている。
  - 高さと深さは配列で別に持っておく。各ノードの深さを測る際に高さも一緒に出す
    - 各ノードの深さを求める時は親ノードを根まで辿る。
    - あるノードから根までたどる際に、途中ノード時点での深さを一時的な高さとして入れておく。別ノードから根までたどる時に、一時的な高さを比較し、数値の大きい方を入れる
- 2は各ノードに必要最低限持っておき、出力時に必要な値をとって来る
  - 高さと深さは別々に計算。

### tree_walk

- http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_7_C
- 各ノードのidを配列に入れるのが、左の子を辿りリーフノードの行き着いてからなのか、右の子もリーフノードに行き着いてからなのか、あるいは順次なのかによって、巡回の種類が変わる。
- 1, 2は、リーフノードなのかを再帰する前にチェックするか、再帰関数内でチェックするかの違いでほとんど同じ。

## section_9 - binary_search_tree

### binary_search_tree_1

- http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_8_A
- 二分探索木への挿入
- 挿入操作は木の高さはhとするとO(h)、なので、入力に偏りがなければO(logn)となる。
  - 入力が偏っている場合には、最悪O(n)となる。
    - 例えば、与えられた数字が徐々に大きくなっていく場合など右方向だけに伸び、そのときO(n)。

### binary_search_tree_2

- http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_8_B
- 二分探索木の探索
- 計算量は挿入と同じ。
- 1は再帰、2はwhileを使っているがどちらもやっていることは大きくは変わらない。

### binary_search_tree_3

- http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_8_C
- 二分探索木の削除
- hを木の高さとして、削除対象節点を探索する計算量がO(h)、対象節点の次節点を探索する計算量がO(h)なのでO(h)
- 節点と節点が持つキーを分けて考えると理解しやすいかもしれない。

## section_10 - heap

### complete_binary_tree

- http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_9_A
- ソートされていないヒープ

### maximum_heap

- http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_9_B
- 最大ヒープの生成
- 二分ヒープのサイズをHとすると計算量はO(H)

### priority_queue

- http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_9_C
- 優先度付きキュー
- 1~4はヒープモジュールなし。タイムアウト
- 5はヒープモジュール利用。ただし、モジュールでは最小ヒープが構成されるため、各キーをマイナスにしている。
- 木の高さに比例する数だけ要素の交換を行うので、要素数がNの優先度付きキューへの挿入と削除はともにO(logN)

## section_11 - dynamic_programming

### fibonacci_number

- http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_10_A
- フィボナッチ数列
- 1はメモ化再帰を利用。すなわち、小さい部分問題の解を記憶しておき大きい問題の解に利用する
- 2は2つの変数を1にした状態で対象の数値分ループを回し、1つの数値は前回ループ分の両者の和、1つの変数には今回ループ分の両者の和を代入していく。

## section_12 - graph

### graph

- http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_11_A
- 隣接行列表現
  - 長所
    - M[u][v]で辺(u,v)を参照できるので、頂点uと頂点vの関係を定数時間O(1)で確認できる
    - 辺の追加や変更も同様にO(1)
  - 短所
    - 頂点の2乗に比例するメモリを消費する。辺の少ないグラフの場合はメモリが無駄になりやすい
    - 1つの隣接行列では頂点uと頂点vの関係を1つしか記録できない

### depth_first_search

- http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_11_B
- 各頂点について全ての頂点に隣接しているか調べるので、|V|を頂点の数として、O(|V|²)となる
- スタックで経路を持ち、各頂点について未探索、探索中、探索済みのステータスを配列で持つ
- または再帰でも探索可能

### breadth_first_search

- http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_11_C
- 深さ優先探索と同様にO(|V|²)
- 深さ優先探索は、スタックで探索の探索順序を決めていたが、幅優先探索はキューで探索順序を決定する。

### connected_components

- http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_11_D
- 隣接行列表現ではなく、隣接リスト表現を用いることで、O(|V|+|E|) (頂点の数+辺の数)の計算量になる
- 無向グラフなので、頂点u,v両方が行き来できるよう二次元配列での辺を表現する
- 先にグルーピングして、出題に対して同一グループかを確認する

### minimum_spanning_tree

- http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_12_A
- 重みが最小である頂点を探すためにグラフの頂点の数だけ探索を行うので、O(|V|²)

### single_source_shortest_path_1

- http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_12_B
- セールスマン巡回問題やダイクストラのアルゴリズムと呼ばれる問題
- minimun_spanning_tree(MST, 最小全域木)と同様にO(|V|²)
- 最小全域木と同様の考え方で解答することができる
  - 最小全域木の場合は最小全域木からそれ以外の頂点への最小の重みを求める
  - 最短経路問題の場合は始点からそれ以外の頂点の最小の重みを求める

### single_source_shortest_path_2

- http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_12_C
- ダイクストラ法に優先度付きキューを用いて実装する
- |V|の数だけキューから頂点が取り出され( O(|V|log|V|) )、|E|の数だけキューに挿入される( O(|E|log|V|) )ので、O((|V|+|E|)log|V|)