## Dijkstra原理（Shortest path）：

1.介紹

* Dijkstra算法是典型最短路徑算法，用於計算一個節點到其他節點的最短路徑。
* 它的主要特點是以起始點為中心向外層層擴展(廣度優先搜索思想)，直到擴展到終點為止。
* Dijkstra算法能得出最短路徑的最優解，但由於它遍歷計算的節點很多，所以效率低。

2.原理

* 首先，引入一個輔助向量D，它的每個分量 D[i]保存當前所找到的從起始點v到其它每個頂點vi的長度；一個保存已經找到了最短路徑的頂點的集合：T
* D的初始狀態為: 若從v到vi有弧，則D[i]為弧上的權值否則置D[i]為∞; T的初始狀態為{v}
* 從D數組選擇最小值，則該值就是源點v到該值對應的頂點的最短路徑，並且把該點加入到T中，OK，此時完成一個頂點。
* 然後，我們需要看看新加入的頂點是否可以到達其他頂點並且看看通過該頂點到達其他點的路徑長度是否比源點直接到達短，如果是，那麼就替換這些頂點D中的值
* 從D中找出最小值，重復上述動作，直到T中包含了圖的所有頂點


3.流程圖
![-w80](https://github.com/Maddiezheng/MyLearningNote/blob/master/Data%20Structures%20and%20Algorithms/Picture/Dijkstra.jpeg)
## Kruskal原理（Minimum Spanning tree）：

1.介紹

* 生成樹的概念 ：在一個連通圖中取出這個圖的全部頂點和一部分邊形成的一個無環圖就是這個連通圖的生成樹。在圖中，任意取出圖中的一條邊都使得這個圖中沒有環路，也就形成了一棵樹。
* 最小生成樹：在一個連通圖的所有生成樹中，邊的權重之和最小的那棵樹稱為最小生成樹

2.原理

* 記Graph中有v個頂點，e個邊

* 新建圖Graph_new，Graph_new中擁有原圖中相同的e個頂點，但沒有邊
* 將原圖Graph中所有e個邊按權值從小到大排序
* 循環：從權值最小的邊開始遍歷每條邊 直至圖Graph中所有的節點都在同一個連通分量中
                If 這條邊連接的兩個節點於圖Graph_new中不在同一個連通分量中
                                         添加這條邊到圖Graph_new中


3.流程圖
![-w80](https://github.com/Maddiezheng/MyLearningNote/blob/master/Data%20Structures%20and%20Algorithms/Picture/kruskal.jpeg)
#參考資料

