# **REACTO FRAMEWORK**

Il metodo REACTO è un framework strutturato per affrontare i problemi di coding durante le interviste tecniche. Vediamolo nel dettaglio:

### R - Repeat

* Ripeti il problema con parole tue
* Chiedi chiarimenti
* Verifica assumptions

```
"Let me make sure I understand the problem correctly..."
"So, we need to find [X] given [Y], and we need to handle [Z] cases?"
```

### E - Examples

* Scrivi 2-3 esempi concreti
* Includi edge cases
* Verifica gli esempi con l'intervistatore

```
"Let me write down some examples:
Input: [1,2,3] → Output: 6
Edge case 1: [] → Output: 0
Edge case 2: [-1,2] → Output: 1"
```

### A - Approach
* Pensa ad alta voce
* Discuti diverse soluzioni
* Analizza pro/contro di ogni approccio

```
"We could solve this in several ways:
1. Brute force approach: O(n²)
2. Using hash table: O(n) space, O(n) time
3. Two pointer approach: O(1) space, O(n) time"
```

### C - Code
* Scrivi codice pulito e leggibile
* Usa nomi di variabili significativi
* Commenta sezioni importanti
```
def solution(nums):
    # Initialize variables
    left, right = 0, len(nums) - 1
    
    # Process array using two pointers
    while left < right:
        # Logic here
```

### T - Test
* Testa con gli esempi discussi
* Verifica edge cases
* Dry run del codice
```
Let me walk through the code with our example:
Input: [1,2,3]
Step 1: left=0, right=2
Step 2: ..."
```

### O - Optimize
* Discuti complessità (tempo/spazio)
* Proponi ottimizzazioni
* Discuti trade-offs
```
The current solution is O(n) time and O(1) space.
We could optimize by..."
```

Esempio Pratico:
```
Problem: Two Sum
# Given an array of integers nums and an integer target, 
# return indices of two numbers that add up to target.

# REACTO Analysis:

# R - Repeat
"We need to find two numbers in the array that sum to the target
and return their indices. Numbers can't be used twice."

# E - Examples
"Let's look at some examples:
nums = [2,7,11,15], target = 9 → [0,1]
nums = [3,3], target = 6 → [0,1]
nums = [], target = 0 → []"

# A - Approach
"We could use a hash table to store numbers we've seen.
This gives us O(n) time complexity instead of O(n²) of brute force."

# C - Code
def twoSum(nums, target):
    seen = {}  # val -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

# T - Test
"Let's test with [2,7,11,15], target = 9:
i=0: seen={2:0}
i=1: 9-7=2 found in seen → return [0,1]"

# O - Optimize
"Time: O(n), Space: O(n)
Could use two pointers if array was sorted, 
but would need O(n log n) for sorting."
```
Questo metodo è particolarmente efficace perché:

Ti forza a essere strutturato
Dimostra il tuo processo di pensiero
Non salti passaggi importanti
Comunichi efficacemente con l'intervistatore