# SimAb
Simulating Abundances (SimAb) is a planet formation simulation, focusing on the atmosphere acretion of gas gian planets. To read more about the assumptions in this simulation you can read SimAb.

At this moment you can run the simulation in two different modes.
-The single simulation mode that is run through running Srun.py, by specifying the initial conditions, and the mature planet mass and orbital distance.
-The multi run simulation mode that is possible through running the Mrun.py. When using this mode, you can specify the mass and the final orbital distance of the mature planet and the simulation randomly asigns initial orbital distance, initial core mass, initial planetesimal ratio, and initial dut grain fraction. These parameters are explain in detail in the SimAb paper. You need to also indicate the number of the random rus, and the folder name where the output is recorded. Also make sure to creat a folder with the name run(n), where (n) is the number of the run that you are running. The outputs of each single run is recorded in a text file in the folder run(n) under test(m).txt, m is the indicator of which random test it is. The final composition is recorded in a file called run_sum(n).txt as [(x/H)of the planet]/[(X/H) of the sun].

You can plot the results using the jupyter codes available.

The values used to write the SimAb paper are available in the output folder.

We kindly ask you to reference the paper if your usage of this simulation resulted in a publication.
