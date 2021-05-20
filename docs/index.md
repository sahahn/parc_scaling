---
layout: default
---

<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>


This project uses the idea of random surface parcellations extensively. Random parcellations are generated as follows: For a random parcellation of size N, N random points are first selected at random across both hemisphere’s 59,412 vertices (medial wall vertices excluded). Each selected point is then assigned as the seed of a new region and is randomly assigned a size probability between 0 and 1. Next, a region is randomly selected according to a weighted random choice between all regions (e.g., if a region was assigned an initial probability of .5 it would be picked on average twice as often as a region assigned .25). A random vertex is then added to the selected region from the list of valid neighboring unassigned vertices. This sequence, of selecting a region and adding one valid vertex, is repeated until all regions have no unassigned neighbors and therefore all non-medial wall vertices are assigned to a region. 

Example generated random parcellation:

![Random Parc Gif](https://raw.githubusercontent.com/sahahn/Parcs_Project/master/data/rand_parc.gif)

Note: The above example, in contrast to the random parcellations generated in this project, is in fsaverage5 space (vs. fs_LR_32k) and doesn't mask the medial wall (the medial wall is masked in this project).
[Link to another page](./test.html)
Source code for generating random parcellations is implemented and available through the Brain Predictability toolbox (BPt) at https://github.com/sahahn/BPt/blob/master/BPt/extensions/random_parcellation.py. In this project, random parcels are generated within Setup/process_random_parcels.py script.

{% include test.html %}
