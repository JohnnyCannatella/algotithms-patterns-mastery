# Floyd's Cycle Finding Algorithm

Other name: Tortoise and Hare Algorithm

È una specifica implementazione del pattern "two pointer" che usa l'approccio "fast and slow" specificamente per:

Trovare cicli
Trovare il punto di inizio di un ciclo
Trovare il punto medio di una linked list
Altri problemi simili su linked list


Time Complexity: O(n)

Technically O(n/2) but again we factor out the constant and we are left with linear time. 
Worst case we have, O(2n) as the small pointer moves around the entire array once. Either way we have O(n) time complexity.

Space Complexity: O(1)

```
Template 1:

def has_cycle(nodes: Node) -> bool:
    p1=p2=nodes
    while p2 and p2.next:
        p1 = p1.next
        p2 = p2.next.next
        if p1 == p2:
            return True
    return False
```
```
Template 2:
def has_cycle(nodes: Node) -> bool:
    tortoise = node_next(nodes)
    hare = node_next(node_next(nodes))
    while tortoise != hare and hare.next is not None:
        tortoise = node_next(tortoise)
        hare = node_next(node_next(hare))
    return hare.next is not None
```