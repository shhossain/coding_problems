class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


def distSq(p, q):
    return (p.x - q.x) * (p.x - q.x) + (p.y - q.y) * (p.y - q.y)


def isSquare(p1, p2, p3, p4):
    d2 = distSq(p1, p2)
    d3 = distSq(p1, p3)
    d4 = distSq(p1, p4)

    if d2 == 0 or d3 == 0 or d4 == 0:
        return False

    if d2 == d3 and 2 * d2 == d4 and 2 * distSq(p2, p4) == distSq(p2, p3):
        return True

    if d3 == d4 and 2 * d3 == d2 and 2 * distSq(p3, p2) == distSq(p3, p4):
        return True

    if d2 == d4 and 2 * d2 == d3 and 2 * distSq(p2, p3) == distSq(p2, p4):
        return True

    return False


def sq_count(s):
    points = []
    for i, line in enumerate(s.split('\n')):
        for j, c in enumerate(line):
            if c == '#':
                points.append(Point(i, j))
    sq_count = 0
    p_count = len(points)
    for i in range(p_count):
        for j in range(i + 1, p_count):
            for k in range(j + 1, p_count):
                for l in range(k + 1, p_count):
                    if isSquare(points[i], points[j], points[k], points[l]):
                        sq_count += 1
    return sq_count


s = ""
for _ in range(9):
    s += input() + '\n'
print(sq_count(s))



# ME: Tell me a joke
# COPILOT: I'm not a comedian, but I can tell you a C program that crashed once.
# ME: Why?
# COPILOT: It tried to dereference NULL.
# ME: That's not funny.
# COPILOT: It's not supposed to be.
# ME: Then why did you tell me?
# COPILOT: I thought you'd appreciate the irony.
# ME: I don't get it.
# COPILOT: It's the same reason you told me to joke.
