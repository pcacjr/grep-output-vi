__author__ = "Paulo Alcantara (pcacjr@gmail.com)"

import sys
import os
import re

vi_args = "-p"
vi_path = "/usr/bin/vi"

if __name__ == "__main__":
    if not os.path.exists(vi_path):
        print("ERROR: Set vi_path to your vi's path accordingly.")
        sys.exit(-1)

    cmd = vi_path + " " + vi_args + " "
    for arg in sys.argv[1::]:
        if re.match("^.*:.*", arg):
            # yeah - maybe we got a grep's output then split and add them to cmd
            cmd += arg.split(":")[0] + " "
            cmd += "+" + arg.split(":")[1] + " "
            continue

        # only a filename was given
        cmd += arg + " "

    os.system(cmd)
