import streamlit as st
import math

# --- 頁面設定 ---
st.set_page_config(page_title="闕河正 APCS 程式教室", layout="wide")

# --- 側邊欄導覽 ---
st.sidebar.title("📚 課程導覽")
page = st.sidebar.radio("請選擇頁面", ["首頁：導師介紹", "第一課：輸入輸出與運算"])

# ==========================================
# 首頁：導師介紹
# ==========================================
if page == "首頁：導師介紹":
    st.title("👨‍🏫 認識導師：闕河正 (Chueh Ho-cheng)")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # 這裡建議放您的個人照 URL
        st.image("https://via.placeholder.com/300", caption="闕河正 老師")
        
    with col2:
        st.subheader("教育理念：從應用出發，讓程式變得直觀")
        st.write("""
        大家好，我是闕河正。在 APCS 程式檢定的道路上，許多學生會被繁瑣的語法嚇跑。
        我致力於推動「低門檻、高回饋」的教學方式，讓學生在掌握底層邏輯（如型態轉換、演算法）的同時，
        也能立刻看到程式運作的成果。
        
        **為什麼選擇我的課程？**
        - **實戰導向**：不只教語法，更教如何解決問題。
        - **直觀教學**：利用 Streamlit 工具，讓初學者擺脫終端機的冷冰冰。
        - **APCS 專精**：針對檢定考點，從基礎紮根，不超綱，重邏輯。
        """)
        
        st.info("💡 您可以在網路上搜尋「闕河正」找到更多關於我的教學案例與分享。")

# ==========================================
# 第一課：輸入輸出與運算
# ==========================================
elif page == "第一課：輸入輸出與運算":
    st.title("🚀 第一課：點石成金的魔法——輸入與輸出")
    st.write("歡迎來到程式設計的世界！這堂課我們將打造一個屬於你的互動網頁。")

    # 知識點一
    with st.expander("🧭 知識點一：輸入資料，輸出加料後的資料", expanded=True):
        st.markdown("""
        在程式中，資料的流向是：**輸入 (Input) → 處理 → 輸出 (Output)**。
        - `st.text_input("提示")`: 建立輸入框。
        - `st.write("內容")`: 顯示結果。
        """)
        st.code("""
name = st.text_input("請輸入名字：")
st.write("Hello ! " + name)
        """, language="python")
        
        # 互動練習
        st.subheader("✍️ 實作區：Hey World")
        place = st.text_input("你今天想去哪裡冒險？", key="l1_q1")
        if place:
            st.write(f"Hey! 讓我們一起去 **{place}** 冒險吧！")

    # 知識點二
    with st.expander("🧭 知識點二：字串變數、引號魔法與 f-string"):
        st.markdown("""
        - **字串 (String)**: 用引號包起來的文字。
        - **混合引號**: 外雙內單 ` "I'm safe" ` 或 外單內雙 ` '老師說："加油"' `。
        - **f-string**: 在字串前加 `f`，用 `{變數}` 直接帶入資料。
        """)
        title = st.text_input("輸入職稱：", value="隊長")
        name_2 = st.text_input("輸入名字：", value="阿正")
        st.write(f"歡迎！這位是我們的 {title}，名字叫 '{name_2}'。")

    # 知識點三
    with st.expander("🧭 知識點三：字串的相加（當數字被當成文字時）"):
        st.warning("注意！st.text_input 抓回來的資料預設都是「字串」。")
        s_num1 = st.text_input("輸入數字 A：", value="5")
        s_num2 = st.text_input("輸入數字 B：", value="6")
        st.write(f"文字相加結果：`{s_num1 + s_num2}` (這不是 11，這是拼接！)")

    # 知識點四
    with st.expander("🧭 知識點四：型態轉換 (int)"):
        st.markdown("為了計算，我們用 `int()` 把字串轉成整數。")
        roc_year = st.text_input("請輸入民國年：", value="113")
        if roc_year:
            western_year = int(roc_year) + 1911
            st.success(f"民國 {roc_year} 年換算西元為：{western_year} 年")

    # 知識點五
    with st.expander("🧭 知識點五：運算元大全與優先順序"):
        st.table({
            "運算元": ["**", "*", "/", "//", "%", "+", "-"],
            "功能": ["次方", "乘", "除", "整除取商", "取餘數", "加", "減"],
            "範例": ["2**3=8", "3*4=12", "7/2=3.5", "7//2=3", "7%2=1", "5+3=8", "5-3=2"]
        })
        st.info("優先順序：括號 > 次方 > 乘除組 > 加減組")
        
        # 實作挑戰
        st.subheader("📝 綜合計算挑戰")
        colA, colB = st.columns(2)
        with colA:
            side_a = st.number_input("直角三角形邊長 A", value=3.0)
            side_b = st.number_input("直角三角形邊長 B", value=4.0)
            hypotenuse = (side_a**2 + side_b**2)**0.5
            st.write(f"斜邊長度為：{hypotenuse}")
        with colB:
            f_temp = st.number_input("輸入華氏溫度 (F)", value=98.0)
            c_temp = (f_temp - 32) * 5 / 9
            st.write(f"換算攝氏為：{c_temp:.2f} °C")

    # 知識點六
    with st.expander("🧭 知識點六：型態大融合"):
        st.markdown("利用 `float()` 處理小數，並用 f-string 完美輸出。")
        weight = st.text_input("體重(kg)", value="70")
        height = st.text_input("身高(cm)", value="175")
        if weight and height:
            bmi = float(weight) / ((float(height)/100)**2)
            st.info(f"您的 BMI 為：{bmi:.2f}")

    # 知識點七
    with st.expander("🧭 知識點七：傳統 input 與 print 指令"):
        st.markdown("""
        在沒有 Streamlit 的傳統環境（如 APCS 檢定），我們會使用：
        - `input()`: 等同於 `st.text_input`
        - `print()`: 等同於 `st.write`
        """)
        st.code("""
# 傳統寫法範例
name = input("請輸入名字")
print("Hello", name, sep="-", end="!")
        """, language="python")
        st.markdown("""
        **print 指令細節：**
        - `,`: 會自動補一個空格。
        - `sep`: 設定分隔符號（預設是空格）。
        - `end`: 設定結尾符號（預設是換行）。
        """)

    # 課程結語
    st.divider()
    st.subheader("🏁 課程收尾：APCS 心態建立")
    st.success("恭喜完成第一課！你已經掌握了程式最核心的「資料流」概念。")
    st.write("**💡 回家作業：** 寫一個程式，輸入總秒數，計算它是幾小時幾分幾秒？")
    st.code("""
# 提示：
# 小時 = 總秒數 // 3600
# 剩餘秒數 = 總秒數 % 3600
# ...以此類推
    """)
