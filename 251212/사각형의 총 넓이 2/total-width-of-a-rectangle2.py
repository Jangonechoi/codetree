import sys

input_lines = sys.stdin.read().split('\n')
n_val = int(input_lines[0])
rects_input = []

for i in range(1, n_val + 1):
    x1, y1, x2, y2 = map(int, input_lines[i].split())
    rects_input.append((x1, y1, x2, y2))

def calculate_area(n, rectangles):
    events = []
    for x1, y1, x2, y2 in rectangles:
        x_min, x_max = min(x1, x2), max(x1, x2)
        y_min, y_max = min(y1, y2), max(y1, y2)
        events.append((x_min, 0, y_min, y_max))
        events.append((x_max, 1, y_min, y_max))
    
    events.sort()

    y_coords = sorted(list(set([r[1] for r in rectangles] + [r[3] for r in rectangles])))
    y_len = len(y_coords)

    if y_len <= 1:
        return 0

    count = [0] * (y_len -1)

    total_area = 0
    current_x = events[0][0]
    
    for x, event_type, y1, y2 in events:
        if x > current_x:
            coverd_length = 0
            for i in range(y_len -1):
                if count[i] > 0:
                    coverd_length += (y_coords[i+1] - y_coords[i])
            total_area += coverd_length * (x - current_x)
        current_x = x

        for i in range(y_len - 1):
            if y_coords[i] >= y1 and y_coords[i+1] <= y2:
                if event_type == 0:
                    count[i] += 1
                else:
                    count[i] -= 1
    return total_area

print(calculate_area(n_val, rects_input))


    