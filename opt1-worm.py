# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.6
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
#
# # Option 1: Worm brain
# In this project, you will worm your way through a dataset,
# mapping the full C. elegans nervous system (all 302 neurons),
# and tell an interesting story about the process,
# using both prose text (written here in the notebook),
# as well as using python code and plots.
# This worm is easy enough to study,
# that we can get a weighted directed network with plenty of meta-data;
# this information is more rich than the human in terms of low-level detail.
#
# ## Bio graphs
# **Option 1**: connectome of:
# <https://en.wikipedia.org/wiki/Caenorhabditis_elegans> 
#
# The first multicellular genome, the first connectome, the first whole animal simulation, etc.
#
# <https://en.wikipedia.org/wiki/History_of_research_on_Caenorhabditis_elegans>
#
# ### Connectome:
# Meta-data for the worm set2 (includes organ data):
# * <http://wormwiring.org/>
# * <http://wormwiring.org/sex/male.php>
# * <http://wormwiring.org/sex/hermaphrodite.php>
#
# ### Genome:
# <https://www.science.org/doi/10.1126/science.282.5396.2012>
#
# ### Whole animal simulation:
# <https://openworm.org/>
# <https://github.com/openworm>
#
# ### Brain gene expression map:
# <https://www.cengen.org/>
#
# ## Steps
#
# 1.  Read/watch the folling links:
#     * <https://en.wikipedia.org/wiki/Caenorhabditis_elegans>
#     * <https://en.wikipedia.org/wiki/History_of_research_on_Caenorhabditis_elegans>
#     * <http://www.wormbook.org/chapters/www_celegansintro/celegansintro.html>
#     * <https://www.youtube.com/watch?v=zjqLwPgLnV0>
#     * <https://wormwiring.org/>
#     * <http://browser.openworm.org/>
#     * <http://openworm.org/>
#
# 2.  Check out the data in `./c_elegans_neuron_conn/set2/` (that is your primary data set to analyze)
#     -   There are two other data sets:
#         - the set0 has some coordinate data (but is not as good otherwise),
#         - and the set1 is the original dataset with more detail.
#     - You are welcome to check them out, but are not required to.
#
# 3.  Import the data from set2 into a NetworkX graph format,
#     doing as much pre-processing and formatting in Python3 as is reasonably convenient.
#     -   What graph type do you need?
#     *You need a DiGraph from NetworkX, since there are sources and targets for the neurons, which indicates there is a direction of neuron firing for the graph.*
#
#     -   What meta-data can you include, such as node names, edge weights, synapse type, etc.?
#     *This graph includes neuron has node names, which are the neurons of C. Elegans, the edge weights, which are the connection strength, the targets, which is where the nerves are supplied, and the synapse type, which is how it is transmitted.*
#
#     -   Can you use any of the meta-data in your interpretations?
#     *Yes, you can use weights to see which neurons fire together more, which can be used to make inferences on the structures and complexity of the organism.*
#     -   Check out the graph by drawing it like this:
#         <https://networkx.github.io/documentation/stable/auto_examples/drawing/plot_directed.html#sphx-glr-auto-examples-drawing-plot-directed-py>
#
# 4.  Analyze the graph!
#     -   Try many of the analyses I demonstrated with the human brain,
#         both global, local, and sub-network based statistics/metrics.
#         Write a several sentence interpretation of each metric as applied to this dataset.
#
#         **Degree Centrality:**
#         
#              For the degree centrality calculation, the nodes with the most direct neighbors were AVAR, AVAL, DVA, AVAL, and PVCR. The AVAR are AVAL neurons are along the ventral nerve cord, and they relay information to ventral motor neurons. The ventral nerve cord is a significant part of C, Elegans' central nervous system, so it makes sense that the neurons within it have high degree centrality, since they must transmit many signals around the body for coordinating movement. PVC neurons are important for the forward movement of C. Elegans, so high degree centrality is also logical, since they need to connect to other motor neurons.
#         
#
#
#         **Betweeness Centrality:**
#         
#               The betweeness centrality calculation, which counts the proportion of shortest paths, had I1L, I2L, I3, I5, I6, as its top nodes for the data. The neurons with the highest betweeness centrality are important in pharyngeal  pumping, movements that assist in the feeding and movement of C. Elegans, due to how they connect somatic and pharyngeal nervous systems.  The high betweeness centrality number of these nodes reflect their importance in bridging these regions to ensure they can communicate properly. They allow for signals to pass through so the muscles and nervous system of the C. Elegans are coordinated. Since feeding and movement are one of the principal functions of an organism, it makes sense these neurons would have high betweenness centrality.
#
#
#
#         **Closeness Centrality:**
#         
#               The closeness centrality finds how central a node is in comparision to other nodes. In this data, the AVAL, AVAR, hyp, AVAR, AVBR were the most central degrees. The AVAL/AVAR/AVBR neurons were also found to be the nodes with the most direct neighbors, and they are located in the ventral nerve cord. This is crucial to reach the other neurons. The ventral nerve cord is down the midline of the nematode's body, which accurately reflects the high closeness centrality of the neurons within it. This allows for the C. Elegans' locomotion, which requires the entire body.
#    -   Try at least 1 new measure that we did not cover in class
#         (you may need to search around for one).
#         Write several paragraphs about your interpretation of that measure.
#        
#           Katz Centrality:
#               The Katz centrality is used to find the influence of a node. It is the centrality based on the centrality of the nodes surrounding it. This is done by finding the number of first degree nodes and the nodes connecting to those nodes. I chose Katz as it helps to see which neurons are also influential in a C. Elegan's body, even if they are not the most obvious hubs in the worms' body. These neurons are still areas of significant signals, even if they do not connect to many other nodes.
#               The nodes with the highest Katz centrality were also the AVAL, AVAR, hyp, AVAR, AVBR neurons, similar to both the degree centrality and closeness centrality measures. These nodes have both major direct and indirect influence, which is logical due to their role in movement of the C. Elegans. As previously stated, C. Elegans require their entire body to move, which requires connections throughout the body to ensure the signals are properly sent. This aligns with how these neurons have the highest measure of influence, since there must be coordination between the muscles and various other regions.
#
# 5.  Compare the graph to other graphs
#     -   Compare at least 10 of the metrics between:
#         (a) a random graph,
#         (b) a randomly generated scale-free network,
#         (c, d) the two human brain datasets I showed
#     -   What is your interpretation of the differences between these graphs?
#
#
#           The graph of the C. Elegans has both similarities and differences compared to a random graph, a randomly generated scale graph, and the two human brain datasets. Firstly, the graph of the C. Elegans is not dense; however, there are significant neurons, such as AVAL and AVAR that appear in several of the centrality measures. The random graph has a similar density, but does not have the structure. The values of the degree centrality are much lower than that of the worm, showing that degree centrality is even in the random graph and there are not major structures.
#           The scale-free graph has a lower density compared to the C. Elegans, showing that many nodes are not connected to the others in it. The degree centrality is slightly higher than the random graph, but lower than the C. Elegans, showing there are a few major structures within it.")
#           Densities are much higher in the human brains, along with more degree centrality. This shows the organization of the human brain, and how there are various structures that are modular. Additionally, the high density shows the complexity of networks in the brains, in comparison to the worm, which is more efficient and minimal.
#           The differences between the graphs show how complex and modular each organism is.
#
# 7.  Document the whole process here, and tell an engaging story with the data and your plots!
#
# 8.  Submit via git-classes
#
# ![images/image0.png](images/image0.png)
#
# ![images/image1.png](images/image1.png)
#
# ![images/image2.png](images/image2.png)

# %%
import networkx as nx
import pandas as pd
import numpy as np

print("3. Import the data from set2 into a NetworkX graph format, doing as much pre-processing and formatting in Python3 as is reasonably convenient.")
print(f" * What graph type do you need?\n You need a DiGraph from NetworkX, since there are sources and targets for the neurons, which indicates there is a direction of neuron firing for the graph.")
print(f" * What meta-data can you include, such as node names, edge weights, synapse type, etc.?\n This graph includes neuron has node names, which are the neurons of C. Elegans, the edge weights, which are the connection strength, the targets, which is where the nerves are supplied, and the synapse type, which is how it is transmitted.")
print(f" * Can you use any of the meta-data in your interpretations?\nYes, you can use weights to see which neurons fire together more, which can be used to make inferences on the structures and complexity of the organism.\n")

print(f"------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
herm_df = pd.read_csv("./opt1-worm/c_elegans_neuron_conn/set2/herm_full_edgelist.csv")
graph = nx.DiGraph()

for _, row in herm_df.iterrows():
    graph.add_edge(row['Source'], row['Target'], weight=row['Weight'], synapse_type=row['Type'])

print("\nNum Neurons:", graph.number_of_nodes())
print("Num Connections):", graph.number_of_edges())
print("Density:", nx.density(graph))

sub_nodes = list(graph.nodes)[:20]
subgraph = graph.subgraph(sub_nodes)

print("Graph visualization")
print("Subgraph nodes:")
print(subgraph.nodes())

print("Subgraph edges:")
for u, v, data in subgraph.edges(data=True):
    print(f"{u} -> {v}, weight={data['weight']}, synapse={data['synapse_type']}")

degree_centrality = nx.degree_centrality(graph)
degree = sorted(degree_centrality.items(), key=lambda x: x[1], reverse=True)[:5]
print("Degree Centrality (Has most direct neighbors):")
for neuron, centrality in degree:
    print(f"{neuron.strip()}: {centrality:.4f}")

betweeness_centrality = nx.betweenness_centrality(graph)
betweeness = sorted(betweeness_centrality.items(), key=lambda x: x[1], reverse=True)[:5]
print("\nBetweenness Centrality (Proportion of shortest paths):")
for neuron, centrality in betweeness:
    print(f"{neuron.strip()}: {centrality:.4f}")

closeness_centrality = nx.closeness_centrality(graph)
closeness = sorted(closeness_centrality.items(), key=lambda x: x[1], reverse=True)[:5]
print("\nCloseness Centrality (most central degree globally):")
for neuron, centrality in closeness:
    print(f"{neuron.strip()}: {centrality:.4f}")

print(f"\nOne new measure we did not cover in class: Katz Centrality\n")
katz_centrality = nx.katz_centrality_numpy(graph, alpha=0.005, beta=1.0)
top_katz = sorted(katz_centrality.items(), key=lambda x: x[1], reverse=True)[:5]
print("\nKatz centrality (relative influence through immediate neighbors and their connections):")
for neuron, value in top_katz:
    print(f"{neuron.strip()}: {value:.4f}")


print(f"------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("4.  Analyze the graph!") 

# https://www.wormatlas.org/ (for explanation of neurons)
print(f"\nFor the degree centrality calculation, in this dataset, the nodes with the most direct neighbors were AVAR, AVAL, DVA, AVAL, and PVCR. The AVAR are AVAL neurons are along the ventral nerve cord, and they relay information to ventral motor neurons. The ventral nerve cord is a significant part of C, Elegans' central nervous system, so it makes sense that the neurons within it have high degree centrality, since they must transmit many signals around the body for coordinating movement. PVC neurons are important for the forward movement of C. Elegans, one of the most vital functions and one that requires full body coordination, so high degree centrality is also logical, since they need to connect to other motor neurons.")

# https://www.nature.com/articles/srep22940 (neurons explanation)
# https://www.wormatlas.org/neurons/Individual%20Neurons/I1frameset.html
print(f"\nThe betweeness centrality calculation, which counts the proportion of shortest paths, had I1L, I2L, I3, I5, I6, as its top nodes for the data. The neurons with the highest betweeness centrality are important in pharyngeal  pumping, movements that assist in the feeding and movement of C. Elegans, due to how they connect somatic and pharyngeal nervous systems.  The high betweeness centrality number of these nodes reflect their importance in bridging these regions to ensure they can communicate properly. They allow for signals to pass through so the muscles and nervous system of the C. Elegan are coordinated. Since feeding and movement are one of the principal functions of an organism, it makes sense these neurons would have high betweenness centrality.")

# https://pmc.ncbi.nlm.nih.gov/articles/PMC4776678/ (C. Elegans locomotion explanation)
print(f"\nThe closeness centrality finds how central a node is in comparision to other nodes. In this data, the AVAL, AVAR, hyp, AVAR, AVBR were the most central degrees. The AVAL/AVAR/AVBR neurons were also found to be the nodes with the most direct neighbors, and they are located in the ventral nerve cord. This is crucial to reach the other neurons. The ventral nerve cord is down the midline of the nematode's body, which accurately reflects the high closeness centrality of the neurons within it. This allows for the C. Elegans' locomotion, which requires the entire body.")

# https://en.wikipedia.org/wiki/Katz_centrality https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.centrality.katz_centrality.html
print(f"\nThe Katz centrality is used to find the influence of a node. It is the centrality based on the centrality of the nodes surrounding it. This is done by finding the number of first degree nodes and the nodes connecting to those nodes. I chose Katz as it helps to see which neurons are also influential in a C. Elegan's body, even if they are not the most obvious hubs in the worms' body. These neurons are still areas of significant signals, even if they do not connect to many other nodes.")
print(f"The nodes with the highest Katz centrality were also the AVAL, AVAR, hyp, AVAR, AVBR neurons, similar to both the degree centrality and closeness centrality measures. These nodes have both major direct and indirect influence, which is logical due to their role in movement of the C. Elegans. As previously stated, C. Elegans require their entire body to move, which requires connections throughout the body to ensure the signals are properly sent. This aligns with how these neurons have the highest measure of influence, since there must be coordination between the muscles and various other regions.")

print("5. Compare the graph to other graphs")
randG = nx.gnp_random_graph(graph.number_of_nodes(), nx.density(graph), directed=True)
print("\n(a) Random graph:")
print("Nodes:", randG.number_of_nodes())
print("Edges:", randG.number_of_edges())
print("Density:", nx.density(randG))
print("Degree centrality:", sorted(nx.degree_centrality(randG).items(), key=lambda x: x[1], reverse=True)[:5])

print("\n(b) Scale-free graph:")
scale_free_graph = nx.scale_free_graph(graph.number_of_nodes())
scale_free_graph = nx.DiGraph(scale_free_graph)
print("Nodes:", scale_free_graph.number_of_nodes())
print("Edges:", scale_free_graph.number_of_edges())
print("Density:", nx.density(scale_free_graph))
print("Degree centrality:", sorted(nx.degree_centrality(scale_free_graph).items(), key=lambda x: x[1], reverse=True)[:5])


print(f"The graph of the C. Elegans has both similarities and differences compared to a random graph, a randomly generated scale graph, and the two human brain datasets. Firstly, the graph of the C. Elegans is not dense; however, there are significant neurons, such as AVAL and AVAR that appear in several of the centrality measures. The random graph has a similar density, but does not have the structure. The values of the degree centrality are much lower than that of the worm, showing that degree centrality is even in the random graph and there are not major structures.")
print(f"The scale-free graph has a lower density compared to the C. Elegans, showing that many nodes are not connected to the others in it. The degree centrality is slightly higher than the random graph, but lower than the C. Elegans, showing there are a few major structures within it.")
print(f"Densities are much higher in the human brains, along with more degree centrality. This shows the organization of the human brain, and how there are various structures that are modular. Additionally, the high density shows the complexity of networks in the brains, in comparison to the worm, which is more efficient and minimal. The differences between the graphs show how complex and modular each organism is.")

# %%
