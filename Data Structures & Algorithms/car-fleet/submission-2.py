class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)

        fleet_count = 0
        last_fleet_time = 0.0

        for current_position, current_speed in cars:
            arrival_time = (target - current_position)/current_speed
            if arrival_time > last_fleet_time:
                fleet_count += 1
                last_fleet_time = arrival_time
        
        return fleet_count