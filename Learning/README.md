# Learning — SPM Experiment Notes

Personal study notes and annotated raw data files from SPM experiments processed through pynxtools-spm.

Each subfolder under `SPM_Experiments/` covers one specific experiment type or instrument combination, containing:
- `experiment_analysis.md` — structured notes (technique, geometry, measured properties, instruments, references)
- `raw_data/` — copy of the original data file(s) used as examples

---

## Index

### SPM Experiments

| Folder | Technique | Vendor | Flavor | Key science |
|---|---|---|---|---|
| [Bruker_AFM_PeakForce_QNM](SPM_Experiments/Bruker_AFM_PeakForce_QNM/experiment_analysis.md) | AFM | Bruker Dimension Icon | PeakForce QNM Force-Volume | Nanomechanical mapping: modulus, adhesion, deformation, dissipation |

---

## How to add a new entry

1. Create `SPM_Experiments/<Vendor>_<Technique>_<Flavor>/`
2. Add `experiment_analysis.md` covering: file type, experiment type, scan geometry, measured properties, instruments, references, pynxtools-spm connection.
3. Place a copy of the raw data file(s) in `raw_data/`.
4. Add a row to the index table above.

---

## Techniques covered (planned)

- [ ] Bruker AFM — PeakForce QNM (force-volume) ✓
- [ ] Bruker AFM — Standard contact/tapping imaging
- [ ] Nanonis STM — Constant-current imaging
- [ ] Nanonis STS — Bias spectroscopy (dI/dV)
- [ ] Nanonis AFM — Non-contact imaging
- [ ] Omicron STM — UHV imaging
