from typing import List


# time limit
class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        if len(security) <= 2 * time:
            return []
        if time == 0:
            return [i for i in range(len(security))]
        result = []
        for i in range(time, len(security) - time):
            if security[i] > security[i - 1] or security[i] > security[i + 1]:
                continue
            good_day = True
            tmp_num = security[i - time]
            for num in security[i - time:i]:
                if num > tmp_num:
                    good_day = False
                    break
                tmp_num = num
            if not good_day:
                continue
            tmp_num = security[i + 1]
            for num in security[i + 1:i + time + 1]:
                if num < tmp_num:
                    good_day = False
                    break
                tmp_num = num

            if good_day:
                result.append(i)
        return result

