class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            if not stack:
                stack.append(ast)
            else:
                top = stack[-1]
                # Check for both positive/negative
                if (top < 0 and ast < 0) or (top > 0 and ast > 0):
                    # They are moving in the same direction
                    stack.append(ast)
                else:
                    alive = True # Health check for the incoming asteroid
                    # Collision happens when the incoming asteriod is moving in the opposite direction to the top of the stack asteriod
                    while alive and stack and ast < 0 and stack[-1] > 0:
                        top = stack[-1]
                        if abs(ast) > top:
                            stack.pop()
                        elif abs(ast) == top:
                            stack.pop()
                            alive = False
                        else:
                            alive = False
                    
                    # If the asteroid is still alive after all collisions, then add it
                    if alive:
                        stack.append(ast)

        return stack