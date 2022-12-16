import ensemble
# Run ensemble (1k,3k,9k steps) for VA
# ensemble.runEnsemble(stateCode = "VA", filePath = "States/VA/Data/VA_precincts.json", num_dist=11, total_steps = 1000, pop_tolerance = .02, district_gap_threshold= .05)
# ensemble.runEnsemble(stateCode = "VA", filePath = "States/VA/Data/VA_precincts.json", num_dist=11, total_steps = 3000, pop_tolerance = .02, district_gap_threshold= .05)
# ensemble.runEnsemble(stateCode = "VA", filePath = "States/VA/Data/VA_precincts.json", num_dist=11, total_steps = 9000, pop_tolerance = .02, district_gap_threshold= .05)

ensemble.runEnsemble(stateCode = "AL", filePath = "States/GA/Data/al-bg-connected.json", num_dist = 11, total_steps = 1000, pop_tolerance = .02, district_gap_threshold=.05)
