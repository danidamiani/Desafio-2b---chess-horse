# Desafio-e---chess-horse

To help yourself get to and from your bunk every day, write a function called solution(src, dest) which takes in two parameters: the source square, on which you start, and the destination square, which is where you need to land to solve the puzzle.  The function should return an integer representing the smallest number of moves it will take for you to travel from the source square to the destination square using a chess knight's moves (that is, two squares in any direction immediately followed by one square perpendicular to that direction, or vice versa, in an "L" shape).  Both the source and destination squares will be an integer between 0 and 63, inclusive, and are numbered like the example chessboard below:

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Python cases --
Input: solution.solution(0, 1)
Output: 3

Input: solution.solution(19, 36)
Output: 1
