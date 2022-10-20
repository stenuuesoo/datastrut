# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. 
# You are given  scores. Store them in a list and find the score of the runner-up.

# The first line contains n. The second line contains an array A[] of integers each separated by a space.
# Print the runner-up score.

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    sorted_arr = sorted(arr, reverse=True)
    rm_duplicates = list(dict.fromkeys(sorted_arr))
    print(rm_duplicates[1])
    