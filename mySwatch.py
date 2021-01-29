#!/usr/bin/python3

# MYSWATCH - Show all SLURM jobs currently running
#          ./mySwatch.py
#          ./mySwatch.py --help
#          ./mySwatch.py --mine

import subprocess as sp
import argparse as ap

parser = ap.ArgumentParser(description= "Show all running SLURM jobs")
parser.add_argument("--mine", action="store_true", help="Display only my jobs")
parser.add_argument("--local", action="store_true", help="Display only jobs local to this cluster")
args = parser.parse_args()

#command = 'squeue -h -i 3 -o "ID: "%A" | PARTITION: "%P" | NAME: "%j" | USER: "%u" | STATE: "%T" | REASON/NODE: "%R" | START: "%S" | TIME USED: "%M" |  TIME LEFT: "%L" | PRIORITY: "%Q" | NODES: "%D" | NODE LIST: "%N'
#command = 'squeue -i 3 -O "jobid,partition,name,username,state,reasonlist,starttime,endtime,prioritylong,maxnodes"'
command = "squeue -i 3 -o %8A%10P%20j%9u%10T%18R%21S%10M%20L%12Q%8D%30N"

# If "mine" argument, only show my jobs
if (args.mine):
    command += " --me"

# If "local" argument, only show jobs local to this cluster
if (args.local):
    command += " --local"

print(f"\n{command}\n")
print("-------------------------------------------------------------------------------------------------------------------------")
sp.run(command, shell=True)
print("\n")

