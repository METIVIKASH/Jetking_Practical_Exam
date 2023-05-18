''' LOOPING AS THE NAME SUJJEST REPEATING AY PARTICULAR CODE AGAIN AND AGAIN . A LOOP IN PYTHON IS A CONTROL FLOW STATEMENT THAT IS USED TO REPEADLY EXECUTE A GROUP OF STATEMENT AS LONG THE CODITION IS SATISFIED .

PYTHON PROVIDES US TWO DIFFERENT TYPES OF LOOPS
1. WHILE LOOP
2. FOR LOOP

WHILE LOOP - WITH USING WHILE LOOP CAN EXECUTE A SET OF STATEMENTS AS LONG AS THE CONDITION IS TRUE.

SYNTAX :-
    i = 1
    while i < 0:
    print (i)
    i +=1 


FOR LOOP -  A FOR LOOP IS USED FOR ITERATING OVER A SEQUENCE EITHER LIST, TUPPLE, DICTIONARY STRING OR A SET.

SYNTAX :-
    for x in items
    print(x)

'''
# EXAMPLE FOR USING WHILE LOOP 
i = 1 
n = 10

while i <= n:
    print(" THE STATEMENT'S ARE ",i)
    i = i+1 

print("-----------------------------------------------------------------")

# EXAMPLE FOR USING FOR LOOP

fruits = ["apple", "banana", "grapes","mango","strawberry"]
for x in fruits:
    print("MY FAVOURITE FRUITS ARE: ",x)