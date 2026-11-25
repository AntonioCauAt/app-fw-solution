# Compute Forward model MEEG

<!-- brainlife-app:begin (generated from the App manifest; edit the manifest, not this block) -->

> **Computes an MEG forward solution with MNE-Python from a raw recording, a head-MRI transform and a FreeSurfer subject, building an oct6 source space and a single-layer BEM.**

Sets up an oct6 source space and a single-layer (MEG) BEM model from the FreeSurfer subject supplied in the bem input, then runs mne.make_forward_solution with the raw file's sensor configuration and the head-MRI transform, saving fwd.fif and an (empty) HTML report. Use it before inverse modelling of MEG data. Only include_meg is read from the parameters; EEG is always excluded and mindist (5 mm) and n_jobs (1) are hard-coded, so the other parameters have no effect.

| | |
|---|---|
| 📥 **Inputs** | `raw` · `neuro/meeg/mne/raw` · `neuro/meeg/mne/covariance` |
| 📤 **Outputs** | `neuro/meeg/mne/forward-inverse` |
| 🐳 **Container** | `brainlife/mne:1.2.1` |
| ⚙️ **Resources** | 8 CPUs · 20 GB memory · 1 h walltime |
| 🔗 **Run it** | [doi.org/10.25663/brainlife.app.827](https://doi.org/10.25663/brainlife.app.827) |

#### 📥 Inputs

| Input | Datatype | Required | Description |
|---|---|---|---|
| `bem1` | `raw` (bem) | yes | Directory holding a FreeSurfer subject named 'output' (used as subjects_dir) for the source space and BEM. |
| `fif1` | `neuro/meeg/mne/raw` | yes | Raw MEG recording in MNE .fif format providing the sensor configuration. |
| `trans1` | `neuro/meeg/mne/covariance` (trans) | yes | Head-to-MRI coregistration transform (-trans.fif), registered under the covariance datatype with the 'trans' tag. |

#### 📤 Outputs

| Output | Datatype | Description |
|---|---|---|
| `out_dir` | `neuro/meeg/mne/forward-inverse` | MEG forward solution (fwd.fif). |

<details>
<summary><b>⚙️ Parameters</b> (9)</summary>

| Parameter | Type | Default | Description |
|---|---|---|---|
| `trans` | string | `true` | If str, the path to the head<->MRI transform *-trans.fif file produced during coregistration. Can also be 'fsaverage' to use the built-in fsaverage transformation. If trans is None, an identity matrix is assumed. |
| `src` | string |  | Either a path to a source space file or a loaded or generated SourceSpaces. |
| `bem` | string |  | Filename of the BEM (.fif) to use, or a loaded ConductorModel. See make_bem_model() and make_bem_solution() to create a mne.bem.ConductorModel. |
| `include_meg` | boolean | `true` | Include MEG channels in the forward computation (the only parameter the code reads). |
| `include_eeg` | boolean | `true` | If True (default), include EEG computations. |
| `mindist` | number | `5` | Minimum distance of sources from inner skull surface (in mm). |
| `ignore_ref` | boolean | `true` | If True, do not include reference channels in compensation. This option should be True for KIT files, since forward computation with reference channels is not currently supported. |
| `n_jobs` | number | `1` | The number of jobs to run in parallel. If -1, it is set to the number of CPU cores. Requires the joblib package. None (default) is a marker for ‘unset’ that will be interpreted as n_jobs=1 (sequential execution) unless the call is performed under a joblib.parallel_config context manager that sets another value for n_jobs. |
| `verbose` | boolean | `false` | Control verbosity of the logging output. If None, use the default verbosity level. See the logging documentation and mne.verbose() for details. Should only be passed as a keyword argument. |

</details>

📚 **References used by this App:**
- Gramfort A, Luessi M, Larson E, et al. MEG and EEG data analysis with MNE-Python. Front Neurosci 7:267 (2013). [doi:10.3389/fnins.2013.00267](https://doi.org/10.3389/fnins.2013.00267)
- Avesani P, McPherson B, Hayashi S, et al. The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services. Sci Data 6, 69 (2019). [doi:10.1038/s41597-019-0073-y](https://doi.org/10.1038/s41597-019-0073-y)

<!-- brainlife-app:end -->

[![Abcdspec-compliant](https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg)](https://github.com/brain-life/abcd-spec)
[![Run on Brainlife.io](https://img.shields.io/badge/Brainlife-bl.app.672-blue.svg)](https://doi.org/10.25663/brainlife.app.672)

Brainlife App to compute the Forward Model (MEEG) using the `mne.make_forward_solution` function to create a forward solution for combined MEG and EEG data based on the BEM model, source space setup, and sensor configuration.



1) Input file is:
    * `fif` meeg data file
    * `trans` covariance data file
    * `bem` meeg data file
    
2) Input parameters are:

* `src` Source Space File.

* `meg` Include MEG computations.

* `eeg` Include EEG computations.

* `mindist` Distance of sources.

* `ignore_ref` Reference channels.

* `n_jobs` The number of jobs to run in parallel.

* `verbose` Control verbosity of the logging output.


3) Ouput files are:
    * forward solution
    * a html report
   

## Authors
- Guiomar Niso (guiomar.niso@gmail.com)
- Antonio Caulín (antoniocaulinatienzar@gmail.com)

## Citations
We kindly ask that you cite the following articles when publishing papers and code using this code. 

*- brainlife.io Publishing and Apps:*

Avesani, P., McPherson, B., Hayashi, S. et al. **The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services**. Sci Data 6, 69 (2019). https://doi.org/10.1038/s41597-019-0073-y

*- MNE-Python package:* 

Gramfort A, Luessi M, Larson E, Engemann DA, Strohmeier D, Brodbeck C, Goj R, Jas M, Brooks T, Parkkonen L, and Hämäläinen MS.  **MEG and EEG data analysis with MNE-Python**. Frontiers in Neuroscience, 7(267):1–13, 2013. https://doi.org/10.3389/fnins.2013.00267

## Funding Acknowledgement
brainlife.io is publicly funded and for the sustainability of the project it is helpful to Acknowledge the use of the platform. We kindly ask that you acknowledge the funding below in your publications and code reusing this code.

[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-1636893](https://img.shields.io/badge/NSF_BCS-1636893-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-ACI-1916518](https://img.shields.io/badge/NSF_ACI-1916518-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1916518)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NIH-NIBIB-R01EB030896](https://img.shields.io/badge/NIH_NIBIB-R01EB030896-green.svg)](https://grantome.com/grant/NIH/R01-EB030896-01)


#### MIT Copyright (c) 2021 brainlife.io The University of Texas at Austin and Indiana University
