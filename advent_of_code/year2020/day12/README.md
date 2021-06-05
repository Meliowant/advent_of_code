# Notes
The task wasn't complex enough. The main issue was to rotate the ferry (task 1)
and the waypoint (task 2). Therefore I decided to extend the waypoint rotation
by adding a code that will allow to rotate waypoint to *any* random angle.
Those rotations, defined in the task: 90, 180 and 270 degrees CW and CCW were
boring enough. So after I implemented the original idea and reported the code,
I decided to extend it.

After few evenings I came to idea, that my initial assumption about 
computer-based axis orientation was bad. It was counter-intuitive, and,
therefore it was hard to debug the solution. So I decided to change the whole
waypoint and ship rotation to the "normal" axis orientation.

Another issue I had to solve was to work with the angles in the negative
axises. There my intiial idea was to determine the waypoint angle using acos 
for positive "y-axis" and for negative asin, with extra calculations. But it 
was over-complicated, so I returned to idea to use simply acos to calculate the
angle, and extract its walue from 360 degrees, if the waypoint's y coordinate
is less than 0.

The old code remains in the module, as example of the robust solution, that
perfectly suits requirements. Also it can be treated as the flag for the
compact code. The universal code is a bit longer in term of occupied lines, but
it is short enough to grab the idea.

## What did I learn on this day
1. Problems must be solved in the most fast way. More efficient (or universal,
   feel free to name it if you want so) eolution will take much more time.
2. Universal code can be as short as the robust one, but it requires more
   experience to write it efficiently.
3. School geometry classes are the things that will catch you when you don't
   expect for that.
