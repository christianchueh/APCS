import streamlit as st

st.set_page_config(page_title="第二課：條件式與流程控制", page_icon="⚖️", layout="wide")

st.title("⚖️ 第二課：讓程式學會做選擇——條件式與流程控制")
st.caption("授課教師：闕河正 老師")
st.markdown("---")

# ==========================================
# 知識點 0：複合指定運算子（已擴充 Tabs 互動魔鬼閱讀題）
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

    # ---------------------------------------------------------
    # 新增：APCS 縮寫與優先權魔鬼特訓區（使用 Tabs 呈現）
    # ---------------------------------------------------------
    st.markdown("---")
    st.markdown("### 🧠 APCS 觀念奠基：複合指定算式魔鬼特訓")
    st.warning("💡 **闕老師的破題金鑰**：看到 `x *= 算式` 時，右手邊的算式永遠被視為**「有一個隱形的括號」**！一定要把右邊全部算完，最後才能跟 `x` 進行 `*=` 運算！")
    
    # 建立 Tabs 閱讀題
    tab_q1, tab_q2, tab_q3 = st.tabs(["🔥 挑戰一：減法優先權陷阱", "🔥🔥 挑戰二：連鎖四則運算", "💀 挑戰三：APCS 終極大魔王"])
    
    # --- 挑戰一 ---
    with tab_q1:
        st.markdown("##### 📝 閱讀思考題：`x *= 3 - 1`")
        st.code("""
x = 5
x *= 3 - 1
print(x)
        """, language="python")
        
        q0_1 = st.radio("請問最終印出的 `x` 是多少？", ["14", "10", "2", "15"], key="q0_1")
        
        with st.expander("🔍 查看【挑戰一解析與答案】"):
            st.write("**正確答案：`10`**")
            st.markdown("""
            > **常見錯誤**：很多同學會直覺從左到右算，變成 `x * 3 - 1` $\rightarrow$ $5 \\times 3 - 1 = 14$。**這是大錯特錯的！**
            > 
            > **正確拆解步驟**：
            > 1. 複合指定運算子的右邊有隱形括號，所以原式等同於：`x = x * (3 - 1)`
            > 2. 先算括號右邊：$3 - 1 = 2$
            > 3. 最後拿 `x` 原本的值來乘：$5 \\times 2 = 10$
            """)

    # --- 挑戰二 ---
    with tab_q2:
        st.markdown("##### 📝 閱讀思考題：除法與整除混搭")
        st.code("""
x = 20
x //= 2 + 3 * 2
print(x)
        """, language="python")
        
        q0_2 = st.radio("請問最終印出的 `x` 是多少？", ["16", "2", "2.5", "1"], key="q0_2")
        
        with st.expander("🔍 查看【挑戰二解析與答案】"):
            st.write("**正確答案：`2`**")
            st.markdown("""
            > **正確拆解步驟**：
            > 1. 先把右邊視為一個整體：`x = x // (2 + 3 * 2)`
            > 2. 計算右邊的四則運算（先乘除後加減）：$3 \\times 2 = 6$，接著 $2 + 6 = 8$
            > 3. 最後拿 `x` 進行整除（只取商數）：$20 \\mathbin{//} 8 = 2 \\dots 4$，所以答案為 `2`。
            """)

    # --- 挑戰三 ---
    with tab_q3:
        st.markdown("##### 📝 閱讀思考題：APCS 模擬地獄題")
        st.code("""
x = 5
x *= 3 + 2 * 3 // (4 + 2 // 2)
print(x)
        """, language="python")
        
        q0_3 = st.radio("請問最終印出的 `x` 是多少？", ["20", "25", "45", "30"], key="q0_3")
        
        with st.expander("🔍 查看【挑戰三解析與答案】"):
            st.write("**正確答案：`20`**")
            st.markdown("""
            > **別慌！我們一步一步像剝洋蔥一樣拆解右邊的算式：** `3 + 2 * 3 // (4 + 2 // 2)`
            > 
            > 1. **最內層括號優先**：`(4 + 2 // 2)` 
            >    * 先算裡面的整除：$2 \\mathbin{//} 2 = 1$
            >    * 括號內變成 $4 + 1 = 5$
            > 2. **原式簡化為**：`3 + 2 * 3 // 5`
            > 3. **處理同級的乘法與整除（由左至右）**：
            >    * 先算乘法：$2 \\times 3 = 6$
            >    * 再算整除：$6 \\mathbin{//} 5 = 1$ (商數為 1)
            > 4. **完成右側最後的加法**：$3 + 1 = 4$
            > 5. **最後大融合 (`*=`)**：`x = x * 4` $\rightarrow$ $5 \\times 4 = 20$
            """)


# ==========================================
# 知識點 1：流程圖與循序結構（已新增：循序式程式閱讀範例與追蹤特訓）
# ==========================================
with st.expander("🧭 知識點一：像高鐵一樣一路到底——循序結構"):
    st.markdown("""
    在第一課中，我們寫的所有程式都是**「循序結構 (Sequential Structure)」**。
    意思是電腦會**從第一行開始，毫無懸念地、由上而下、一行一行執行到最後一行**，中間不會轉彎，也不會回頭。
    
    ##### 📊 循序結構流程圖 (Flowchart)
    """)
    
    # 使用網頁最穩定的 CSS Flexbox 呈現純 HTML 循序流程圖
    st.components.v1.html("""
    <div style="display: flex; flex-direction: column; align-items: center; font-family: sans-serif; gap: 10px; padding: 10px;">
        <div style="background-color: #bfff00; border: 2px solid #333; padding: 8px 20px; border-radius: 20px; font-weight: bold; color: black;">開始</div>
        <div style="font-size: 18px; color: #555;">⬇️</div>
        <div style="background-color: #f0f2f6; border: 1px solid #ccc; padding: 10px 15px; border-radius: 4px; color: black; font-size: 14px;">輸入資料 (st.text_input)</div>
        <div style="font-size: 18px; color: #555;">⬇️</div>
        <div style="background-color: #f0f2f6; border: 1px solid #ccc; padding: 10px 15px; border-radius: 4px; color: black; font-size: 14px;">數學計算 (int / 運算子)</div>
        <div style="font-size: 18px; color: #555;">⬇️</div>
        <div style="background-color: #f0f2f6; border: 1px solid #ccc; padding: 10px 15px; border-radius: 4px; color: black; font-size: 14px;">輸出結果 (st.write)</div>
        <div style="font-size: 18px; color: #555;">⬇️</div>
        <div style="background-color: #bfff00; border: 2px solid #333; padding: 8px 20px; border-radius: 20px; font-weight: bold; color: black;">結束</div>
    </div>
    """, height=300)

    st.markdown("---")
    st.markdown("### 🔬 APCS 觀念奠基：循序式程式閱讀題（變數追蹤特訓）")
    st.markdown("請全班同學跟著電腦的腳步，**由上而下**一行行追蹤變數箱子裡的數值變化：")
    
    st.code("""
# 【程式追蹤範例】
a = 10      # 第一步：a 箱子放入 10
b = 5       # 第二步：b 箱子放入 5
a = a + b   # 第三步：把目前的 a(10) 和 b(5) 加起來得到 15，覆蓋回 a 箱子
b = a * 2   # 第四步：把最新更新的 a(15) 乘以 2 得到 30，放入 b 箱子
print(b)    # 第五步：印出最終的 b
    """, language="python")

    # 互動單選題讓學生動腦
    q_seq = st.radio(
        "🧠 請問這段程式碼最後執行到 `print(b)` 時，畫面上會印出什麼數字？", 
        ["10", "15", "20", "30"], 
        key="q_seq"
    )
    
    with st.expander("🔍 查看【循序結構解析與答案】"):
        st.write("**正確答案：`30`**")
        st.markdown("""
        > **闕老師碎碎念**：這就是標準的循序結構！
        > * 當執行到第四行 `b = a * 2` 時，第三行已經將 `a` 的值更新為 `15` 了。
        > * 電腦**絕對不可能**回頭去用第一行的 `a = 10` 來計算。記住，高鐵是不開倒車的！
        """)


# ==========================================
# 知識點 2：布林值變數與所有基礎比較運算子（已全面擴充比較運算子表）
# ==========================================
with st.expander("🧭 知識點二：非黑即白的世界——布林值 (Boolean) 與比較運算子"):
    st.markdown("""
    在現實世界中，有很多問題的答案只有兩種可能：對或錯、是或非。
    在 Python 中，這種「只有兩種狀態」的資料型態叫做 **布林值 (Boolean)**：
    * **`True`** （代表「真」、正確、成立）
    * **`False`**（代表「偽」、錯誤、不成立）
    
    *注意：T 和 F 必須大寫，而且不需要加引號！*
    
    ##### 🎯 布林值的用途：
    它是轉向開關！電腦就是透過判斷一個箱子裡是 `True` 還 `False`，來決定接下來程式要往左邊走還是往右邊走。
    """)
    
    # ---------------------------------------------------------
    # 擴充：所有基礎比較運算子表格
    # ---------------------------------------------------------
    st.markdown("### ⚖️ Python 六大基礎比較運算子（算出來一律是布林值）")
    st.warning("🔥 【超高頻考點】單等於 `=` 是「指定/裝箱」，雙等於 `==` 才是「檢查有沒有相等」！")
    
    st.table([
        {"運算子": "==", "功能": "檢查「等於」", "範例": "5 == 5 (True) / 5 == 3 (False)", "備註": "APCS 選擇題爆破大魔王"},
        {"運算子": "!=", "功能": "檢查「不等於」", "範例": "5 != 3 (True) / 5 != 5 (False)", "備註": "驚嘆號代表「不」"},
        {"運算元": ">", "功能": "大於", "範例": "10 > 3 (True)", "備註": "不包含等於"},
        {"運算元": "<", "功能": "小於", "範例": "3 < 10 (True)", "備註": "不包含等於"},
        {"運算元": ">=", "功能": "大於或等於", "範例": "18 >= 18 (True)", "備註": "只要滿足其中一個就成立"},
        {"運算元": "<=", "功能": "小於或等於", "範例": "15 <= 18 (True)", "備註": "只要滿足其中一個就成立"},
    ])
    
    # 互動展示關係運算子
    st.markdown("##### 🔬 關係運算子全套體驗（改動下方數字，觀察右側布林值變化！）")
    
    col_num1, col_num2 = st.columns(2)
    with col_num1:
        x_val = st.number_input("請輸入數字 X：", value=10, step=1)
    with col_num2:
        y_val = st.number_input("請輸入數字 Y：", value=20, step=1)
        
    st.markdown("**💻 電腦即時關係判斷報告：**")
    
    # 用表格或多欄位漂亮展現所有比較結果
    c1, c2, c3 = st.columns(3)
    with c1:
        st.info(f"🔹 `X == Y` $\\rightarrow$ `{x_val == y_val}`")
        st.info(f"🔹 `X != Y` $\\rightarrow$ `{x_val != y_val}`")
    with c2:
        st.info(f"🔹 `X > Y` $\\rightarrow$ `{x_val > y_val}`")
        st.info(f"🔹 `X < Y` $\\rightarrow$ `{x_val < y_val}`")
    with c3:
        st.info(f"🔹 `X >= Y` $\\rightarrow$ `{x_val >= y_val}`")
        st.info(f"🔹 `X <= Y` $\\rightarrow$ `{x_val <= y_val}`")


# ==========================================
# 知識點 3-1：邏輯運算子（已擴充至 8 題 Tabs 複合條件魔鬼特訓）
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

    # ---------------------------------------------------------
    # APCS 比較 x 邏輯運算子 8 題魔鬼特訓區（使用 Tabs 呈現）
    # ---------------------------------------------------------
    st.markdown("---")
    st.markdown("### 🧠 APCS 觀念奠基：比較 × 邏輯複合閱讀特訓（8題全開）")
    st.warning("💡 **闕老師的解題金鑰**：優先權順序為：`算術運算子` ➡️ `比較運算子` ➡️ `not` ➡️ `and` ➡️ `or`。由高到低，層層拆解！")

    # 建立 8 個 Tabs 閱讀題
    tabs = st.tabs([
        "💎 題一", "💎 題二", "💎 題三", "🔥 題四", 
        "🔥 題五", "🔥 題六", "💀 題七", "💀 題八"
    ])

    # --- 題一 ---
    with tabs[0]:
        st.markdown("##### 📝 閱讀思考題：`and` 的生死關頭")
        st.code("""
a = 10
b = 5
ans = (a > 5) and (b == 3)
print(ans)
        """, language="python")
        q3_1 = st.radio("請問最終印出的 `ans` 是什麼？", ["請選擇答案...", "True", "False", "10", "5"], key="q3_1")
        
        if q3_1 != "請選擇答案...":
            if q3_1 == "False":
                st.success("🎉 太棒了！答對了！")
            else:
                st.error("❌ 差一點點！再想想看？")
            with st.expander("🔍 查看【題一解析】"):
                st.write("**正確答案：`False`**")
                st.markdown("> **解析**：\n> 1. `a > 5` -> `10 > 5` 成立，得到 **`True`**。\n> 2. `b == 3` -> `5 == 3` 不成立，得到 **`False`**。\n> 3. `True and False` 結果為 **`False`**（`and` 只要有一邊錯就是錯）。")

    # --- 題二 ---
    with tabs[1]:
        st.markdown("##### 📝 閱讀思考題：`or` 的一線生機")
        st.code("""
score = 45
is_teacher_pet = True
pass_lesson = (score >= 60) or is_teacher_pet
print(pass_lesson)
        """, language="python")
        q3_2 = st.radio("請問最終印出的結果是什麼？", ["請選擇答案...", "True", "False", "45", "報錯（Error）"], key="q3_2")
        
        if q3_2 != "請選擇答案...":
            if q3_2 == "True":
                st.success("🎉 太棒了！答對了！")
            else:
                st.error("❌ 差一點點！再想想看？")
            with st.expander("🔍 查看【題二解析】"):
                st.write("**正確答案：`True`**")
                st.markdown("> **解析**：\n> 1. `score >= 60` -> `45 >= 60` 得到 **`False`**。\n> 2. `is_teacher_pet` 為 **`True`**。\n> 3. `False or True` 最終得到 **`True`**（`or` 只要有一邊對就全對）。")

    # --- 題三 ---
    with tabs[2]:
        st.markdown("##### 📝 閱讀思考題：`not` 的反轉魔法")
        st.code("""
age = 15
is_minor = not (age >= 18)
print(is_minor)
        """, language="python")
        q3_3 = st.radio("請問最終印出的結果是什麼？", ["請選擇答案...", "True", "False", "15", "18"], key="q3_3")
        
        if q3_3 != "請選擇答案...":
            if q3_3 == "True":
                st.success("🎉 太棒了！答對了！")
            else:
                st.error("❌ 差一點點！再想想看？")
            with st.expander("🔍 查看【題三解析】"):
                st.write("**正確答案：`True`**")
                st.markdown("> **解析**：\n> 1. 內層 `age >= 18` -> `15 >= 18` 得到 **`False`**。\n> 2. 外層 `not False` 反轉後得到 **`True`**。")

    # --- 題四 ---
    with tabs[3]:
        st.markdown("##### 📝 閱讀思考題：不等於 `!=` 的邏輯轉折")
        st.code("""
num = 12
result = (num % 3 != 0) or (num > 10)
print(result)
        """, language="python")
        q3_4 = st.radio("請問最終印出的結果是什麼？", ["請選擇答案...", "True", "False", "0", "12"], key="q3_4")
        
        if q3_4 != "請選擇答案...":
            if q3_4 == "True":
                st.success("🎉 太棒了！答對了！")
            else:
                st.error("❌ 差一點點！再想想看？")
            with st.expander("🔍 查看【題四解析】"):
                st.write("**正確答案：`True`**")
                st.markdown("> **解析**：\n> 1. `num % 3` 得到 `0`。比較算式 `0 != 0`（0不等於0）不成立，得到 **`False`**。\n> 2. 後半段 `num > 10` -> `12 > 10` 成立，得到 **`True`**。\n> 3. `False or True` 得到 **`True`**。")

    # --- 題五 ---
    with tabs[4]:
        st.markdown("##### 📝 閱讀思考題：Python 獨門絕活「連續比較」")
        st.code("""
x = 7
result = 5 < x < 10
print(result)
        """, language="python")
        q3_5 = st.radio("請問這段程式在 Python 中會如何？", ["請選擇答案...", "True", "False", "報錯（不允許連續比較）", "7"], key="q3_5")
        
        if q3_5 != "請選擇答案...":
            if q3_5 == "True":
                st.success("🎉 太棒了！答對了！")
            else:
                st.error("❌ 差一點點！再想想看？")
            with st.expander("🔍 查看【題五解析】"):
                st.write("**正確答案：`True`**")
                st.markdown("> **解析**：許多程式語言不允許這樣寫，但 **Python 完美支援連續比較**！`5 < x < 10` 在後台等同於 `(5 < x) and (x < 10)`。因為 7 確實介於 5 到 10 之間，所以兩邊皆為 True，結果為 **`True`**。")

    # --- 題六 ---
    with tabs[5]:
        st.markdown("##### 📝 閱讀思考題：and 與 or 的驚悚優先權")
        st.code("""
# 記住：and 的優先權大於 or！
result = True or False and False
print(result)
        """, language="python")
        q3_6 = st.radio("請問最終結果為何？", ["請選擇答案...", "True", "False", "None", "報錯"], key="q3_6")
        
        if q3_6 != "請選擇答案...":
            if q3_6 == "True":
                st.success("🎉 觀念很紮實喔！沒被挖坑給騙了！")
            else:
                st.error("❌ 掉進 APCS 的經典優先權陷阱了！")
            with st.expander("🔍 查看【題六解析】"):
                st.write("**正確答案：`True`**")
                st.markdown("> **解析**：**`and` 的優先級比 `or` 高**！\n> 1. 電腦會先處理後半段的 `False and False` -> 得到 `False`。\n> 2. 算式簡化成 `True or False` -> 最終得到 **`True`**。\n> 如果這題從左到右算就會錯，APCS 超愛挖這個坑！")

    # --- 題七 ---
    with tabs[6]:
        st.markdown("##### 📝 閱讀思考題：字串與數字的大崩潰陷阱")
        st.code("""
a = "10"
b = 5
result = (a > b)
print(result)
        """, language="python")
        q3_7 = st.radio("請問這段程式會輸出什麼？", ["請選擇答案...", "True", "False", "程式大崩潰（TypeError）", "10"], key="q3_7")
        
        if q3_7 != "請選擇答案...":
            if q3_7 == "程式大崩潰（TypeError）":
                st.success("🎉 厲害！一眼看出型別錯誤的陷阱！")
            else:
                st.error("❌ 踢到鐵板了吧！再仔細看資料型態！")
            with st.expander("🔍 查看【題七解析】"):
                st.write("**正確答案：`程式大崩潰（TypeError）`**")
                st.markdown("> **解析**：踢到鐵板了吧！`a` 是**字串（文字）** `"10"`，而 `b` 是**整數（數字）** `5`。在 Python 中，**不同型別的生物是無法直接用 `>`, `<`, `>=`, `<=` 來比較大小的**！程式會立刻噴出 `TypeError` 錯誤。")

    # --- 題八 ---
    with tabs[7]:
        st.markdown("##### 📝 閱讀思考題：APCS 綜合大亂鬥（終極挑戰）")
        st.code("""
x = 8
y = 15
ans = not (x * 2 == y + 1) or (y % x == 7) and (x > 5)
print(ans)
        """, language="python")
        q3_8 = st.radio("試著當看看電腦，最後算出的結果是？", ["請選擇答案...", "True", "False", "報錯", "23"], key="q3_8")
        
        if q3_8 != "請選擇答案...":
            if q3_8 == "True":
                st.success("🎉 太神啦！終極挑戰關卡成功破關！")
            else:
                st.error("❌ 大軍亂了陣腳！重新拆解三路大軍看看？")
            with st.expander("🔍 查看【題八解析】"):
                st.write("**正確答案：`True`**")
                st.markdown("""
                > **我們分三路大軍擊破它：**
                > 1. **第一部分**：`not (x * 2 == y + 1)` -> `not (16 == 16)` -> `not True` 得到 **`False`**。
                > 2. **第二部分**：`(y % x == 7)` -> `15 % 8` 餘數是 `7`，`7 == 7` 成立，得到 **`True`**。
                > 3. **第三部分**：`(x > 5)` -> `8 > 5` 成立，得到 **`True`**。
                > 
                > **大融合時間（算式簡化為：`False or True and True`）：**
                > * `and` 優先！先算後半段：`True and True` 得到 **`True`**。
                > * 最後算 `or`：`False or True` 最終得到 **`True`**！
                """)

# ==========================================
# 知識點 3-2：單向條件式與 ZeroJudge 實作
# ==========================================
with st.expander("🧭 知識點三(下)：如果...就...——單向條件式 (If)"):
    st.markdown("""
    當滿足某個條件時，程式才去執行特定的事；如果不滿足，就當作沒這回事直接跳過。
    
    ##### 📊 單向條件式流程圖
    """)
    
    # 使用純網頁樣式取代會漏線的菱形，確保結構方正清晰、100% 不出錯
    st.components.v1.html("""
    <div style="font-family: sans-serif; max-width: 400px; margin: 0 auto; border: 1px solid #ddd; padding: 15px; border-radius: 8px; background-color: #fafafa; color: black;">
        <div style="text-align: center; font-weight: bold; background: #fffa00; padding: 8px; border: 1px solid #cc0; border-radius: 4px;">❓ 檢查條件 (Condition)</div>
        <div style="display: flex; justify-content: space-between; padding: 5px 40px; font-weight: bold; color: blue;">
            <span>🏼 True</span>
            <span>🏼 False</span>
        </div>
        <div style="display: flex; justify-content: space-between; align-items: flex-start;">
            <div style="width: 45%; background: #e3f2fd; border: 1px solid #90caf9; padding: 8px; border-radius: 4px; font-size: 13px; text-align: center;">🟢 執行特定程式區塊 (縮排部分)</div>
            <div style="width: 45%; background: #ffebee; border: 1px solid #ffcdd2; padding: 8px; border-radius: 4px; font-size: 13px; text-align: center;">❌ 跳過不執行</div>
        </div>
        <div style="text-align: center; margin-top: 10px; font-size: 18px; color: #555;">⬇️</div>
        <div style="text-align: center; background: #eee; padding: 6px; border-radius: 4px; font-size: 13px;">繼續往下走共同程式碼</div>
    </div>
    """, height=180)
    
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
    
    ##### 📊 多向條件式分流決策圖
    """)
    
    # 採用多層表格區塊，完美展現 if -> elif -> else 的樹狀決策分流
    st.components.v1.html("""
    <div style="font-family: sans-serif; max-width: 500px; margin: 0 auto; border: 1px solid #ccc; padding: 15px; border-radius: 8px; background-color: #fff; color: black; font-size: 14px;">
        <div style="background: #ff9900; color: white; padding: 8px; text-align: center; font-weight: bold; border-radius: 4px;">第一關：if 條件 1 成立？</div>
        <div style="display: flex; margin-top: 8px;">
            <div style="width: 30%; background: #e8f5e9; padding: 10px; border: 1px solid #a5d6a7; text-align: center; border-radius: 4px;">👉 <b>Yes</b><br>執行區塊 1<br>(結束分流)</div>
            <div style="width: 5%; text-align: center; padding-top: 15px; font-weight: bold; color: red;">No</div>
            <div style="width: 65%; border-left: 2px dashed #bbb; padding-left: 10px;">
                <div style="background: #ff9900; color: white; padding: 6px; text-align: center; font-weight: bold; border-radius: 4px;">第二關：elif 條件 2 成立？</div>
                <div style="display: flex; margin-top: 8px;">
                    <div style="width: 50%; background: #e8f5e9; padding: 8px; border: 1px solid #a5d6a7; text-align: center; border-radius: 4px;">👉 <b>Yes</b><br>執行區塊 2</div>
                    <div style="width: 10%; text-align: center; padding-top: 10px; font-weight: bold; color: red;">No</div>
                    <div style="width: 40%; background: #eceff1; padding: 8px; border: 1px solid #b0bec5; text-align: center; border-radius: 4px;">👉 <b>else</b><br>執行最終區塊</div>
                </div>
            </div>
        </div>
    </div>
    """, height=160)
    
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
        st.info("💡 闕老師提示：這題是經典的階梯式計分。需要用 `elif` 去細分：1~10題、11~20題、21~40題與40題以上的不同給分邏輯。")
        
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
