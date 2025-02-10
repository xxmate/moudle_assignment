'''
Write a function that does the following task.

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:

Input: numRows = 5

Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

1

1 1

1 2 1

1 3 3 1

1 4 6 4 1
'''
numRows = 7
Output = []

for i in range(numRows):
    if i == 0:
        Output.append([1])
    elif i == 1:
        Output.append([1, 1])
    else:
        l = [1]
        for j in range(len(Output[-1]) - 1):
            l.append(Output[-1][j] + Output[-1][j+1])
        l.append(1)
        Output.append(l)

print(Output)
