import streamlit as st

st.set_page_config(page_title="第五課：APCS觀念題兩階段實戰", page_icon="📝", layout="wide")

st.title("📝 第五課：APCS 觀念題程式識讀——兩階段實戰特訓")
st.caption("授課教師：闕河正 老師")
st.markdown("---")

st.info("""
🎯 **課程目標**：參考 APCS 官方最新程式識讀題本結構，針對「變數型別、if條件式、陣列索引、for迴圈」四大基礎進行高強度人肉電腦追蹤訓練。
""")

# ==========================================
# 核心心法：APCS 觀念題四大破題密碼
# ==========================================
st.header("🎯 闕老師開講：觀念題的「四大核心攻略」")
st.markdown("""
解 APCS 觀念題時，絕對不能只用眼睛「盲看」，必須帶領學生養成建立**「變數變化追蹤表」**的習慣：
""")

st.table([
    {"戰略要點": "1️⃣ 迴圈邊界一定要「開完號碼牌」", "具體核心攻略": "一看到 `range(a, b)` 或 `range(len(d)-1, -1, -1)`，第一件事是在題目旁邊寫下這台數數機倒出來的所有數字，避免被『顧前不顧後』坑死。"},
    {"戰略要點": "2️⃣ 陣列索引與值的雙向分清", "具體核心攻略": "隨時分清 `i`（抽屜號碼）與 `d[i]`（抽屜裡的寶物）。題目最喜歡故意寫成 `d[d[i]]` 這種多層牽引來讓學生大腦打結。"},
    {"戰略要點": "3️⃣ 邏輯變數的旗標（Flag）狀態", "具體核心攻略": "注意像 `is_match = True` 這種變數何時被觸發改寫，通常這就是找到『反例』或『特殊條件』的關鍵節點。"},
    {"戰略要點": "4️⃣ 人肉電腦表格法", "具體核心攻略": "每執行一行程式，就把變數最新的值填入表格，舊的值劃掉，這樣在多重迴圈時才不會算到後面忘記前面。"}
])

st.markdown("---")

# ==========================================
# 階段一：基礎邏輯與單層迴圈能力鞏固（5題）
# ==========================================
st.header("🔥 第一階段：基礎邏輯與單層迴圈能力鞏固")
st.write("本階段專注於單層迴圈搭配 if、陣列基本索引操作，目標是速度要快、100% 答對。")

p1_t1, p1_t2, p1_t3, p1_t4, p1_t5 = st.tabs(["📌 實戰 1", "📌 實戰 2", "📌 實戰 3", "📌 實戰 4", "📌 實戰 5"])

with p1_t1:
    st.markdown("#### 【第 1 題】陣列特殊索引與字串加法運算")
    st.code("""
data = [10, 20, 30, 40, 50]
s = ""
for i in range(1, len(data) - 1):
    if data[i] > data[i-1]:
        s += "Y"
    else:
        s += "N"
print(s)
    """, language="python")
    
    st.markdown("**請問程式執行後會輸出什麼結果？**")
    ans1 = st.radio("請選擇你的答案：", ["(A) YYYY", "(B) YY", "(C) YYY", "(D) YNYN"], key="ans1")
    with st.expander("👀 查看闕老師的人肉電腦追蹤分析"):
        st.info("💡 **正確答案：(C) YYY**")
        st.markdown("""
        **🔍 拆解軌跡：**
        1. `len(data)` 是 5，所以 `range(1, 4)` 產生的號碼牌 `i` 分別是：**1, 2, 3**（不包含 4）。
        2. 當 `i = 1`：比較 `data[1] > data[0]` (20 > 10) ➔ 成立，`s` 變成 `"Y"`。
        3. 當 `i = 2`：比較 `data[2] > data[1]` (30 > 20) ➔ 成立，`s` 變成 `"YY"`。
        4. 當 `i = 3`：比較 `data[3] > data[2]` (40 > 30) ➔ 成立，`s` 變成 `"YYY"`。
        """)

with p1_t2:
    st.markdown("#### 【第 2 題】倒著走的數數機與累加")
    st.code("""
sum_val = 0
for i in range(10, 2, -2):
    if i % 3 == 0:
        sum_val += i
print(sum_val)
    """, language="python")
    
    ans2 = st.radio("請選擇你的答案：", ["(A) 18", "(B) 6", "(C) 12", "(D) 0"], key="ans2")
    with st.expander("👀 查看解題桌分析"):
        st.info("💡 **正確答案：(B) 6**")
        st.markdown("""
        **🔍 人肉電腦變數追蹤表：**
        * `range(10, 2, -2)` 倒出來的 `i` 為：**10, 8, 6, 4**（不含 2）。
        """)
        st.table([
            {"Currently i": "10", "i % 3 == 0": "否 (餘2)", "sum_val 的變化": "0"},
            {"Currently i": "8", "i % 3 == 0": "否 (餘2)", "sum_val 的變化": "0"},
            {"Currently i": "6", "i % 3 == 0": "是 (整除) ⭐", "sum_val 的變化": "0 + 6 = 6"},
            {"Currently i": "4", "i % 3 == 0": "否 (餘1)", "sum_val 的變化": "6"}
        ])

with p1_t3:
    st.markdown("#### 【第 3 題】經典 Flag 旗標與 break 提前煞車")
    st.code("""
items = [11, 22, 35, 44, 57]
flag = False
for i in range(len(items)):
    if items[i] % 11 == 0 and i > 0:
        flag = True
        break
print(flag)
    """, language="python")
    
    ans3 = st.radio("請選擇你的答案：", ["(A) True", "(B) False", "(C) None", "(D) 程式出錯"], key="ans3")
    with st.expander("👀 查看解題桌分析"):
        st.info("💡 **正確答案：(A) True**")
        st.markdown("""
        **🔍 拆解軌跡：**
        * `i = 0`：`items[0]` 是 11。雖然 `11 % 11 == 0`，但條件要求 `i > 0`。此時不滿足，繼續迴圈。
        * `i = 1`：`items[1]` 是 22。`22 % 11 == 0` 且 `1 > 0` 成立！
        * 觸發 `flag = True`，並執行 `break` 急煞車，迴圈解散。最終印出 `True`。
        """)

with p1_t4:
    st.markdown("#### 【第 4 題】鄰近元素交互作用（APCS 超高機率考題）")
    st.code("""
d = [5, 3, 8, 2, 4]
for i in range(len(d) - 1):
    if d[i] > d[i+1]:
        d[i], d[i+1] = d[i+1], d[i] # 兩抽屜物品對調
print(*d)
    """, language="python")
    
    ans4 = st.radio("請選擇你的答案：", ["(A) [2, 3, 4, 5, 8]", "(B) 3 5 2 4 8", "(C) 3 5 8 2 4", "(D) 2 3 8 5 4"], key="ans4")
    with st.expander("👀 查看解題桌分析"):
        st.info("💡 **正確答案：(B) 3 5 2 4 8**")
        st.markdown("""
        **🔍 這是經典泡沫排序法（Bubble Sort）的其中一輪走訪！變數動態追蹤表：**
        """)
        st.table([
            {"步驟": "初始陣列", "對比與動作": "無", "陣列現況": "[5, 3, 8, 2, 4]"},
            {"步驟": "i = 0", "對比與動作": "d[0] > d[1] (5 > 3) ➔ 對調", "陣列現況": "[3, 5, 8, 2, 4]"},
            {"步驟": "i = 1", "對比與動作": "d[1] > d[2] (5 > 8) ➔ 不動", "陣列現況": "[3, 5, 8, 2, 4]"},
            {"步驟": "i = 2", "對比與動作": "d[2] > d[3] (8 > 2) ➔ 對調", "陣列現況": "[3, 5, 2, 8, 4]"},
            {"步驟": "i = 3", "對比與動作": "d[3] > d[4] (8 > 4) ➔ 對調", "陣列現況": "[3, 5, 2, 4, 8]"}
        ])
        st.markdown("最後使用 `print(*d)`，中括號跟逗號剝落，輸出：`3 5 2 4 8`。")

with p1_t5:
    st.markdown("#### 【第 5 題】等差跳著切與反向索引結合")
    st.code("""
arr = [2, 4, 6, 8, 10, 12]
count = 0
for i in range(0, len(arr), 2):
    count += arr[i] - arr[-1]
print(count)
    """, language="python")
    
    ans5 = st.radio("請選擇你的答案：", ["(A) -18", "(B) 18", "(C) -24", "(D) 0"], key="ans5")
    with st.expander("👀 查看解題桌分析"):
        st.info("💡 **正確答案：(A) -18**")
        st.markdown("""
        **🔍 拆解軌跡：**
        * `arr[-1]` 永遠代表最後一個櫃子，值為 `12`。
        * `range(0, 6, 2)` 產生的號碼牌是：**0, 2, 4**。
        * `i = 0`：`arr[0] - 12` ➔ `2 - 12 = -10`
        * `i = 2`：`arr[2] - 12` ➔ `6 - 12 = -6`
        * `i = 4` : `arr[4] - 12` ➔ `10 - 12 = -2`
        * 總計 `count` = `(-10) + (-6) + (-2) = -18`。
        """)

st.markdown("---")

# ==========================================
# 階段二：雙重迴圈與索引互相牽引實戰（5題）
# ==========================================
st.header("🔥 第二階段：雙重迴圈與索引互相牽引實戰")
st.write("本階段屬於 APCS 觀念題中高難度區（約第 3、4 級難度）。外層迴圈會動態控制內層迴圈的步伐或陣列索引，請同學拿出紙筆精確追蹤。")

p2_t1, p2_t2, p2_t3, p2_t4, p2_t5 = st.tabs(["🔥 挑戰 1", "🔥 挑戰 2", "🔥 挑戰 3", "🔥 挑戰 4", "🔥 挑戰 5"])

with p2_t1:
    st.markdown("#### 【第 6 題】外層 i 決定內層 j 的起點")
    st.code("""
val = 0
for i in range(3):
    for j in range(i, 3):
        val += 1
print(val)
    """, language="python")
    
    ans6 = st.radio("請選擇你的答案：", ["(A) 9", "(B) 6", "(C) 3", "(D) 4"], key="ans6")
    with st.expander("👀 查看人肉電腦精準軌跡表"):
        st.info("💡 **正確答案：(B) 6**")
        st.markdown("這題屬於標準的三角形疊代。內層的計數次數會隨著外層增加而越來越少：")
        st.table([
            {"外層 i": "i = 0", "內層 j 範圍 range(i, 3)": "range(0, 3) 👉 數出 0, 1, 2", "val 增加次數": "增加 3 次"},
            {"外層 i": "i = 1", "內層 j 範圍 range(i, 3)": "range(1, 3) 👉 數出 1, 2", "val 增加次數": "增加 2 次"},
            {"外層 i": "i = 2", "內層 j 範圍 range(i, 3)": "range(2, 3) 👉 數出 2", "val 增加次數": "增加 1 次"}
        ])
        st.markdown("總計執行次數 = `3 + 2 + 1 = 6` 次，故 `val` 最終為 6。")

with p2_t2:
    st.markdown("#### 【第 7 題】內外層雙重索引與陣列改寫")
    st.code("""
box = [1, 2, 3]
for i in range(len(box)):
    for j in range(i):
        box[i] += box[j]
print(*box)
    """, language="python")
    
    ans7 = st.radio("請選擇你的答案：", ["(A) 1 3 7", "(B) 1 2 3", "(C) 1 3 6", "(D) 2 4 6"], key="ans7")
    with st.expander("👀 查看人肉電腦精準軌跡表"):
        st.info("💡 **正確答案：(A) 1 3 7**")
        st.markdown("""
        **🔍 串列內容會一邊跑一邊被同步改寫：**
        * **`i = 0`**：`range(0)` 是空的，內層不執行。此時 `box = [1, 2, 3]`。
        * **`i = 1`**：`range(1)` 數出 `j = 0`。
          * 執行：`box[1] += box[0]` ➔ `2 += 1` ➔ `box[1]` 變成 **3**。
          * 此時 `box = [1, 3, 3]`。
        * **`i = 2`**：`range(2)` 數出 `j = 0, 1`。
          * `j = 0` 時：`box[2] += box[0]` ➔ `3 += 1` ➔ `box[2]` 變成 4。
          * `j = 1` 時：`box[2] += box[1]` ➔ **注意此時 box[1] 已經是 3 了！** ➔ `4 += 3` ➔ `box[2]` 變成 **7**。
        * 最終結果：`1 3 7`。
        """)

with p2_t3:
    st.markdown("#### 【第 8 題】外層控制內層步伐（跳著走的雙重迴圈）")
    st.code("""
total = 0
for i in range(1, 4):
    for j in range(0, 10, i):
        total += 1
print(total)
    """, language="python")
    
    ans8 = st.radio("請選擇你的答案：", ["(A) 30", "(B) 17", "(C) 19", "(D) 15"], key="ans8")
    with st.expander("👀 查看人肉電腦精準軌跡表"):
        st.info("💡 **正確答案：(C) 19**")
        st.markdown("""
        **🔍 當外層變數變成內層的『步長(Step)』時的展開軌跡：**
        * **`i = 1`**：`range(0, 10, 1)` ➔ 數出 0,1,2,3,4,5,6,7,8,9 (共 **10** 個數)
        * **`i = 2`**：`range(0, 10, 2)` ➔ 數出 0, 2, 4, 6, 8 (共 **5** 個數)
        * **`i = 3`**：`range(0, 10, 3)` ➔ 數出 0, 3, 6, 9 (共 **4** 個數)
        * 總累加次數 = `10 + 5 + 4 = 19`。
        """)

with p2_t4:
    st.markdown("#### 【第 9 題】布林旗標變數在雙重迴圈中的生死控制")
    st.code("""
matrix_data = [5, 8, 12]
found = False

for i in range(len(matrix_data)):
    for j in range(2, matrix_data[i]):
        if matrix_data[i] % j == 0:
            found = True
            break
    if found:
        print(i)
        break
    """, language="python")
    
    ans9 = st.radio("請選擇你的答案：", ["(A) 0", "(B) 1", "(C) 2", "(D) 什麼都不會印出"], key="ans9")
    with st.expander("👀 查看解題桌 analysis"):
        st.info("💡 **正確答案：(B) 1**")
        st.markdown("""
        **🔍 戰略分析（這題其實是在找這串陣列中『第一個合數(非質數)』的索引位置）：**
        * `i = 0`：`matrix_data[0]` 為 5。內層 `j` 從 2 數到 4，都無法整除 5（5是質數）。`found` 依舊是 `False`。
        * `i = 1`：`matrix_data[1]` 為 8。內層 `j = 2` 時，`8 % 2 == 0` 成立！
          * 內部觸發 `found = True` 並 `break` 跳出內層迴圈。
        * 回到外層，此時 `if found:` 成立，執行 `print(i)` 印出目前的索引值 **1**，接著外層也 `break` 結束整段程式。
        """)

with p2_t5:
    st.markdown("#### 【第 10 題】利用單維陣列與 range 計算模擬 2D 鄰近比對")
    st.code("""
v = [1, 0, 1, 0, 1, 0]
res = 0
for i in range(1, len(v) - 1):
    if v[i-1] == 1 and v[i+1] == 1:
        res += 1
print(res)
    """, language="python")
    
    ans10 = st.radio("請选择你的答案：", ["(A) 0", "(B) 1", "(C) 2", "(D) 3"], key="ans10")
    with st.expander("👀 查看解題桌分析"):
        st.info("💡 **正確答案：(C) 2**")
        st.markdown("""
        **🔍 夾心餅乾（特徵比對）檢測：**
        * `range(1, 5)` 產生的索引 `i` 為：1, 2, 3, 4。
        * `i = 1`：檢查 `v[0] == 1` 且 `v[2] == 1` ➔ `1 == 1` 且 `1 == 1` (成立！⭐ `res` 變成 1)
        * `i = 2`：檢查 `v[1] == 1` 且 `v[3] == 1` ➔ `0 == 1` (失敗)
        * `i = 3`：檢查 `v[2] == 1` 且 `v[4] == 1` ➔ `1 == 1` 且 `1 == 1` (成立！⭐ `res` 變成 2)
        * `i = 4`：檢查 `v[3] == 1` 且 `v[5] == 1` ➔ `0 == 1` (失敗)
        * 最終結果：2。
        """)

    # --- 多重迴圈高階閱讀練習題 二 ---
    st.markdown("---")
    st.markdown("### 📝 課後加碼：雙重迴圈幾何追蹤")
    mq1, mq2 = st.tabs(["🔥 進階挑戰 一", "🔥 進階挑戰 二"])
    with mq1:
        st.markdown("**題目：請問以下程式執行後，變數 `count` 的最終數值是多少？**")
        st.code("""
count = 0
for i in range(1, 4):
    for j in range(i):
        count += 1
print(count)
        """, language="python")
        with st.expander("👀 查看人肉電腦分析解答"):
            st.success("**答案：6**")
            st.markdown("""
            * 當 `i = 1`：`j` 範圍是 `range(1)` (數字 0)，內層跑 1 次 👉 `count` 變成 1
            * 當 `i = 2`：`j` 範圍是 `range(2)` (數字 0, 1)，內層跑 2 次 👉 `count` 變成 3
            * 當 `i = 3`：`j` 範圍是 `range(3)` (數字 0, 1, 2)，內層跑 3 次 👉 `count` 變成 6
            * 總共加了：1 + 2 + 3 = 6 次。
            """)
    with mq2:
        st.markdown("**題目：這段程式碼會印出什麼圖形？（注意 `end=''` 代表不換行）**")
        st.code("""
for i in range(3, 0, -1):
    for j in range(i):
        print("#", end="")
    print()
        """, language="python") # 👈 這裡已完美修正為 language="python"
        with st.expander("👀 查看人肉電腦分析解答"):
            st.success("**答案：一個倒三角形**")
            st.code("""
###
##
#
            """, language="text")

# ==========================================
# 課程結語
# ==========================================
st.divider()
# ==========================================
# 階段三：高強度課後自主練習題庫（10題，無詳解）
# ==========================================
st.markdown("---")
st.header("🎯 第三階段：APCS 觀念題自主特訓（足量實戰練習）")
st.write("本區提供 10 題高仿 APCS 識讀測驗題，無即時詳解，考驗同學們能否獨立用「紙筆變數追蹤法」找出正確答案！")

p3_t1, p3_t2, p3_t3, p3_t4, p3_t5, p3_t6, p3_t7, p3_t8, p3_t9, p3_t10 = st.tabs([
    "📝 練習 1", "📝 練習 2", "📝 練習 3", "📝 練習 4", "📝 練習 5", 
    "📝 練習 6", "📝 練習 7", "📝 練習 8", "📝 練習 9", "📝 練習 10"
])

with p3_t1:
    st.markdown("#### 【練習 1】字串切片與 range 邊界陷阱")
    st.code("""
word = "PROG"
result = ""
for i in range(len(word) - 1, 0, -1):
    result += word[i]
print(result)
    """, language="python")
    st.radio("請選擇你的答案：", ["(A) GORP", "(B) GOR", "(C) RO", "(D) ORP"], key="ex1")

with p3_t2:
    st.markdown("#### 【練習 2】複合條件篩選與跳格累加")
    st.code("""
ans = 0
for i in range(1, 15, 3):
    if i % 2 != 0:
        ans += i
print(ans)
    """, language="python")
    st.radio("請選擇你的答案：", ["(A) 12", "(B) 16", "(C) 25", "(D) 22"], key="ex2")

with p3_t3:
    st.markdown("#### 【練習 3】陣列走訪與動態條件覆蓋")
    st.code("""
nums = [4, 2, 7, 1, 9]
val = nums[0]
for i in range(1, len(nums)):
    if nums[i] < val:
        val = nums[i]
print(val)
    """, language="python")
    st.radio("請選擇你的答案：", ["(A) 4", "(B) 9", "(C) 1", "(D) 2"], key="ex3")

with p3_t4:
    st.markdown("#### 【練習 4】雙指標相鄰差值統計")
    st.code("""
A = [10, 15, 12, 18, 20]
count = 0
for i in range(len(A) - 1):
    if A[i+1] - A[i] > 2:
        count += 1
print(count)
    """, language="python")
    st.radio("請選擇你的答案：", ["(A) 1", "(B) 2", "(C) 3", "(D) 4"], key="ex4")

with p3_t5:
    st.markdown("#### 【練習 5】旗標狀態與反向 break 偵測")
    st.code("""
data = [5, 10, 15, 21, 25]
status = True
for i in range(len(data)):
    if data[i] % 2 == 0:
        status = False
    if data[i] > 20:
        break
print(status)
    """, language="python")
    st.radio("請選擇你的答案：", ["(A) True", "(B) False", "(C) None", "(D) 程式出錯"], key="ex5")

with p3_t6:
    st.markdown("#### 【練習 6】雙重迴圈矩陣次數走訪")
    st.code("""
k = 0
for i in range(1, 4):
    for j in range(1, 4):
        if i != j:
            k += 1
print(k)
    """, language="python")
    st.radio("請選擇你的答案：", ["(A) 9", "(B) 6", "(C) 3", "(D) 0"], key="ex6")

with p3_t7:
    st.markdown("#### 【練習 7】內層結束值受外層變數動態控制")
    st.code("""
total = 0
for i in range(4,




st.subheader("🏁 闕老師特訓章節總結")
st.success("""
恭喜你完成了這 10 題高強度的 APCS 程式識讀模擬題！
官方的題本核心邏輯不外乎就是這些變數的連鎖反應。只要同學們能耐下心來，在紙上把「號碼牌」與「變數追蹤表」畫出來，觀念題拿到 4 級分（高標）絕對指日可待！下課！
""")
