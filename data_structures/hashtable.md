# hashmap 

Una HashTable (o Dictionary in Python) è una struttura dati che memorizza coppie chiave-valore usando una funzione di hashing

Time complexity:
• update: O(1) in media
• find: O(1) in media
• remove: O(1) in media
• get: O(1) in media

NOTA IMPORTANTE: Ho detto "in media" perché nel caso peggiore (molte collisioni) potrebbe diventare O(n).


```
Two Sum (LeetCode #1)
def twoSum(nums, target):
    seen = {}  # HashMap per memorizzare i numeri già visti
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
```

## **Creazione e Operazioni Base:**
```
# Creazione
dict1 = {}  # dizionario vuoto
dict2 = {'nome': 'Marco', 'età': 25}  # con valori iniziali

# Inserimento/Modifica
dict1['chiave'] = 'valore'  # aggiunge o modifica
dict1.update({'k1': 'v1', 'k2': 'v2'})  # aggiunge/modifica multiple chiavi

# Accesso
valore = dict1['chiave']  # lancia KeyError se non esiste
valore = dict1.get('chiave', 'default')  # return 'default' se non esiste

# Eliminazione
del dict1['chiave']  # elimina una coppia
dict1.pop('chiave', None)  # elimina e ritorna il valore (None se non esiste)
dict1.clear()  # svuota il dizionario

# 1. Copia di dizionari
dict1 = {'a': 1, 'b': 2}
shallow_copy = dict1.copy()  # copia superficiale
deep_copy = import copy; copy.deepcopy(dict1)  # copia profonda

# 2. Unione di dizionari
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
# Metodo 1 (Python 3.5+)
unione1 = {**dict1, **dict2}
# Metodo 2 (Python 3.9+)
unione2 = dict1 | dict2

# 3. Dizionario da liste
chiavi = ['a', 'b', 'c']
valori = [1, 2, 3]
nuovo_dict = dict(zip(chiavi, valori))  # {'a': 1, 'b': 2, 'c': 3}

# 4. Dizionario comprehension
quadrati = {x: x**2 for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# 5. Operazioni con setdefault
dict1 = {}
# Aggiunge la chiave con un valore default se non esiste
valore = dict1.setdefault('chiave', []).append(1)

# 6. Operazioni con valori nested
nested_dict = {
    'persona1': {'nome': 'Marco', 'età': 25},
    'persona2': {'nome': 'Laura', 'età': 30}
}
# Accesso a valori nested
età_marco = nested_dict['persona1']['età']

# 7. Filtraggio di dizionari
dict1 = {'a': 1, 'b': 2, 'c': 3}
# Filtra chiavi che soddisfano una condizione
filtered = {k: v for k, v in dict1.items() if v > 1}

# 8. Inversione chiavi-valori
dict1 = {'a': 1, 'b': 2}
inverted = {v: k for k, v in dict1.items()}

# 9. fromkeys() - crea dizionario con valori default
chiavi = ['a', 'b', 'c']
dict_default = dict.fromkeys(chiavi, 0)  # {'a': 0, 'b': 0, 'c': 0}

# 10. Controlli vari
dict1 = {'a': 1, 'b': 2}
len(dict1)  # numero di coppie chiave-valore
'a' in dict1  # verifica esistenza chiave
2 in dict1.values()  # verifica esistenza valore

# 11. Ordinamento
dict1 = {'c': 3, 'a': 1, 'b': 2}
# Per chiavi
sorted_keys = dict(sorted(dict1.items()))
# Per valori
sorted_values = dict(sorted(dict1.items(), key=lambda x: x[1]))
```

## **Metodi utili:**
```
# Verifica esistenza
if 'chiave' in dict1:  # verifica se esiste una chiave
    print("Chiave trovata!")

# Ottenere tutte le chiavi/valori
chiavi = dict1.keys()
valori = dict1.values()
coppie = dict1.items()  # ritorna tuple (chiave, valore)

# Iterazione
for chiave in dict1:  # itera sulle chiavi
    print(chiave)

for chiave, valore in dict1.items():  # itera su chiavi e valori
    print(f"{chiave}: {valore}")
```
## **Casi d'uso comuni::**
* Conteggio frequenze
* Raggruppamento
* Caching/Memoization (Fibonacci)


## **Pattern comuni nei colloqui** ##
```
# Pattern: HashMap come contatore
def trova_duplicati(nums):
    counter = {}
    duplicati = []
    for num in nums:
        if num in counter:
            duplicati.append(num)
        counter[num] = counter.get(num, 0) + 1
    return duplicati

# Pattern: HashMap per lookup veloce
def trova_anagrammi(parole):
    gruppi = {}
    for parola in parole:
        # Ordina i caratteri come chiave
        chiave = ''.join(sorted(parola))
        if chiave not in gruppi:
            gruppi[chiave] = []
        gruppi[chiave].append(parola)
    return list(gruppi.values())`
```

## **Trucchi e Best Practices:**
* Usa .get() invece di [] quando possibile per evitare KeyError
* Per conteggi, usa collections.Counter
* Per valori di default, considera collections.defaultdict
* Ricorda che le chiavi devono essere immutabili (no liste, sì tuple)