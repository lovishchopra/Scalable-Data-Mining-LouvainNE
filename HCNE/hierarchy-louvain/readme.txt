1. Run the following 3 commands on the input graph file 'graph.txt' containing edge list:
 
 a) ./convert -i graph.txt -o graph.bin

 b) ./louvain graph.bin -l -1 -v > graph.tree

 c) ./hierarchy graph.tree -n

 d) ./hierarchy graph.tree -l N > graph-1-RMap.txt

  where N is number of levels obtained by running 1.c)

 e) mkdir graph
 	mv graph-1-RMap.txt graph/


 2. Run `python parse.py graph/ graph.txt` to get the hierarchical clustering 

 * This gives edgelist of subgraphs in files of the form graph-1-*.txt as well as node to community mapping at each level of the hierarchy in files of the form *-RMap.txt


 3. Run `python ranking.py graph/ graph.txt` to get the ranking of nodes based on Louvain hierarchy for every node

 4. Run `python jac-score.py graph-hierarchy-rank.p graph.txt` to get the distribution of similarity score 



