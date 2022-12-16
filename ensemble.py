# Import necessary packages
import networkx as nx
import matplotlib.pyplot as plt
from numpy import random
import gerrychain
from gerrychain import Graph, Partition, proposals, updaters, constraints, accept, MarkovChain
from gerrychain.updaters import cut_edges, Tally
from gerrychain.tree import recursive_tree_part
from gerrychain.proposals import recom
from gerrychain.accept import always_accept
from functools import partial
import csv

def runEnsemble(stateCode, filePath, num_dist, total_steps = 9000, pop_tolerance = .02, district_gap_threshold= .05):
    #stateCode = States Code ex: VA MN WI
    #total_steps =  Number of steps in random walk ensemble  Default:(1000, 3000, 9000)
    #num_dist =  Number of Congressional Districts in State
    #pop_tolerance = population variation tolerance allowed in redistricting plan (.02/2% default)
    #district_gap_threshold = threshold for a district to be competitive (.05/5% default)
    #filePath = path to dual graph data ex: "VA/VA_precincts.json"

    # import alabama dual graph
    data = Graph.from_json(filePath)

    # Get total population
    tot_pop = 0
    for v in data.nodes():
        tot_pop = tot_pop + data.nodes()[v]['TOTPOP20']


    ## Make an initial districting plan using recursive_tree_part (from last time)
    ideal_pop = tot_pop/num_dist
    initial_plan = recursive_tree_part(data, range(num_dist), ideal_pop, 'TOTPOP20', pop_tolerance, 10)

    # initial partition
    initial_partition = Partition(
        data, # dual graph
        assignment = initial_plan, #initial districting plan
        updaters={
        "our cut edges": cut_edges,
        "district population": Tally("TOTPOP20", alias = "district population"), # across districts, add total population
        "district democrat votes": Tally("G18DSEN", alias = "district democrat votes"),
        "district republican votes": Tally("G18RSEN", alias = "district republican votes"),
        "district independent votes": Tally("G18OSEN", alias = "district independent votes"),
    })

    # random walk proposal
    rw_proposal = partial(recom, ## how you choose a next districting plan
                          pop_col = "TOTPOP20", ## What data describes population?
                          pop_target = ideal_pop, ## What the target/ideal population is for each district
                                                  ## (we calculated ideal pop above)
                          epsilon = pop_tolerance,  ## how far from ideal population you can deviate
                                                  ## (we set pop_tolerance above)
                          node_repeats = 1 ## How many times you attempt before resrating
                          )

    ## Contraint on population: stay within pop_tolerance of ideal
    population_constraint = constraints.within_percent_of_ideal_population(
        initial_partition,
        pop_tolerance,
        pop_key="district population")

    ## Creating the chain
    # Set sup the chain, but doesn't run it!
    our_random_walk = MarkovChain(
        proposal = rw_proposal,
        constraints = [population_constraint],
        accept = always_accept, # Accept every proposed plan that meets the population constraints
        initial_state = initial_partition,
        total_steps = total_steps)


    # What ensembles we want to build
    ensemble = {}
    ensemble['cutedge'] = []
    ensemble['competitiveness_index'] = []
    # threshold for the competitiveness index set to 5%
    ensemble['distGap_threshold'] = district_gap_threshold
    counter = 1


    # This actually runs the random walk!
    for part in our_random_walk:
        if counter % 100 == 0:
            print("Running Dist #:")
            print(counter)
        ensemble['cutedge'].append(len(part["our cut edges"]))

        num_competitive = 0
        for i in range(num_dist):
            # calculate district gap for each district in ensemble
            # total votes = democrat votes + republican votes
            dist_gap = abs(part["district democrat votes"][i] - part["district republican votes"][i]) / (part["district democrat votes"][i] + part["district republican votes"][i])

            # if the district gap is less than the threshold (.05 default) then the district is competitive
            if dist_gap < ensemble['distGap_threshold']:
                num_competitive = num_competitive + 1

            # add the # of competitive districts in the plan to the ensemble
            ensemble['competitiveness_index'].append(num_competitive)


    print(ensemble['cutedge'])

    plt.figure()
    plt.hist(ensemble['cutedge'], edgecolor = "black")
    plt.title("{} Cutedge Ensemble ({} steps)".format(stateCode,total_steps))
    plt.xlabel("# Cutedges")
    plt.savefig("States/"+stateCode+"/Results/"+str(total_steps)+"Cutedge.png")
    #plt.show()


    print(ensemble['competitiveness_index'])
    #bins = range(0,num_dist+1)
    bins = [0,1,2,3,4,5,6,7,8,9,10,11]
    plt.figure()
    plt.hist(ensemble['competitiveness_index'], bins = bins, edgecolor = "black")
    plt.title("{} Competitive Index Ensemble ({} steps)".format(stateCode,total_steps))
    plt.xlabel("# Competitive districts ({} Total)".format(num_dist))
    plt.savefig("States/"+stateCode+"/Results/"+str(total_steps)+"CompetitivenessIndex.png")
    #plt.show()

    newFilePath = ""+stateCode+"/Results/"+str(total_steps)+"Ensemble.csv"
    with open(newFilePath, 'w') as myFile:
        writer = csv.writer(myFile)
        writer.writerow(['cutedge', 'competitiveness_index'])
        for i in range(0, len(ensemble['cutedge'])):
            writer.writerow([ensemble['cutedge'][i],ensemble['competitiveness_index'][i]])
