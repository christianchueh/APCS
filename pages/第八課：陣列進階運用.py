import streamlit as st

# 設定網頁標題與風格
st.set_page_config(page_title="APCS 第八課：陣列進階運用", layout="wide")

st.title("🚀 APCS 第八課：陣列進階運用")
st.caption("適用 Python 3.14 環境 | 程式老師專用互動教材")

# 建立側邊欄導覽
page = st.sidebar.radio(
    "課程目錄",
    [
        "1. 統計與極值 (sum, max, min)", 
        "2. 競賽核心：排序 (sort, sorted)", 
        "3. 成員檢查與複製 (in, copy)",
        "🎯 例題 1：d190 3n+1", 
        "🎯 例題 2：e313 最少相異字母", 
        "🎯 例題 3：f605 購買力"
    ]
)

# ==========================================
# 1. 統計與極值
# ==========================================
if page == "1. 統計與極值 (sum, max, min)":
    st.header("📊 陣列統計與極值工具")
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
    user_arr_str = st.text_input("輸入一組數字陣列（用空格隔開）：", value="25 88 12 99 43")
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

# ==========================================
# 2. 競賽核心：排序
# ==========================================
elif page == "2. 競賽核心：排序 (sort, sorted)":
    st.header("⚡ 競賽必備：陣列排序技巧")
    st.markdown("排序是 APCS 的大熱門。Python 內建的 Timsort 演算法時間複雜度為 $O(N \log N)$，在競賽中非常高效。")
    
    tab1, tab2, tab3 = st.tabs(["基本排序", "自訂條件排序 (Lambda)", "自訂二維陣列排序"])
    
    with tab1:
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

    with tab2:
        st.subheader("進階：使用 `key=lambda` 進行複雜排序")
        st.markdown("當陣列內裝的是字串，或我們想依據「特定規則」排序時，`key` 指令是競賽神兵。")
        st.code(r"""
words = ["apple", "banana", "kiwi", "pear"]

# 規則：依據字串的「長度」由短到長排序
words.sort(key=lambda x: len(x))
print(words) # ['kiwi', 'pear', 'apple', 'banana']
""", language="python")

    with tab3:
        st.subheader("APCS 魔王關：多重條件排序")
        st.markdown("例如：學生分數「由大到小」排；若分數相同，則依據學號「由小到大」排。")
        st.code(r"""
# 每個元素格式：(學號, 分數)
students = [(101, 85), (102, 92), (103, 85), (104, 95)]

# 排序規則：分數加負號(代表降序)，學號正號(代表升序)
students.sort(key=lambda x: (-x[1], x[0]))

print(students)
# 輸出: [(104, 95), (101, 85), (103, 85), (102, 92) 的分數高於85，所以102在前面...]
# 正確輸出順序應為：[(104, 95), (102, 92), (101, 85), (103, 85)]
""", language="python")

# ==========================================
# 3. 成員檢查與複製
# ==========================================
elif page == "3. 成員檢查與複製 (in, copy)":
    st.header("🔍 成員檢查與陣列複製陷阱")
    
    st.subheader("1. 成員檢查 `in` 與 `not in`")
    st.markdown("檢查某個元素是否存在於陣列中，時間複雜度為 $O(N)$（若重視效率，大數據競賽題通常會改用 `set`）。")
    st.code(r"""
lucky_numbers = [7, 13, 22, 88]
if 7 in lucky_numbers:
    print("發財了！")
    
if 99 not in lucky_numbers:
    print("安全過關！")
""", language="python")

    st.subheader("2. 陣列複製的致命陷阱 `copy` vs `deepcopy`")
    st.error("⚠️ 競賽警訊：在 Python 中直接使用 `b = a` 並不是複製，而是「建立參照（捷徑）」。修改 `b` 的同時 `a` 也會被修改！")
    
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

# ==========================================
# 例題 1：d190
# ==========================================
elif page == "🎯 例題 1：d190 3n+1":
    st.header("🎯 例題：d190 - 3n+1")
    st.markdown("🔗 [ZeroJudge d190 題目連結](https://zerojudge.tw/ShowProblem?problemid=d190)")
    
    st.subheader("💡 老師的解題思維引導")
    st.warning("請注意：此處僅提供演算法核心想法，請同學依據提示自行完成程式。")
    st.info(
        "**解題想法**：\n"
        "1. 題目會給定一組受測者的年齡資料，資料量可能很大。\n"
        "2. 我們的任務是將這些年齡「由小到大」依序輸出。\n"
        "3. **核心工具**：這題是經典的排序應用。讀入整組陣列後，直接使用高效的 `.sort()` 或 `sorted()` 進行排序即可。\n"
        "4. **優化小步撇步**：因為測資可能很多，輸出時可以使用 `' '.join(map(str, arr))` 來加速印出結果。"
    )
    
    st.subheader("📝 學生實作填空練習區")
    st.code(r"""
import sys

def main():
    # 讀取所有輸入
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    idx = 0
    while idx < len(input_data):
        n = int(input_data[idx])
        if n == 0:
            break
        idx += 1
        
        # 1. 讀取接下來的 n 個年齡並轉換為數字陣列
        ages = [int(x) for x in input_data[idx : idx + n]]
        idx += n
        
        # ===== 請同學在下方補全排序與輸出程式碼 =====
        # Hint: 使用本課學到的排序指令，並依序輸出結果
        
        # ============================================

if __name__ == '__main__':
    main()
""", language="python")

# ==========================================
# 例題 2：e313
# ==========================================
elif page == "🎯 例題 2：e313 最少相異字母":
    st.header("🎯 例題：e313 最少相異字母")
    st.markdown("🔗 [ZeroJudge e313 題目連結](https://zerojudge.tw/ShowProblem?problemid=e313)")
    
    st.subheader("💡 老師的解題思維引導")
    st.warning("請注意：此處僅提供演算法核心想法，請同學依據提示自行完成程式。")
    st.info(
        "**解題想法**：\n"
        "1. 給定 $N$ 個長度相同的字串，我們要找出「相異字母最少」的字串。如果有好幾個字串的相異字母一樣少，則輸出字典序最小（即最靠前的字串）。\n"
        "2. **如何計算相異字母？**：可以利用 Python 的 `set()` 特性。例如 `set(\"AAB\")` 會變成 `{'A', 'B'}`，其長度 `len(set(\"AAB\"))` 就是 2，代表有 2 個相異字母。\n"
        "3. **多重條件排序應用**：我們可以將每個字串處理成一個三元組：`(相異字母數量, 字串本身)`。接著利用 `min()` 找出最優解，或是利用 `key=lambda` 排序。因為 `min()` 或 `sort()` 預設在比對元組時，會先比對第一個元素（相異字數，愈小愈好），若相同則比對第二個元素（字串字典序，愈小愈好），完美契合題目要求！"
    )
    
    st.subheader("📝 學生實作填空練習區")
    st.code(r"""
import sys

def main():
    lines = sys.stdin.read().split()
    if not lines:
        return
        
    n = int(lines[0])
    words = lines[1:n+1]
    
    # ===== 請同學在下方補全程式碼 =====
    # 提示 1: 建立一個新陣列，裡面儲存每個字串的 (相異字數, 字串)
    # 提示 2: 利用 len(set(word)) 來取得相異字數
    # 提示 3: 使用 min() 或 sort() 找出最佳的字串並印出
    
    # ==================================

if __name__ == '__main__':
    main()
""", language="python")

# ==========================================
# 例題 3：f605
# ==========================================
elif page == "🎯 例題 3：f605 購買力":
    st.header("🎯 例題：f605 購買力 (APCS 2020年10月實作題一)")
    st.markdown("🔗 [ZeroJudge f605 題目連結](https://zerojudge.tw/ShowProblem?problemid=f605)")
    
    st.subheader("💡 老師的解題思維引導")
    st.warning("請注意：此處僅提供演算法核心想法，請同學依據提示自行完成程式。")
    st.info(
        "**解題想法**：\n"
        "1. 題目給定 $N$ 物品在 3 個不同時間點的價格，以及一個門檻值 $D$。\n"
        "2. 對於每樣物品，我們必須檢查它的「最高價格」與「最低價格」之差是否 $\ge D$。\n"
        "3. 如果滿足上述條件（即購買力足夠/價格波動大），代表我們要購買它。此時該物品的購買成本為這 3 個時間點價格的「平均值」（題目保證能整除）。\n"
        "4. 最終要統計「總共買了幾樣物品」以及「這些購買物品的總花費」。\n"
        "5. **核心工具**：每一行讀進來的 3 個價格放入陣列後，直接用 `max(arr)` 找最大、`min(arr)` 找最小，用 `sum(arr) // 3` 算平均，非常直觀！"
    )
    
    st.subheader("📝 學生實作填空練習區")
    st.code(r"""
import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    d = int(input_data[1])
    
    total_bought = 0
    total_cost = 0
    
    idx = 2
    for _ in range(n):
        # 讀取某樣物品的 3 個價格
        prices = [int(input_data[idx]), int(input_data[idx+1]), int(input_data[idx+2])]
        idx += 3
        
        # ===== 請同學在下方補全判斷邏輯 =====
        # 1. 找出 prices 陣列中的 max 與 min 
        # 2. 判斷差值是否 >= d
        # 3. 若成立，將 total_bought 加 1，並計算平均值累加至 total_cost
        
        # ====================================
        
    print(f"{total_bought} {total_cost}")

if __name__ == '__main__':
    main()
""", language="python")
