def solution(A):
     # Convert list to set for O(1) lookups
    A_set = set(A)

    number = 1

    # If the largest number is negative, return 1
    if max(A) < 0:
        return number

    for num in range(number, max(A) + 2):
        if num not in A_set:
            return num
        

A = [-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]
A = [1,2,2,3,1]
print(solution(A))