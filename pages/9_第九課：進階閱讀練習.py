import streamlit as st

# 設定網頁標題與風格
st.set_page_config(page_title="APCS 第九課：字串與陣列綜合挑戰賽", layout="wide")

st.title("🏆 APCS 第九課：字串與陣列進階觀念挑戰賽")
st.caption("適用 Python 3.14 環境 | 15 題符合進階閱讀練習題（全面修正引號與語法錯誤）")
st.markdown("👉 **請仔細閱讀程式碼並追蹤變數變化，點選選項後系統將即時回饋正誤與詳細解析！**")
st.markdown("---")

# ==============================================================================
# Q1 - Q15 題目與即時反饋系統（嚴格限制教學範圍內，全面修正 Python 3.14 語法解析錯誤）
# ==============================================================================

# --- Q1 ---
st.subheader("💡 Q1. 字串與步長切片迷宮")
st.markdown("請閱讀以下程式碼，請問最後輸出的結果為何？")
st.code(r"""
s = "APCS2026_Python"
res = s[-4:2:-2]
print(res)
""", language="python")

q1_ans = st.radio(
    "請選擇答案：",
    ["(A) 'y_0'", "(B) 'htP_02'", "(C) 'hP_2'", "(D) 'yP0'"],
    index=None,
    key="q1"
)
if q1_ans:
    if q1_ans.startswith("(C)"):
        st.success("🎉 答對了！")
        st.info(r"""💡 **正確解析**：
* 索引 `-4` 指的是字元 `'y'`。
* 索引 `2` 指的是字元 `'C'`。
* 步長為 `-2` 代表從 `'y'` 開始往左邊跳著數（每隔一個字元取一個）。
* 依序取到：索引 -4 的 `'y'` $\rightarrow$ 索引 -6 的 `'_'` $\rightarrow$ 索引 -8 的 `'6'` $\rightarrow$ 索引 -10 的 `'2'` 點結束（不含邊界值索引 2 的 `'C'`）。
* 實質抓到為 `'h'`（第11格）、`'P'`（第9格）、`'_'`（第7格）、`'2'`（第5格），拼起來就是 `'hP_2'`。""")
    else:
        st.error("❌ 答錯囉，再仔細推導一次！提示：負數步長是往左走，且不包含終點。")

st.markdown("---")

# --- Q2 ---
st.subheader("💡 Q2. 一維陣列的淺複製（Shallow Copy）行為")
st.markdown("請閱讀以下程式碼，請問最後輸出的 `A` 陣列內容為何？")
st.code(r"""
A = [10, 20, 30]
B = A.copy()
B[1] = 99
B.append(40)
print(A)
""", language="python")

q2_ans = st.radio(
    "請選擇答案：",
    ["(A) [10, 20, 30]", "(B) [10, 99, 30]", "(C) [10, 99, 30, 40]", "(D) [10, 20, 30, 40]"],
    index=None,
    key="q2"
)
if q2_ans:
    if q2_ans.startswith("(A)"):
        st.success("🎉 答對了！完全掌握一維陣列的複製行為！")
        st.info("💡 **解析**：因為 `A` 是一維陣列，`A.copy()` 會產生一個完全獨立的全新記憶體空間。因此不論我們對 `B` 進行修改（`B[1] = 99`）或是新增元素（`B.append(40)`），原始的 `A` 陣列都不會受到任何影響。")
    else:
        st.error("❌ 答錯了！這是一維陣列的獨立複製，修改 B 不會牽連到 A 喔。")

st.markdown("---")

# --- Q3 ---
st.subheader("💡 Q3. 陣列的極值與索引定位")
st.markdown("請閱讀以下程式碼，請問最後輸出的結果為何？")
st.code(r"""
nums = [40, 10, 50, 20, 50, 30]
val = max(nums)
idx = nums.index(val)
print(val, idx)
""", language="python")

q3_ans = st.radio(
    "請選擇答案：",
    ["(A) 50 2", "(B) 50 4", "(C) 40 0", "(D) 50 5"],
    index=None,
    key="q3"
)
if q3_ans:
    if q3_ans.startswith("(A)"):
        st.success("🎉 答對了！")
        st.info("💡 **解析**：`max(nums)` 會找到陣列中的最大值為 `50`。而 `nums.index(50)` 會由左至右尋找第一個出現的 `50` 的索引位置。雖然索引 2 和索引 4 都是 50，但它只會回傳第一個遇到的位置，也就是 `2`。")
    else:
        st.error("❌ 答錯囉！請特別注意 index() 指令遇到重複數值時的回傳規則。")

st.markdown("---")

# --- Q4 ---
st.subheader("💡 Q4. 陣列倒序切片與元素檢查")
st.markdown("請閱讀以下程式碼，請問最後輸出的結果為何？")
st.code(r"""
arr = [5, 10, 15, 20, 25]
sub = arr[::-2]
res = 15 in sub
print(res)
""", language="python")

q4_ans = st.radio(
    "請選擇答案：",
    ["(A) False", "(B) True", "(C) 15", "(D) 語法錯誤"],
    index=None,
    key="q4"
)
if q4_ans:
    if q4_ans.startswith("(B)"):
        st.success("🎉 答對了！")
        st.info("💡 **解析**：`arr[::-2]` 代表從最尾端倒序往回跳著取元素，會得到 `[25, 15, 5]`。接著我們使用 `15 in sub` 檢查 15 是否在這個新陣列中，因為 15 確實在裡面，所以回傳布林值 `True`。")
    else:
        st.error("❌ 答錯囉！`in` 指令會檢查元素是否存在，並回傳布林值。")

st.markdown("---")

# --- Q5 ---
st.subheader("💡 Q5. ASCII 碼字元轉換計算")
st.markdown("請閱讀以下程式碼，請問最後輸出的變數 `ans` 值為何？")
st.code(r"""
n1 = ord('d') - ord('a')
n2 = ord('B') - ord('A')
ans = chr(ord('A') + n1 + n2)
print(ans)
""", language="python")

q5_ans = st.radio(
    "請選擇答案：",
    ["(A) 'E'", "(B) 'F'", "(C) 'D'", "(D) 'e'"],
    index=None,
    key="q5"
)
if q5_ans:
    if q5_ans.startswith("(A)"):
        st.success("🎉 答對了！字母距離計算非常精準！")
        st.info("💡 **解析**：`ord('d') - ord('a')` 的距離是 `3`；`ord('B') - ord('A')` 的距離是 `1`。因此 `ord('A') + 3 + 1` 等於 `ord('A') + 4`。大寫 'A' 往後數 4 格（A $\rightarrow$ B $\rightarrow$ C $\rightarrow$ D $\rightarrow$ E），用 `chr()` 轉回字元就是 `'E'`。")
    else:
        st.error("❌ 答錯囉！請仔細用手指頭數一下英文字母的相對距離。")

st.markdown("---")

# --- Q6 ---
st.subheader("💡 Q6. 字串大寫與狀態檢查組合")
st.markdown("請閱讀以下程式碼，請問最後輸出的結果為何？")
st.code(r"""
s = "apcs2026"
s2 = s.upper()
res1 = s2.isalpha()
res2 = s2.isdigit()
print(res1, res2)
""", language="python")

q6_ans = st.radio(
    "請選擇答案：",
    ["(A) True False", "(B) False True", "(C) False False", "(D) True True"],
    index=None,
    key="q6"
)
if q6_ans:
    if q6_ans.startswith("(C)"):
        st.success("🎉 答對了！觀念非常扎實！")
        st.info("💡 **解析**：`s.upper()` 會把字串變成 'APCS2026'。因為字串中包含了英文字母與數字：\n* `isalpha()` 要求必須「全部都是字母」才會是 True，因為有數字所以是 False。\n* `isdigit()` 要求必須「全部都是數字」才會是 True，因為有字母所以是 False。\n故兩者皆輸出 `False`。")
    else:
        st.error("❌ 答錯囉！請記得 isalpha() 與 isdigit() 都必須是在「純字母」或「純數字」的情況下才會成立。")

st.markdown("---")

# --- Q7 ---
st.subheader("💡 Q7. 陣列的基礎排序與反轉")
st.markdown("請閱讀以下程式碼，請問最後印出的結果為何？")
st.code(r"""
nums = [15, 5, 25, 10]
nums.sort(reverse=True)
res = nums[1:3]
print(res)
""", language="python")

q7_ans = st.radio(
    "請選擇答案：",
    ["(A) [10, 5]", "(B) [15, 10]", "(C) [25, 15]", "(D) [15, 10, 5]"],
    index=None,
    key="q7"
)
if q7_ans:
    if q7_ans.startswith("(B)"):
        st.success("🎉 答對了！")
        st.info("💡 **解析**：`nums.sort(reverse=True)` 會將陣列由大到小排序，變為 `[25, 15, 10, 5]`。接著進行切片 `nums[1:3]`，會取出索引 1 和索引 2 的元素（不包含索引 3），也就是 `[15, 10]`。")
    else:
        st.error("❌ 答錯囉！請注意由大到小排序後的陣列順序，以及切片左閉右開的特性。")

st.markdown("---")

# --- Q8 ---
st.subheader("💡 Q8. 陣列元素的指定刪除與長度變化")
st.markdown("請閱讀以下程式碼，追蹤 `arr` 陣列的最後狀態與長度：")
st.code(r"""
arr = [1, 2, 3, 2, 4]
arr.remove(2)
del arr[2]
print(arr, len(arr))
""", language="python")

q8_ans = st.radio(
    "請選擇答案：",
    ["(A) [1, 3, 4] 3", "(B) [1, 2, 2, 4] 4", "(C) [1, 2, 4] 3", "(D) [1, 2, 2] 3"],
    index=None,
    key="q8"
)
if q8_ans:
    if q8_ans.startswith("(A)"):
        st.success("🎉 答對了！")
        st.info("💡 **解析**：\n1. 初始狀態為 `[1, 2, 3, 2, 4]`。\n2. `arr.remove(2)` 會刪除從左邊數來第一個遇到的 `2`，此時陣列縮短為 `[1, 3, 2, 4]`。\n3. `del arr[2]` 會刪除當前索引為 2 的元素（此時索引 2 的元素是 `2`），刪除後陣列變為 `[1, 3, 4]`。\n4. 長度則為 3。")
    else:
        st.error("❌ 答錯囉！請一步一步追蹤 remove 與 del 執行後，陣列索引位置產生的動態移位變化。")

st.markdown("---")

# --- Q9 ---
st.subheader("💡 Q9. 不改變原陣列的排序法 `sorted()`")
st.markdown("請閱讀以下程式碼，請問最後印出的 `ans` 數值是多少？")
st.code(r"""
nums = [9, 3, 7, 1]
new_nums = sorted(nums)
ans = nums[0] + new_nums[0]
print(ans)
""", language="python")

q9_ans = st.radio(
    "請選擇答案：",
    ["(A) 2", "(B) 10", "(C) 6", "(D) 18"],
    index=None,
    key="q9"
)
if q9_ans:
    if q9_ans.startswith("(B)"):
        st.success("🎉 答對了！清楚分辨了 sort 與 sorted 的本質差異！")
        st.info("💡 **解析**：`sorted(nums)` 會回傳一個排序好的『全新陣列』`[1, 3, 7, 9]` 給 `new_nums`，而原始的 `nums` 保持不變，依然是 `[9, 3, 7, 1]`。因此 `nums[0]` 是 9，`new_nums[0]` 是 1，兩者相加等於 `10`。")
    else:
        st.error("❌ 答錯囉！請注意 `sorted()` 是不會動到原本的陣列內容的。")

st.markdown("---")

# --- Q10 ---
st.subheader("💡 Q10. 字串的純數字檢查與轉換陷阱")
st.markdown("請閱讀以下程式碼，請問最後輸出的結果是什麼？")
st.code(r"""
data = "123a5"
if data.isdigit():
    print(int(data) + 5)
else:
    print(data + "5")
""", language="python")

q10_ans = st.radio(
    "請選擇答案：",
    ["(A) 12340", "(B) '123a55'", "(C) 語法錯誤", "(D) 12350"],
    index=None,
    key="q10"
)
if q10_ans:
    if q10_ans.startswith("(B)"):
        st.success("🎉 答對了！")
        st.info("💡 **解析**：字串 '123a5' 中包含英文字母 'a'，因此 `data.isdigit()` 的結果為 `False`。程式會執行 `else` 區塊，進行字串的接合：`'123a5' + '5'` 得到 `'123a55'`。")
    else:
        st.error("❌ 答錯囉！請注意 data 內含有非數字字元，且字串相加是進行接合而非數學加法。")

st.markdown("---")

# --- Q11 ---
st.subheader("💡 Q11. 陣列記憶體參照的致命錯誤")
st.markdown("請閱讀以下程式碼，這是沒有使用任何 copy 的直接賦值，請問輸出為何？")
st.code(r"""
list1 = [1, 2, 3]
list2 = list1
list2.append(4)
print(len(list1))
""", language="python")

q11_ans = st.radio(
    "請選擇答案：",
    ["(A) 3", "(B) 4", "(C) 5", "(D) 0"],
    index=None,
    key="q11"
)
if q11_ans:
    if q11_ans.startswith("(B)"):
        st.success("🎉 答對了！完全識破指標參照！")
        st.info("💡 **解析**：在 Python 中寫 `list2 = list1` 並不是複製，而是讓兩個變數同時指向『同一個陣列記憶體』。所以當我們對 `list2` 進行 `append(4)` 時，`list1` 內容也會同時增加。因此 `list1` 的長度變成了 `4`。")
    else:
        st.error("❌ 答錯囉！直接用等號賦值會共享同一個陣列，這是初學者最常犯的錯。")

st.markdown("---")

# --- Q12 ---
st.subheader("💡 Q12. 字串切片的預設邊界")
st.markdown("請閱讀以下程式碼，請問最後印出的結果為何？")
st.code(r"""
s = "Python"
res = s[:2] + s[4:]
print(res)
""", language="python")

q12_ans = st.radio(
    "請選擇答案：",
    ["(A) 'Pyon'", "(B) 'Pyth'", "(C) 'Pytn'", "(D) 'ytho'"],
    index=None,
    key="q12"
)
if q12_ans:
    if q12_ans.startswith("(A)"):
        st.success("🎉 答對了！字串切片掌握得非常好！")
        st.info("💡 **解析**：\n* `s[:2]` 省略起點代表從頭開始，取到索引 1（不含2），即 `'Py'`。\n* `s[4:]` 省略終點代表一路取到最後，從索引 4 開始取，即 `'on'`。\n兩者相加拼接後，結果為 `'Pyon'`。")
    else:
        st.error("❌ 答錯囉！請細心核對每個字元的索引位置（P:0, y:1, t:2, h:3, o:4, n:5）。")

st.markdown("---")

# --- Q13 ---
st.subheader("💡 Q13. 陣列的加總與長度組合計算")
st.markdown("請閱讀以下程式碼，請問最後輸出的結果是多少？")
st.code(r"""
scores = [10, 20, 30, 40]
avg = sum(scores) // len(scores)
print(avg)
""", language="python")

q13_ans = st.radio(
    "請選擇答案：",
    ["(A) 25.0", "(B) 25", "(C) 100", "(D) 20"],
    index=None,
    key="q13"
)
if q13_ans:
    if q13_ans.startswith("(B)"):
        st.success("🎉 答對了！")
        st.info("💡 **解析**：`sum(scores)` 計算總和為 100。`len(scores)` 的長度為 4。進行 `100 // 4` 整除運算（無條件捨去至整數），得到的結果是整數 `25`。")
    else:
        st.error("❌ 答錯囉！請特別看清楚是除法 `/` 還是整除法 `//` 的符號差異。")

st.markdown("---")

# --- Q14 ---
st.subheader("💡 Q14. 尋找數值在陣列中的安全檢查")
st.markdown("請閱讀以下程式碼，追蹤 `ans` 的最終數值：")
st.code(r"""
nums = [5, 15, 25]
target = 20
ans = 0
if target in nums:
    ans = nums.index(target)
else:
    ans = -1
print(ans)
""", language="python")

q14_ans = st.radio(
    "請選擇答案：",
    ["(A) 0", "(B) 1", "(C) 2", "(D) -1"],
    index=None,
    key="q14"
)
if q14_ans:
    if q14_ans.startswith("(D)"):
        st.success("🎉 答對了！這就是競賽中的安全防守寫法！")
        st.info("💡 **解析**：因為 `target` (20) 並不存在於 `nums` 陣列中，所以 `target in nums` 的條件判斷為 `False`。程式會跳到 `else` 執行 `ans = -1`。這樣寫可以有效避免直接使用 `.index()` 找不到元素而造成的程式崩潰。")
    else:
        st.error("❌ 答錯囉！請先判斷 20 有ない在陣列裡面。")

st.markdown("---")

# --- Q15 ---
st.subheader("💡 Q15. 字串的大小寫轉換與元素比對")
st.markdown("請仔細閱讀以下程式碼，請問最後輸出的結果為何？")
st.code(r"""
s1 = "Apcs"
s2 = "APCS"
res = s1.lower() == s2.lower()
print(res)
""", language="python")

q15_ans = st.radio(
    "請選擇答案：",
    options=["(A) True", "(B) False", "(C) None", "(D) 語法錯誤"],
    index=None,
    key="q15"
)
if q15_ans:
    if q15_ans.startswith("(A)"):
        st.success("🎉 恭喜你！完全修正成功，順利通關所有測試！")
        st.info("💡 **解析**：`s1.lower()` 會把 'Apcs' 轉換為全小寫的 'apcs'；同樣地，`s2.lower()` 也會把 'APCS' 轉換為全小寫的 'apcs'。因為轉換後的兩字串內容完全相同，所以使用 `==` 比對的結果為 `True`。")
    else:
        st.error("❌ 答錯囉！請把兩邊都試著轉換成全小寫之後再進行字串比對。")

st.markdown("---")
st.balloons()
st.markdown("### 🏁 綜合挑戰結束！請老師根據學生的答對回饋來進行盲點總結與講講評喔！")
