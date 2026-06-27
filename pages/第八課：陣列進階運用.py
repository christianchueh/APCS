import streamlit as st

# 設定網頁標題與風格，採用 wide 滿版
st.set_page_config(page_title="APCS 第八課：陣列進階運用", layout="wide")

st.title("🚀 APCS 第八課：陣列進階運用")
st.caption("適用 Python 3.14 環境 | 程式老師專用教學教材（直條流式網頁設計）")
st.markdown("---")

# ==========================================
# 🟢 核心觀念 1：統計與極值（直接呈現）
# ==========================================
st.header("📊 1. 統計與極值 (sum, max, min)")
st.markdown("在競賽中，我們經常需要快速求出陣列的總和、最大值、最小值，甚至要找出最大值的「索引位置」。")

st.subheader("💡 核心指令介紹")
st.code(r"""
arr = [10, 30, 5, 40, 20]

# 1. 基本統計
total = sum(arr)   # 總和: 105
highest = max(arr) # 最大值: 40
lowest = min(arr)  # 最小值: 5

# 2. 進階：找出極值的「索引位置」 (Index)
max_idx = arr.index(max(arr)) # 找出最大值 40 的索引 -> 3
min_idx = arr.index(min(arr)) # 找出最小值 5 的索引 -> 2

print(f"總和: {total}, 最大值: {highest} (索引 {max_idx})")
""", language="python")

st.subheader("🧪 課堂互動觀測站")
user_arr_str = st.text_input("輸入一組數字陣列（用空格隔開）：", value="25 88 12 99 43", key="arr_input_1")
if user_arr_str:
    try:
        arr = [int(x) for x in user_arr_str.split()]
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("陣列總和 `sum()`", sum(arr))
        col2.metric("最大值 `max()`", max(arr))
        col3.metric("最小值 `min()`", min(arr))
        col4.metric("最大值索引 `index()`", arr.index(max(arr)))
    except ValueError:
        st.error("請確保輸入的內容全部都是整數！")

st.markdown("---")

# ==========================================
# 🟢 核心觀念 2：陣列排序（直接呈現）
# ==========================================
st.header("⚡ 2. 競賽核心：排序 (sort, sorted)")
st.markdown("排序是 APCS 的大熱門。Python 內建的 Timsort 演算法時間複雜度為 $O(N \log N)$，在競賽中非常高效。")

# 排序內部我們稍微用小 Tab 區分不同層次的排序技巧，保持畫面整潔
sub_tab1, sub_tab2, sub_tab3 = st.tabs(["基本排序", "自訂條件排序 (Lambda)", "自訂二維陣列排序"])

with sub_tab1:
    st.subheader("`sort()` 與 `sorted()` 的差異")
    st.markdown("* `arr.sort()`：**原地排序**，會直接改變原陣列，不回傳新陣列。\n* `sorted(arr)`：**回傳新陣列**，原陣列保持不變。")
    st.code(r"""
arr = [5, 2, 9, 1]

# 由小到大 (預設)
arr.sort() # arr 變成 [1, 2, 5, 9]

# 由大到小 (加上 reverse=True)
arr.sort(reverse=True) # arr 變成 [9, 5, 2, 1]

# 不影響原陣列的作法
origin = [5, 2, 9, 1]
new_arr = sorted(origin) # new_arr=[1, 2, 5, 9], origin=[5, 2, 9, 1]
""", language="python")

with sub_tab2:
    st.subheader("進階：使用 `key=lambda` 進行複雜排序")
    st.markdown("當陣列內裝的是字串，或我們想依據「特定規則」排序時，`key` 指令是競賽神兵。")
    st.code(r"""
words = ["apple", "banana", "kiwi", "pear"]

# 規則：依據字串的「長度」由短到長排序
words.sort(key=lambda x: len(x))
print(words) # ['kiwi', 'pear', 'apple', 'banana']
""", language="python")

with sub_tab3:
    st.subheader("APCS 魔王關：多重條件排序")
    st.markdown("例如：學生分數「由大到小」排；若分數相同，則依據學號「由小到大」排。")
    st.code(r"""
# 每個元素格式：(學號, 分數)
students = [(101, 85), (102, 92), (103, 85), (104, 95)]

# 排序規則：分數加負號(代表降序)，學號正號(代表升序)
students.sort(key=lambda x: (-x[1], x[0]))

print(students)
# 正確輸出順序為：[(104, 95), (102, 92), (101, 85), (103, 85)]
""", language="python")

st.markdown("---")

# ==========================================
# 🟢 核心觀念 3：成員檢查與複製（直接呈現）
# ==========================================
st.header("🔍 3. 成員檢查與複製 (in, copy)")

st.subheader("1. 成員檢查 `in` 與 `not in`")
st.markdown("檢查某個元素是否存在於陣列中，時間複雜度為 $O(N)$。")
st.code(r"""
lucky_numbers = [7, 13, 22, 88]
if 7 in lucky_numbers:
    print("發財了！")
    
if 99 not in lucky_numbers:
    print("安全過關！")
""", language="python")

st.subheader("2. 陣列複製的致命陷阱 `copy` vs `deepcopy`")
st.error("⚠️ 競賽警訊：在 Python 中直接使用 `b = a` 並不是複製，而是「建立參照」。修改 `b` 的同時 `a` 也會被修改！")

st.code(r"""
import copy

# 狀況 A：一維陣列的淺複製 (Shallow Copy)
a = [1, 2, 3]
b = a.copy() # 或 b = a[:]
b[0] = 99
print(a) # [1, 2, 3] -> a 沒有被影響，安全！

# 狀況 B：二維/多維陣列的深複製陷阱 (Deep Copy)
matrix_a = [[1, 2], [3, 4]]
matrix_b = matrix_a.copy() # 這只是淺複製！外層獨立，內層仍共用記憶體
matrix_b[0][0] = 99
print(matrix_a) # [[99, 2], [3, 4]] -> matrix_a 竟然被污染了！

# 正確應對二維陣列的複製：
matrix_c = copy.deepcopy(matrix_a)
""", language="python")

st.markdown("---")


# ==========================================
# 🎯 底部：實作練習區（採用 Tabs 切換題號）
# ==========================================
st.header("📝 課堂實作演練")
st.markdown("請同學們結合上方學到的觀念，思考並完成以下三道 ZeroJudge 經典競賽題。")

# 在底部建立三題的 Tabs
tab_d190, tab_e313, tab_f605 = st.tabs([
    "🎯 例題 d190：11462 - Age Sort", 
    "🎯 例題 e313：最少相異字母", 
    "🎯 例題 f605：購買力"
])

# ---- Tab: d190 ----
with tab_d190:
    st.subheader("🔗 [ZeroJudge d190 基礎排序題目連結](https://zerojudge.tw/ShowProblem?problemid=d190)")
    st.info(
        "**解題想法引導**：\n"
        "1. 題目會給定一組受測者的年齡資料，資料量可能很大。\n"
        "2. 我們的任務是將這些年齡「由小到大」依序輸出。\n"
        "3. **核心工具**：這題是經典的排序應用。讀入整組陣列後，直接使用高效的 `.sort()` 或 `sorted()` 進行排序即可。\n"
        "4. **優化小撇步**：因為測資可能很多，輸出時可以使用 `' '.join(map(str, arr))` 來加速印出結果。"
    )
    

if __name__ == '__main__':
    main()
""", language="python")

# ---- Tab: e313 ----
with tab_e313:
    st.subheader("🔗 [ZeroJudge e313 最少相異字母題目連結](https://zerojudge.tw/ShowProblem?problemid=e313)")
    st.info(
        "**解題想法引導**：\n"
        "1. 給定 $N$ 個長度相同的字串，我們要找出「相異字母最少」的字串。如果有好幾個字串的相異字母一樣少，則輸出字典序最小（即最靠前的字串）。\n"
        "2. **如何計算相異字母？**：可以利用 Python 的 `set()` 特性。例如 `set(\"AAB\")` 會變成 `{'A', 'B'}`，其長度 `len(set(\"AAB\"))` 就是 2。\n"
        "3. **多重條件排序應用**：我們可以將每個字串處理成一個二元組：`(相異字母數量, 字串本身)`。接著利用 `min()` 找出最優解，或是利用 `key=lambda` 排序。因為 Python 預設在比對元組時，會先比第一個元素，相同再比第二個元素，完美契合題目要求！"
    )
    

# ---- Tab: f605 ----
with tab_f605:
    st.subheader("🔗 [ZeroJudge f605 購買力題目連結](https://zerojudge.tw/ShowProblem?problemid=f605)")
    st.info(
        "**解題想法引導**：\n"
        "1. 題目給定 $N$ 物品在 3 個不同時間點的價格，以及一個門檻值 $D$。\n"
        "2. 對於每樣物品，我們必須檢查它的「最高價格」與「最低價格」之差是否 $\ge D$。\n"
        "3. 如果滿足條件，該物品的購買成本為這 3 個價格的「平均值」（題目保證能整除 `// 3`）。\n"
        "4. 最終要統計「總共買了幾樣物品」以及「這些購買物品的總花費」。\n"
        "5. **核心工具**：將每行的 3 個價格放入陣列後，直接用 `max(arr)` 找最大、`min(arr)` 找最小，用 `sum(arr) // 3` 算平均！"
    )
    
