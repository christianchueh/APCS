import streamlit as st

st.set_page_config(page_title="第二課：條件式與流程控制", page_icon="⚖️", layout="wide")

st.title("⚖️ 第二課：讓程式學會做選擇——條件式與流程控制")
st.caption("授課教師：闕河正 老師")
st.markdown("---")

# ==========================================
# 知識點 0：補充說明複合指定運算子
# ==========================================
with st.expander("🧭 知識點零：程式碼的縮寫魔法——複合指定運算子", expanded=True):
    st.markdown("""
    在寫程式時，我們經常需要「讓變數自己加減乘除」。例如：`count = count + 1`（把原本的箱子拿出來加 1 再放回去）。
    因為這種寫法太常用了，Python 提供了超方便的**縮寫魔法（複合指定運算子）**：
    """)
    
    st.table([
        {"完整寫法": "x = x + 2", "縮寫寫法": "x += 2", "含意": "x 自己加 2"},
        {"完整寫法": "x = x - 3", "縮寫寫法": "x -= 3", "含意": "x 自己減 3"},
        {"完整寫法": "x = x * 5", "縮寫寫法": "x *= 5", "含意": "x 自己乘以 5"},
        {"完整寫法": "x = x // 2", "縮寫寫法": "x //= 2", "含意": "x 自己整除 2"},
        {"完整寫法": "x = x % 10", "縮寫寫法": "x %= 10", "含意": "x 自己取 10 的餘數"},
    ])
    
    st.markdown("##### 📄 程式小體驗")
    st.code("""
score = 60
score += 10  # score 變成 70
score *= 2   # score 變成 140
    """, language="python")

# ==========================================
# 知識點 1：流程圖與循序結構
# ==========================================
with st.expander("🧭 知識點一：像高鐵一樣一路到底——循序結構"):
    st.markdown("""
    在第一課中，我們寫的所有程式都是**「循序結構 (Sequential Structure)」**。
    意思是電腦會**從第一行開始，毫無懸念地、由上而下、一行一行執行到最後一行**，中間不會轉彎，也不會回頭。
    
    ##### 📊 循序結構流程圖 (Flowchart)
    """)
    
    # 使用新版 Markdown 區塊渲染 Mermaid 流程圖
    st.markdown("""
    ```mermaid
    graph TD
        A([開始]) --> B[輸入資料 st.text_input]
        B --> C[數學計算 int/運算子]
        C --> D[輸出結果 st.write]
        D --> E([結束])
        style A fill:#bfff00,stroke:#333,stroke-width:2px,color:#000
        style E fill:#bfff00,stroke:#333,stroke-width:2px,color:#000
    ```
    """)

# ==========================================
# 知識點 2：布林值變數與其用途
# ==========================================
with st.expander("🧭 知識點二：非黑即白的世界——布林值 (Boolean)"):
    st.markdown("""
    在現實世界中，有很多問題的答案只有兩種可能：對或錯、是或非。
    在 Python 中，這種「只有兩種狀態」的資料型態叫做 **布林值 (Boolean)**：
    * **`True`** （代表「真」、正確、成立）
    * **`False`**（代表「偽」、錯誤、不成立）
    
    *注意：T 和 F 必須大寫，而且不需要加引號！*
    
    ##### 🎯 布林值的用途：
    它是轉向開關！電腦就是透過判斷一個箱子裡是 `True` 還 `False`，來決定接下來程式要往左邊走還是往右邊走。
    """)
    
    # 互動展示關係運算子
    st.markdown("##### 🔬 關係運算子體驗（他們算出來的結果就是布林值！）")
    user_age = st.number_input("請輸入你的年齡：", value=18, step=1)
    
    is_adult = user_age >= 18
    st.write(f"👉 程式執行 `user_age >= 18` 的結果是：`{is_adult}` (型態：Boolean)")

# ==========================================
# 知識點 3-1：邏輯運算子
# ==========================================
with st.expander("🧭 知識點三(上)：複合條件的黏著劑——邏輯運算子 (Logical Operators)"):
    st.markdown("""
    當我們有兩個以上的條件要同時判斷時（例如：滿 18 歲 **且** 帶身分證），就需要邏輯運算子：
    1.  **`and` (且)**：所有條件都必須是 `True`，結果才是 `True`。（只要有一個錯，就全錯）
    2.  **`or` (或)**：只要其中一個條件是 `True`，結果就是 `True`。（只要有一個對，就過關）
    3.  **`not` (非)**：顛倒黑白。`not True` 會變成 `False`；`not False` 變成 `True`。
    """)
    
    # 互動表格感受邏輯閘
    st.markdown("##### 🎛️ 邏輯運算子即時測試")
    c1 = st.checkbox("條件 A (True / False)")
    c2 = st.checkbox("條件 B (True / False)")
    
    col_l, col_r = st.columns(2)
    with col_l:
        st.info(f"🟢 `A and B` 的結果為：`{c1 and c2}`")
    with col_r:
        st.info(f"🔵 `A or B` 的結果為：`{c1 or c2}`")

# ==========================================
# 知識點 3-2：單向條件式與 ZeroJudge 實作
# ==========================================
with st.expander("🧭 知識點三(下)：如果...就...——單向條件式 (If)"):
    st.markdown("""
    當滿足某個條件時，程式才去執行特定的事；如果不滿足，就當作沒這回事直接跳過。
    
    ##### 📊 單向條件式流程圖
    """)
    
    st.markdown("""
    ```mermaid
    graph TD
        A[檢查條件 Condition] -- True --> B[執行特定程式碼區塊]
        A -- False --> C[繼續往下走]
        B --> C
        style A fill:#fffa00,stroke:#333,color:#000
    ```
    """)
    
    st.markdown("""
    ##### 📄 真實程式範例：
    Python 語法中，`if` 後面要加冒號 `:`，且接下來要做的事情**必須縮排（按 Tab 鍵空四格）**！
    """)
    st.code("""
# 如果分數小於 60 分，就說需要加把勁
score = 55
if score < 60:
    print("需要加把勁喔！")
print("成績檢查完畢")
    """, language="python")
    
    # --- ZeroJudge 題目串接區 ---
    st.markdown("---")
    st.markdown("### 🏆 APCS 練兵場：ZeroJudge 單向條件式經典題庫")
    st.write("請同學們點擊下方題目連結，並在解題系統中嘗試用今天學到的 `if` 來解題！")
    
    zj_a799, zj_d050, zj_d063, zj_d064, zj_d068 = st.tabs([
        "1. 正值國 (a799)", "2. 妳那裡幾點 (d050)", "3. 0 與 1 (d063)", "4. ㄑ一ˊ數 (d064)", "5. 該減肥了 (d068)"
    ])
    
    with zj_a799:
        st.markdown("[🔗 前往題目：a799. 正值國](https://zerojudge.tw/ShowProblem?problemid=a799)")
        st.info("💡 闕老師提示：輸入一個整數，如果是負數就把它乘以 -1 變成正數再印出。這就是最標準的單向 `if` 應用！")
        
    with zj_d050:
        st.markdown("[🔗 前往題目：d050. 妳那裡幾點](https://zerojudge.tw/ShowProblem?problemid=d050)")
        st.info("💡 闕老師提示：美國時間比台灣慢 15 小時。如果減完 15 小時後小於 0，要記得補 24 小時回來喔！")
        
    with zj_d063:
        st.markdown("[🔗 前往題目：d063. 0 與 1](https://zerojudge.tw/ShowProblem?problemid=d063)")
        st.info("💡 闕老師提示：輸入 0 要變 1，輸入 1 要變 0。試試看用 `if` 來重新指定變數的值。")
        
    with zj_d064:
        st.markdown("[🔗 前往題目：d064. ㄑ一ˊ數](https://zerojudge.tw/ShowProblem?problemid=d064)")
        st.info("💡 闕老師提示：運用第一課學到的 `% 2`（取 2 的餘數）。如果餘數是 1，就是奇數（Odd）！")
        
    with zj_d068:
        st.markdown("[🔗 前往題目：d068. 該減肥了](https://zerojudge.tw/ShowProblem?problemid=d068)")
        st.info("💡 闕老師提示：如果體重超過 50 公斤，就讓體重 `-= 1`。最後再把體重印出來。")

# ==========================================
# 知識點 4：雙向與多向條件式
# ==========================================
with st.expander("🧭 知識點四：人生不是二分法——雙向 (If-Else) 與多向 (If-Elif-Else) 條件式"):
    st.markdown("""
    * **雙向條件式 (if...else)**：非 A 即 B，如果條件成立做這件事，**否則 (else)** 做另一件事。
    * **多向條件式 (if...elif...else)**：多重選擇，當第一個條件不符合時，再檢查第二個條件 (`elif`)。
    
    ##### 📊 多向條件式流程圖
    """)
    
    st.markdown("""
    ```mermaid
    graph TD
        A[條件 1 成立?] -- Yes --> B[執行區塊 1]
        A -- No --> C[條件 2 成立?]
        C -- Yes --> D[執行區塊 2]
        C -- No --> E[執行最終 else 區塊]
        B --> F[繼續往下執行]
        D --> F
        E --> F
        style A fill:#ff9900,stroke:#333,color:#fff
        style C fill:#ff9900,stroke:#333,color:#fff
    ```
    """)
    
    st.markdown("##### 📄 真實程式範例：成績評等")
    st.code("""
score = 85
if score >= 90:
    print("A 等級")
elif score >= 80:
    print("B 等級")
else:
    print("C 等級")
    """, language="python")
    
    # --- 關鍵技術解說：多變數輸入 ---
    st.error("🔑 APCS 解題必備核心技術：如何在同一行讀取多個數字？")
    st.markdown("""
    在接下來的檢定題中，經常會遇到同一行測資用空格隔開兩個數字（例如輸入：`13 25`）。
    請全班同學把這行指令記在小本本上，這是未來解題的固定公式：
    """)
    st.code("x, y = [int(i) for i in input().split()]", language="python")
    st.caption("它的意思是：把一整行字串用空格切開 (split)，把切開的每個碎塊強迫轉成整數 (int)，最後分別丟給變數 x 和 y。")

    # --- ZeroJudge 進階題目串接區 ---
    st.markdown("---")
    st.markdown("### 🏆 APCS 進階練兵場：ZeroJudge 多向條件式題庫")
    
    zj_a053, zj_b758, zj_b877, zj_c636 = st.tabs([
        "1. 得分計分 (a053)", "2. 牛仔很忙 (b758)", "3. 我是電視迷 (b877)", "4. 十二生肖 (c636)"
    ])
    
    with zj_a053:
        st.markdown("[🔗 前往題目：a053. 得分計分](https://zerojudge.tw/ShowProblem?problemid=a053)")
        st.info("💡 闕老師提示：這題是經典的階梯式計分。需要用 `elif` 去細分：1-10題、11-20題、21-40題與40題以上的不同給分邏輯。")
        
    with zj_b758:
        st.markdown("[🔗 前往題目：b758. 牛仔很忙](https://zerojudge.tw/ShowProblem?problemid=b758)")
        st.warning("🔥 注意：本題會在一行內輸入兩個數字，請務必使用上面教的 `x, y = [int(i) for i in input().split()]` 指令來接收喔！")
        st.info("💡 闕老師提示：牛仔辦案需要 2 小時 30 分。將現在的小時加上 2，分鐘加上 30。如果分鐘滿 60 要進位到小時；如果小時滿 24 點要記得歸零！")
        
    with zj_b877:
        st.markdown("[🔗 前往題目：b877. 我是電視迷](https://zerojudge.tw/ShowProblem?problemid=b877)")
        st.info("💡 闕老師提示：電視台只有 0 到 99 台。如果從 A 台到 B 台是順向，直接 `B - A`；如果跨越了 100 台的循環（例如從 90 台轉到 10 台），要想一下怎麼用 `if-else` 或 `%` 來處理距離！")
        
    with zj_c636:
        st.markdown("[🔗 前往題目：c636. 十二生肖](https://zerojudge.tw/ShowProblem?problemid=c636)")
        st.info("💡 闕老師提示：民國年與生肖具有週期性。利用 `(民國年 - 1) % 12` 或類似的餘數計算，再搭配長長的 `if...elif...elif...else` 就能把對應的生肖印出來囉！")

# ==========================================
# 課程收尾
# ==========================================
st.divider()
st.subheader("🏁 第二課成果驗收與 APCS 邏輯思維建立")
st.success("""
太棒了！你已經解開了程式從「直線思考」走向「具備決策能力」的封印。
在 APCS 的第一題（基礎題）中，幾乎 100% 都需要運用這一課所學到的 `if-elif-else` 來進行資料的分類與統計。
""")

st.info("""
### 🧠 本週思維挑戰（挑戰 ZeroJudge 滿分）
今天我們給出的幾道題目（如牛仔很忙、電視迷），雖然看起來是生活日常，但本質上都是在考驗你對**「數字循環（餘數觀念）與邊界條件（if 判斷點）」**的敏銳度。回家請務必上 ZeroJudge 註冊帳號，並將這幾道題目刷出綠色的 **AC (Accepted)** 標籤！
""")
