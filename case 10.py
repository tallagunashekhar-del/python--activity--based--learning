

points = [(0, 0), (3, 4), (6, 8), (6, 14), (10, 14)]

total = 0
longest = 0
longest_segment = ""

for i in range(len(points) - 1):
    x1, y1 = points[i]            # tuple unpacking
    x2, y2 = points[i + 1]
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    total = total + distance
    print("Segment", i + 1, ":", points[i], "->", points[i + 1], "=", round(distance, 2))
    if distance > longest:
        longest = distance
        longest_segment = str(points[i]) + " -> " + str(points[i + 1])

print("\nTotal route length:", round(total, 2))
print("Longest segment:", longest_segment, "=", round(longest, 2))
