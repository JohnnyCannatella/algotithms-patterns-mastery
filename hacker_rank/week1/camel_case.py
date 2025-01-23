#!/bin/python3
import re
import sys

#EXCERCISE
"""
    excercise:
    Camel Case is a naming style common in many programming languages. In Java, method and variable names typically start with a
    lowercase letter, with all subsequent words starting with a capital letter (example: startThread).
    Names of classes follow the same pattern, except that they start with a capital letter (example: BlueCar).
    Your task is to write a program that creates or splits Camel Case variable, method, and class names.

    arg:
    Each line of the input file will begin with an operation (S or C)
    followed by a semi-colon followed by M, C, or V followed by a semi-colon followed by the words you'll need to operate on.

    output:
    For each input line, your program should print either the space-delimited list of words (in the case of a split operation)
    or the appropriate camel case string (in the case of a combine operation).

    notes:
    - The operation will either be S (split) or C (combine)
    - M indicates method, C indicates class, and V indicates variable
    - In the case of a split operation, the words will be a camel case method, class or variable name that you need to split into a space-delimited list of words starting with a lowercase letter.
    - In the case of a combine operation, the words will be a space-delimited list of words starting with lowercase letters that you need to combine into the appropriate camel case String.
    - Methods should end with an empty set of parentheses to differentiate them from variable names.
"""


#PROBLEM SOLVING
"""
    Arg:
    the scope of this program is write down a code that creates or split Camel Case for variables, methods and classes.
    I'll receive one or more input line that in base of operations and case type indicated have to process transform in camel case.
    How can we procede:
    So the first step will be to get and parse the input we can do it on the main method.
    I can create two classes that will take care of split or create the input by applying the rule.
    I thought to manage the different operation by using and if statement 
    
    
    questions:
    - in case of wrong string format I have to report an error ?
"""

#INTERVIEWER QUESTION
"""
Interviewer questions:
    1. Hai menzionato la creazione di due classi per gestire le operazioni di split e create. 
        Potresti spiegare perché hai scelto di usare classi invece di semplici funzioni?
        
    2. Hai parlato di utilizzare un'istruzione if per gestire le diverse operazioni. 
        Ci sono alternative a questo approccio che potresti considerare?
        
    3. Hai sollevato una buona domanda sulla gestione degli errori. 
        Come pensi di gestire i casi in cui l'input non è nel formato corretto?
        
    4. Non hai menzionato come gestiresti le differenze tra variabili, metodi e classi. 
        Potresti elaborare su come pensi di affrontare queste differenze nel tuo codice?
        
    5. Hai considerato come gestire i casi speciali, come le parole multiple per l'operazione di combine o 
        le maiuscole consecutive per l'operazione di split?
        
    6. Quale struttura dati pensi di utilizzare per memorizzare e 
        manipolare le parole durante le operazioni di split e combine?
        
    Second step
    1. L'uso dell'OOP è un approccio interessante. Potresti spiegare quali benefici specifici vedi nell'usare le classi per questo problema?
    2. Hai ragione, per pochi casi l'if statement può essere più leggibile. Hai considerato l'uso di un dizionario per mappare le operazioni alle funzioni?
    3. L'uso di try-catch è una buona pratica. Potresti essere più specifico su quali tipi di errori prevedi di catturare?
    4. L'approccio con if annidati può funzionare, ma potrebbe diventare complesso. Hai considerato di usare una struttura come un dizionario di funzioni per gestire i diversi casi?
    5. Per chiarire, un esempio di parole multiple per l'operazione di combine potrebbe essere "C;V;mobile phone". Come gestiresti questo caso?
    6. Usare una singola stringa per il risultato è un buon inizio. Per l'operazione di split, hai considerato come dividerai la stringa in parole separate?
    7. Come gestiresti il caso in cui una stringa Camel Case contiene numeri o acronimi (es. "parseXMLFile")?
    8. Hai considerato l'efficienza del tuo approccio? Quale pensi che sia la complessità temporale delle tue operazioni di split e combine?

1.Answers
    1. I thought to apply the OOP paradigm and use the benefit of this application
    2. We can use a switch case but in case like this therefore with a little case to be examined it's better to us if statements
    3. With a try catch I would manage the cases of error so if something of the input will be wrong it will be manage by catch and will report you the message
    4. I thought to manage it with concatenated if statement, in first concatenament we can examine operations while in second step will be examine the type, after that 
        we are able to procede to apply the rule.
    5. Could you provide an example of do you mean with multiple words ?
    6. I thought to use a single string variable to memorize the result of the combination
    
2.Answers
    1. Onestly in this case can lengthen the time using this approach so it's not wrong but we can use a simple functions to solve it
    2. How can use a dictonary to do that ?
    3. I imagined to catch error like incorrect Format, if input for example is in this way -> test or S:test 
        -  or the case where there isn't the correct command -> W:L:test or S:T:test
    4. No because i don't know what is the possibile with dictinary uses
    5. ok, so yes I have considered to manage this kind of input, in the split case after that i parsed the input will have an array with 3 value, follow the example:
        - "C;V;mobile phone" -> [C,V,mobile phone]
        - I'll passe it on method split and i can split even array[2] to take the single word ad apply the rule
    6. Yes, I hadn't actually thought of that, but after I thought it we can procede to split even array[2] to take the single word ad apply the rule
    7. In case of number we can catch an error in case of acronim theire will be addressed as normal value
    8. Not in all the case but i think that could be O(n) 

"""


#EXECUTE SOLUTION
def split_function(words):
    # Optimized solution
    # _str = words[2]
    # str_array = re.findall(r'[A-Z]?[a-z]+|[A-Z]+(?=[A-Z][a-z]|\d|\W|$)|\d+', _str)
    # new_words = ' '.join(word.lower() for word in str_array)
    # return new_words.rstrip('()')

    _str = re.sub('[^A-Za-z0-9]+', '', words[2])
    str_array = re.split('(?<=.)(?=[A-Z])', _str)
    new_words = str_array[0].lower()
    for word in str_array[1:]:
        new_words += " " + word.lower()
    return new_words


def combine_function(words):
    type = words[1]
    str_array = words[2].split(' ')
    new_words = ""

    if type == 'V':
        new_words = str_array[0].lower()
        for word in str_array[1:]:
            new_words += word.capitalize()
    elif type == 'C':
        new_words = str_array[0].capitalize()
        for word in str_array[1:]:
            new_words += word.capitalize()
    elif type == 'M':
        new_words = str_array[0].lower()
        for word in str_array[1:]:
            new_words += word.capitalize()
        new_words += "()"

    # Optimized solution
    # if type in ['V', 'M']:
    #     new_words = str_array[0].lower() + ''.join(word.capitalize() for word in str_array[1:])
    # else:  # type == 'C'
    #     new_words = ''.join(word.capitalize() for word in str_array)
    #
    # if type == 'M':
    #     new_words += "()"

    return new_words



#operations dictionary
operations = {
    'S': split_function,
    'C': combine_function
}

for line in sys.stdin:
    try:
        camelCaseWord = line.strip().split(';')

        if len(camelCaseWord) != 3:
            raise ValueError("Input must have exactly three parts separated by semicolons")

        if camelCaseWord[0] not in ['S', 'C']:
            raise ValueError("First part must be either 'S' or 'C'")

        if camelCaseWord[1] not in ['C', 'M', 'V']:
            raise ValueError("Second part must be either 'C', 'M', or 'V'")

        print(operations[camelCaseWord[0]](camelCaseWord))

    except (ValueError, TypeError) as e:
        print(f"Error: {e}", file=sys.stderr)
