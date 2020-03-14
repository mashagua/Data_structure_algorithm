"""
n = 3
posting = "
Herbal sauna uses the healing properties of herbs in combination with distilled water.
The water evaporates and distributes the effect of the herbs throughout the room.
A visit to the herbal sauna can cause real miracles, especially for colds.
"

output = [
    ('the', 6),
    ('herbal', 2),
    ('sauna', 2),
]

"""
def top_n(posting,n):
    data=posting.lower().split(" ")