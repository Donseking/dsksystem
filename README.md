## DSK System

```

這是 Donseking 寫的命令操作系統  
要使用命令需要前綴 "-"  

直接打 "math" 會切換成 math 模式  
math 模式前綴 "#"   
                   --2022.06.30

```

### dsk.py

命令 : 

pit   > 輸出文字  

    -pit Hello

et    > 關閉程式

    -et
    
path  > 查看當前路徑

    -path
    
open  > 打開檔案

    -open ex.txt

cls   > 清屏

    -cls

defile > 清除文件

    -defile ex.txt

rename  > 重新命名

    -rename oldfilename.txt newfilename.txt

mdf     > 建立檔案

    -mdf newfilename.txt

run     > 執行程式或開啟檔案

    -run will_run_file.py

t       > 開啟 txt 檔 ` 不用副檔名 `

    -t file_name

p       > 開啟 python 檔 ` 不用副檔名 `

    -p file_name

'+'       > 執行 dos 指令
