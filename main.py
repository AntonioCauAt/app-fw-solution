# set up environment
import os
import json
import mne

import numpy as np


import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Current path
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

# Populate mne_config.py file with brainlife config.json
with open(__location__+'/config.json') as config_json:
    config = json.load(config_json)
    

# == CONFIG PARAMETERS ==
fname_raw    = config['mne']
subjects_dir = config['output'] 
fname_trans  = config ['cov']
include_meg  = config['include_meg']
subject = 'output'
fname_cov = config ['cov']

# == SOURCE SPACE ==
#Assume that coregistration is done
src = mne.setup_source_space(subject, spacing='oct6', subjects_dir=subjects_dir,add_dist=False)


#Visualization?
#mne.viz.plot_alignment(raw, trans_fname, subject=subject, dig=False, src=src,subjects_dir=subjects_dir, verbose=True, meg=False,eeg=False);
                             

# == FORWARD SOLUTION ==

# Compute BEM Model
conductivity = (0.3,)  # for single layer (MEG)
# conductivity = (0.3, 0.006, 0.3)  # for three layers (EEG)
model = mne.make_bem_model(subject=subject, ico=4, conductivity=conductivity, subjects_dir=subjects_dir)
bem = mne.make_bem_solution(model)


# Compute Forward Model
fwd = mne.make_forward_solution(fname_raw, 
            trans=fname_trans,
            src=src, 
            bem=bem,
            meg=include_meg,  # include MEG channels
            eeg=False,  # exclude EEG channels
            mindist=5.0,  # ignore sources <= 5mm from inner skull
            n_jobs=1)  # number of jobs to run in parallel

# How each point in the brain space contributes to the signal measured at each sensor
leadfield = fwd['sol']['data']

# == SAVE RESULTS ==

# SAVE DATA (fwd.fif)
fwd_fname = os.path.join('out_dir', 'fwd.fif')
mne.write_forward_solution(fwd_fname, fwd, overwrite=True)

# SAVE FIGURE
#

# SAVE REPORT
report = mne.Report(title='Report')
report_path = os.path.join('out_dir_report', 'report.html')
report.save(report_path, overwrite=True)