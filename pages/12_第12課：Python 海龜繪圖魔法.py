import streamlit as st

# 設定網頁標題與寬度
st.set_page_config(page_title="Python 海龜繪圖魔法", page_icon="🐢", layout="wide")

# 主標題與前言
st.title("🐢 Python 海龜繪圖魔法：從 0 到 1 的絢麗幾何")
st.markdown("""
歡迎來到海龜繪圖（Turtle Graphics）的世界！在這裡，程式碼就是你的畫筆。
我們將一步步學習如何下指令，最後畫出令人驚豔的彩色幾何圖形。
""")

# 提示實作網站
st.info("💡 **實作練習平台**：請在瀏覽器另開分頁打開 👉 [Trinket Turtle](https://trinket.io/turtle) ，將下方的範例程式碼複製貼上，並依照【實作練習】的提示動手挑戰看看！")

st.divider()

# --- 第一步 ---
st.header("第一步：呼叫海龜與基本移動 (0 基礎起點)")
st.markdown("""
首先，我們要先「邀請」海龜出場，並教牠最基本的直走與轉彎。
* `forward(距離)`：往前走
* `backward(距離)`：往後退
* `left(角度)`：向左轉
* `right(角度)`：向右轉
""")

st.code('''import turtle

t = turtle.Turtle()

t.forward(100)  # 往前走 100 步
t.left(90)      # 向左轉 90 度 (直角)
t.forward(100)  # 再往前走 100 步
''', language='python')

with st.expander("🎯 【實作練習 1】點擊展開挑戰！", expanded=True):
    st.success("""
    **任務：畫出一個大寫英文字母「L」**
    1. 前往 [Trinket](https://trinket.io/turtle) 網站。
    2. 試著運用 `forward()` 和轉彎指令，讓海龜畫出一個倒放或正放的字母「L」。
    3. *提示：你可以先往下走 (向右轉90度再前進)，再往右走。*
    """)

st.divider()

# --- 第二步 ---
st.header("第二步：加上「迴圈」，讓海龜自動重複動作")
st.markdown("""
如果我們要畫一個正方形，本來需要寫 4 次「前進 + 轉彎」。
身為聰明的程式設計師，我們可以用 `for` 迴圈讓電腦幫我們自動重複！
""")

st.code('''import turtle

t = turtle.Turtle()

# 讓底下的縮排動作重複 4 次
for i in range(4):
    t.forward(100)  
    t.left(90)      
''', language='python')

with st.expander("🎯 【實作練習 2】點擊展開挑戰！", expanded=True):
    st.success("""
    **任務：畫出一個正三角形 (等邊三角形)**
    1. 請修改上面的迴圈程式碼。
    2. 三角形有 3 個邊，所以迴圈要重複幾次呢？
    3. *重要提示：海龜轉彎的角度是「外角」。正三角形的內角是 60 度，所以海龜每次需要轉 `180 - 60 = 120` 度喔！*
    """)

st.divider()

# --- 第三步 ---
st.header("第三步：讓圖形變漂亮（顏色與速度）")
st.markdown("""
黑白線條太單調了！我們可以改變背景顏色、畫筆顏色，並把海龜的速度調快，這在畫複雜圖形時非常實用。
* `t.color("顏色名稱")`：改變畫筆顏色 (如 "yellow", "red", "cyan")
* `t.speed(0)`：設定速度，0 是最快，1 是最慢
""")

st.code('''import turtle

# 設定背景為黑色
screen = turtle.Screen()
screen.bgcolor("black")  

t = turtle.Turtle()
t.color("yellow")  # 設定畫筆顏色為黃色
t.speed(0)         # 設定畫筆速度為最快

# 畫一個黃色星星
for i in range(5):
    t.forward(150)
    t.right(144)   # 轉 144 度就可以畫出五角星
''', language='python')

with st.expander("🎯 【實作練習 3】點擊展開挑戰！", expanded=True):
    st.success("""
    **任務：畫一個紅色的八角形**
    1. 試著把背景換成你喜歡的顏色（例如 `"lightblue"`）。
    2. 把畫筆換成紅色（`"red"`）。
    3. 寫一個重複 8 次的迴圈。
    4. *提示：八角形每次要轉幾度呢？ (360 ÷ 8 = 45 度)*
    """)

st.divider()

# --- 第四步 ---
st.header("第四步：終極大絕招——「隨機顏色」與「幾何迴圈」")
st.markdown("""
現在，我們要結合所有絕招：**迴圈 + 速度 + 隨機顏色**！
為了讓所有網頁版海龜都能看懂，我們用 `random` 隨機產生 RGB 數值後，轉成網頁常用的 **16進位色碼 (例如：#FF5733)**。

每一次畫圓，海龜都會換上獨一無二的色彩！
""")

st.code('''import turtle
import random

# 1. 基本設定
screen = turtle.Screen()
screen.bgcolor("black")  
t = turtle.Turtle()
t.speed(0)               
t.width(2)               # 把畫筆調粗一點

# 2. 畫出絢麗的幾何圖形
# 迴圈 72 次 (每次轉 5 度，72 * 5 = 360 度剛好一圈)
for i in range(72):
    
    # --- 產生隨機顏色 (RGB 轉 16 進位色碼) ---
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_hex = f"#{r:02x}{g:02x}{b:02x}"  # 組合出色碼
    
    t.color(color_hex)   # 換上隨機顏色
    
    # --- 繪畫動作 ---
    t.circle(100)        # 畫一個半徑 100 的圓
    t.right(5)           # 向右轉 5 度
''', language='python')

with st.expander("🎯 【實作練習 4：結業挑戰】點擊展開挑戰！", expanded=True):
    st.success("""
    **任務：打造你的專屬「彩色方塊曼陀羅」**
    1. 將上面畫圓（`t.circle(100)`）的程式碼刪除。
    2. 取代為**畫正方形的程式碼**（可以使用第二步學到的裡面再包一個迴圈，也就是「巢狀迴圈」，或者直接往前走再轉 90 度共四次）。
    3. 讓這個隨機顏色的正方形，每次畫完就旋轉 10 度，重複 36 次！
    4. *挑戰看看你會畫出什麼魔幻的圖案吧！*
    """)

st.divider()
st.balloons()
st.markdown("<h3 style='text-align: center;'>🎉 恭喜你完成所有挑戰，成為 Python 海龜繪圖大師！</h3>", unsafe_allow_html=True)
