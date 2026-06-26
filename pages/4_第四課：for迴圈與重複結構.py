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
# 用 range 配合索引提取清單資料
# ==========================================
with st.expander("🧭 知識點二：🔥 核心大絕招——用 range() 索引提取清單資料（正取、倒取、跳取）", expanded=True):
    st.markdown("""
    學完了第三課的置物櫃（清單索引），我們要怎麼讓 `for` 迴圈幫我們把置物櫃裡面的東西「一個一個拿出來」呢？
    答案就是：**利用 `range(len(d))` 產生清單的號碼牌（索引），再用 `d[i]` 把物品取出來！**
    
    假設我們有一個清單：`d = ["A", "B", "C", "D", "E"]`（總長度 `len(d)` 是 5，號碼牌是 0, 1, 2, 3, 4）。
    我們來看看如何利用不同的 `range()` 刀法，實現各種拿取方式：
    """)
    
    st.table([
        {"提取方式": "1️⃣ 正著拿取 (從頭到尾)", "範例程式碼": "for i in range(len(d)):\\n    print(d[i])", "號碼牌 i 的變化": "0, 1, 2, 3, 4", "拿出來的物品": "A ➔ B ➔ C ➔ D ➔ E"},
        {"提取方式": "2️⃣ 跳著拿取 (每 2 個拿一次)", "範例程式碼": "for i in range(0, len(d), 2):\\n    print(d[i])", "號碼牌 i 的變化": "0, 2, 4", "拿出來的物品": "A ➔ C ➔ E"},
        {"提取方式": "3️⃣ 倒著拿取 (從尾到頭)", "範例程式碼": "for i in range(len(d) - 1, -1, -1):\\n    print(d[i])", "號碼牌 i 的變化": "4, 3, 2, 1, 0", "拿出來的物品": "E ➔ D ➔ C ➔ B ➔ A"}
    ])
    
    st.warning("⚠️ 闕老師的黑板重點：為什麼倒著拿的範圍是 `range(len(d) - 1, -1, -1)`？")
    st.markdown("""
    * **起點是 `len(d) - 1`**：因為長度是 5，但最後一個置物櫃的號碼牌是 `4`！
    * **終點是 `-1`**：因為「顧前不顧後」！我們必須數到 `0` 號櫃子，所以結束值必須寫 `0` 的下一個，也就是 `-1`！
    * **步伐是 `-1`**：代表號碼牌要倒著扣回去。
    """)
    
    # --- 足量清單提取閱讀題 ---
    st.markdown("---")
    st.markdown("### 📝 清單提取能力閱讀特訓（足量練習題）")
    
    dq1, dq2, dq3 = st.tabs(["📌 清單提取題 一", "📌 清單提取題 二", "📌 清單提取題 三"])
    with dq1:
        st.markdown("**題目：請問以下程式執行後，會印出什麼結果？**")
        st.code("""
scores = [90, 80, 70, 60]
for i in range(0, len(scores), 3):
    print(scores[i])
        """, language="python")
        with st.expander("👀 查看解答"):
            st.success("**答案：\\n90\\n60**")
            st.caption("分析：len(scores) 是 4，range(0, 4, 3) 會產生號碼牌 0 和 3。scores[0] 是 90，scores[3] 是 60。")
            
    with dq2:
        st.markdown("**題目：請問以下程式執行後，變數 `ans` 的最終結果是多少？**")
        st.code("""
data = [1, 2, 3, 4, 5]
ans = 0
for i in range(len(data) - 1, 1, -1):
    ans += data[i]
print(ans)
        """, language="python")
        with st.expander("👀 查看解答"):
            st.success("**答案：12**")
            st.markdown("""
            分析：
            * `len(data) - 1` 是 4，結束值是 1（不包含 1，只數到 2），步伐是 -1。
            * 產生的號碼牌 `i` 分別為：`4, 3, 2`。
            * 對應的資料：`data[4]`是5，`data[3]`是4，`data[2]`是3。
            * 累加結果：5 + 4 + 3 = 12。
            """)
            
    with dq3:
        st.markdown("**題目：這題大陷阱！請問以下程式會發生什麼事，或是印出什麼？**")
        st.code("""
words = ["Apple", "Banana", "Cherry"]
for i in range(len(words)):
    print(words[i + 1])
        """, language="python")
        with st.expander("👀 查看解答"):
            st.error("**答案：程式會崩潰，噴出 IndexError: list index out of range 錯誤！**")
            st.caption("分析：len(words) 是 3，i 會是 0, 1, 2。當迴圈跑到最後一輪 i = 2 時，程式企圖去印 words[2 + 1] 也就是 words[3]。但清單最大號碼牌只到 2，根本沒有 3 號櫃子，所以直接報錯崩潰！這在解相鄰兩項比較的題目時是學生最常犯的錯！")


# ==========================================
# 知識點 3：for 迴圈搭配 range 常見運算
# ==========================================
with st.expander("🧭 知識點三：for 迴圈的搬運魔法與累加/累乘技術"):
    st.markdown("""
    除了拿取清單資料，`for` 迴圈最常拿來做純數字的數學運算。
    """)
    
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
    st.markdown("### 🏆 實戰特訓：ZeroJudge 基礎迴圈題庫（含經典 N 次
