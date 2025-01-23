
# LINKED LIST

Una linked list normale è una sequenza di nodi dove ogni nodo punta al successivo, e l'ultimo nodo punta a null:
1 -> 2 -> 3 -> 4 -> null

Una linked list con un ciclo è quando un nodo, invece di puntare a null, punta a un nodo precedente nella lista, creando un "loop" infinito:
 1 -> 2 -> 3 -> 4
 ^         |
 |_________|

in una linked list conosco solo il .next e non so mai chi è il precedente
Non ho la lunghezza della lista -> len(head) non posso farlo
Non è sortable

Caratteristiche principali:
* Elementi sparsi in memoria
* Ogni nodo contiene il dato e il riferimento al prossimo
* No accesso diretto, necessario attraversamento

PATTERN COMUNI PER LINKED LIST:
* Floyd's Tortoise and Hare (quando usata per trovare cicli)
  * Fast/Slow Pointers
  * Runner Technique
  * Two Pointer Technique (nella variante fast/slow)
* Reverse in gruppi di K
* Dummy Node

### Base function
```
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

1. Creazione di un nuovo nodo:
new_node = ListNode(val)

2.Accesso al valore:
node_value = curr.val

3.Spostamento al nodo successivo:
curr = curr.next

4.Inserimento dopo un nodo:
new_node = ListNode(val)
new_node.next = curr.next
curr.next = new_node

```

### Pattern
```
1.Pattern Dummy Node:
dummy = ListNode(0)
curr = dummy
# ... operazioni ...
return dummy.next

2.Pattern Two Pointer (Fast/Slow):
slow = head
fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
```

### build function
```
class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, val):  # O(n)
        if not self.head:
            self.head = ListNode(val)
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = ListNode(val)
    
    def prepend(self, val):  # O(1)
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node
```


### Advanced function
```
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0  # utile per tenere traccia della dimensione
    
    # Inserimento in posizione specifica O(n)
    def insert_at(self, index, val):
        if index < 0 or index > self.size:
            raise ValueError("Indice non valido")
            
        if index == 0:
            self.head = ListNode(val, self.head)
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            current.next = ListNode(val, current.next)
        self.size += 1
    
    # Eliminazione per valore O(n)
    def delete_value(self, val):
        if not self.head:
            return
        
        if self.head.val == val:
            self.head = self.head.next
            self.size -= 1
            return
            
        current = self.head
        while current.next and current.next.val != val:
            current = current.next
            
        if current.next:
            current.next = current.next.next
            self.size -= 1
    
    # Reverse della lista O(n)
    def reverse(self):
        prev = None
        current = self.head
        
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            
        self.head = prev
    
    # Ricerca di un ciclo (Floyd's Algorithm) O(n)
    def has_cycle(self):
        if not self.head:
            return False
            
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
       
```