#!/usr/bin/env python
'''
Example script to load and plot results from the CFM.
'''

# Copyright (C) 2019 C. Max Stevens <maxstev@uw.edu>
# Distributed under terms of the MIT license.

import matplotlib.pyplot as plt 
import h5py as h5
import os
import sys
import numpy as np
import scipy as sp
import pickle
import seaborn as sns 
sns.set()

def plotter(rfolder,saver):
	'''
	Function that plots.
	'''

	rfile = 'CFMresults_test2.hdf5'
	fn = os.path.join(rfolder,rfile)
	f = h5.File(fn,'r')

	timesteps = f['depth'][1:,0]
	stps = len(timesteps)
	depth = f['depth'][1:,1:]
	density = f['density'][1:,1:]
	temperature = f['temperature'][1:,1:]
	# dip_all = f['DIP'][:,:]
	f.close()

	f1,a1 = plt.subplots()
	a1.plot(density[0,:],depth[0,:])
	a1.plot(density[853,:],depth[853,:])
	a1.plot(density[-1,:],depth[-1,:])
	a1.invert_yaxis()
	a1.grid(True)
	plt.xlabel('density [kg m-3]')
	plt.ylabel('depth [m]')
	plt.title('density-depth plot')
	if saver:
		f1.savefig('Example_DepthDensity.png')

if __name__ == '__main__':
	
	saver = True
	rfolder = 'C:\\Users\\ClerxN\\Documents\\GitHub\\CommunityFirnModel\\CFM_main\\test_results\\KAN_U' # alter this to point to the results folder.

