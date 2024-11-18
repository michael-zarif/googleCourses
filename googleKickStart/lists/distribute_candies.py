# This function distributes candies among kids eventually, and handles multiple test cases at the same time
# Check https://codingcompetitions.withgoogle.com/kickstart/round/00000000008f4332/0000000000942404

def dist_candies(num_cases):
    result = []
    for num_case in range(num_cases):
        num_candy_bags, num_kids = map(int, input().split())
        candy_counts = list(map(int, input().split()))
    
        total = 0
        for candy_count in candy_counts:
            total += candy_count
    
        result.append(total % num_kids)

    for num_case in range(num_cases):
        print(f'Case #{num_case + 1}: {result[num_case]}')
        
num_cases = int(input())
dist_candies(num_cases)


'''
Input
First Line has Number of Cases
The first line in each case has Number of Candy Bags and Kids (space separated)
The second line in each case has Number of Candies in each bag (space separated)

2
7 3
1 2 3 4 5 6 7
5 10
7 7 7 7 7

Output
Case #1: 1
Case #2: 5
'''