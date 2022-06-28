# This function distributes candies among kids eventually, and handles multiple test cases at the same time
def dist_candies():
    num_candy_bags, num_kids = map(int, input('Number of Candy Bags and Kids (space separated): ').split())
    candy_counts = list(map(int, input('Number of Candies in each bag (space separated): ').split()))
    
    total = 0
    for candy_count in candy_counts:
        total += candy_count
    
    return total % num_kids
            
            
num_cases = int(input('Number of Cases: '))
for num_case in range(num_cases):
    print(f'Case #{num_case + 1}: {dist_candies()}')

'''
Input
2
7 3
1 2 3 4 5 6 7
5 10
7 7 7 7 7

Output
Case #1: 1
Case #2: 5
'''