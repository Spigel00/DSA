class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        answer = float('inf')

        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):

                land_start = landStartTime[i]
                land_duration = landDuration[i]

                water_start = waterStartTime[j]
                water_duration = waterDuration[j]

                land_finish = land_start + land_duration

                water_open = max (water_start, land_finish)
                water_finish = water_open + water_duration
                answer = min(answer,water_finish)

                water_finish = water_start + water_duration

                land_open = max (land_start, water_finish)
                land_finish = land_open + land_duration
                answer = min(answer,land_finish)
        return answer





