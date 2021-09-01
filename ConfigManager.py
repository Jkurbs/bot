__author__      = "Kerby Jean"
__copyright__   = "Copyright 2021, GreedyBoy"
__credits__     = ["Kerby Jean"]
__license__     = "Proprietary"
__version__     = "1.0.0"
__maintainer__  = "Kerby Jean"
__email__       = "kerby.jean@gmail.com"
__status__      = "Test"

import csv

def getConfig():
    with open("config.csv", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(row)
            return row['apiKey'], row['b64secret'], row['passphrase'], row['githubToken'], row['repoName'], row['dataBranchName']