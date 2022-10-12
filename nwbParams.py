'''
NWB parameters common across all animals and recording sessions
Parameters that may change:
  dataset
'''

import pathlib
import os
import re

global rawDataFolder, derivedDataFolder, derivedDataFolderNWB

projectName = 'Brainwide Infraslow Activity Dynamics'
experimenter = 'Martynas Dervinis'
institution = 'University of Leicester'
publications = []
lab = 'Michael Okun lab'
dataset = 'neuropixels'
videoFrameRate = 25.0 # Hz

# Find the repository root folder
rootFolderName = 'convert2nwbPyNpx'
rootFolderCandidate = pathlib.Path(__file__).parent.resolve()
endInd = re.search(rootFolderName, str(rootFolderCandidate)).end()
rootFolder = str(rootFolderCandidate)[:endInd]

# Assign data folders
if 'neuronexus' in dataset:
  rawDataFolder = os.path.join(rootFolder, 'nnx_raw_derived_data'); # Raw and certain derived Neuronexus data for all animals
  derivedDataFolder = os.path.join(rootFolder, 'nnx_derived_data'); # Neuroscience Gateway analysis scripts, functions, and downloaded processed Neuronexus data for all animals
  derivedDataFolderNWB = os.path.join(rootFolder, 'nnx_derived_data_nwb'); # Derived Neuronexus data for all animals placed in NWB format
elif 'neuropixels' in dataset:
  rawDataFolder = os.path.join(rootFolder, 'npx_raw_derived_data'); # Raw and certain derived Neuropixels data for all animals
  derivedDataFolder = os.path.join(rootFolder, 'npx_derived_data'); # Neuroscience Gateway analysis scripts, functions, and downloaded processed Neuropixels data for all animals
  derivedDataFolderNWB = os.path.join(rootFolder, 'npx_derived_data_nwb'); # Derived Neuropixels data for all animals placed in NWB format