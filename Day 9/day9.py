from collections import deque
INPUT = "459 players; last marble is worth 71790 points"


def play_marbles(num_players, highest_marble):
    scores = [0 for _ in range(num_players)]

    # current is always in position 0
    marbles = deque([0])
    next_player = 0

    def move_left(n = 1):
        for _ in range(n):
            val = marbles.pop()
            marbles.appendleft(val)

    def move_right(n = 1):
        for _ in range(n):
            val = marbles.popleft()
            marbles.append(val)

    for marble in range(1, highest_marble + 1):
        if marble % 23 == 0:
            scores[next_player] += marble

            move_left(7)
            scores[next_player] += marbles.popleft()
        else:
            # -> a -> b
            move_right(2)
            # insert between a and b
            marbles.appendleft(marble)
            print(marbles);

        next_player = (next_player + 1) % num_players

    return scores

print(max(play_marbles(459,7179000)))