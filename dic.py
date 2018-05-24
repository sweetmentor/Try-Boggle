Dictionary Comprehension Challenges
Example:
Question 
                range(5) 
                -> { 0: "", 1:"*", 2:"**", 3:"***", 4:"****" }
Answer
                { i:"*" * i for i in range(5)}
1. ['Hi', 'There', 'Everyone'] 
-> {'Hi':2, 'There':5, 'Everyone':8}
2. 'code'
-> {'c': 99, 'e': 101, 'd': 100, 'o': 111}
3. ['car', 'cat', 'maps', 'if', 'level'] 
-> {'car':False, 'pop':True, 'maps':False, 'if':False, 'level':True}