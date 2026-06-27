import streamlit as st

# 設定網頁標題與風格
st.set_page_config(page_title="APCS 第十課：函式與遞迴", layout="wide")

st.title("🚀 APCS 第十課：資料的加工廠——函式與遞迴基礎")
st.caption("適用 Python 3.14 環境 | 程式老師專用教學教材（直條流式設計）")
st.markdown("---")

# ==========================================
# 🟢 1. 函式的四種基本型態
# ==========================================
st.header("🧱 1. 函式的四種基本架構")
st.markdown("""
當程式碼越寫越長，重複的片段越來越多時，我們就需要將程式封裝成**「函式 (Function)」**。
函式就像是一台資料加工機器，丟入原料（參數），產出成品（回傳值）。
根據「有沒有原料」和「有沒有成品」，可以分為四種經典基本型態：
""")

# 建立四種形態的排版
c1, c2 = st.columns(2)
with c1:
    st.subheader("📦 型態一：不帶參數 ➡️ 不回傳")
    st.markdown("純粹用來執行固定的連續動作（如印出固定選單、歡迎詞）。")
    st.code(r"""
def show_welcome():
    print("====================")
    print(" 歡迎來到 APCS 訓練營 ")
    print("====================")

# 呼叫方式
show_welcome()
""", language="python")

    st.subheader("📦 型態二：不帶參數 ➡️ 有回傳")
    st.markdown("不用給原料，但加工廠會主動吐回一個特定資料（如讀取系統狀態、固定常數）。")
    st.code(r"""
def get_pi():
    return 3.14159

# 呼叫方式（必須用變數去接住回傳值）
val = get_pi()
print(val) # 輸出: 3.14159
""", language="python")

with c2:
    st.subheader("📦 型態三：有帶參數 ➡️ 不回傳")
    st.markdown("丟入原料讓加工廠處理，但處理完後不需要把資料交回主程式（直接在函式內印出）。")
    st.code(r"""
def print_square(n):
    result = n * n
    print(f"數字 {n} 的平方是: {result}")

# 呼叫方式
print_square(5) # 輸出: 數字 5 的平方是: 25
""", language="python")

    st.subheader("📦 型態四：有帶參數 ➡️ 有回傳")
    st.markdown("**【APCS 最常用、最重要！】** 丟入原料，加工完後將關鍵結果 `return` 帶回主程式繼續運算。")
    st.code(r"""
def add_two_nums(a, b):
    sum_val = a + b
    return sum_val

# 呼叫方式
ans = add_two_nums(10, 20)
print(ans) # 輸出: 30
""", language="python")

# --- 閱讀練習 1 ---
st.markdown("#### 📝 挑戰一：四型態綜合閱讀練習")
st.code(r"""
def calc(x):
    if x % 2 == 0:
        return x // 2
    print("No Return")

res1 = calc(4)
res2 = calc(5)
print(res1, res2)
""", language="python")

q1_ans = st.radio(
    "請問最後印出的結果為何？",
    ["(A) 2 2.5", "(B) 2 None （且過程中印出 No Return）", "(C) 2 0 （且過程中印出 No Return）", "(D) 語法錯誤，因為奇數沒有寫 return"],
    index=None,
    key="fq1"
)
if q1_ans:
    if q1_ans.startswith("(B)"):
        st.success("🎉 答對了！非常優秀！")
        st.info(r"""💡 **核心觀念解析**：
* 當 `x = 4` 時，滿足 `4 % 2 == 0`，執行 `return 2`，因此 `res1 = 2`。
* 當 `x = 5` 時，不滿足條件，程式繼續往下執行 `print("No Return")`。
* 關鍵在於：**在 Python 中，如果一個函式執行完畢卻沒有遇到任何 `return` 指令，它會默認回傳 `None`**。因此 `res2` 接收到的值是 `None`！""")
    else:
        st.error("❌ 答錯囉！請特別注意 Python 函式沒有寫 return 時的預設回傳機制。")

st.markdown("---")

# ==========================================
# 🟢 2. 預設參數值（Default Parameters）與其規則
# ==========================================
st.header("⚙️ 2. 函式的預設參數值與語法規則")
st.markdown("""
在設計函式時，我們可以為參數設定**「預設值」**。如果主程式呼叫時沒有傳入該變數，就會自動套用預設值。
這在實戰中非常方便，但設定時有一條**絕對不能犯的語法鐵律**！
""")

st.subheader("💡 語法Ａ：所有參數皆有預設值")
st.code(r"""
def greet(name="學生", message="你好"):
    print(f"{name}，{message}！")

greet()               # 輸出: 學生，你好！ (全部套用預設)
greet("河正老師")      # 輸出: 河正老師，你好！ (傳入的取代第一個參數)
greet("小明", "早安")  # 輸出: 小明，早安！ (全部取代)
""", language="python")

st.subheader("⚠️ 語法Ｂ：部分參數有預設值（鐵律規則）")
st.error("🔥 **語法鐵律**：在定義參數時，**「有預設值的參數」必須全部排在「沒有預設值的參數」後面！** 否則 Python 語法解析器會直接報錯崩潰。")

st.code(r"""
# 正確寫法：沒預設值的 a 排在前面，有預設值的 b, c 排在後面
def compute(a, b=10, c=20):
    return a + b + c

# 錯誤寫法 (會引發 SyntaxError: non-default argument follows default argument)
# def error_compute(a=10, b):
#     return a + b
""", language="python")

# --- 閱讀練習 2 ---
st.markdown("#### 📝 挑戰二：預設值參數陷阱題")
st.code(r"""
def power_sum(base, exp=2, bias=0):
    return (base ** exp) + bias

ans1 = power_sum(3)
ans2 = power_sum(2, 3, 5)
ans3 = power_sum(4, bias=3)
print(ans1, ans2, ans3)
""", language="python")

q2_ans = st.radio(
    "請問最後印出的三個答案分別是多少？",
    ["(A) 9, 13, 19", "(B) 6, 11, 19", "(C) 9, 13, 7", "(D) 6, 13, 11"],
    index=None,
    key="fq2"
)
if q2_ans:
    if q2_ans.startswith("(A)"):
        st.success("🎉 答對了！精準無誤！")
        st.info(r"""💡 **核心觀念解析**：
* `ans1 = power_sum(3)`：`base=3`，其餘套預設。 $3^2 + 0 = 9$。
* `ans2 = power_sum(2, 3, 5)`：所有參數被覆蓋。 $2^3 + 5 = 8 + 5 = 13$。
* `ans3 = power_sum(4, bias=3)`：`base=4`，`bias=3`（指定名稱傳參），而 `exp` 維持預設值 2。 $4^2 + 3 = 16 + 3 = 19$。""")
    else:
        st.error("❌ 答錯囉！請重新細算一次 ans3，注意它指定了 bias，那 exp 會是多少呢？")

st.markdown("---")

# ==========================================
# 🟢 3. 帶陣列參數與記憶體共享特性
# ==========================================
st.header("📋 3. 當函式傳入「陣列 (List) 參數」")
st.markdown("""
將陣列當作參數傳入函式中，是 APCS 實作題最經典的結構（例如：把地圖陣列、成績清單丟進函式處理）。
這裡必須緊扣第八課學到的觀念：**「陣列傳遞的是記憶體位址（參照）」**。
如果在函式內部修改了陣列的內容，外面的原始陣列也會**同步被修改**！
""")

st.code(r"""
def modify_array(arr):
    arr[0] = 99
    arr.append(50)

# 主程式
nums = [10, 20, 30]
modify_array(nums)
print(nums) # 輸出: [99, 20, 30, 50]  <-- 裡面的修改影響到了外面！
""", language="python")

# --- 閱讀練習 3 ---
st.markdown("#### 📝 挑戰三：陣列傳參魔王題")
st.code(r"""
def process(data):
    data = data.copy()
    data[0] = 77
    data.append(88)

# 主程式
my_list = [10, 20]
process(my_list)
print(my_list, len(my_list))
""", language="python")

q3_ans = st.radio(
    "請問主程式最後印出的 my_list 與其長度為何？",
    ["(A) [77, 20, 88] 3", "(B) [10, 20] 2", "(C) [77, 20] 2", "(D) [10, 20, 88] 3"],
    index=None,
    key="fq3"
)
if q3_ans:
    if q3_ans.startswith("(B)"):
        st.success("🎉 太厲害了！完全沒有被這題騙到！")
        st.info(r"""💡 **核心觀念解析**：
在函式內部的第一行寫了 `data = data.copy()`！這行指令讓內部的 `data` 複製出了一份完全獨立的全新記憶體副本。
從這一刻起，內部 `data` 的任何修改（改值、append）都只發生在副本上，**切斷了與外部 my_list 的連結**。所以外面的 `my_list` 依然完好如初，長度仍為 2。""")
    else:
        st.error("❌ 哇！踩中陷阱了！請仔細看第一行 data.copy() 對記憶體關係做了什麼重大的改變。")

st.markdown("---")

# ==========================================
# 🟢 4. 全域變數 vs 區域變數
# ==========================================
st.header("🌐 4. 全域變數 (Global) vs 區域變數 (Local)")
st.markdown("""
在 APCS 觀念題中，每一屆幾乎必考一到兩題**變數生命週期（Scope）**。
* **區域變數 (Local Variable)**：定義在函式內部的變數。它只活在函式執行期間，函式結束就**人間蒸發**，外面的人完全拿不到它。
* **全域變數 (Global Variable)**：定義在所有函式外面的主程式變數。所有函式都看得到它，但如果想在函式內部「直接修改它的值」，必須用關鍵字宣告！
""")

st.subheader("💡 關鍵字 `global` 的重要性")
st.code(r"""
score = 100 # 這是一個全域變數

def try_change():
    score = 200 # 錯誤！這只是在內部建立一個同名的「區域變數」，動不到外面的全域變數

def real_change():
    global score # 正確！宣告「我要抓外面那個全域變數來改」
    score = 500

try_change()
print(score) # 依然是 100

real_change()
print(score) # 成功變成 500！
""", language="python")

# --- 閱讀練習 4 ---
st.markdown("#### 📝 挑戰四：APCS 模擬真實觀念題（變數生命週期）")
st.code(r"""
x = 5

def func1():
    x = 10
    return x

def func2():
    global x
    x += 2

print(func1(), end=" ")
func2()
print(x)
""", language="python")

q4_ans = st.radio(
    "請問這段程式碼最後的輸出內容是什麼？",
    ["(A) 10 5", "(B) 10 7", "(C) 5 7", "(D) 10 12"],
    index=None,
    key="fq4"
)
if q4_ans:
    if q4_ans.startswith("(B)"):
        st.success("🎉 恭喜你！完全看穿變數的生存範圍！")
        st.info(r"""💡 **逐行解讀流程**：
1. 全域變數 `x = 5`。
2. 呼叫 `func1()`：內部建立區域變數 `x = 10` 並回傳 `10`。此時外面的全域變數 `x` 依然是 5。第一個印出 `10`。
3. 呼叫 `func2()`：使用 `global x` 抓取外面的全域變數 `x`（其值為5），執行 `x += 2`，全域變數 `x` 成功變成 `7`。
4. 最後印出全域變數 `x` 的值，即為 `7`。故答案為 `10 7`。""")
    else:
        st.error("❌ 答錯囉！請分清楚 func1() 是回傳它內部的區域變數，而 func2() 才是真正去改造外面的世界。")

st.markdown("---")

# ==========================================
# 🟢 5. 遞迴 (Recursion) 的深度追蹤與核心原理
# ==========================================
st.markdown("---")
st.header("🔄 5. 魔王關卡：遞迴 (Recursion) 的深度追蹤")
st.markdown("""
遞迴是 APCS 觀念題的核心命題焦點。簡單來說，遞迴就是**「一個函式在執行過程中，自己呼叫自己」**。
許多同學在初學時，常會陷入「無窮無盡、不知道什麼時候該出來」的混亂中。

要完美駕馭遞迴，腦中必須牢記**「遞迴兩大支柱」**與**「堆疊 (Stack) 運作機制」**：
1. **終止條件 (Base Case)**：什麼時候必須停下來。這是遞迴的「出口」，沒有寫或寫錯，程式就會發生 `RecursionError`（記憶體爆滿崩潰）。
2. **遞迴關係式 (Recursive Step)**：如何把大問題切成更小的同類問題，逐步逼近出口。

### 📥 核心運作原理：堆疊 (Stack) 的「呼叫」與「回溯」
當一個函式呼叫自己時，舊的函式並沒有結束，而是**暫停執行並被壓入記憶體的「堆疊（置物櫃）」深處**。直到最頂層的函式觸發了「終止條件」拿到真實數值後，才會**由上往下、一層一層地「回溯」**把答案送回來！
""")

st.subheader("💡 經典基礎示範：階乘計算 ($N!$)")
st.markdown("數學上 $4! = 4 * 3 * 2 * 1$，也可以看成 $4! = 4 * 3!$。以下是程式碼與人肉電腦的追蹤歷程：")

st.code(r"""
def fact(n):
    if n == 1:
        return 1       # 支柱一：終止條件
    return n * fact(n - 1)  # 支柱二：遞迴關係式

print(fact(3))
""", language="python")

# 用精美的巢狀 blockquote 模擬記憶體堆疊與回溯過程
st.markdown("##### 🕵️‍♂️ `fact(3)` 的置物櫃堆疊分解歷程：")
st.info("""
* **【第一階段：瘋狂向下呼叫（疊高置物櫃）】**
    * 呼叫 `fact(3)` ➡️ 發現 `n != 1` ➡️ 暫停，等待 `fact(2)` 的答案。 (此時記憶體記住：$3 * text{?}$)
    * 呼叫 `fact(2)` ➡️ 發現 `n != 1` ➡️ 暫停，等待 `fact(1)` 的答案。 (此時記憶體記住：$2 * text{?}$)
    * 呼叫 `fact(1)` ➡️ **觸發終止條件！** ➡️ 直接回傳大門鑰匙：`1`。
* **【第二階段：拿到答案，向上回溯（拆除置物櫃）】**
    * `fact(1)` 的結果 `1` 往上送給 `fact(2)` ➡️ 計算 $2 * 1 = 2$，`fact(2)` 回傳 `2`。
    * `fact(2)` 的結果 `2` 往上送給 `fact(3)` ➡️ 計算 $3 * 2 = 6$，`fact(3)` 回傳最終答案 `6`！
""")

# ==========================================
# 🎯 遞迴專用：APCS 觀念題特訓（3 題高難度閱讀題）
# ==========================================
st.markdown("---")
st.subheader("📝 遞迴專項：APCS 真實模擬閱讀挑戰賽")
st.markdown("請同學們拿出紙筆，在桌上畫出「呼叫樹狀圖」，徹底追蹤變數，別被出題老師的障眼法騙了！")

# 建立三道遞迴挑戰題的 Tabs
r_tab1, r_tab2, r_tab3 = st.tabs([
    "🔥 遞迴挑戰一：單線條件分支", 
    "🔥🔥 遞迴挑戰二：雙重複合遞迴", 
    "👑 遞迴挑戰三：APCS 歷屆經典 - 費氏變形魔王題"
])

# ---- 遞迴挑戰一 ----
with r_tab1:
    st.markdown("**【題目】請仔細追蹤以下程式碼，請問 `print(mystery(7))` 最後的輸出為何？**")
    st.code(r"""
def mystery(n):
    if n <= 2:
        return n
    if n % 2 == 0:
        return n + mystery(n - 1)
    else:
        return mystery(n - 2)

print(mystery(7))
""", language="python")

    rq1_ans = st.radio(
        "請選擇答案：",
        ["(A) 7", "(B) 1", "(C) 12", "(D) 14"],
        index=None,
        key="rq1"
    )
    if rq1_ans:
        if rq1_ans.startswith("(B)"):
            st.success("🎉 答對了！單線追蹤非常細心！")
            st.markdown(r"""💡 **人肉電腦追蹤歷程：**
* 呼叫 `mystery(7)`：7 是奇數 $\rightarrow$ 執行 `mystery(7 - 2)`，意即要求 `mystery(5)`
* 呼叫 `mystery(5)`：5 是奇數 $\rightarrow$ 執行 `mystery(5 - 2)`，意即要求 `mystery(3)`
* 呼叫 `mystery(3)`：3 是奇數 $\rightarrow$ 執行 `mystery(3 - 2)`，意即要求 `mystery(1)`
* 呼叫 `mystery(1)`：滿足 `1 <= 2`，**終止條件觸發**，回傳 `1`。
* **回溯開始：**
    * `mystery(3)` 得到 `mystery(1)` 的結果 $\rightarrow$ 回傳 `1`
    * `mystery(5)` 得到 `mystery(3)` 的結果 $\rightarrow$ 回傳 `1`
    * `mystery(7)` 得到 `mystery(5)` 的結果 $\rightarrow$ 回傳 `1`？")
        else:
            st.error("❌ 答錯囉！再檢查一次有沒有任何一條路徑有執行到『 n + 』的動作？")

# ---- 遞迴挑戰二 ----
with r_tab2:
    st.markdown("**【題目】請仔細追蹤以下程式碼，請問最後輸出的變數 `ans` 值為何？**")
    st.code(r"""
def g(x, y):
    if x <= 0 or y <= 0:
        return 1
    if x > y:
        return g(x - 1, y) + 2
    else:
        return g(x, y - 2) + 1

ans = g(3, 2)
print(ans)
""", language="python")

    rq2_ans = st.radio(
        "請選擇答案：",
        ["(A) 4", "(B) 5", "(C) 6", "(D) 7"],
        index=None,
        key="rq2"
    )
    if rq2_ans:
        if rq2_ans.startswith("(A)"):
            st.success("🎉 答對了！雙參數遞迴追蹤非常精準！")
            st.markdown(r"""💡 **人肉電腦追蹤歷程：**
1. `g(3, 2)`：因為 $3 > 2$ (x > y)，執行 `g(2, 2) + 2`
2. `g(2, 2)`：因為 $2 \ngtr 2$ (不滿足 x > y)，執行 `g(2, 0) + 1`
3. `g(2, 0)`：滿足終止條件 `y <= 0`，直接回傳 `1`。
4. **開始往上回溯計算：**
    * `g(2, 2)` = `g(2, 0) + 1` $\rightarrow 1 + 1 = 2$
    * `g(3, 2)` = `g(2, 2) + 2` $\rightarrow 2 + 2 = 4$？
    * 答案為 4。(A)""")
        else:
            st.error("❌ 答錯囉！請拿紙筆把 (x, y) 的數值變化紀錄下來，看清楚每一次是滿足哪一個 if 條件。")

# ---- 遞迴挑戰三 ----
with r_tab3:
    st.markdown("**【題目】本題為真實 APCS 觀念題超級大魔王（費氏數列雙向分支變形）。請精準計算 `ans` 的值：**")
    st.code(r"""
count = 0

def fib_style(n):
    global count
    count += 1  # 每次進入函式，計數器就 +1
    if n <= 1:
        return n
    return fib_style(n - 1) + fib_style(n - 2)

ans = fib_style(4)
print(count) # 請問這裡印出的 count（函式被呼叫的總次數）是多少？
""", language="python")

    rq3_ans = st.radio(
        "請選擇答案：",
        ["(A) 5 次", "(B) 7 次", "(C) 9 次", "(D) 15 次"],
        index=None,
        key="rq3"
    )
    if rq3_ans:
        if rq3_ans.startswith("(C)"):
            st.success("🎉 太神了！您已經具備 APCS 觀念題頂尖高手的實力了！")
            st.markdown(r"""💡 **樹狀圖完全拆解歷程：**
這種雙向呼叫的題目，必須在紙上畫出**「呼叫樹（Execution Tree）」**，每一個節點就是一次呼叫（count +1）：
    * `f(4)`
      ├── `f(3)`
      │    ├── `f(2)`
      │    │    ├── `f(1)` (終止)
      │    │    └── `f(0)` (終止)
      │    └── `f(1)` (終止)
      └── `f(2)`
           ├── `f(1)` (終止)
           └── `f(0)` (終止)
* **總節點大清點：**
    * `f(4)`：1 次
    * `f(3)`：1 次
    * `f(2)`：共出現 2 次
    * `f(1)`：共出現 3 次
    * `f(0)`：共出現 2 次
    * 總呼叫次數 = $1 + 1 + 2 + 3 + 2 = 9$ 次！
* 因此 `count` 的總數就是 **9**。答案選 (C)。""")
        else:
            st.error("❌ 差一點點！這題是雙向擴散，呼叫次數成長得非常快，請務必在紙上完整畫出樹狀圖才不會漏數喔！")

# ==========================================
# 課程收尾
# ==========================================
st.divider()
st.subheader("🏁 第十課章節總結")
st.info("""
恭喜各位同學！學會了**函式與遞迴**，你已經從「寫一行算一行」的初學者，進化為具備「架構設計能力」的工程師了。
在競賽中，善用函式可以幫你把複雜的題目（例如：大富翁模擬、走迷宮）拆解成小零件，逐一擊破。
本章的進階作業：請試著去思考「費氏數列 (Fibonacci)」如何用遞迴表達，我們下堂課見！
""")
