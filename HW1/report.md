# 密碼學作業一
###### 409410050 王謙靜


## 程式檔案架構
![](https://i.imgur.com/8uKeINQ.png)
1. `plaintext_gen.py` 是用來產生 `plain_text.txt` 的
2. 三種加密法個放在一個資料夾中，分別有加密與解密的程式
3. `run.sh` 可以用來執行三個密碼的加解密，正確性檢查以及時間的測量

### 被加密的檔案大小
被加密的檔案大小 191MB
![](https://i.imgur.com/VSafpsL.png)

## 執行畫面
我寫了一個 `run.sh` 的 script 來執行加解密、時間測量以及檢查與一開始加密的內容是否一樣。
`run.sh`
```shell=
cipher=("AESCBC" "AESCTR" "ChaCha20")

for i in ${cipher[@]}
do
    cd $i
    echo "running $i"
    rm *.txt
    time python3 encrypt.py
    python3 decrypt.py
    echo "diff retrive.txt ../plaintext.txt"
    diff retrive.txt ../plaintext.txt
    cd ../
done
```
執行結果如下
![](https://i.imgur.com/ADgzg7l.png)

## 三種加密方式的速度
精確來說 plaintext.txt 有 $200,000,000$ 個 bytes

故 AESCBC 加密一個 bytes 平均需要：$\frac{1.008}{2\cdot 10^8}=5.04\times 10^{-9}$ 秒

故 AESCTR 加密一個 bytes 平均需要：$\frac{0.846}{2\cdot 10^8}=4.23\times 10^{-9}$ 秒

故 ChaCha20 加密一個 bytes 平均需要：$\frac{0.846}{2\cdot 10^8}=5.24\times 10^{-9}$ 秒

## 比較解密後的檔案與原始檔案

![](https://i.imgur.com/ilEg7RO.png)

## reference
1. https://pycryptodome.readthedocs.io/en/latest/src/cipher/classic.html#cbc-mode
2. https://pycryptodome.readthedocs.io/en/latest/src/cipher/chacha20.html?highlight=ChaCha20
3. https://www.w3schools.com/python/python_file_write.asp
4. https://www.geeksforgeeks.org/python-write-bytes-to-file/

