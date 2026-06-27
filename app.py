import streamlit as st

# --- 頁面全域設定 ---
st.set_page_config(
    page_title="闕河正 APCS 程式教室",
    page_icon="👨‍🏫",
    layout="wide"
)

# --- 側邊欄標題 ---
st.sidebar.markdown("# 📚 APCS 檢定課程")
st.sidebar.info("請在上方選擇想要學習的課堂頁面！")

# --- 主頁內容 ---
st.title("🎯 闕河正 APCS 程式檢定先修課")
st.markdown("---")

col1, col2 = st.columns([1, 2], gap="large")

with col1:
    # 教師形象區（建議可以替換成老師的個人照片網址）
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRlANdTAi4j2wpKH8mES2Sxeh3wI1xiSZLX2wLgnAaGqQ&s=10", use_container_width=True)
    st.markdown("<h3 style='text-align: center;'>闕河正 老師</h3>", unsafe_allow_html=True)
    
    # 榮譽與背景標籤
    st.success("💻 資深程式設計專家")
    st.info("🏫 大學資訊工程系講師")
    st.warning("🤖 機器人與資訊競賽金牌教練")

with col2:
    st.subheader("👨‍🏫 關於導師：闕河正")
    st.write("""
    歡迎來到我的 APCS 教室！在多年的教學與競賽指導實務中，我發現許多同學直接挑戰進階檢定題時，
    往往容易陷入語法碎片的迷宮，甚至因為黑底白字的終端機環境而失去興趣。
    
    這套教程是我精心設計的**「高效直觀學習法」**——我們利用 **Streamlit 網頁框架**，
    讓每一次的代碼改動都能轉化為網頁上的即時互動元件。
    在「所見即所得」的高回饋環境中，我們不偷懶、不超綱，用最紮實的實作建立最純正的演算法思維。
    """)
    
    st.markdown("### 🛠️ 本套教程三大亮點")
    st.markdown("""
    1. **不走積木懶人路**：拒絕過於幼稚的積木語言，從第一天起就寫核心 Python 語法。
    2. **拒絕死板黑視窗**：網頁元件即時互動，輸入、輸出、資料型態用眼睛就看得懂。
    3. **對接真實檢定環境**：每個知識點都包含與 APCS（如 ZeroJudge）解題環境的對接轉換，基本功絕不打折。
    """)
    
    st.markdown("---")
    st.info("📢 **開始學習**：請點選左側選單的「1_第一課：輸入輸出與運算」進入第一堂課！")
