from collections import defaultdict

openings_by_player: dict[str, int] = defaultdict(int)
# openings_by_player: dict[str, int] = {}
print(openings_by_player)
openings_by_player['Dima']
print(openings_by_player)

openings_by_player['Dima'] += 1
print(openings_by_player)
