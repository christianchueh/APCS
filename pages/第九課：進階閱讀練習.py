import streamlit as st

# 設定網頁標題與風格
st.set_page_config(page_title="APCS 第九課：字串與陣列綜合挑戰賽", layout="wide")

st.title("🏆 APCS 第九課：字串與陣列進階觀念挑戰賽")
st.caption("適用 Python 3.14 環境 | 15 題高難度程式閱讀與觀念辨析題")
st.markdown("👉 **請仔細閱讀程式碼並追蹤變數變化，點選選項後系統將即時回饋正誤與詳細解析！**")
st.markdown("---")

# 初始化分數（如果需要統計）
if "score" not in st.session_state:
    st.session_state.score = 0

# ==============================================================================
# Q1 - Q15 題目與即時反饋系統
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
    ["(A) 'y_0'", "(B) 'htP_02'", "(C) 'hP_2'", "(D) 'yP2'"],
    index=None,
    key="q1"
)
if q1_ans:
    if q1_ans.startswith("(C)"):
        st.success("🎉 答對了！")
        st.info("💡 **解析**：`s[-4]` 是 'y'。起點為索引 -4（'y'），終點為索引 2（'C'，但不包含），步長為 `-2`（向左每兩格跳一次）。因此會抓取索引 -4 ('y') $\rightarrow$ 索引 -6 ('_') $\rightarrow$ 索引 -8 ('6') $\rightarrow$ 索引 -10 ('2') $\rightarrow$ 索引 -12 ('C'已超出範圍不含)。答案為 `'hP_2'`。")
    else:
        st.error("❌ 答錯囉，再仔細推導一次！提示：負數步長是往左走，且不包含終點。")

st.markdown("---")

# --- Q2 ---
st.subheader("💡 Q2. 二維陣列的淺複製（Shallow Copy）陷阱")
st.markdown("請閱讀以下程式碼，請問最後輸出的 `A` 陣列內容為何？")
st.code(r"""
A = [[1, 2], [3, 4]]
B = A.copy()
B.append([5, 6])
B[0][1] = 99
print(A)
""", language="python")

q2_ans = st.radio(
    "請選擇答案：",
    ["(A) [[1, 2], [3, 4]]", "(B) [[1, 99], [3, 4]]", "(C) [[1, 99], [3, 4], [5, 6]]", "(D) [[1, 2], [3, 4], [5, 6]]"],
    index=None,
    key="q2"
)
if q2_ans:
    if q2_ans.startswith("(B)"):
        st.success("🎉 答對了！老師給您點讚！")
        st.info("💡 **解析**：`A.copy()` 是淺複製。外層獨立，所以 `B.append([5, 6])` 不會影響 `A`；但是內層的子陣列 `[1, 2]` 與 `[3, 4]` 的記憶體位置是共享的。因此修改 `B[0][1] = 99` 會連帶改變 `A[0][1]`。")
    else:
        st.error("❌ 答錯了！這是經典的二維陣列複製大坑，請注意外層與內層記憶體的共享關係。")

st.markdown("---")

# --- Q3 ---
st.subheader("💡 Q3. 雙重條件排序（Lambda）之謎")
st.markdown("請閱讀以下程式碼，請問最後排序後的輸出結果為何？")
st.code(r"""
data = [(3, "apple"), (2, "banana"), (3, "ants"), (1, "cherry")]
data.sort(key=lambda x: (-x[0], x[1]))
print(data)
""", language="python")

q3_ans = st.radio(
    "請選擇答案：",
    ["(A) [(1, 'cherry'), (2, 'banana'), (3, 'ants'), (3, 'apple')]", 
     "(B) [(3, 'apple'), (3, 'ants'), (2, 'banana'), (1, 'cherry')]", 
     "(C) [(3, 'ants'), (3, 'apple'), (2, 'banana'), (1, 'cherry')]", 
     "(D) [(1, 'cherry'), (2, 'banana'), (3, 'apple'), (3, 'ants')]"],
    index=None,
    key="q3"
)
if q3_ans:
    if q3_ans.startswith("(C)"):
        st.success("🎉 答對了！完美掌握多重排序！")
        st.info("💡 **解析**：排序鍵為 `(-x[0], x[1])`。第一個欄位 `-x[0]` 代表數字「由大到小（降序）」排，所以數字 3 的元素會排在前面；當第一個欄位相同時（都是 3），則比對第二個欄位 `x[1]`（字串字典序由小到大），因 `'ants'` 字典序小於 `'apple'`，故 `'ants'` 在前。")
    else:
        st.error("❌ 答錯囉！請注意元組內第一個欄位加上負號後的排列順序變化。")

st.markdown("---")

# --- Q4 ---
st.subheader("💡 Q4. 萬惡的列表推導式與條件過濾")
st.markdown("請問下列程式碼執行後，變數 `result` 的長度 `len(result)` 為何？")
st.code(r"""
result = [x * y for x in range(1, 5) for y in range(1, 5) if (x + y) % 3 == 0]
print(len(result))
""", language="python")

q4_ans = st.radio(
    "請選擇答案：",
    ["(A) 4", "(B) 5", "(C) 6", "(D) 16"],
    index=None,
    key="q4"
)
if q4_ans:
    if q4_ans.startswith("(B)"):
        st.success("🎉 答對了！程式碼追蹤能力一流！")
        st.info("💡 **解析**：雙重迴圈的 $x$ 與 $y$ 範圍皆為 1 到 4。滿足 `(x + y) % 3 == 0` 的配對有：(1,2), (2,1), (2,4), (3,3), (4,2)。總共 5 個組合，故長度為 5。")
    else:
        st.error("❌ 答錯囉！請動手列出所有 $1 \le x, y \le 4$ 且和為 3 的倍數的組合。")

st.markdown("---")

# --- Q5 ---
st.subheader("💡 Q5. ASCII 碼與字元循環平移")
st.markdown("請閱讀以下程式碼，此演算法常用於密碼學（凱撒密碼），請問輸出為何？")
st.code(r"""
def shift_char(c, k):
    if c.isalpha():
        base = ord('A') if c.isupper() else ord('a')
        return chr((ord(c) - base + k) % 26 + base)
    return c

print(shift_char('z', 3))
""", language="python")

q5_ans = st.radio(
    "請選擇答案：",
    ["(A) 'c'", "(B) 'b'", "(C) 'a'", "(D) '{'"],
    index=None,
    key="q5"
)
if q5_ans:
    if q5_ans.startswith("(A)"):
        st.success("🎉 答對了！演算法邏輯非常清晰！")
        st.info("💡 **解析**：'z' 的 `ord('z') - ord('a')` 等於 25。加上平移量 3 變成 28，經過 `% 26` 餘數為 2。最後 `2 + ord('a')` 得到 `ord('c')`，轉回字元即為 `'c'`。實現了英文字母底部的循環平移。")
    else:
        st.error("❌ 答錯囉！請特別注意 `% 26` 的循環邊界處理。")

st.markdown("---")

# --- Q6 ---
st.subheader("💡 Q6. 字串與陣列成員檢查（in）的效率陷阱")
st.markdown("關於 Python 指令 `if x in container:` 的時間複雜度，下列敘述何者**錯誤**？")
st.code(r"""
# 假設 A 是長度為 N 的 List
# 假設 B 是長度為 N 的 String
# 假設 C 是長度為 N 的 Set
""", language="python")

q6_ans = st.radio(
    "請選擇答案：",
    ["(A) 在 A 中檢查的時間複雜度為 O(N)", 
     "(B) 在 B 中檢查的時間複雜度為 O(N)", 
     "(C) 在 C 中檢查的時間複雜度為 O(1)", 
     "(D) 三者在大數據競賽題中的檢查效率完全一致"],
    index=None,
    key="q6"
)
if q6_ans:
    if q6_ans.startswith("(D)"):
        st.success("🎉 答對了！觀念題拿下了！")
        st.info("💡 **解析**：List 與 String 的 `in` 檢查需要逐一比對，時間複雜度為 $O(N)$；而 Set 基於雜湊表（Hash Table），其 `in` 檢查平均只需要 $O(1)$。所以在 APCS 等大數據量競賽中，效率差異極大！(D) 敘述是錯誤的。")
    else:
        st.error("❌ 答錯囉！請回想第三課或第八課提及的雜湊（Set）與線性搜尋（List）的效能差異。")

st.markdown("---")

# --- Q7 ---
st.subheader("💡 Q7. 位元反轉（~）在切片中的神奇妙用")
st.markdown("請閱讀以下程式碼，請問最後印出的結果為何？")
st.code(r"""
arr = [10, 20, 30, 40, 50]
res = [arr[i] + arr[~i] for i in range(2)]
print(res)
""", language="python")

q7_ans = st.radio(
    "請選擇答案：",
    ["(A) [20, 40]", "(B) [60, 60]", "(C) [50, 70]", "(D) [10, 50]"],
    index=None,
    key="q7"
)
if q7_ans:
    if q7_ans.startswith("(B)"):
        st.success("🎉 答對了！連二進位補數切片都難不倒你！")
        st.info("💡 **解析**：在 Python 索引中，`~i` 等同於 `-i - 1`。當 `i = 0` 時，`arr[0]` 為 10，`arr[~0]`（即 `arr[-1]`）為 50，和為 60；當 `i = 1` 時，`arr[1]` 為 20，`arr[~1]`（即 `arr[-2]`）為 40，和亦為 60。故答案為 `[60, 60]`。這個技巧常用於首尾兩兩對稱配對。")
    else:
        st.error("❌ 答錯囉！提示：Python 中 ~0 = -1, ~1 = -2，這代表從陣列後方倒數過來的索引。")

st.markdown("---")

# --- Q8 ---
st.subheader("💡 Q8. 陣列原地修改（In-place）與走訪機制")
st.markdown("請閱讀以下程式碼，追蹤 `nums` 陣列的最後狀態：")
st.code(r"""
nums = [1, 2, 3, 4, 5]
for x in nums:
    if x % 2 == 0:
        nums.remove(x)
print(nums)
""", language="python")

q8_ans = st.radio(
    "請選擇答案：",
    ["(A) [1, 3, 5]", "(B) [1, 2, 3, 5]", "(C) [1, 3, 4, 5]", "(D) [1, 3]"],
    index=None,
    key="q8"
)
if q8_ans:
    if q8_ans.startswith("(C)"):
        st.success("🎉 答對了！成功避開動態刪除的陷阱！")
        st.info("💡 **解析**：在走訪 List 的同時進行 `remove` 會導致索引指標錯位。當指標走到索引 1（元素 2）時將其刪除，陣列縮短為 `[1, 3, 4, 5]`。下一步迴圈指標走向索引 2，這時索引 2 的元素已經變成 4 了，因此**元素 3 被完美漏掉了**！隨後元素 4 符合條件被刪除，陣列變為 `[1, 3, 5]`。接著指標走向索引 3，而此時陣列最大索引僅到 2，迴圈提前結束。因此 4 被刪除了，但 2 後面的部分受了影響，最終存留的是 `[1, 3, 4, 5]`。")
    else:
        st.error("❌ 答錯囉！這題極具迷惑性，迴圈走訪時刪除元素會導致後方元素往前遞補，造成「漏看」下一項的現象。")

st.markdown("---")

# --- Q9 ---
st.subheader("💡 Q9. 多維陣列初始化大魔王")
st.markdown("以下兩種建立二維陣列的方法，哪一種敘述是正確的？")
st.code(r"""
method1 = [[0] * 3] * 3
method2 = [[0] * 3 for _ in range(3)]

method1[0][0] = 5
method2[0][0] = 5
""", language="python")

q1_ans = st.radio(
    "請選擇答案：",
    ["(A) 兩種方法修改後，對應的二維陣列都只有一個元素變成 5", 
     "(B) method1 的第一直行全部變成 5；method2 只有一個元素變成 5", 
     "(C) method2 的第一直行全部變成 5；method1 只有一個元素變成 5", 
     "(D) 兩種方法修改後，兩者的第一直行都會全部變成 5"],
    index=None,
    key="q9"
)
if q1_ans:
    if q1_ans.startswith("(B)"):
        st.success("🎉 答對了！APCS 實作題最常因為這個除錯除到崩潰！")
        st.info("💡 **解析**：`[[0]*3]*3` 是把同一個子陣列物件「複製了三次參照」，因此改變其中一個，另外兩列也會跟著變！而 `List 推導式` 的 `method2` 每次循環都是重新產出獨立的新陣列，彼此不干擾。")
    else:
        st.error("❌ 答錯囉！乘號 `*` 用於複製巢狀物件時只會複製記憶體指標，請特別小心。")

st.markdown("---")

# --- Q10 ---
st.subheader("💡 Q10. 陣列的累計前綴和（Prefix Sum）與切片運用")
st.markdown("前綴和是演算法必修。閱讀以下程式碼，請問 `sum(P[1:4])` 計算的是原陣列 `A` 的哪一部分？")
st.code(r"""
A = [2, 4, 1, 5, 3]
P = [0] * (len(A) + 1)
for i in range(len(A)):
    P[i+1] = P[i] + A[i]
# P 目前為 [0, 2, 6, 7, 12, 15]
""", language="python")

q10_ans = st.radio(
    "請選擇答案：",
    ["(A) A[1] + A[2] + A[3]", "(B) P[1] + P[2] + P[3] 的值，與 A 無關", "(C) A[0] + A[1] + A[2]", "(D) A[0] + A[1] + A[2] + A[3]"],
    index=None,
    key="q10"
)
if q10_ans:
    if q10_ans.startswith("(B)"):
        st.success("🎉 答對了！")
        st.info("💡 **解析**：題目問的是 `sum(P[1:4])`，也就是 `P[1] + P[2] + P[3]` 三個數字相加，純粹是前綴和陣列本身的元素加總（$2+6+7=15$）。如果是要求原陣列某區間的區間和，公式通常是 `P[R] - P[L]` 這種相減形式，而非對 P 直接進行 `sum()`。")
    else:
        st.error("❌ 答錯囉！請看清楚題目是問 `sum(P[1:4])` 還是利用 P 的相減求 A 的區間和，不要落入思維慣性。")

st.markdown("---")

# --- Q11 ---
st.subheader("💡 Q11. 字串狀態判斷 methods 聯手突擊")
st.markdown("請閱讀以下程式碼，請問最後印出的結果是什麼？")
st.code(r"""
data = ["123", "Python3", "APCS", "  "]
res = [x.isalnum() and not x.isdigit() for x in data]
print(res)
""", language="python")

q11_ans = st.radio(
    "請選擇答案：",
    ["(A) [True, True, True, False]", 
     "(B) [False, True, True, False]", 
     "(C) [False, True, False, False]", 
     "(D) [True, True, False, False]"],
    index=None,
    key="q11"
)
if q11_ans:
    if q11_ans.startswith("(B)"):
        st.success("🎉 答對了！邏輯判斷非常精準！")
        st.info("💡 **解析**：條件為「是英文或數字（`isalnum()`）」且「不能純粹是數字（`not isdigit()`）」：\n* `'123'`：`isalnum` 為 True，但 `isdigit` 為 True，故結果為 False。\n* `'Python3'`：滿足兩者，為 True。\n* `'APCS'`：滿足兩者（全英文也是 alnum 之一），為 True。\n* `'  '`：不滿足 alnum，為 False。")
    else:
        st.error("❌ 答錯囉！請記住 `isalnum()` 在純英文字母或純數字時，都會回傳 True。")

st.markdown("---")

# --- Q12 ---
st.subheader("💡 Q12. 矩陣轉置（Transpose）的一行流")
st.markdown("請閱讀以下利用 `zip` 配合拆解運算子（`*`）的經典語法，請問它的功能為何？")
st.code(r"""
matrix = [[1, 2, 3], 
          [4, 5, 6]]
transposed = [list(x) for x in zip(*matrix)]
print(transposed)
""", language="python")

q12_ans = st.radio(
    "請選擇答案：",
    ["(A) [[1, 4], [2, 5], [3, 6]]", "(B) [[1, 2, 3], [4, 5, 6]]", "(C) [[3, 2, 1], [6, 5, 4]]", "(D) [[4, 5, 6], [1, 2, 3]]"],
    index=None,
    key="q12"
)
if q12_ans:
    if q12_ans.startswith("(A)"):
        st.success("🎉 答對了！連高階的 zip 拆解都難不倒您！")
        st.info("💡 **解析**：`zip(*matrix)` 等同於 `zip([1, 2, 3], [4, 5, 6])`。它會把相同索引的元素打包在一起，分別打包出 `(1, 4)`、`(2, 5)`、`(3, 6)`。轉成 list 後就成功將 $2 \times 3$ 的矩陣翻轉轉置成 $3 \times 2$ 矩陣！")
    else:
        st.error("❌ 答錯囉！這行指令在 APCS 地圖/矩陣題型中是非常常見的「轉置（翻轉橫縱軸）」神技，建議背下來。")

st.markdown("---")

# --- Q13 ---
st.subheader("💡 Q13. 貪婪的字串最大連續不重複子字串")
st.markdown("請仔細追蹤以下迴圈，計算變數 `max_len` 最後的數值是多少？")
st.code(r"""
s = "pwwkew"
seen = []
max_len = 0
for char in s:
    while char in seen:
        seen.pop(0)
    seen.append(char)
    max_len = max(max_len, len(seen))
print(max_len)
""", language="python")

q13_ans = st.radio(
    "請選擇答案：",
    ["(A) 2", "(B) 3", "(C) 4", "(D) 5"],
    index=None,
    key="q13"
)
if q13_ans:
    if q13_ans.startswith("(B)"):
        st.success("🎉 答對了！LeetCode 經典滑動視窗題被你秒殺了！")
        st.info("💡 **解析**：這是經典的「滑動視窗（Sliding Window）」演算法。遇到重複字元時會吐出左側字元直到不重複。字串 `\"pwwkew\"` 的最長不重複子字串為 `\"wke\"` 或 `\"kew\"`，長度皆為 3。")
    else:
        st.error("❌ 答錯囉！請拿紙筆模擬 `seen` 陣列在遇到第二個 'w' 還有最後一個 'w' 時的 `pop(0)` 變化歷程。")

st.markdown("---")

# --- Q14 ---
st.subheader("💡 Q14. 陣列的深複製與多層巢狀修改")
st.markdown("請閱讀以下程式碼，使用了 `copy.deepcopy()`，請問最後輸出的 `data` 內容為何？")
st.code(r"""
import copy
data = [1, [2, 3], (4, 5)]
new_data = copy.deepcopy(data)
new_data[1][0] = 99
print(data)
""", language="python")

q14_ans = st.radio(
    "請選擇答案：",
    ["(A) [1, [99, 3], (4, 5)]", "(B) [1, [2, 3], (4, 5)]", "(C) [1, [2, 3], (99, 5)]", "(D) 程式會拋出 TypeError 錯誤"],
    index=None,
    key="q14"
)
if q14_ans:
    if q14_ans.startswith("(B)"):
        st.success("🎉 答對了！深複製的概念掌握得天衣無縫！")
        st.info("💡 **解析**：因為使用的是 `copy.deepcopy()`，不論物件巢狀疊了多少層，所有的可變物件（如裡面的 List）都會在獨立的記憶體中重新生成一份副本。因此修改 `new_data` 絕對不會影響到元始的 `data`。")
    else:
        st.error("❌ 答錯囉！請認清 `deepcopy`（深複製）與 `copy`（淺複製）在處理內部可變物件時的本質差別。")

st.markdown("---")

# --- Q15 ---
st.subheader("💡 Q15. 終極魔王：字串排序與 ASCII 權重結合")
st.markdown("請仔細閱讀以下排序規則，請問最後經 `sorted()` 處理後的字串為何？")
st.code(r"""
s = "A1b2C3d"
# 排序規則：如果是數字排前面，字母排後面
# 若同類，則維持原本的字元大小
res = sorted(s, key=lambda x: (x.isalpha(), x))
print("".join(res))
""", language="python")

q15_ans = st.radio(
    "請選擇答案：",
    ["(A) '123AbCd'", "(B) '123ACbd'", "(C) '123AbCd'", "(D) '123ACbd'（註：請注意選項細微大小寫順序）", "(E) '123ACbd'"], 
    options=["(A) '123ACbd'", "(B) '123AbCd'", "(C) '123bAdC'", "(D) 'AbCd123'"],
    index=None,
    key="q15"
)
if q15_ans:
    if q15_ans.startswith("(A)"):
        st.success("🎉 恭喜你！通過了終極魔王關卡！太厲害了！")
        st.info("💡 **解析**：`key=lambda x: (x.isalpha(), x)` 建立了一個二元組排序標準：\n1. 第一關 `x.isalpha()`：數字會得到 `False` (0)，字母得到 `True` (1)。因為 0 < 1，所以所有數字會被排在所有字母的前面。\n2. 第二關 `x`：當同為數字或同為字母時，比對字元本身的 ASCII 碼大小。數字部分 `'1' < '2' < '3'`；字母部分，ASCII 碼中大寫字母小於小寫字母（如 `'A'`是65，`'b'`是98），所以大寫排在小寫前面，即 `'A' < 'C' < 'b' < 'd'`。綜合兩關，結果為 `'123ACbd'`。")
    else:
        st.error("❌ 哇！差一點點！請特別比對 ASCII 碼中，大寫字母與小寫字母的大小順序關係。")

st.markdown("---")
st.balloons()
st.center = st.markdown("### 🏁 挑戰結束！老師可以統計一下同學們答對了幾題喔！")
