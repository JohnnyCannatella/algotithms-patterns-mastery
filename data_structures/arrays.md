
# ARRAY (List in Python)

Caratteristiche principali:
* Memoria contigua
* Accesso diretto agli elementi tramite indice
* Dimensione dinamica in Python

Operazioni e complessità:
```
# Operazioni base - List
lst = []  # creazione, O(1)
lst.append(5)  # aggiunta in coda, O(1) amortized
lst.insert(0, 3)  # inserimento in posizione, O(n)
lst.pop()  # rimozione dall'ultimo, O(1)
lst.pop(0)  # rimozione da posizione, O(n)
elemento = lst[2]  # accesso diretto, O(1)
length = len(lst)  # lunghezza, O(1)`
```

```
# Slicing
lst = [1, 2, 3, 4, 5]
sub_list = lst[1:4]  # [2, 3, 4]
reversed_list = lst[::-1]  # [5, 4, 3, 2, 1]

# List Comprehension
squares = [x**2 for x in range(10) if x % 2 == 0]

# Operazioni con multiple liste
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2  # concatenazione
zipped = list(zip(list1, list2))  # [(1,4), (2,5), (3,6)]

# Ordinamento
lst.sort()  # in-place
lst.sort(key=lambda x: len(str(x)))  # ordinamento custom
sorted_list = sorted(lst, reverse=True)  # nuovo array ordinato

# Filtraggio
filtered = list(filter(lambda x: x > 0, lst))
```