import streamlit as st

st.set_page_config(page_title="第一課：輸入輸出與運算", page_icon="🚀", layout="wide")

st.title("🚀 第一課：點石成金的魔法——輸入與輸出")
st.caption("授課教師：闕河正 老師")
st.markdown("---")

# ==========================================
# 課程導入（將 Streamlit 加上超連結）
# ==========================================
st.markdown("""
### 🧭 課程導入：為什麼我們用 [Streamlit](https://streamlit.io/playground) 開始？
歡迎來到程式設計的世界！很多人學程式的第一眼看到的是黑底白字的指令視窗，這讓人很容易迷失。
我們這堂課不走老路！我們使用 **[Streamlit](https://streamlit.io/playground)**，這是一個可以讓你用 Python 直接做出漂亮網頁的工具。
想像一下，你寫的每一行程式碼，都會立刻變成網頁上的輸入框與文字。今天，你不是在對著機器說話，你是在打造一個屬於你的互動網頁應用程式！
""")

# ==========================================
# 知識點一
# ==========================================
with st.expander("🧭 知識點一：輸入資料，輸出加料後的資料", expanded=True):
    st.markdown("""
    在程式的世界裡，最核心的本質就是**處理資料**。我們會把資料「輸入」給電腦，電腦處理完後再「輸出」給我們。
    * **輸入指令**：`st.text_input("提示文字")` — 這會在網頁上產生一個讓你打字的輸入框。
    * **輸出指令**：`st.write("要顯示的內容")` — 這會把括號內的內容丟到網頁上顯示出來。
    """)
    
    st.markdown("##### 📄 範例代碼：Hello World 改良版")
    st.code("""
import streamlit as st
name = st.text_input("請輸入你的英文名字：")
st.write("Hello ! " + name)
    """, language="python")
    
    st.markdown("##### 📝 互動實作練習：Hey World")
    st.caption("題目需求：提示使用者輸入「你今天最想去的地方」，並在網頁上輸出「Hey! 讓我們一起去 [地點] 冒險吧！」。")
    
    # 讓學生實際操作的互動區
    place = st.text_input("你今天最想去的地方是？", placeholder="例如：日本")
    if place:
        st.success(f"Hey! 讓我們一起去 {place} 冒險吧！")

# ==========================================
# 知識點二
# ==========================================
with st.expander("🧭 知識點二：字串變數、引號魔法與 f-string 格式化"):
    st.markdown("""
    1. **變數**：就像一個貼了標籤的「紙箱」，用來存放資料。
    2. **字串 (String)**：任何「純文字」都叫做字串。必須用引號包起來。
    3. **單雙引號混合**：如果字串內有單引號，外面就用雙引號 ` "I'm Python learner." `；反之則外面用單引號。
    4. **高級加工技巧：f-string**：字串前面加一個 `f`，就可以在字串內用 `{變數名稱}` 直接帶入變數！
    """)
    
    st.markdown("##### 📄 範例代碼：特製名片生成器")
    st.code("""
title = st.text_input("請輸入你的職稱：")
user_name = st.text_input("請輸入你的名字：")
st.write(f"歡迎光臨！這位是我們團隊的 {title}，名字叫做 '{user_name}'。")
    """, language="python")
    
    st.markdown("##### 📝 互動實作練習：經典對話框")
    st.caption("題目需求：利用 f-string 讓使用者輸入「偶像的名字」與「追星年數」，並輸出：愛慕宣言：我喜歡 \"[偶像名字]\" 已經 [年數] 年了！")
    
    idol = st.text_input("請輸入偶像的名字：", key="idol_input")
    years = st.text_input("請輸入追星年數：", key="years_input")
    if idol and years:
        st.info(f'愛慕宣言：我喜歡 "{idol}" 已經 {years} 年了！')

# ==========================================
# 知識點三
# ==========================================
with st.expander("🧭 知識點三：字串的相加（當數字被當成文字時）"):
    st.warning("🔥 初學者超級大重地：st.text_input 接收到的資料，電腦一律把它當成「字串（文字）」處理！")
    st.markdown("""
    如果我們把兩個「字串」相加，電腦不會做數學運算，而是做**文字拼接**（就像用磁鐵吸在一起）！
    """)
    
    st.markdown("##### 📄 範例代碼與體驗：數字碰壁記")
    st.code("""
num1 = st.text_input("請輸入第一個數字：")
num2 = st.text_input("請輸入第二個數字：")
st.write(f"相加結果是：{num1 + num2}")
    """, language="python")
    
    num1 = st.text_input("請輸入第一個數字：", value="5", key="n1")
    num2 = st.text_input("請輸入第二個數字：", value="6", key="n2")
    st.error(f"⚠️ 網頁實際顯示相加結果為：{num1 + num2} （看到了嗎？5 和 6 被黏在一起變成 56 了！）")
    
    st.markdown("##### 📝 互動實作練習：文字黏貼機")
    last_name = st.text_input("請輸入您的「姓氏」：", value="闕")
    first_name = st.text_input("請輸入您的「名字」：", value="河正")
    if last_name and first_name:
        st.write(f"全名拼貼結果：`{last_name + first_name}`")
        st.write(f"標準稱呼：{last_name} 同學，{first_name} 是個好名字！")

# ==========================================
# 知識點四
# ==========================================
with st.expander("🧭 知識點四：數字變數與型態轉換（初探）"):
    st.markdown("""
    為了讓電腦幫我們做真正的數學運算，我們必須把輸入的「字串」轉換成「數字」。
    * **整數轉換**：`int()`（將文字變成整數，如 1, 2, 3）
    """)
    
    st.markdown("##### 📄 範例與例題：臺灣專屬——民國年轉西元年")
    st.code("""
taiwan_year_str = st.text_input("請輸入今年是民國幾年：")
if taiwan_year_str:
    taiwan_year_int = int(taiwan_year_str)
    western_year = taiwan_year_int + 1911
    st.write(f"民國 {taiwan_year_int} 年，換算成西元就是 {western_year} 年！")
    """, language="python")
    
    taiwan_year_str = st.text_input("請輸入今年是民國幾年（例如：115）：", value="115")
    if taiwan_year_str:
        taiwan_year_int = int(taiwan_year_str)
        western_year = taiwan_year_int + 1911
        st.success(f"💡 運算結果：民國 {taiwan_year_int} 年，換算成西元就是 {western_year} 年！")

# ==========================================
# 知識點五
# ==========================================
with st.expander("🧭 知識點五：運算元大全與優先順序"):
    st.markdown("### Python 常用數學運算元表")
    
    # 建立表格
    st.table([
        {"運算元": "**", "功能": "次方 (冪運算)", "範例": "2 ** 3", "結果": "8"},
        {"運算元": "*", "功能": "乘法", "範例": "3 * 4", "結果": "12"},
        {"運算元": "/", "功能": "除法 (結果一定是小數)", "範例": "7 / 2", "結果": "3.5"},
        {"運算元": "//", "功能": "整除 (只取商數，無條件捨去)", "範例": "7 // 2", "結果": "3"},
        {"運算元": "%", "功能": "取餘數 (Mod)", "範例": "7 % 2", "結果": "1"},
        {"運算元": "+", "功能": "加法", "範例": "5 + 3", "結果": "8"},
        {"運算元": "-", "功能": "減法", "範例": "5 - 3", "結果": "2"},
    ])
    
    st.markdown("""
    ### 🔢 運算元的優先順序（由高到低）
    1. **括號 `()`**：永遠最高優先。
    2. **次方 `**`**
    3. **乘、除、整除、取餘數 `*`, `/`, `//`, `%`**：（同等級，由左至右算）
    4. **加、減 `+`, `-`**：（等級最低）
    """)
    
    st.markdown("### 📝 本節必刷實作例題（APCS 基本邏輯奠基）")
    
    # 實作題一
    st.markdown("##### 🛠️ 題一：直角三角形求斜邊（畢氏定理）")
    st.caption("公式：斜邊 = (邊1**2 + 邊2**2)**0.5")
    col1, col2 = st.columns(2)
    with col1:
        side1 = st.text_input("輸入直角邊 1：", value="3", key="s1")
    with col2:
        side2 = st.text_input("輸入直角邊 2：", value="4", key="s2")
    if side1 and side2:
        ans1 = (float(side1)**2 + float(side2)**2)**0.5
        st.info(f"計算出來的斜邊長度為：`{ans1}`")
        
    # 實作題二
    st.markdown("##### 🛠️ 題二：等差數列求總和（梯形公式）")
    st.caption("公式：總和 = (首項 + 末項) * 項數 / 2")
    c1, c2, c3 = st.columns(3)
    with c1: a1 = st.text_input("輸入首項：", value="1")
    with c2: an = st.text_input("輸入末項：", value="100")
    with c3: n = st.text_input("輸入項數：", value="100")
    if a1 and an and n:
        ans2 = (int(a1) + int(an)) * int(n) / 2
        st.info(f"等差數列總和為：`{ans2}`")

    # 實作題三
    st.markdown("##### 🛠️ 題三：華氏溫度轉攝氏溫度")
    st.caption("公式：攝氏 = (華氏 - 32) * 5 / 9")
    f_deg = st.text_input("請輸入華氏溫度：", value="98.6")
    if f_deg:
        c_deg = (float(f_deg) - 32) * 5 / 9
        st.info(f"華氏 {f_deg}°F 換算成攝氏為：`{c_deg:.2f}`°C")

    # 實作題4
    st.markdown("""#### [買鉛筆](https://zerojudge.tw/ShowProblem?problemid=d827 買鉛筆)""")

# ==========================================
# 知識點六
# ==========================================
with st.expander("🧭 知識點六：型態大融合——強制轉型與 f-string 完美搭配"):
    st.markdown("""
    ### 三大核心轉型工具
    * `int(資料)`：強迫轉成**整數**。
    * `float(資料)`：強迫轉成**浮點數（小數）**。
    * `str(資料)`：強迫轉成**字串（文字）**。
    
    只要使用 **f-string**，Python 會在背後自動幫你把 `{}` 裡面的數字轉成字串輸出，不用再痛苦地寫 `+ str(answer)` 了！
    """)
    
    st.markdown("##### 📄 範例：綜合 BMI 計算器")
    user_w = st.text_input("請輸入體重 (kg)：", value="70")
    user_h = st.text_input("請輸入身高 (cm)：", value="175")
    if user_w and user_h:
        w_float = float(user_w)
        h_float = float(user_h) / 100
        bmi = w_float / (h_float ** 2)
        st.warning(f"【計算報告】您的身高為 {user_h} 公分，體重為 {user_w} 公斤，計算出的 BMI 為：`{bmi:.2f}`")

# ==========================================
# 知識點七
# ==========================================
with st.expander("🧭 知識點七：脫離網頁——認識 APCS 標準指令 input 與 print"):
    st.markdown("""
    雖然我們用 Streamlit 學得很開心，但未來的 APCS 檢定系統是**沒有網頁介面**的！
    我們必須學會如何在傳統環境下進行輸入與輸出：
    * `input()` $\rightarrow$ 等同於 Streamlit 的 `st.text_input()`
    * `print()` $\rightarrow$ 等同於 Streamlit 的 `st.write()`
    """)
    
    st.code("""
# 傳統 Python 的寫法
name = input("請輸入名字：")
print("哈囉", name)
    """, language="python")
    
    st.markdown("""
    ### 🔬 print 指令的進階細節
    在傳統 `print()` 中，有幾個高頻率出現在檢定的控制參數：
    1. **逗號 `,` 隔開**：在 `print` 裡放多個資料用逗號隔開時，輸出的文字中間會**自動補一個空格**。
    2. **`sep` (Separation) 參數**：設定資料與資料之間的分隔文字（預設是一個空格）。
    3. **`end` 參數**：設定這一行印完後，結尾要做什麼（預設是換行 `\\n`）。
    """)
    
    st.code("""
# 範例一：改變分隔符號
print("A", "B", "C", sep="-")
# 畫面會印出: A-B-C

# 範例二：印完不換行
print("Hello", end="")
print("World")
# 畫面會印出: HelloWorld (接在一起，沒有換行)
    """, language="python")

# ==========================================
# 課程收尾
# ==========================================
st.markdown("---")
st.subheader("🏁 課程收尾：第一課成果驗收與 APCS 心態建立")
st.success("""
恭喜你完成了第一課！我們今天擺脫了死板板的黑視窗，利用 Streamlit 學會了：
1. 程式運作的本質：**輸入（Input）→ 處理（Process）→ 輸出（Output）**。
2. 資料的分類：文字（字串）與數字（整數/小數）是兩種完全不同的生物。
3. 算術的規則：Python 的 `//`、`%`、`**` 是未來演算法的核心工具。
""")

st.info("""
### 💡 APCS 思考題（回家作業）
今天我們學到了 `//`（整除取商）和 `%`（取餘數）。
請試著想一想：如果今天使用者輸入一個正整數秒數（例如：`3750` 秒），你要怎麼運用這兩個運算元，計算出這相當於「幾小時、幾分鐘、幾秒」呢？
""")
