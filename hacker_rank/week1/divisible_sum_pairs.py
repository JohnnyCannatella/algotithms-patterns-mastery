#!/bin/python3
import math
import os

#EXCERCISE
"""
    excercise:
        Given an array of integers and a positive integer , determine the number of  pairs where  and  +  is divisible by .
    arg:
        - array of positive integer
        - positivi integer that i need to apply the condition
    output:
        - the number of  pairs
    notes:
    divisibleSumPairs has the following parameter(s):
        - int n: the length of array 
        - int ar[n]: an array of integers
        - int k: the integer divisor
    The first line contains  space-separated integers, n and k
    The second line contains n space-separated integers, each a value of arr[i]
"""


#PROBLEM SOLVING
"""
    Arg:
    we'll receive in the first line a two positive integers n -> lenght of array and k -> integer divisor
    in the second line instead we'll receive  the array to process.
    So i need to get that values and pass them in divisibleSumPairs where we can procede with this steps:
    - we'll need a count_pairs variable used to count the pairs
    - we'll need to an nested loops to combine all the pairs and apply the rule
    - for each combination we'll increase count_pairs
    a the end we'll return count_pairs
    
    Rule to apply:
    - I have to apply this rule where i < j and ar[i] + ar[j] is / k
    
    Output:
    - is a positive int number that rappresent count of pairs combinations that respect before rule
    
    questions:
    - I can use particular python math library ?
    - is the array just of positive integer ? 
    
"""

#INTERVIEWER QUESTION
"""
Interviewer questions:  
    - Hai menzionato l'uso di cicli annidati. Quale sarebbe la complessità temporale di questo approccio? Ci sono potenziali problemi con questa strategia per array molto grandi?
    - Hai considerato come gestire il caso in cui l'array è vuoto o contiene un solo elemento?
    - La tua domanda sulle librerie matematiche di Python è interessante. Quali operazioni matematiche specifiche pensi potrebbero essere utili per questo problema?
    - Riguardo alla tua domanda sugli interi positivi nell'array, è una buona osservazione. Come cambierebbe il tuo approccio se l'array contenesse anche numeri negativi?
    - Hai pensato a possibili ottimizzazioni per ridurre il numero di operazioni necessarie?
    - Come gestiresti il caso in cui k è uguale a zero?
    - Hai considerato come potresti testare la tua soluzione con diversi casi di input, inclusi casi limite?
    ----------------------
    5. Le ottimizzazioni sono un aspetto importante da considerare. Potresti pensare a modi per ridurre il numero di iterazioni o calcoli?
    6. La tua osservazione su k=0 è corretta. Come gestiresti questo caso specificamente nel tuo codice?
    7. Il testing è cruciale. Potresti pensare a alcuni casi di test specifici che coprirebbero vari scenari?
    8. Hai considerato la possibilità di utilizzare strutture dati aggiuntive per ottimizzare la soluzione?
    9. Come gestiresti il caso in cui n è molto grande (ad esempio, milioni di elementi) in termini di efficienza?
    10. Puoi pensare a un modo per evitare di controllare le stesse coppie più volte?
    
Answers
    1. O(log(n)) -> yes, we can occur in a problem because if the array it's wide we can take up memory
    2. We can approch a try catch solutions to handling errors, so in that case can i controll if the array.lenght > 1 or if is null in that case i can raise a valuerror
    3. In this case i think that's not useful use a math libray because it's banal to apply the rule
    4. in fact it's not change the result 
    5. nope
    6. being that a number divisible by 0 it's always 0 can we answare with a error
    7. nope
    ------------------------
    5. then can start to:
         - exclude from the calculate the combination that are < of K -> example [1 2 3 4] k=5 -> after i compose 1+2= 3 can i verify if < of 5
         - We can memorize in a var the couple that we already compose ?
     6. We can add a try catch on the main method and before divisibleSumPairs could verify if k=0 and in case raise a error
     7. Yes, follow the test:
     - [1 2 3 4 5] n=5 k=5 
     - [1 2 3 4 5] n=5 k=0 
     - [1 2 3 4 5] n=0 k=2
     - [] n=4 k=2
     8. I can use a dictonary to take note about pairs that I have already used 
     9. First can we sort the array to rule out some calculate, and I not have other idea
     10. I can use a dictonary to take note about pairs that I have already used 
   
"""


#EXECUTE SOLUTION
def divisibleSumPairs(n, k, ar):
    countPairs = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (ar[i] + ar[j]) % k == 0:
                countPairs += 1
    return countPairs

# AI Solutions:
def divisibleSumPairs(n, k, ar):
    count = 0
    # Dizionario per memorizzare i resti
    remainder_count = {i: 0 for i in range(k)}

    for num in ar:
        remainder = num % k
        # Incrementa il conteggio per il complemento del resto corrente
        count += remainder_count[(k - remainder) % k]
        # Aggiorna il conteggio per il resto corrente
        remainder_count[remainder] += 1

    return count


if __name__ == '__main__':
    try:
        n, k = map(int, input().split())
        if (n or k) == 0:
            raise ValueError('n or k can be 0 or < -1')

        ar = list(map(int, input().split()))
        if len(ar) == 0:
            raise ValueError('array can be empty')

        result = divisibleSumPairs(n, k, ar)

        print(result)

    except ValueError as e:
        print(e)
