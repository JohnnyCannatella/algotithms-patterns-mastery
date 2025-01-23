#!/bin/python3
"""
    excercise:
          Maria plays college basketball and wants to go pro. Each season she maintains a record of her play. 
          She tabulates the number of times she breaks her season record for most points and least points in a game. 
          Points scored in the first game establish her record for the season, and she begins counting from there.
    arg:
        - an array of integer
    output:
        - an array of the numbers of times she broke her records, int[0] -> max record, int[1] -> min record
    steps:
        - init max_score and min_score with the first score
        - init max_count  and min_count that we'll use as return value
        - iterate through the array and count the number of times she breaks her record
        - return the number of times she breaks her record
    notes:
        - Scores are in the same order as the games played.
        - Points scored in the first game establish her record for the season
    questions:
    
"""

def breakingRecords(scores):
    max_score = min_score = scores[0]
    max_count = min_count = 0

    for score in scores[1:]:
        if score > max_score:
            max_score = score
            max_count += 1
        elif score < min_score:
            min_score = score
            min_count += 1
    return [max_count, min_count]



if __name__ == '__main__':
    scores = list(map(int, input().rstrip().split()))
    result = breakingRecords(scores)
    print(result)
