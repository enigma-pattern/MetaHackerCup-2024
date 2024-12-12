# Copyright (c) 2024 kamyu. All rights reserved.
#
# Meta Hacker Cup 2024 Final Round - Problem C. Chicken Tender
# https://www.facebook.com/codingcompetitions/hacker-cup/2024/final-round/problems/C
#
# Time:  O(N * ((logR) * N)) = O(N^2 * logR)
# Space: O(N)
#

from math import sin, cos, atan2

def rotate(x_y, theta):
    return [[x*cos(theta)-y*sin(theta), x*sin(theta)+y*cos(theta)] for x, y in x_y]

def vector(a, b):
    return [b[i]-a[i] for i in range(len(a))]

def angle(v1, v2):
    return atan2(v2[1], v2[0])-atan2(v1[1], v1[0])

def ternary_search(left, right, check):
    while right-EPS >= left+EPS:
        mid1 = left+(right-left)/3
        mid2 = right-(right-left)/3
        if check(mid1, mid2):
            right = mid2
        else:
            left = mid1
    return left

def chicken_tender():
    def center_at(X_Y, idx):
        result = [[X_Y[(idx+i)%N][0]-X_Y[idx][0], X_Y[(idx+i)%N][1]-X_Y[idx][1]] for i in range(N)]
        return rotate(result, angle(vector(result[0], result[1]), [1, 0]))

    def width(theta):
        new_X_Y = rotate(X_Y, theta)
        mn, mx = float("inf"), float("-inf")
        for i in range(N):
            x1, y1 = new_X_Y[i]
            x2, y2 = new_X_Y[(i+1)%N]
            if y1 > y2:
                (x1, y1), (x2, y2) = (x2, y2), (x1, y1)
            if y1+EPS2 > D:
                continue
            if y2+EPS2 > D:
                x2 = x1+(D-y1)*(x2-x1)/(y2-y1)
            mn = min(mn, x1, x2)
            mx = max(mx, x1, x2)
        return mx-mn

    def check(x, y):
        return width(x) < width(y)

    N, W, D = list(map(int, input().split()))
    X_Y = [list(map(int, input().split())) for _ in range(N)]
    result = float("inf")
    for _ in range(N):
        X_Y = center_at(X_Y, N-1)
        theta = angle(vector(X_Y[-1], X_Y[0]), vector(X_Y[0], X_Y[1]))
        degree = ternary_search(0, theta, check)
        result = min(result, width(degree))
        if result <= W+EPS2:
            return "Yes"
    return "No"

EPS = 1e-15
EPS2 = 1e-9
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, chicken_tender()))
