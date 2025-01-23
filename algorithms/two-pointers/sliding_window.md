# Sliding window Pattern

**Description**
Sliding window problems are a variant of the same direction two pointers problems
This pattern involves a “window” that slides across the array or string. The window can be of a fixed or variable length, 
helping you maintain a subset of elements as you move along, such as a cumulative sum or count.

**Common Uses**
It’s useful in problems requiring you to find subarrays or substrings with certain properties, such as a target sum or unique elements within a range. 
Sliding window is ideal for keeping track of contiguous intervals.

**Example**
Finding the longest substring without repeating characters, or the maximum sum of k consecutive elements.

**When use it**
Focuses on maintaining a subset of contiguous elements within the data.
Somma/media/massimo di k elementi consecutivi
Sottostringa più lunga con certe proprietà
Subarrays che soddisfano una condizione

**Classification**
1. Fixed Size windo
```
# Esempio: trova la massima somma di k elementi consecutivi
`window_sum = sum(arr[:k])  # prima finestra
max_sum = window_sum

for i in range(k, len(arr)):
    window_sum = window_sum + arr[i] - arr[i-k]  # aggiungi nuovo, togli vecchio
    max_sum = max(max_sum, window_sum)
```

2. Flexible Size Sliding Window
```
# Esempio: trova la sottostringa più lunga senza caratteri ripetuti
start = 0
max_length = 0
char_set = set()

for end in range(len(s)):
    while s[end] in char_set:  # riduci finestra se necessario
        char_set.remove(s[start])
        start += 1
    char_set.add(s[end])  # espandi finestra
    max_length = max(max_length, end - start + 1)
```

**keywords**
```
• consecutive
• substring
• subarray
• window of dimension k
• all the contiguous elements
```
**Trucchi e Pattern comuni**

1. Spesso usi due puntatori: start e end della finestra
2. Mantieni una variabile per tracciare la condizione nella finestra
3. Pattern comune:
```
start = 0
for end in range(len(array)):
    # 1. Aggiungi elemento a end
    # 2. Mentre la condizione non è soddisfatta:
    #    - Rimuovi elementi da start
    #    - Incrementa start
    # 3. Aggiorna il risultato
```

**Flexible Size Sliding Window Template - Shortest**
```
def sliding_window_flexible_shortest(input):
    initialize window, ans
    left = 0
    for right in range(len(input)):
        append input[right] to window
        while valid(window):
            ans = min(ans, window)      # window is guaranteed to be valid here
            remove input[left] from window
            left += 1
    return ans
```