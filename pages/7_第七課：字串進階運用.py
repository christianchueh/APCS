import streamlit as tf # 這裡我們習慣用 st，但若您需要特殊縮寫可調整，以下統一使用 st
import streamlit as st

# 設定網頁標題與風格
st.set_page_config(page_title="APCS 第七課：字串與進階運用", layout="wide")

st.title("🚀 APCS 第七課：字串與進階運用")
st.caption("適用 Python 3.14 環境 | 程式老師專用教學教材")

# 建立側邊欄導覽
page = st.sidebar.radio(
    "課程目錄",
    ["核心觀念教學", "例題 1：a149 乘乘樂", "例題 2：c382 加減乘除", "例題 3：d306 All You Need Is Love", "例題 4：c290 秘密差"]
)

# ==========================================
# 頁面：核心觀念教學
# ==========================================
if page == "核心觀念教學":
    st.header("📝 字串進階操作核心觀念")
    
    tab1, tab2, tab3 = st.tabs(["1. 字串切片與反轉", "2. 字元轉換 (chr, ord)", "3. 字串狀態判斷與大小寫"])
    
    with tab1:
        st.subheader("字串切片 (Slicing) 與反轉")
        st.markdown("語法：`string[start:end:step]`（左閉右開區間）")
        st.code(r"""
s = "HelloAPCS"
print(s[0:5])   # 'Hello' (索引 0 到 4)
print(s[5:])    # 'APCS' (索引 5 到最後)
print(s[::-1])  # 'SCPAolleH' (字串完全反轉)
""", language="python")

    with tab2:
        st.subheader("ASCII 碼與字元轉換")
        st.markdown("* `ord(ch)`：將字元轉換為對應的 ASCII 碼 (整數)\n* `chr(num)`：將 ASCII 碼 (整數) 轉換為對應的字元")
        st.code(r"""
# 字元轉數字
print(ord('A'))  # 65
print(ord('a'))  # 97

# 數字轉字元
print(chr(66))   # 'B'

# 常見應用：計算字母相對位置
diff = ord('c') - ord('a') # 2
""", language="python")

    with tab3:
        st.subheader("大小寫轉換與狀態判斷")
        st.markdown("常用於檢查輸入格式或處理大小寫不敏感的題目。")
        st.code(r"""
s = "Python3.14"

# 1. 大小寫轉換
print(s.upper())  # 'PYTHON3.14'
print(s.lower())  # 'python3.14'

# 2. 字串內容判斷
print("12345".isdigit())  # True (是否全為數字)
print("APCS".isalpha())    # True (是否全為英文字母)
print("APCS2026".isalnum()) # True (是否全為英文或數字)
""", language="python")

# ==========================================
# 頁面：a149 乘乘樂
# ==========================================
elif page == "例題 1：a149 乘乘樂":
    st.header("🎯 a149: 乘乘樂")
    st.markdown("**題目解說**：輸入一個非負整數，將其每一位數（Digit）分離後全部相乘，求其乘積。這題是將數字當作「字串」處理的經典範例！")
    
    st.subheader("💡 解題思路")
    st.info("直接將輸入視為字串，用 `for` 迴圈逐一取出字元，轉成整數後與答案相乘。")
    

# ==========================================
# 頁面：c382 加減乘除
# ==========================================
elif page == "例題 2：c382 加減乘除":
    st.header("🎯 c382: 加減乘除")
    st.markdown("**題目解說**：輸入一個簡單的算式（如 `3 + 5`），其中包含兩個整數與一個運算子（`+`, `-`, `*`, `/`），請輸出運算結果。")
    
    st.subheader("💡 解題思路")
    st.info("利用字串的 `.split()` 功能，自動切開數字與運算子，再透過條件判斷 (`if-elif`) 進行對應的數學運算。")
    
   

# ==========================================
# 頁面：d306 All You Need Is Love
# ==========================================
elif page == "例題 3：d306 All You Need Is Love":
    st.header("🎯 d306: All You Need Is Love")
    st.markdown("**題目解說**：給定兩個二進位字串，判斷它們是否擁有大於 1 的公因數。若有，輸出 `All you need is love!`，否則輸出 `Love is not all you need!`。")
    
    st.subheader("💡 解題思路")
    st.info("1. 用 Python 內建的 `int(string, 2)` 將二進位字串轉為十進位整數。\n2. 使用 `math.gcd()` 計算最大公因數。\n3. 判斷 GCD 是否大於 1。")
    
    

# ==========================================
# 頁面：c290 秘密差
# ==========================================
elif page == "例題 4：c290 秘密差":
    st.header("🎯 c290: 秘密差 (APCS 2017年3月實作題)")
    st.markdown("**題目解說**：給定一個很大的正整數（長度可達 1000 位），求其「奇數位數和」與「偶數位數和」之差的絕對值。")
    
    st.subheader("💡 解題思路")
    st.info("因為數字非常大，不能直接當成整數處理。必須當成「字串」，利用索引值（或 `enumerate`）區分奇數項與偶數項進行加總，最後取絕對值 `abs()`。")
    
   
