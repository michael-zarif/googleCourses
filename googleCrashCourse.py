import numpy as np

# Domino Tiles
for left in range(7):
    for right in range(left, 7):
        print(f"[{left}|{right}]", end=" ")
    print()

# Home-Away Tournament
teams = ["Dragons", "Wolves", "Pandas", "Unicorns"]
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(f"{home_team} vs {away_team}")

def create_step_array(start, end, segments):
  arr = [start]
  step = (end - start) / segments
  for i in np.arange(start, end, step):
    arr.append(round(i + step, 4))
  print(arr)

create_step_array(0, 5, 10)
