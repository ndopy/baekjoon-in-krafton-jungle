import sys

friends_count = int(sys.stdin.readline())
friends_tracks = list(map(str, sys.stdin.readline().split()))
hellobit_track = sys.stdin.readline().strip()

print(friends_tracks.count(hellobit_track))