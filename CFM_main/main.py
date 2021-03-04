#!/usr/bin/env python
"""
main.py
=======
The core file to run the CFM

This file creates classes for the spin up and main runs and runs the model.
"""

import sys
import os
from firn_density_spin import FirnDensitySpin
from firn_density_nospin import FirnDensityNoSpin
from datetime import datetime
import time
import json
import shutil
import pdb

__author__ = "C. Max Stevens, Vincent Verjans, Brita Horlings, Annikah Horlings, Jessica Lundin"
__license__ = "MIT"
__version__ = "1.0.5"
__maintainer__ = "Max Stevens"
__email__ = "maxstev@uw.edu"
__status__ = "Production"


if __name__ == '__main__':

    if len(sys.argv) >= 2:
        configName = os.path.join(os.path.dirname(__file__), sys.argv[1])
        print(configName)
    else:
        print('No .json configuration file specified. Exiting.')
        sys.exit()
        # configName = os.path.join(os.path.dirname(__file__), 'generic.json')

    with open(configName, "r") as f:
        jsonString = f.read()
        c = json.loads(jsonString)

    tic=time.time()

    print("")
    print("-----------------------------------------------------------------------")
    print("-----------------------------------------------------------------------")
    print("<<<<<<<< Running the Community Firn Model (CFM), Version %s >>>>>>>>" %__version__)
    print("<<<<<<<< Developed at the University of Washington             >>>>>>>>")
    print("<<<<<<<< Please cite your use!                                 >>>>>>>>")
    print("<<<<<<<< Distributed under terms of the MIT license.           >>>>>>>>")
    print("-----------------------------------------------------------------------")
    print("-----------------------------------------------------------------------")
    print("")
    print('start model run at %s' % datetime.now().strftime('%m/%d/%Y, %H:%M:%S'))

    if os.path.isfile(c['resultsFolder']+'/'+c['spinFileName']) and '-n' not in sys.argv:
        print('Skipping Spin-Up run;', c['resultsFolder']+'/'+c['spinFileName'], 'exists already')
        try:
            os.remove(c['resultsFolder']+'/'+c['resultsFileName'])
            print('deleted', c['resultsFolder']+'/'+c['resultsFileName'])
        except:
            pass
        firn = FirnDensityNoSpin(configName)
        firn.time_evolve()

    else:

        firnS = FirnDensitySpin(configName)
        firnS.time_evolve()

        print('end spin-up run at %s' % datetime.now().strftime('%m/%d/%Y, %H:%M:%S'))

        firn = FirnDensityNoSpin(configName)
        firn.time_evolve()

    shutil.copy(configName,c['resultsFolder'])
    
    print('end model run at %s' % datetime.now().strftime('%m/%d/%Y, %H:%M:%S'))
    print('run time =' , time.time()-tic , 'seconds')
