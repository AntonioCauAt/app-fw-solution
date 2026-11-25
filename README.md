<h1 align="center">Compute forward model MEEG</h1>

<p align="center">
  Computes an MEG forward solution with MNE-Python from a raw recording, a head-MRI transform and a FreeSurfer subject, building an oct6 source space and a single-layer BEM.
</p>

<p align="center">
  <a href="https://github.com/brainlife/abcd-spec"><img src="https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg" alt="ABCD Spec v1.1"></a>
  <a href="https://doi.org/10.25663/brainlife.app.827"><img src="https://img.shields.io/badge/Brainlife-brainlife.app.827-blue.svg" alt="Run on brainlife.io"></a>
</p>

## At a glance

<!-- brainlife-app:begin (generated from the App manifest; edit the manifest, not this block) -->

> **Computes an MEG forward solution with MNE-Python from a raw recording, a head-MRI transform and a FreeSurfer subject, building an oct6 source space and a single-layer BEM.**

Sets up an oct6 source space and a single-layer (MEG) BEM model from the FreeSurfer subject supplied in the bem input, then runs mne.make_forward_solution with the raw file's sensor configuration and the head-MRI transform, saving fwd.fif and an (empty) HTML report. Use it before inverse modelling of MEG data. Only include_meg is read from the parameters; EEG is always excluded and mindist (5 mm) and n_jobs (1) are hard-coded, so the other parameters have no effect.

| | |
|---|---|
| **Inputs** | `raw` · `neuro/meeg/mne/raw` · `neuro/meeg/mne/covariance` |
| **Outputs** | `neuro/meeg/mne/forward-inverse` |
| **Container** | `brainlife/mne:1.2.1` |
| **Resources** | 8 CPUs · 20 GB memory · 1 h walltime |
| **Run it** | [doi.org/10.25663/brainlife.app.827](https://doi.org/10.25663/brainlife.app.827) |

#### Inputs

| Input | Datatype | Required | Description |
|---|---|---|---|
| `bem1` | `raw` (bem) | yes | Directory holding a FreeSurfer subject named 'output' (used as subjects_dir) for the source space and BEM. |
| `fif1` | `neuro/meeg/mne/raw` | yes | Raw MEG recording in MNE .fif format providing the sensor configuration. |
| `trans1` | `neuro/meeg/mne/covariance` (trans) | yes | Head-to-MRI coregistration transform (-trans.fif), registered under the covariance datatype with the 'trans' tag. |

#### Outputs

| Output | Datatype | Description |
|---|---|---|
| `out_dir` | `neuro/meeg/mne/forward-inverse` | MEG forward solution (fwd.fif). |

<details>
<summary><b>Parameters</b> (9)</summary>

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

<!-- brainlife-app:end -->

## Running the App

### On brainlife.io

Open the App at [doi.org/10.25663/brainlife.app.827](https://doi.org/10.25663/brainlife.app.827), choose `raw`, `neuro/meeg/mne/raw`, `neuro/meeg/mne/covariance` from your project, set the parameters and press **Execute**. The results are saved to your project as `neuro/meeg/mne/forward-inverse`.

### Locally

You need [Singularity/Apptainer](https://apptainer.org/) (the App runs in `brainlife/mne:1.2.1`), [`jq`](https://jqlang.github.io/jq/).

1. Clone this repository.
2. Create `config.json` with the paths to your inputs and the parameters:

   ```json
   {
       "output": "/path/to/bem1/output",
       "mne": "/path/to/fif1/mne",
       "cov": "/path/to/trans1/cov",
       "trans": "true",
       "src": "",
       "bem": "",
       "include_meg": true,
       "include_eeg": true,
       "mindist": 5,
       "ignore_ref": true,
       "n_jobs": 1,
       "verbose": false
   }
   ```

3. Run `./main`.

## Citing

If you use this App, please cite it, the software it builds on and brainlife.io:

- Compute forward model MEEG. brainlife.io App. [doi:10.25663/brainlife.app.827](https://doi.org/10.25663/brainlife.app.827)
- Gramfort A, Luessi M, Larson E, et al. MEG and EEG data analysis with MNE-Python. Front Neurosci 7:267 (2013). [doi:10.3389/fnins.2013.00267](https://doi.org/10.3389/fnins.2013.00267)
- Fischl. FreeSurfer. *NeuroImage* 62:774-781 (2012). [doi:10.1016/j.neuroimage.2012.01.021](https://doi.org/10.1016/j.neuroimage.2012.01.021)
- Hayashi S, Caron BA, Heinsfeld AS, et al. brainlife.io: a decentralized and open-source cloud platform to support neuroscience research. *Nature Methods* 21:809–813 (2024). [doi:10.1038/s41592-024-02237-2](https://doi.org/10.1038/s41592-024-02237-2)
- Avesani P, McPherson B, Hayashi S, et al. The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services. *Scientific Data* 6:69 (2019). [doi:10.1038/s41597-019-0073-y](https://doi.org/10.1038/s41597-019-0073-y)

## Authors

- Guiomar Niso
- Antonio Caulín

## Funding

[![Wellcome-226486/Z/22/Z](https://img.shields.io/badge/Wellcome-226486%2FZ%2F22%2FZ-purple.svg)](https://wellcome.org/)
[![NIH-NINDS-U24NS140384](https://img.shields.io/badge/NIH_NINDS-U24NS140384-green.svg)](https://reporter.nih.gov/project-details/11261037)
[![NIH-NINDS-UM1NS132207](https://img.shields.io/badge/NIH_NINDS-UM1NS132207-green.svg)](https://reporter.nih.gov/project-details/11411328)
[![NIH-NIBIB-R01EB029272](https://img.shields.io/badge/NIH_NIBIB-R01EB029272-green.svg)](https://reporter.nih.gov/project-details/10262925)
[![NIH-NIBIB-R01EB030896](https://img.shields.io/badge/NIH_NIBIB-R01EB030896-green.svg)](https://reporter.nih.gov/project-details/10428625)
[![NIH-NIMH-R01MH126699](https://img.shields.io/badge/NIH_NIMH-R01MH126699-green.svg)](https://reporter.nih.gov/project-details/10460628)
[![NIH-NIDCD-R01DC020088](https://img.shields.io/badge/NIH_NIDCD-R01DC020088-green.svg)](https://reporter.nih.gov/project-details/11140284)
[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-2203524](https://img.shields.io/badge/NSF_BCS-2203524-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2203524)
[![NSF-IIS-1636893](https://img.shields.io/badge/NSF_IIS-1636893-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-OAC-2148729](https://img.shields.io/badge/NSF_OAC-2148729-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2148729)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NSF-IIS-2148700](https://img.shields.io/badge/NSF_IIS-2148700-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2148700)
[![NSF-OAC-1916518](https://img.shields.io/badge/NSF_OAC-1916518-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1916518)

<sub>brainlife.io, which runs this App, is publicly funded by Wellcome, the U.S. National Institutes of Health and the U.S. National Science Foundation; acknowledging that support helps keep it running.</sub>
