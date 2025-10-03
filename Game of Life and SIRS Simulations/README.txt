***ANIMATIONS***

GoLanimation.py:
To run the Game of Life Animation, type:
"%run GoLanimation.py {size} {random/oscillator/glider}"

SIRSanimation.py:
To run SIRS Animation, type:
"%run SIRSanimation.py {size} {p1} {p2} {p3}"


***DATA FILES Folder***

Contains all the txt data files for the graphs

makes all the graphs.py:
Produces all the graphs from the data files in the folder


***GRAPHS Folder***

Contains PNGs of the graphs

Note 1: The velocity of the glider in the Game of Life is written in the title of the relevant graph

Note 2: The error bars for the plot of the variance of the number of infected sites in SIRS along a cut are small, but still there (in red)

***OTHER CODE***

GoLpart2.py:
Produces a data file (GoLpart2data.txt) for a histogram of the times needed to equilibrate the Game of Life with random intial conditions

GoLpart3.py:
Produces a data file (GoLpart3data.txt) for a plot of the movement of the glider centre of mass in the Game of Life (x-axis and y-axis), to find the velocity of the glider

SIRSpart3.py:
Produces a data file (SIRSpart3data.txt) for a p1-p3 colour plot of the average fraction of infected sites in SIRS with p2 = 0.5

SIRSpart4.py:
Produces a data file (SIRSpart4data.txt) for a plot of the variance of the number of infected sites in SIRS along a cut at fixed p2 = p3 = 0.5

SIRSpart5.py:
Produces a data file (SIRSpart5data.txt) for a plot of Immunity Fraction vs Average Fraction of Infected States in SIRS, to find the minimum immunity fraction to prevent spread




