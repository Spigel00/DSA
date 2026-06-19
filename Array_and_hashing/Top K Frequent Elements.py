class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}

        for num in nums:
            if num not in frequency:
                frequency[num] = 1
            else:
                frequency[num] += 1

        pairs = list(frequency.items())

        pairs.sort(key=lambda x: x[1], reverse=True)

        answer = []

        for i in range(k):
            answer.append(pairs[i][0])

        return answer