# Probe-Designer
A tool to design probes for third generation in situ hybridization

Uses
This tool will allow one to create a set of probes that can be used in the third generation in situ hybridization
The protocol can be found at this link: https://www.ncbi.nlm.nih.gov/pubmed/29945988
The program is written in python and can be run on a machine with python 3.7 installed.
There are two other modules that need to be installed for it to work. 
Biopython wich can be installed with the command pip install biopython
DNA Features viewer is the other and can be installed with the command pip install dna_features_viewer

To run the program download it and run it however you run python programs.
There are three things that will be asked for when you run the script, the first is the file that contains the sequence. This file should only the contain the sequence in a single line in a text file. The next will be the name of the sequence you are working on and finally the sequence of the initiator that will be added to the probes. 
The output of the program will be a folder that contains three things. The first is the set of probes that consists of the probe a two nucelotide TT connector and the initiator. The next will be a bunch of graphs that allow for the visualization of the Probes and the sequence to which they bond. The last is a results file that contains the sequence initiator and all the probes along with their locations within the sequence. 
