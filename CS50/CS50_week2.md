# Week 2 ：Array


```python
#課程連結🔗：https://cs50.harvard.edu/college/2019/fall/weeks/2/
```

### 資料類型

在C語言中，我們可以使用不同類型的變量來存儲數據：




```python
# bool 1 byte
# char 1 byte
# int 4 bytes
# float 4 bytes
# long 8 bytes
# double 8 bytes
# string ? bytes
```

這些類型中的每一種都會為我們創建的每個變量佔用一定數量的字節，並且上面的大小是沙箱，IDE的大小，並且很可能是您的計算機在C中為每種類型使用的大小。

### 記憶體

在我們的計算機內部，我們擁有稱為RAM的芯片，即隨機存取存儲器，用於存儲數據以供短期使用。我們可能會將程序或文件保存到硬盤（或SSD）中以進行長期存儲，但是當我們打開程序或文件時，會先將其複製到RAM中。儘管RAM很小，並且是臨時的（直到電源關閉），但速度要快得多。
我們可以想到存儲在RAM中的字節，就像它們在網格中一樣：

![-w180](https://upload.cc/i1/2020/01/10/oqGSOy.png)


在C語言中，當我們創建一個char類型的變量時，該變量的大小為1個字節，它將實際存儲在RAM的其中一個框中。一個帶有4個字節的整數將佔用其中四個框。
每個框都標有一些數字或地址，從0到1到2，依此類推。

### Array

假設我們要存儲三個變量：

![](https://upload.cc/i1/2020/01/10/20Hdgq.png)

請注意，我們使用單引號表示文字字符，並在字符串中將多個字符一起使用雙引號。

我們可以編譯並運行它，以查看H I ！。





而且我們知道字符只是數字，所以如果我們將字符串格式更改為printf（“％i％i％i \ n”，c1，c2，c3）;，我們可以看到每個已打印字符的數值：72 73 33。

我們可以在使用（int）c1之前將每個字符顯式轉換或轉換為int，但是我們的編譯器可以為我們隱式執行此操作。

在內存中，我們可能會有三個框，分別用c1，c2和c3標記，每個框代表一個二進製字節，其中包含每個變量的值。

## 課程簡報

![-w80](https://upload.cc/i1/2020/01/10/Eau38G.png)
![-w80](https://upload.cc/i1/2020/01/10/c0KdXs.png)
![-w80](https://upload.cc/i1/2020/01/10/YkBo1n.png)


```python

```