import os, sys

os.system(sys.executable + " LMCassembler.py program.txt program.lmc") # assemble/compile from program.txt to program.lmc
os.system(sys.executable + " LMC.py program.lmc") # run program.lmc