class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # using zip to pair position and speed into tuples
        # then sort based on position while
        # keeping that cars speed
        cars = sorted(zip(position, speed), reverse=True)

        stack = []

        for p, s in cars:
            # time to reach target tells us if other
            # cars will be able to hit the fleet
            # in front of them, if car is <= time
            # that car will never reach the fleet
            time = (target - p) / s

            # if the stack is empty, or this car
            # takes longer than the fleet ahead
            # make that car be its own fleet
            # now that car is the next target fleet for
            # the car behind it
            if not stack or time > stack[-1]:
                stack.append(time)

        # now we return len stack because thats
        # the number of distint fleets
        return len(stack)