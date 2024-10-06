# Copyright (c) 2024 kamyu. All rights reserved.
#
# Meta Hacker Cup 2024 Round 1 - Problem D. Substitution Cipher
# https:#www.facebook.com/codingcompetitions/hacker-cup/2024/round-1/problems/D
#
# Time:  O(N)
# Space: O(1)
#

def substitution_cipher():
    def kth_largest(K):
        for i in reversed(range(len(E))):
            if E[i] != '?':
                continue
            if i+1 < len(E) and E[i+1] == '0':
                E[i] = chr(ord('2')-K%2)
                K //= 2
            elif i+1 < len(E) and E[i+1] == '?':
                q, r = divmod(26-K%15-int((26-K%15) <= 20), 10)  # 11-19, 21-26
                E[i], E[i+1] = chr(ord('0')+q), chr(ord('0')+r)
                K //= 15
            elif i+1 == len(E) or (i+2 < len(E) and E[i+2] == '0'):
                if i-1 >= 0 and E[i-1] == '?':
                    pass
                elif i-1 >= 0 and E[i-1] == '2':
                    E[i] = chr(ord('6')-K%6)  # 1-6
                    K //= 6
                else:
                    E[i] = chr(ord('9')-K%9)  # 1-9
                    K //= 9
            elif '1' <= E[i+1] and E[i+1] <= '6':
                E[i] = chr(ord('2')-K%2)  # 1-2
                K //= 2
            elif '7' <= E[i+1] and E[i+1] <= '9':
                E[i] = '1'  # 1
            else:
                assert(False)
        assert(K == 0)

    def count():
        dp = [0]*3
        dp[0] = 1
        for i in range(1, len(E)+1):
            dp[i%3] = 0
            if E[i-1] != '0':
                dp[i%3] = (dp[i%3]+dp[(i-1)%3])%MOD
            if i-2 >= 0 and ((E[i-2] == '1' and '0' <= E[i-1] <= '9') or E[i-2] == '2' and '0' <= E[i-1] <= '6'):
                dp[i%3] = (dp[i%3]+dp[(i-2)%3])%MOD
        return dp[len(E)%3]

    E, K = input().split()
    E, K = list(E), int(K)
    kth_largest(K-1)
    return f"{''.join(E)} {count()}"

MOD = 998244353
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, substitution_cipher()))