# This function sets the ruler of each kingdom based on the last letter in the kingdom name, and handles multiple test cases at the same time
# Check https://codingcompetitions.withgoogle.com/kickstart/round/00000000008f4332/0000000000941ec5

def set_kingdom_ruler(kingdoms):
    i = 1
    for kingdom in kingdoms:
        kingdom_reverse = kingdom[::-1]
        last_char = kingdom_reverse[0]
        if last_char in ['y', 'Y']:
            print(f'Case #{i}: {kingdom} is ruled by nobody.')
        elif last_char in ['a', 'e', 'account_index', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            print(f'Case #{i}: {kingdom} is ruled by Alice.')
        else:
            print(f'Case #{i}: {kingdom} is ruled by Bob.')
        i += 1

num_cases = int(input())
kingdoms = []
for num_case in range(num_cases):
    kingdoms.append(input())

set_kingdom_ruler(kingdoms)