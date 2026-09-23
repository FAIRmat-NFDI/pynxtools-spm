# Evidence files: the scan offset is the centre of the scan area

Raw files behind the empirical test described in
[Scan region, axes and scan direction](../../explanation/scan-region-conventions.md).
Both scans have the same `OffsetX`/`OffsetY`, so the 5 µm scan sits in the middle
of the 20 µm scan if the offset is the centre, and in a corner if it is not.
Unmodified copies, checked against the Zenodo MD5 checksums.

| File | Scan size | Channel |
|---|---|---|
| `spmlab/PMIS2-C8_ML2_p1_5__040925135420.SIG_HEIGHT_SENSOR_FRW.FLT` | 5 µm | Height sensor, forward |
| `spmlab/PMIS2-C8_ML2_p1_20__040925132340.SIG_HEIGHT_SENSOR_FRW.FLT` | 20 µm | Height sensor, forward |

Both come from `AFM.zip` of A. James et al. (2025), *PiF-IR data of PMIS-C8
monolayer films on nanostructured and planar Au substrates, complementary AFM,
FTIR/ATR and BAM data and calculated PMIS-C8 spectra*,
[10.5281/zenodo.18060234](https://doi.org/10.5281/zenodo.18060234), CC BY 4.0.

The Omicron `.sm4` files used in the same test are not copied here because of
their size. Take them by name from P. M. Leidinger (2024), *Influence of zinc
oxide nanoparticles on the carbon accumulation on silver exposed to carbon
dioxide hydrogenation reaction conditions*,
[10.5281/zenodo.14268803](https://doi.org/10.5281/zenodo.14268803), CC BY 4.0:
`VT231211_A1_0064.sm4`, `VT231211_A1_0065.sm4`, `VT231205_A1_0063.sm4` and
`VT231205_A1_0064.sm4`. The record holds many more files.

The RHK parameter-block comparison uses
`tests/data/omicron/stm/sm4_dflt_conf_down/Figure_6c.SM4`, already in the repository.
