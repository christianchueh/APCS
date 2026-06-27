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
    
    st.subheader("💻 範例程式碼")
    st.code(r"""
import sys

def solve():
    # 讀取測試資料筆數
    lines = sys.stdin.read().split()
    if not lines:
        return
    
    t = int(lines[0])
    for i in range(1, t + 1):
        num_str = lines[i]
        ans = 1
        for digit in num_str:
            ans *= int(digit)
        print(ans)

if __name__ == '__main__':
    solve()
""", language="python")

    st.subheader("🧪 線上模擬測試")
    user_input = st.text_input("請輸入一個整數（例如：356）：", value="356")
    if user_input:
        if user_input.isdigit():
            ans = 1
            process = []
            for d in user_input:
                ans *= int(d)
                process.append(d)
            st.success(f"運算過程：{' × '.join(process)} = {ans}")
        else:
            st.error("請輸入合法的非負整數！")

# ==========================================
# 頁面：c382 加減乘除
# ==========================================
elif page == "例題 2：c382 加減乘除":
    st.header("🎯 c382: 加減乘除")
    st.markdown("**題目解說**：輸入一個簡單的算式（如 `3 + 5`），其中包含兩個整數與一個運算子（`+`, `-`, `*`, `/`），請輸出運算結果。")
    
    st.subheader("💡 解題思路")
    st.info("利用字串的 `.split()` 功能，自動切開數字與運算子，再透過條件判斷 (`if-elif`) 進行對應的數學運算。")
    
    st.subheader("💻 範例程式碼")
    st.code(r"""
import sys

def solve():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        # 使用 split() 拆分，會自動忽略多餘空格
        parts = line.split()
        num1 = int(parts[0])
        op = parts[1]
        num2 = int(parts[2])
        
        if op == '+':
            print(num1 + num2)
        elif op == '-':
            print(num1 - num2)
        elif op == '*':
            print(num1 * num2)
        elif op == '/':
            print(num1 // num2) # 題目通常要求整數除法

if __name__ == '__main__':
    solve()
""", language="python")

    st.subheader("🧪 線上模擬測試")
    expr = st.text_input("請輸入算式（例如：12 * 13 或 20 / 4）：", value="12 * 13")
    if expr:
        try:
            parts = expr.split()
            if len(parts) == 3:
                n1, op, n2 = int(parts[0]), parts[1], int(parts[2])
                if op == '+': res = n1 + n2
                elif op == '-': res = n1 - n2
                elif op == '*': res = n1 * n2
                elif op == '/': res = n1 // n2
                else: res = "未知的運算子"
                st.success(f"計算結果：{res}")
            else:
                st.warning("格式錯誤，請用空格隔開（如：12 + 5）")
        except Exception as e:
            st.error(f"輸入格式有誤或計算出錯：{e}")

# ==========================================
# 頁面：d306 All You Need Is Love
# ==========================================
elif page == "例題 3：d306 All You Need Is Love":
    st.header("🎯 d306: All You Need Is Love")
    st.markdown("**題目解說**：給定兩個二進位字串，判斷它們是否擁有大於 1 的公因數。若有，輸出 `All you need is love!`，否則輸出 `Love is not all you need!`。")
    
    st.subheader("💡 解題思路")
    st.info("1. 用 Python 內建的 `int(string, 2)` 將二進位字串轉為十進位整數。\n2. 使用 `math.gcd()` 計算最大公因數。\n3. 判斷 GCD 是否大於 1。")
    
    st.subheader("💻 範例程式碼")
    st.code(r"""
import sys
import math

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    idx = 1
    for pair in range(1, n + 1):
        s1 = input_data[idx]
        s2 = input_data[idx+1]
        idx += 2
        
        # 二進位字串轉十進位
        num1 = int(s1, 2)
        num2 = int(s2, 2)
        
        # 求最大公因數
        if math.gcd(num1, num2) > 1:
            print(f"Pair #{pair}: All you need is love!")
        else:
            print(f"Pair #{pair}: Love is not all you need!")

if __name__ == '__main__':
    solve()
""", language="python")

    st.subheader("🧪 線上模擬測試")
    col1, col2 = st.columns(2)
    with col1:
        b1 = st.text_input("二進位字串 1", value="11011")
    with col2:
        b2 = st.text_input("二進位字串 2", value="10010")
        
    if b1 and b2:
        try:
            dec1, dec2 = int(b1, 2), int(b2, 2)
            import math
            g = math.gcd(dec1, dec2)
            st.write(f"十進位數值分別為：`{dec1}` 與 `{dec2}`，最大公因數 (GCD) = `{g}`")
            if g > 1:
                st.success("✨ Pair #1: All you need is love!")
            else:
                st.error("💔 Pair #1: Love is not all you need!")
        except ValueError:
            st.error("請確認輸入的字串只包含 0 與 1！")

# ==========================================
# 頁面：c290 秘密差
# ==========================================
elif page == "例題 4：c290 秘密差":
    st.header("🎯 c290: 秘密差 (APCS 2017年3月實作題)")
    st.markdown("**題目解說**：給定一個很大的正整數（長度可達 1000 位），求其「奇數位數和」與「偶數位數和」之差的絕對值。")
    
    st.subheader("💡 解題思路")
    st.info("因為數字非常大，不能直接當成整數處理。必須當成「字串」，利用索引值（或 `enumerate`）區分奇數項與偶數項進行加總，最後取絕對值 `abs()`。")
    
    st.subheader("💻 範例程式碼")
    st.code(r"""
import sys

def solve():
    line = sys.stdin.read().strip()
    if not line:
        return
        
    odd_sum = 0
    even_sum = 0
    
    # Python 索引從 0 開始
    # 題目要求的第 1 位數（奇數項）對應 Python 索引 0
    # 題目要求的第 2 位數（偶數項）對應 Python 索引 1
    for idx, char in enumerate(line):
        digit = int(char)
        if idx % 2 == 0:
            odd_sum += digit  # 題目第 1, 3, 5... 位
        else:
            even_sum += digit # 題目第 2, 4, 6... 位
            
    secret_diff = abs(odd_sum - even_sum)
    print(secret_diff)

if __name__ == '__main__':
    solve()
""", language="python")

    st.subheader("🧪 線上模擬測試")
    secret_num = st.text_input("請輸入一個超長整數（例如：263541）：", value="263541")
    if secret_num:
        if secret_num.isdigit():
            odd_digits = [secret_num[i] for i in range(len(secret_num)) if i % 2 == 0]
            even_digits = [secret_num[i] for i in range(len(secret_num)) if i % 2 != 0]
            
            o_sum = sum(map(int, odd_digits))
            e_sum = sum(map(int, even_digits))
            
            st.write(f"🔴 奇數位數 (第1, 3, 5...位)：{', '.join(odd_digits)} ➡️ 總和 = {o_sum}")
            st.write(f"🔵 偶數位數 (第2, 4, 6...位)：{', '.join(even_digits)} ➡️ 總和 = {e_sum}")
            st.success(f"🔥 秘密差 = | {o_sum} - {e_sum} | = {abs(o_sum - e_sum)}")
        else:
            st.error("請輸入純數字組成的字串！")
