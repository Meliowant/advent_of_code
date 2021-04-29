# A note on implementation
This task was quite challenging for me. There were two main issues I met with:
a) computation complexity is huge
b) working with recursion structures
c) use IDE for debugging instead of pdb

As for computation complexity, there are too many possible combinations, so my 
initial idea failed, and I got a `Segmentation Failure` error after an hour 
and a half of the program's working. At this point, I realized (again), that 
taking a straight approach doesn't work well in each case. Sometimes, we need 
to think differently. Well, I knew that, but, knowing and feeling are different
things. 
And some other way must be found.

At that point I came to the idea, I can build the longest path, that will 
contain all possible adapters that can reach at least once the target device. 
From that list, I can go back, to the top. Each adapter I will meet during my 
reversed return will be tested for the presence of the next possible adapters. 
If any of these adapters are located in the longest path starting from the 
current adapter till the final one, then these adapters will be added to the 
list of next adapters. So I won't need to check all the possible combinations 
in the future but simply will copy the known combinations.

The recursion appears in the place when I want to create possible paths for 
existing combinations, and it was another tricky thing. I had to play with 
`[].append()` and `[].extend()` functions, so each possible path fits into its 
own list. At this point I first time in my life used recursion outside the 
reference "factorial example", and it was even complicated because each path 
could be split into few others. Of course, I could avoid using recursion, but 
it seemed for me natural to use it here. And, also, it was a good test for me, 
to understand its implementation.

Extra tricking thing was using IDE's debugger instead of pdb. It was more 
comfortable to use it, because with pdb I've been losing the context. Instant
keeping in memory current variables' values was a quite tricky. Thus, I decided
to switch to PyCharm to track the issue, and it saved me much time. Just, to be 
more precise, I found the issue and fixed it in few minutes, and with pdb I 
spent near few days. So, I need either to learn more about pdb or I simply 
picked incorrect tool for solving the problem.
Nevertheless, picking IDE's debugger was the silver bullet.

It seems like my initial idea to build the whole tree, and later count its
branches was also bad. I run into huge amount of memory, but the process was
not speeded up. That's how `adapter_array_p2_slow2.py` appeared. So I decided
to update the `adapter_array_p2.py`'s class with the new property, that will
contain amount of possible pathes from this adapter towards the target. This
property will be initially set with 1 at the device's joltage. Then, I will
move backward, and for parent adapter I will determite its childs. Thus its 
amount of possible pathes will be sum of the chilren's possible pathes.
I.e. for combination `0 -> 1 -> 2 -> 3` the possible pathes will be:
- at `3` - 1;
- at `2` that has only one child, `3`, amount of possible pathes will be 1
- at `1` that has two children, `2` (1 possible path) and `3` (1 possible
  path), amount of possible pathes will be 2;
- at `0` that has three children: `1` (2 possible pathes), `2` (1 possible
  path), `3` (1 possible path), total amount of pathes is 4.
Thus 4 will be a solution for this task.
A complete list of possible paths is:
```
0 -> 1 -> 2 -> 3
|    +--> 3
|
+--> 2 -> 3 
|
+--> 3
```
