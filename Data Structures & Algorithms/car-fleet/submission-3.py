class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        paired = sorted(zip(position, speed), reverse = True)
        position, speed = map(list, zip(*paired))

        stack = [] #keeps track of slow cars, mono dec
        # as the cars come, see if it is faster to the one in the stack
        for pos, sp in zip(position, speed):
            #calculate time to target
            time = (target-pos)/sp
            if not stack or time > stack[-1]:
                stack.append(time)
        print(stack)
        return len(stack)