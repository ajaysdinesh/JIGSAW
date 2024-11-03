# JIGSAW
Solve any sized Jigsaw puzzles without any reference image other than to perform final validation.

Thought process:

If you have the reference image for a jigsaw puzzle, you can pretty much look for the actual position of each piece by matching the pixels.
This code should work even when you do not have a reference image. This would now involve finding neighboring pieces by matching edges, building up the puzzle block by block and then merging all the blocks together to form the image.
Corner cases: Edges that are not obviously connected because that coincides with a graphical anomaly, for example like a straight wall with different colours on both sides. A normal human would think both edges have similar colours or gradients.

