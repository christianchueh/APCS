import streamlit as st

st.set_page_config(page_title="第四課：for 迴圈與重複結構", page_icon="🔁", layout="wide")

st.title("🔁 第四課：讓電腦當苦工——for 迴圈與重複結構")
st.caption("授課教師：闕河正 老師")
st.markdown("---")

# ==========================================
# 知識點 1：range() 函式全解析
# ==========================================
with st.expander("🧭 知識點一：自動數數機——range() 函式的三大密碼", expanded=True):
    st.markdown("""
    當我們想要讓程式重複執行某些事情時，我們需要給它一個「範圍」。
    Python 內建的 `range()` 函式就像一個自動數數機，它的語法結構是：`range(起始值, 結束值, 跳幾格)`。
    
    ### 🚨 全班注意！`range()` 的終極陷阱：**「顧前不顧後」**
    `range(start, end)` 產生的數字數到 `end` 的**前一個**就會緊急煞車！絕對不會包含 `end` 本身！
    """)
    
    # 使用 st.table 展現各種正著來、倒著來、跳著來的精準對照
    st.markdown("##### 📊 range() 各種切法對照表")
    st.table([
        {"呼叫方式": "單一參數：range(5)", "數出來的數字": "0, 1, 2, 3, 4", "注意事項": "省略起始值時，預設從 0 開始！結束在 5 的前一個。"},
        {"呼叫方式": "正著來：range(2, 6)", "數出來的數字": "2, 3, 4, 5", "注意事項": "從 2 開始，到 6 的前一個（就是 5）。"},
        {"呼叫方式": "跳著來：range(1, 10, 2)", "數出來的數字": "1, 3, 5, 7, 9", "注意事項": "從 1 開始，每次加 2，到 10 之前停下（公差為 2 的等差數列）。"},
        {"呼叫方式": "倒著來：range(5, 0, -1)", "數出來的數字": "5, 4, 3, 2, 1", "注意事項": "大數到小數！從 5 開始扣，每次減 1，到 0 的前一個（就是 1）煞車。"},
        {"呼叫方式": "倒著跳：range(10, 2, -3)", "數出來的數字": "10, 7, 4", "注意事項": "從 10 開始扣，每次減 3，下一個是 1 已經超出範圍，故不包含。"}
    ])
    
    # --- 閱讀練習題區 ---
    st.markdown("---")
    st.markdown("### 📝 `range()` 數數能力即時測驗")
    st.write("請試著在腦中想出這台數數機會吐出什麼數字，再點開解答核對：")
    
    rq1, rq2, rq3 = st.tabs(["📌 數數題 一", "📌 數數題 二", "📌 數數題 三"])
    with rq1:
        st.markdown("**題目：`list(range(4, 12, 3))` 會產生哪些數字？**")
        with st.expander("👀 查看解答"):
            st.success("**答案：[4, 7, 10]**")
            st.caption("分析：從 4 開始，每次加 3 👉 4, 7, 10。下一個是 13，已經超過或等於結束值 12，所以不列入。")
    with rq2:
        st.markdown("**題目：`list(range(6, 2, -1))` 會產生哪些數字？**")
        with st.expander("👀 查看解答"):
            st.success("**答案：[6, 5, 4, 3]**")
            st.caption("分析：倒著數，從 6 開始往下扣。結束值是 2，因為顧前不顧後，所以扣到 3 就停了。")
    with rq3:
        st.markdown("**題目：`list(range(1, 5, -1))` 會產生哪些數字？**")
        with st.expander("👀 查看解答"):
            st.error("**答案：[ ] (空清單，什麼都沒有)**")
            st.caption("分析：大陷阱！起點是 1，終點是 5，但步伐卻要求往後扣（-1）。1 往下扣只會離 5 越來越遠，程式發現不合邏輯，所以直接產生空的範圍。")

# ==========================================
# 知識點 2：for 迴圈搭配 range 運算
# ==========================================
with st.expander("🧭 知識點二：for 迴圈的搬運魔法與累加/累乘技術"):
    st.markdown("""
    `for` 迴圈的基本語法是：
    ```python
    for i in range(範圍):
        # 這裡是要重複做的事情
    ```
    它就像一個指派任務。`for i in range(3)` 代表讓變數 `i` 輪流當作 0, 1, 2，並把裡面的程式碼重複執行 3 次。
    """)
    
    # 示範基礎累加、等差累加、累乘
    st.markdown("### 📄 三大必練基本功程式碼")
    code1, code2, code3 = st.columns(3)
    
    with code1:
        st.subheader("1️⃣ 累加 1 加到 10")
        st.code("""
total = 0
for i in range(1, 11):
    total += i
print(total) # 輸出 55
        """, language="python")
        
    with code2:
        st.subheader("2️⃣ 累加 1, 3, 5 ... 到 31")
        st.code("""
total = 0
for i in range(1, 32, 2):
    total += i
print(total) # 輸出 256
        """, language="python")
        
    with code3:
        st.subheader("3️⃣ 階乘：累乘 1 到 8")
        st.code("""
ans = 1  # 注意：累乘初始值必須是 1！
for i in range(1, 9):
    ans *= i
print(ans) # 輸出 40320
        """, language="python")

    # --- 戰場解題串接區 ---
    st.markdown("---")
    st.markdown("### 🏆 實戰特訓：ZeroJudge 基礎迴圈題庫（含經典 N 次結構）")
    st.write("在 APCS 中，最常見的題目結構就是：**「第一行給一個數字 N，代表接下來有 N 行資料要處理」**。我們直接用 `for i in range(N)` 就能完美控制！")
    
    loop_t1, loop_t2, loop_t3, loop_t4, loop_t5, loop_t6 = st.tabs([
        "b971. 等差數列", "a005. Eva的作業", "m448. n顆星星", "c418. 左下三角", "c419. 右下三角", "c420. bert三角形"
    ])
    
    with loop_t1:
        st.markdown("[🔗 b971. 等差數列的一項](https://zerojudge.tw/ShowProblem?problemid=b971)")
        st.info("💡 闕老師提示：輸入首項、末項、公差。這題可以直接丟進 `range(首項, 末項 + 方向調整, 公差)` 裡面。注意公差可能是負的，結束值要小心設計！")
    with loop_t2:
        st.markdown("[🔗 a005. Eva 的回家作業](https://zerojudge.tw/ShowProblem?problemid=a005)")
        st.warning("🔥 經典的「重複 N 次」結構題！")
        st.info("💡 闕老師提示：先讀入一個數字 N，代表有幾組作業。接著用 `for i in range(N):` 連續讀取四個數字，判斷是等差數列還是等比數列，算出第五項並印出。")
    with loop_t3:
        st.markdown("[🔗 m448. n顆星星](https://zerojudge.tw/ShowProblem?problemid=m448)")
        st.info("💡 闕老師提示：輸入整數 n，利用 `for` 迴圈連續印出 n 個星星。在 Python 裡，`print('*' * i)` 會有奇效喔！")
    with loop_t4:
        st.markdown("[🔗 c418. 📊 雙重迴圈圖形題(一)](https://zerojudge.tw/ShowProblem?problemid=c418)")
        st.info("💡 闕老師提示：直角三角形圖形。第 1 行印 1 顆，第 2 行印 2 顆... 第 n 行印 n 顆。利用單層迴圈配合字串乘法，或雙層迴圈控制即可。")
    with loop_t5:
        st.markdown("[🔗 c419. 📊 雙重迴圈圖形題(二)](https://zerojudge.tw/ShowProblem?problemid=c419)")
        st.info("💡 闕老師提示：右下角的直角三角形。第 i 行需要先印出 `n - i` 個空白，再印出 `i` 個星星。考驗學生對規律的觀察！")
    with loop_t6:
        st.markdown("[🔗 c420. 📊 bert三角形](https://zerojudge.tw/ShowProblem?problemid=c420)")
        st.info("💡 闕老師提示：經典的金字塔型三角形。每一行的星星數是奇數（1, 3, 5...），前面要墊適當數量的空白。這題能做出來，學生的圖形迴圈邏輯就完全通了！")

# ==========================================
# 知識點 3：break 與 continue
# ==========================================
with st.expander("🧭 知識點三：控制迴圈的煞車與油門——break 與 continue"):
    st.markdown("""
    在迴圈執行的過程中，如果遇到突發狀況，我們可以用這兩個關鍵字來改變迴圈的命運：
    * **`break`（急煞車）**：**徹底結束**整個迴圈，直接跳出迴圈外。
    * **`continue`（跳過這回合）**：**只結束這一次**執行，不管後面還沒寫的程式，直接回到迴圈開頭準備數下一個數字。
    """)
    
    # 用表格清晰對照兩者的差別
    st.table([
        {"關鍵字": "break", "功能說明": "毀滅整個迴圈", "實際行為": "一看到它，後面所有次數都不數了，迴圈原地解散。"},
        {"關鍵字": "continue", "功能說明": "跳過本回合", "實際行為": "一看到它，本回合後面的程式碼不做了，立刻進入下一個數字的計數。"}
    ])
    
    # --- 戰場解題串接區 ---
    st.markdown("---")
    st.markdown("### 🏆 實戰特訓：ZeroJudge 條件跳出題庫")
    
    bc_t1, bc_t2, bc_t3 = st.tabs(["e621. 免費停車", "f043. 小豪的回家作業", "f373. 週年慶"])
    with bc_t1:
        st.markdown("[🔗 e621. 免費停車 (Free Parking)](https://zerojudge.tw/ShowProblem?problemid=e621)")
        st.info("💡 闕老師提示：要在 A 到 B 的範圍內找出「不能被 C 整除」的數字。我們可以用 `for i in range(A+1, B):` 走訪，如果 `i % C == 0` 代表能整除，立刻用 `continue` 跳過，剩下的就是答案！")
    with bc_t2:
        st.markdown("[🔗 f043. 小豪的回家作業(Homework)](https://zerojudge.tw/ShowProblem?problemid=f043)")
        st.info("💡 闕老師提示：找出兩個數相加等於 R。我們可以用迴圈去枚舉其中一個數，並利用條件篩選出最符合題目答案大小要求的組合，適時使用 `break` 提高運算效率。")
    with bc_t3:
        st.markdown("[🔗 f373. 週年慶 Anniversary](https://zerojudge.tw/ShowProblem?problemid=f373)")
        st.info("💡 闕老師提示：比較兩種折價方案哪一種便宜。利用迴圈和條件式計算出最終金額後，進行大小比較輸出正確答案。")

# ==========================================
# 知識點 4：APCS 核心戰略：找反例（Flag 旗標法）
# ==========================================
with st.expander("🧭 知識點四：🔥 APCS 高階核心技術：找反例比證明全對快十倍！（Flag 旗標法）"):
    st.markdown("""
    在檢定題中，我們常常需要確認**「一整排資料是不是都符合某個規則」**。
    例如：檢查全班是不是「所有人」都及格？
    
    **❌ 錯誤邏輯（初學者常犯）：** 一看到及格就說全班及格。這不對！因為後面可能有人不及格。
    **🧠 頂尖選手的戰略邏輯：** 先「假設全班都及格」，然後只要在迴圈裡抓到**「任何一個不及格的反例」**，就可以直接一槌定音：「全班沒有都及格！」並立刻 `break` 離開。
    
    這個用來做標記的箱子（變數），在程式設計中我們叫做 **Flag（旗標變數）**。
    
    ### 🎯 實戰示範一：檢查陣列裡是不是「全部都是奇數」？
    """)
    
    st.code("""
nums = [3, 7, 9, 12, 5, 11]

all_odd = True  # 第一步：先樂觀假設「全都是奇數」

for i in range(len(nums)):
    if nums[i] % 2 == 0:  # 抓到了！這傢伙是偶數（反例）
        all_odd = False   # 旗標倒下，假設破滅
        break             # 既然都破滅了，後面不用看了，直接結束迴圈

if all_odd == True:
    print("這串數字全部都是奇數！")
else:
    print("抓到內鬼了，裡面有偶數！")
    """, language="python")
    
    st.markdown("""
    ### 🎯 實戰示範二：APCS 必考題——判斷質數 (Prime Number)
    要怎麼知道一個數字 `N` 是不是質數？
    **質數的定義**：除了 1 和自己以外，沒有任何人能整除它。
    **找反例策略**：我們讓迴圈從 `2` 數到 `N-1`。只要中間有任何一個數字能整除 `N`（抓到反例了！），它就絕對不是質數！
    """)
    st.code("""
N = 37
is_prime = True # 先假設它是質數

for i in range(2, N):
    if N % i == 0:  # 竟然有人能整除它！抓到反例了！
        is_prime = False # 假設破滅，它不是質數
        break

if is_prime:
    print(f"{N} 是一個質數")
else:
    print(f"{N} 只是普通的合數")
    """, language="python")

# ==========================================
# 知識點 5：多重迴圈與變數牽引追蹤
# ==========================================
with st.expander("🧭 知識點五：迴圈中的迴圈——多重迴圈與 i、j 人肉追蹤術"):
    st.markdown("""
    當外層迴圈走一步，內層迴圈就必須「把它的範圍全部數完一遍」。這在處理 2D 平面規律或是矩陣時非常常見。
    我們來看這段经典的 `i` 與 `j` 互相牽引的程式碼：
    """)
    
    st.code("""
for i in range(1, 4):
    for j in range(1, i + 1):  # 內層的結束值被外層的 i 控制了！
        print(f"({i},{j})", end=" ")
    print() # 換行
    """, language="python")
    
    st.markdown("""
    ### 💻 人肉電腦追蹤軌跡（訓練學生的邏輯追蹤能力）
    請全班同學跟著老師一行一行看，這就是電腦大腦運作的軌跡：
    """)
    
    # 用極為整齊的表格呈現追蹤過程，保證不跑版
    st.table([
        {"外層 i 的值": "i = 1", "內層 j 的範圍 (range(1, i+1))": "range(1, 2) 👉 只數出 1", "畫面印出的結果": "(1,1)"},
        {"外層 i 的值": "i = 2", "內層 j 的範圍 (range(1, i+1))": "range(1, 3) 👉 數出 1, 2", "畫面印出的結果": "(2,1) (2,2)"},
        {"外層 i 的值": "i = 3", "內層 j 的範圍 (range(1, i+1))": "range(1, 4) 👉 數出 1, 2, 3", "畫面印出的結果": "(3,1) (3,2) (3,3)"}
    ])
    
    # --- 嵌套迴圈高難度閱讀題 ---
    st.markdown("---")
    st.markdown("### 📝 多重迴圈高階閱讀練習題")
    
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
        st.markdown("**題目：這段程式碼會印出什麼圖形？（注意 `end=""` 代表不換行）**")
        st.code("""
for i in range(3, 0, -1):
    for j in range(i):
        print("#", end="")
    print()
        """, language="python")
        with st.expander("👀 查看人肉電腦分析解答"):
            st.success("**答案：一個倒三角形**")
            st.code("""
###
##
#
            """, language="text")
            st.caption("分析：i 分別是 3, 2, 1。所以第一行內層印 3 個 #，第二行印 2 個 #，第三行印 1 個 #。")

# ==========================================
# 課程收尾
# ==========================================
st.divider()
st.subheader("🏁 第四課章節總結與作業指引")
st.success("""
太厲害了！恭喜大家完成了程式設計中最關鍵的「重複結構」特訓。
結合了第三課的**陣列索引**與本課的**for迴圈**，你已經能寫出為全校成績進行排序、篩選質數、甚至繪製幾何圖形的複雜演算法。
**本週挑戰作業：** 請各位同學務必點擊挑戰 **c420. bert三角形** 與 **a005. Eva的回家作業**。這兩題能順利解出綠燈，你的迴圈結構觀念就非常紮實了！
""")
