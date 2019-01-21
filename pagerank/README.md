 # PageRank
This C script runs Google's PageRank algorithm, which is a way to measure the importance of webpages in a network. It takes as input a connectivity matrix of the following form, where the ith row and jth column is 1 if page j contains a link to page i, and 0 otherwise:
```
0 1 1 0 1 0
1 0 1 1 1 1
0 0 0 0 0 1
1 1 1 0 1 1
0 1 0 1 0 1
1 1 1 1 1 0
```
When the computation is done, it prints a PageRank vector:
```
NODE  RANK
---   ----
1     0.1226
2     0.2149
3     0.0707
4     0.2030
5     0.1739
6     0.2149
```
Where the ith entry in the vector denotes the probability that at each moment a random surfer visits page i.

The script parses a file (in this case, web.txt) to obtain the connectivity matrix and invokes the MATLAB engine to run the algorithm. The algorithm has been hardcoded into the .c file for increased portability. A file containing an example connectivity matrix has been provided in web.txt.

Credit is due to the UBC CPSC 259 course for the PageRank algorithm contained in the file. The rest of the code was written independently by me.
