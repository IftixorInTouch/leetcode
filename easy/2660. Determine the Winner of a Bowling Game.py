class Solution(object):
    def isWinner(self, player1, player2):
        """
        :type player1: List[int]
        :type player2: List[int]
        :rtype: int
        """
        score1 = player1[0]
        score2 = player2[0]
        for i in range(len(player1)):
            if i == 0:
                continue
            elif i == 1 and player1[i - 1] == 10:
                score1 += 2 * player1[i]
            elif i != 1 and (player1[i - 1] == 10 or player1[i - 2] == 10):
                score1 += 2 * player1[i]
            else:
                score1 += player1[i]

            if i == 1 and player2[i - 1] == 10:
                score2 += 2 * player2[i]
            elif i != 1 and (player2[i - 1] == 10 or player2[i - 2] == 10):
                score2 += 2 * player2[i]
            else:
                score2 += player2[i]

        if score1 > score2:
            return 1
        elif score2 > score1:
            return 2
        else:
            return 0

a = Solution()
print(a.isWinner([5,10,3,2], [6,5,7,3]))