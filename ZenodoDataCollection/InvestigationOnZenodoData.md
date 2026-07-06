# Zenodo SPM Dataset Investigation

## Datasets of Interest

*Datasets with known, supported file formats (Bruker `.spm`, Nanonis `.sxm`/`.dat`, Omicron `.sm4`) that are relevant to our SPM parser development.*

1. **Dataset - Autonomous scanning electrochemical cell microscopy enables rapid exploration of large compositionally complex material spaces**

   - **DOI**: 10.5281/zenodo.20439519
   - **URL**: [https://doi.org/10.5281/zenodo.20439519](https://doi.org/10.5281/zenodo.20439519)
   - **Date**: 2026-05-28
   - **Access**: open
   - **License**: CC BY 4.0
   - **By**: Thelen, Felix, Kim, Moonjoo, de Oliveira, Geovane Arruda et al.
   - **Tags**: Hydrogen evolution reaction, Active learning, Electrochemistry, Materials science, Magnetron sputtering, Scanning electrochemical cell microscopy, Gaussian process regression, Electrocatalysis
   - **Desc**: This dataset contains all experimental and computational data associated with the autonomous Scanning Electrochemical Cell Microscopy (SECCM) platform described in the accompanying publication. The platform combines robotic SECCM with active learning and multi-output Gaussian process (GP) modeling for high-throughput electrochemical characterization of compositionally complex thin-film materials libraries, validated on the Au-Ir-Rh ternary system as a model case for hydrogen evolution reaction (HER) electrocatalyst discovery. Three Au-Ir-Rh thin-film materials libraries were fabricated by magnetron co-sputtering onto 100 mm diameter Sapphire wafers and are referred to throughout as Au-rich, Ir-rich, and Rh-rich according to their position in the ternary composition space. All characterization techniques share a unified measurement grid of 342 measurement areas distributed across each library at 4.5 mm spacing. A coordinates file providing the x, y positions of all 342 MAs is included. Dataset contents: Energy-Dispersive X-ray Spectroscopy (EDX) Volume compositions (Au, Ir, Rh in at.%) at all 342 MAs for each of the three libraries. Provided in .csv format. X-ray Photoelectron Spectroscopy (XPS) Due to the lower throughput of XPS, 13 localized surface composition measurements were performed per library. The full set of measurement areas were predicted using a Gaussian process regression model (method described here ). Two files are provided per library: one containing the measured XPS compositions and one containing the GP-predicted values. In addition to Au, Ir, and Rh, the XPS dataset includes surface contents of oxygen (O), carbon (C), native Rh oxide, and Rh hydroxide. Provided in .csv format. X-ray Diffraction (XRD) Diffractograms (2θ position vs. intensity in counts) at all 342 areas for each library. Provided in .csv format. Atomic Force Microscopy (AFM) Raw data from 15 localized AFM measurements (5 per library), recorded in Bruker NanoScope raw data format. Representative images are shown in the Supporting Information of the accompanying paper. SECCM Linear sweep voltammograms (LSVs) acquired at each area for all three libraries. Due to collision risk of the environmental chamber, 20 areas per library were excluded, yielding 322 LSVs per library. Each LSV file contains three columns: potential vs. the reversible hydrogen electrode (RHE, in V), mean current density (in A/cm^2), and the standard deviation of the current density, computed from three individually recorded LSVs that are averaged per measurement area. An additional file contains the parameters extracted by fitting the averaged LSVs to an analytical equation described in the publication: the limiting current density I _lim (A/cm^2), the transfer coefficient α (dimensionless), and the standard rate constant k^0 (cm/s). Provided in .csv format. Active Learning Animations: Two animations (.mp4 format) illustrating the active learning process applied to the Au-Ir-Rh composition space. Each frame corresponds to one iteration of the algorithm and displays the current LSV data, the extracted fit parameters, the GP model predictions across the ternary space, and the acquisition function values used to select the next measurement. One animation corresponds to the baseline GP implementation; the second corresponds to the noise-aware GP variant, which incorporates per-area measurement uncertainty derived from the standard deviations of the individual LSV fit parameters prior to averaging. Measurement Video: (.mp4) of the measurement process of the first 400 measurements/training iterations. It shows the robotic transfer, the environmental chamber and visual capillary approach and the electrocatalytic measurements.

   **Comment**: The dataset might be parsed by the current AFM parser. (Downloaded)

---

2. **Annexin V assembly dynamics on lipid bilayers by High-Speed AFM**

   - **DOI**: 10.5281/zenodo.19254504
   - **URL**: [https://doi.org/10.5281/zenodo.19254504](https://doi.org/10.5281/zenodo.19254504)
   - **Date**: 2026-03-27
   - **Access**: open
   - **License**: CC BY 4.0
   - **By**: Heath, George R
   - **Tags**: AFM, high-speed atomic force microscopy, atomic force microscopy, HS-AFM, annexin V, annexin, lipid bilayer, raw data
   - **Desc**: This dataset contains curated high-speed atomic force microscopy (HS-AFM) videos capturing the dynamic assembly of Annexin V on supported lipid bilayers. Each movie is accompanied by a metadata table detailing key acquisition parameters and imaging conditions. This dataset is released as an open resource and is made freely available to support reuse in high-speed AFM data analysis, algorithm development, machine learning applications, and studies of membrane protein assembly dynamics. Methods Summary Membrane: DOPC:DOPS = 8:2 Protein: Annexin V (33 kDa, human placenta) in imaging solution Imaging Buffer: 10 mM HEPES (pH 7.4), 150 mM NaCl, 2 mMCaCl₂ AFM: NanoRacer (Bruker) Probe: USC-F1.2-k0.15 (NanoWorld) Full method description Annexin V (33 kDa, human placenta) was purchased from Sigma-Aldrich, and lipids dioleoyl-phosphatidylcholine (DOPC) and dioleoyl-phosphatidylserine (DOPS) were obtained from Avanti Polar Lipids. Lipids were mixed in chloroform at a molar ratio of DOPC:DOPS = 8:2. The solvent was evaporated under a nitrogen stream and further dried under vacuum for 2 hours. The resulting lipid film was resuspended in buffer (10 mM HEPES, pH 7.4, 150 mM NaCl, 2 mM CaCl₂) to form multilamellar vesicles. These were subsequently tip-sonicated for 10 minutes to produce small unilamellar vesicles (SUVs). To form supported lipid bilayers (SLBs), 5 µL of the SUV suspension (0.1 mg mL⁻¹ total lipid concentration) was deposited onto freshly cleaved mica. Following vesicle fusion, excess lipids were removed by rinsing with deionized water and then buffer. Annexin V was introduced into the imaging buffer at varying concentrations (100-200nM). All high-speed AFM measurements were performed using the NanoRacer HS-AFM (Bruker) operating in amplitude modulation mode. Imaging was conducted in liquid at ambient temperature within an acoustic isolation enclosure on an active anti-vibration table. Short cantilevers (USC-F1.2-k0.15, NanoWorld) were used, with nominal properties: Spring constant: ~0.15 N·m⁻¹; Resonance frequency: ~0.6 MHz; Quality factor: ~2 Data Access and Tools The dataset includes raw HS-AFM image sequences along with associated metadata for each acquisition. Recommended tools for accessing and analysing the data: NanoLocz PlayNano Note! Use the “Height” channel (feedback signal) rather than the “Height Measured” channel (capacitive measurement). Notes The dataset focuses on time-resolved membrane-protein assembly dynamics. Metadata fields include scan size, pixel resolution, scan speed, line rate, and imaging channel. Image files are organised in 1 zip per image stack, with corresponding entries in the metadata table: Folder Name Frames Use channel Speed (FPS) Scan Size (nm) y pixels x pixels Pixel Per nm Line Speed (Hz) Notes imaging-13.08.28.653 7 Height-ReTrace 0.78 600 256 256 0.43 200 diffusing annexin imaging-13.26.46.569 81 Height -Bi-Directional 1.56 100 256 256 2.56 200 diffusing annexin imaging-13.30.11.268 8 Height -Bi-Directional 1.56 200 256 256 1.28 200 diffusing annexin imaging-13.37.48.575 7 Height -Bi-Directional 0.78 400 512 512 1.28 200 diffusing annexin imaging-13.46.35.510 59 Height -Bi-Directional 0.78 350 512 512 1.46 200 lattice appears imaging-13.47.52.797 9 Height -Bi-Directional 0.78 200 512 512 2.56 200 lattice assembly imaging-13.48.05.546 41 Height -Bi-Directional 1.56 200 256 256 1.28 200 lattice assembly imaging-13.48.42.653 36 Height-ReTrace 0.78 200 256 256 1.28 200 lattice assembly imaging-13.49.30.677 17 Height -Bi-Directional 1.56 200 256 256 1.28 200 lattice assembly imaging-13.49.42.515 100 Height -Bi-Directional 2.73 200 256 256 1.28 350 lattice assembly imaging-13.51.38.236 75 Height -Bi-Directional 12.50 200 128 128 0.64 800 lattice assembly imaging-13.51.54.501 56 Height -Bi-Directional 15.63 200 128 128 0.64 1000 lattice assembly imaging-13.52.13.441 81 Height -Bi-Directional 11.72 200 128 128 0.64 750 lattice assembly imaging-13.52.33.276 73 Height -Bi-Directional 12.50 200 128 128 0.64 800 lattice assembly imaging-13.53.38.041 437 Height -Bi-Directional 23.44 100 64 128 1.28 750 lattice assembly imaging-13.54.14.288 436 Height -Bi-Directional 31.25 100 64 128 1.28 1000 lattice assembly imaging-13.55.22.617 490 Height -Bi-Directional 31.25 85 64 128 1.51 1000 lattice assembly imaging-13.55.40.346 762 Height -Bi-Directional 31.25 85 64 128 1.51 1000 lattice assembly imaging-14.01.11.254 15 Height -Bi-Directional 0.78 170 256 256 1.51 100 lattice assembly imaging-14.04.11.121 276 Height -Bi-Directional 23.44 120 64 128 1.07 750 lattice assembly imaging-14.14.05.504 14 Height-ReTrace 0.75 70 400 400 5.71 300 lattice imaging-14.14.26.048 5 Height-ReTrace 1.17 70 256 256 3.66 300 lattice imaging-14.14.31.069 145 Height -Bi-Directional 2.34 70 256 256 3.66 300 lattice imaging-14.15.34.569 184 Height -Bi-Directional 3.91 70 256 256 3.66 500 lattice imaging-14.16.23.572 57 Height -Bi-Directional 3.91 50 256 256 5.12 500 lattice imaging-14.16.54.040 141 Height -Bi-Directional 7.81 50 128 256 5.12 500 lattice imaging-14.20.38.415 350 Height -Bi-Directional 11.72 40 128 256 6.40 750 lattice imaging-14.21.25.854 723 Height -Bi-Directional 31.25 30 64 128 4.27 1000 lattice imaging-14.23.39.213 201 Height -Bi-Directional 54.69 20 64 128 6.40 1750 lattice imaging-14.23.44.983 2437 Height -Bi-Directional 54.69 20 64 128 6.40 1750 lattice imaging-14.25.58.071 232 Height -Bi-Directional 1.17 85 256 256 3.01 150 lattice imaging-14.29.34.756 96 Height -Bi-Directional 0.59 200 512 512 2.56 150 lattice imaging-14.37.19.845 3 Height-ReTrace 0.38 70 400 400 5.71 150 lattice imaging-14.37.28.689 5 Height-ReTrace 1.00 70 400 400 5.71 400 lattice imaging-14.37.34.764 17 Height-ReTrace 0.50 70 400 400 5.71 200 lattice imaging-14.39.16.156 6 Height-ReTrace 1.56 60 256 256 4.27 400 lattice imaging-14.39.20.305 96 Height -Bi-Directional 3.13 60 256 256 4.27 400 lattice

   **Comment**: Have test parsers; now I need to check if the file properly reads the data, including array data, and verify the `encoding` used in that parser. (Downloaded)

---

12. **Force Volume Atomic Force Microscopy-Infrared for Simultaneous Nanoscale Chemical and Mechanical Spectromicroscopy**

   - **DOI**: 10.5281/zenodo.15326266
   - **URL**: [https://doi.org/10.5281/zenodo.15326266](https://doi.org/10.5281/zenodo.15326266)
   - **Date**: 2025-05-05
   - **Access**: open
   - **License**: CC BY-NC-ND 4.0
   - **By**: Wagner, Martin, Hu, Qichi, Hu, Shuiqing et al.
   - **Tags**: AFM-IR, photothermal, infrared nanospectroscopy, force volume, nanomechanical, contact resonance, Q-factor, damping, infrared spectroscopy, atomic force microscopy
   - **Desc**: The uploaded data is used in the following publication and its Supporting Information: Force Volume Atomic Force Microscopy-Infrared for Simultaneous Nanoscale Chemical and Mechanical Spectromicroscopy ACS Nano 2025 , 19 , 19 , 18791–18803 https://doi.org/10.1021/acsnano.5c04015 ABSTRACT OF THE PUBLICATION: Photothermal atomic force microscopy-infrared (AFM-IR) combines the nanoscale spatial resolution of AFM with the chemical identification capability of infrared spectroscopy and has thrived in various applications. Currently executed in three major AFM modes (contact, tapping and peak force tapping) we introduce a fourth variant built upon force volume mode comprising a defined engage, hold and retract segment in each pixel. IR laser pulsing at a probe resonance frequency during the constant-force hold segment duplicates the resonance enhanced AFM-IR detection principle of contact mode. However, force volume AFM-IR removes the lateral forces that cause tip wear and sample damage while adding the spatial resolution of tapping AFM-IR. As demonstrated on different materials this imaging and spectroscopy technique integrates monolayer sensitivity, sub-10 nm spatial chemical resolution, simultaneous nanomechanical property sensing and precise force control. The ability to sweep the infrared laser repetition rate in each pixel provides additional, rich information in the form of contact resonance curves, while compensating for mechanically induced probe resonance shifts in an alternative to conventional phase-locked loop based frequency tracking. Such sweeps inherently consider the Q-factor ( i.e. mechanical damping) in the AFM-IR response, a little investigated aspect. Furthermore, the probing depth can be varied by selecting different resonances recorded within a single broad frequency sweep. Switching to the surface sensitive AFM-IR detection scheme during the hold segment additionally limits the probing depth. These qualities should position force volume AFM-IR as a valuable addition to established AFM-IR modes. DESCRIPTION OF UPLOADED DATA: File names start with ‘Fig…’ followed by a short description and refer to the specific figure in the publication and its Supporting Information where the data is discussed. The following SI figures are based on the same data sets as other figures: Fig. S6: see spectra of Fig. 3 Fig. S7: same data as Fig. 4 Fig. S8: same data as Fig. 5 Fig. S10: same data as Fig. 5 Fig. S11: same data as Fig. 6. Data sets comprise atomic force microscopy (AFM) imaging files (*.spm, mostly containing force volume data), spectra (*.txt) or curves (*.txt) discussed in the publication. Txt-files contain ASCII data in tab delimited format. The atomic force microscopy (AFM) imaging files (*.spm) can be opened and processed in Bruker NanoScope Analysis V3.00R1sr7. Earlier Nanoscope Analysis versions as well as other AFM imaging software may be used as well but full compatibility is not guaranteed.

   **Comment**: Data sets comprise atomic force microscopy (AFM) imaging files (*.spm, mostly containing force volume data), spectra (*.txt) or curves (*.txt)

---

15. **Raw data for "AFM as a Multimetrological Platform" Manuscript**

   - **DOI**: 10.5281/zenodo.14271622
   - **URL**: [https://doi.org/10.5281/zenodo.14271622](https://doi.org/10.5281/zenodo.14271622)
   - **Date**: 2024-12-04
   - **Access**: open
   - **License**: CC BY 4.0
   - **By**: Aslan, Husnu, Kaja, Khaled, Piquemal, François et al.
   - **Desc**: Attached are the raw scanning probe microscopy data, collected with different instruments. Each instrument has its own data format and needs to be processed to represent the data properly. The processing often includes, false-colour scale assignment, tilt and rotational corrections, and levelling. After processing, the analysis helps extracting the necessary information from the data such as dimensional and electrical properties, which when calibrated can be presented as images, maps or spectroscopy graphs in respective units.

   **Comment**: According to the file extension (.spm) data may come from the Bruker instrument,  NW_GaAs_non-passive_C3275_dark_DOWN_00005.spm

---

16. **Heating by Dissipation of Energy from Absorbed Light: Molecular Mechanisms Underlying the Survival Strategy of Polar Algae**

   - **DOI**: 10.5281/zenodo.14245518
   - **URL**: [https://doi.org/10.5281/zenodo.14245518](https://doi.org/10.5281/zenodo.14245518)
   - **Date**: 2024-11-29
   - **Access**: open
   - **License**: CC BY 4.0
   - **By**: Zubik-Duda, Monika, Grudzinski, Wojciech, Luchowski, Rafal et al.
   - **Desc**: The original data, which served as the source material for the scientific article on the polar alga Pediastrum orientale, co llected from Reindeer Lake on Spitsbergen. Consists of datasets obtained using various techniques: fluorescence microscopy (microscope_fluo), fluorescence lifetime microscopy (FLIM), high-performance liquid chromatography (HPLC), atomic force microscopy (AFM), Raman microspectroscopy (RAMAN), fluorescence lifitime spectroscopy (lifetime) and fluorescence spectroscopy (Fluo). HPLC - Nexera LC-40 (Shimadzu, Japan) FLIM - OLYMPUS IX71 confocal microscope MicroTime 200 with SymPhoTime 64 software package (PicoQuant, GmbH, Germany) RAMAN - inVia Reflex confocal Raman microscope with the WiRE 5.5 software package (Renishaw, UK) AFM - JPK Nanowizard 3 system with JPKSMP data processing software (Bruker, USA) Lifetime - FluoTime 300 spectrometer with FluoFit Pro v 4.5.3.0 (PicoQuant, Germany) Microscope_Fluo - Zeiss LSM980 confocal microscope with Airy2 and Elyra7 detectors and ZEN 3.1 software (Zeiss, Germany) Fluo - OLYMPUS IX71 confocal microscope MicroTime 200 system with the spectrograph SR-163 and the Newton 970 EMCCD camera (Andor Technology)

   **Comment**: Dataset coming from bruker: JPK Nanowizard 3 system with JPKSMP data processing software (Bruker, USA)

---

21. **Revealing the microscopic mechanism of vortex pinning in superconductors**

   - **DOI**: 10.5061/dryad.1g1jwsv49
   - **URL**: [https://doi.org/10.5061/dryad.1g1jwsv49](https://doi.org/10.5061/dryad.1g1jwsv49)
   - **Date**: 2024-03-20
   - **Access**: open
   - **License**: CC0 1.0 (Public Domain)
   - **By**: Li, Dong, Zhang, Yuhang, Lu, Zouyouwei et al.
   - **Tags**: Scanning tunneling microscopy, transport measurement, Vortex pinning
   - **Desc**: Vortex pinning is a crucial factor that determines the critical current of practical superconductors and enables their diverse applications. However, the underlying mechanism of vortex pinning has long been elusive, lacking a clear microscopic explanation. Here, using high-resolution scanning tunneling microscopy, we studied single vortex pinning induced by a point defect in layered FeSe-based superconductors. We found the defect-vortex interaction drives low-energy vortex bound states away from E F , creating a “mini” gap that effectively lowers the system energy and enhances pinning. By measuring the local density of states, we directly obtained the elementary pinning energy and estimated the pinning force via the spatial gradient of pinning energy. The results are consistent with bulk critical current measurement. Furthermore, we show that a general microscopic quantum model incorporating defect-vortex interaction can naturally capture our observation. It suggests that the local pairing near the pinned vortex core is actually enhanced compared to an unpinned vortex, which is beyond the traditional understanding that non-superconducting regions pin vortices. Our study thus unveils a general microscopic mechanism of vortex pinning in superconductors, and provides insights for enhancing the critical current of practical superconductors.

   **Comment**: File formats are: The STM data are included in three types of files: SM4, 3ds, and sxm. It has well explanation.

---

23. **Scanning Tunneling Microscope Images of Atomic Scale Defects in Tungsten Diselenide**

   - **DOI**: 10.5281/zenodo.10443995
   - **URL**: [https://doi.org/10.5281/zenodo.10443995](https://doi.org/10.5281/zenodo.10443995)
   - **Date**: 2023-12-30
   - **Access**: open
   - **License**: CC BY 4.0
   - **By**: Smalley, Darian
   - **Desc**: This dataset contains scanning tunneling microscope (STM) data of single crystal tungsten diselenide (WSe2) provided by the Hone-Barmak Group acquired in constant current mode from two STM systems: a Low Temperature STM (LT-STM) and a room temperature STM (RT-STM). The images are of various sizes and resolutions. 136 of the STM images have associated labels of atomic-scale defects in the form of bouding boxes and image label masks. 38 annotated images were selected to construct an augmented training dataset of images and label masks saved as numpy files for convientent model training. Original, raw STM data of WSe2 is also inculded. Code on GitHub: <https://github.com/darianSmalley/ML-STM>

   **Comment**: Nanonis dataset

---

30. **Supplementary data to publication https://pubs.acs.org/doi/10.1021/acsnano.5c17283**

   - **DOI**: 10.5281/zenodo.19087372
   - **URL**: [https://doi.org/10.5281/zenodo.19087372](https://doi.org/10.5281/zenodo.19087372)
   - **Date**: 2026-03-18
   - **Access**: open
   - **License**: CC BY 4.0
   - **By**: Moresco, Francesca
   - **Desc**: Supplementary row STM data to the publication Subphthalocyanine Platform for Single-Molecule Machines on Surface: Ligand-Directed Adsorption on Au(111) by Franz Plate, Soyoung Park, Ebru Cihan, Natasha Khera, Ningwei Sun, Pranjit Das, Olga Guskova, Dmitry A. Ryndyk, Franziska Lissel, and Francesca Moresco DOI: 10.1021/acsnano.5c17283 The data can be read and analyzed by a standard SPM data visualization and analysis software like Gwyddion.

   **Comment**: Probably a nanonis dataset

---

31. **Supplementary data to publication https://doi.org/10.1002/anie.202424715**

   - **DOI**: 10.5281/zenodo.19086147
   - **URL**: [https://doi.org/10.5281/zenodo.19086147](https://doi.org/10.5281/zenodo.19086147)
   - **Date**: 2026-03-18
   - **Access**: open
   - **License**: CC BY 4.0
   - **By**: Moresco, Francesca
   - **Desc**: Supplementary row STM data to the publication N. Khera, N. Sun, S. Park, P. Das, K. H. Au-Yeung, S. Sarkar, F. Plate, R. Robles, N. Lorente, F. S.-C. Lissel, F. Moresco, N-Heterocyclic Carbene vs. Thiophene – Chiral Adsorption and Unidirectional Rotation on Au(111), Angew. Chem. Int. Ed. 64, e202424715 (2025). The data can be read and analyzed by a standard SPM data visualization and analysis software like Gwyddion.

   **Comment**: Bruker file format, might be interesting

---

32. **Data for: Measurements of the size and physical properties of marine particles using atomic force microscopy (part 2)**

   - **DOI**: 10.5281/zenodo.18847316
   - **URL**: [https://doi.org/10.5281/zenodo.18847316](https://doi.org/10.5281/zenodo.18847316)
   - **Date**: 2026-03-03
   - **Access**: open
   - **License**: CC BY 4.0
   - **By**: Yamada, Yosuke, Mochizuki, Toshiaki, Fukuda, Hideki et al.
   - **Desc**: This dataset contains raw atomic force microscopy (AFM) image data of marine particle samples used in the associated manuscript submitted to Geophysical Research Letters . The data are organized by measurement date using the folder naming convention YYMMDD_particle. Each subfolder corresponds to AFM measurements conducted on a specific date and contains original instrument files (.spm). Each file represents an individual AFM scan. This record is Part 2 of a multi-part dataset. The complete dataset is distributed across multiple Zenodo records due to file size considerations. All quantitative results of particle properties reported in the associated manuscript were derived from these raw AFM image files. Detailed file organization and additional information are provided in the accompanying README file.

   **Comment**: Bruker file format might be interesting

---

33. **Data for: Measurements of the size and physical properties of marine particles using atomic force microscopy (part 1)**

   - **DOI**: 10.5281/zenodo.18847016
   - **URL**: https://doi.org/10.5281/zenodo.18847016
   - **Date**: 2026-03-03
   - **Access**: open
   - **License**: CC BY 4.0
   - **By**: Yamada, Yosuke, Mochizuki, Toshiaki, Fukuda, Hideki et al.
   - **Desc**: This dataset contains raw atomic force microscopy (AFM) image data of marine particle samples used in the associated manuscript submitted to Geophysical Research Letters . The data are organized by measurement date using the folder naming convention YYMMDD_particle. Each subfolder corresponds to AFM measurements conducted on a specific date and contains original instrument files (.spm). Each file represents an individual AFM scan. This record is Part 1 of a multi-part dataset. The complete dataset is distributed across multiple Zenodo records due to file size considerations. All quantitative results of particle properties reported in the associated manuscript were derived from these raw AFM image files. Detailed file organization and additional information are provided in the accompanying README file.

   **Comment**: Bruker file format might be interesting

---

34. **Dataset for 'Living Fiber Dispersions from Mycelium as a New Sustainable Platform for Advanced Materials'**

   - **DOI**: 10.5281/zenodo.17831280
   - **URL**: [https://doi.org/10.5281/zenodo.17831280](https://doi.org/10.5281/zenodo.17831280)
   - **Date**: 2025-12-05
   - **Access**: open
   - **License**: CC BY 4.0
   - **By**: Nystrom, Gustav
   - **Desc**: Functional biopolymeric fibers are key building blocks for developing sustainable materials within the growing bioeconomy. However, their flexible use in emerging advanced materials with smart properties typically requires processing methods that may compromise sustainability. Here, a sustainable route to generate living fiber dispersions (LFD) from mycelium that combines the excellent material-forming properties of biopolymeric fibers, and the highly dynamic properties of living materials is proposed. This is showcased by using industrially available liquid culture and mechanical defibrillation methods to generate well-dispersed living mycelium fibers. These fibers can form materials where precursors with good dispersibility and network formation properties are paramount and can harness dynamic properties through growth even in the absence of added nutrients. This is demonstrated in unique living emulsions with 3.6x slower phase separation and in living films with 2.5x higher tensile strength upon growth, the latter vastly outperforming the strongest pure mycelium materials to date. Further, humidity can be used to modulate mechanical properties and to trigger the superhydrophobic patterning of substrates, mechanical actuation, and degradation of lignocellulosic consumer goods at their end of life. In the future, combining synthetic biology with this promising platform for smart materials can expand the horizons for sustainable material manufacturing.

   **Comment**: It has two bruker file with extension .spm

---

37. **Role of Chalcogen atoms in In-Situ Exfoliation of Large-Area 2D Semiconducting Transition Metal Dichalcogenides**

   - **DOI**: 10.5281/zenodo.14537302
   - **URL**: [https://doi.org/10.5281/zenodo.14537302](https://doi.org/10.5281/zenodo.14537302)
   - **Date**: 2024-12-20
   - **Access**: open
   - **License**: CC BY 4.0
   - **By**: Grubisic-Cabo, Antonija
   - **Tags**: 2D materials, Transition metal dichalcogenides, XPS, LEED, Exfoliation, KISS
   - **Desc**: Datasets for "Role of Chalcogen atoms in In Situ Exfoliation of Large-Area 2D Semiconducting Transition Metal Dichalcogenides" publication. Optical microscopy, atomic force microscopy (AFM), low-energy electron diffraction (LEED) and X-ray photoelectron spectrocopy measurements (XPS). Measurements were conducted at the Zernike Institute for Advanced Materials in Groningen, The Netherlands. All measurements were performed at room temperature. LEED measurements are obtained using electron energy of 125 eV, while XPS measurements were performed using photon energy of 1486.6 eV (Al anode). Experimental data are provided in jpeg format (optical microsopy images, LEED data), spm (AFM data) and txt (XPS data).

   **Comment**: One spm file with extension .spm

---

38. **Data related to "Inverse melting and re-entrant transformations of the vortex lattice in amorphous Re6Zr thin film"**

   - **DOI**: 10.5281/zenodo.14780459
   - **URL**: [https://doi.org/10.5281/zenodo.14780459](https://doi.org/10.5281/zenodo.14780459)
   - **Date**: 2025-01-31
   - **Access**: open
   - **License**: CC BY 4.0
   - **By**: Duhan, Rishabh, Sengupta, Subhamita, Jesudasan, John et al.
   - **Desc**: This work reports the Inverse Melting of the vortex lattice in a 20 nm thick superconducting Re6Zr thin film, through direct imaging of the vortex lattice using low-temperature scanning tunneling spectroscopy and complementary transport measurements. The central result is that in a superconducting thin film with moderate vortex pinning, vortices form an inhomogeneous liquid at low temperatures and magnetic field and gradually transform to a nearly perfect crystalline solid as the magnetic field or temperature is increased, before melting into a liquid again at higher magnetic fields or temperature. This is qualitatively summarised in " raw_image_addition.png ". Here, in each panel, we have added a sequence of 20 successive conductance maps acquired in the same area. In each conductance map the more probable locations for vortices appear as local conductance minima. When the vortices are moving, these minima appear at different locations in each image and the contrast becomes poor in the added image. At 460 mK, we observe a gradual evolution from an inhomogeneous vortex liquid to a vortex solid from 3 kOe to 20 kOe, and a gradual melting of this vortex solid again at higher fields. Similarly, at 3 kOe the inhomogeneous vortex liquid gradually crystallises between 460 mK to 3 K and then melts again at 4K. raw_image_addition.png is created by adding the intensities of 20 conductance maps acquired in the same area. A constant background conductance has been subtracted from each image. All images are plotted with the same relative conductance scale. The STS raw data used in creating " raw_image_addition.png " and in Figures 1, 2, and 3 of the paper are given in *.sxm format. The files numbered 001 to 020 in each subfolder denote the sequence of conductance maps acquired successively over the same area at a given magnetic field and temperature. The data in subfolder "Fig 1 and 2" are at 460 mK. The transport data (processed and unprocessed) are given as *.opju file and classified into subfolders named as per the corresponding figures in the paper.

   **Comment**: Nanonis files

---

42. **Atomic Force Microscopy image of coagulation factor Va in liquid**

   - **DOI**: 10.5281/zenodo.11234725
   - **URL**: [https://doi.org/10.5281/zenodo.11234725](https://doi.org/10.5281/zenodo.11234725)
   - **Date**: 2014-09-04
   - **Access**: open
   - **License**: CC BY 4.0
   - **By**: Pellequer
   - **Desc**: Original raw and corrected AFM images of isolated coagulation factor Va (FVa). The image was acquired in liquid with an OTR8 cantilever using the peak force tapping mode of a multimode V microscope. The image size is 1 x 1 µm² with 1024 x 1024 pixels². The corrected image was obtained using Gwyddion (.gwy file) from the raw image file (.spm). This image was the experimental data used to assemble the A trimer and the two C domains of FVa using the AFMAssembly pipeline described in Chaves et al. (2014): http://dx.doi.org/10.1160/TH14-06-0481. The paper can be downloaded from the HAL repository (https://hal.archives-ouvertes.fr/hal-01146300v1).

   **Comment**: Single spm file with extension .spm

---

47. **Mechanical characterisation of the developing cell wall layers of tension wood fibres by Atomic Force Microscopy**

   - **DOI**: 10.5281/zenodo.6487575
   - **URL**: [https://doi.org/10.5281/zenodo.6487575](https://doi.org/10.5281/zenodo.6487575)
   - **Date**: 2022-01-26
   - **Access**: open
   - **License**: CC BY 4.0
   - **By**: Arnould, Olivier, Capron, Marie, Ramonda, Michel et al.
   - **Tags**: Atomic Force Microscopy, Cell wall, G-layer, Indentation modulus, Maturation, Poplar, Stiffening, Tension wood
   - **Desc**: This dataset corresponds to the Arnould et al. (2022) paper (available at https://www.biorxiv.org/content/10.1101/2021.09.23.461481v1.full) on the mechanical characterization of developing cell wall layers of tension wood fibers by Atomic Force Microscopy. It contains all raw AFM files (Bruker format .spm, readable by the free software Gwyddion for example) corresponding to mechanical measurements of poplar reaction wood cells (clone 717-1B4) along 3 radial lines/rows, starting from the cambium. Each cell is identified by its "macroscopic" distance from the cambium (value in µm in the name of each file corresponding to the displacement of the sample in the AFM) which was corrected after using the AFM optical image captures. Some files, with a -z extension after the distance value, correspond to a zoom into the cell wall. The data also contain measurements made for mechanical calibration on epoxy embedded Kevlar fibers, controlled measurements in the embedding resin between each radial line and measurements in normal wood cells. Two csv files containing final data extracted from AFM measurements that give the value of the indentation modulus and the relative thickness to cell diameter ratio (by AFM and by phase contrast optical microscopy) in each cell wall layer as a function of cambium distance are also provided.

   **Comment**: Bruker files with extension .spm

---

48. **Dataset for 'Layer-dependent oxidation spreading in multilayer graphene during AFM local anodic oxidation'**

   - **DOI**: 10.5281/zenodo.19707666
   - **URL**: [https://doi.org/10.5281/zenodo.19707666](https://doi.org/10.5281/zenodo.19707666)
   - **Date**: 2026-04-23
   - **Access**: open
   - **License**: CC BY 4.0
   - **By**: Vymazal, Jan, Konečný, Martin, Piastek, Jakub et al.
   - **Desc**: Individual files used for Figures 2-12 are assembled in the folders. The COMSOL Multiphysics files are provided in the folder "COMSOL Simulations".

   **Comment**: Bruker files with extension .spm

---

53. **Data underlying the paper "Direct signatures of d-level hybridization and dimerization in magnetic adatom chains on a superconductor"**

   - **DOI**: 10.5281/zenodo.17533355
   - **URL**: [https://doi.org/10.5281/zenodo.17533355](https://doi.org/10.5281/zenodo.17533355)
   - **Date**: 2025-11-05
   - **Access**: open
   - **License**: CC BY 4.0
   - **By**: Rütten, Lisa M., Liebhaber, Eva, Reecht, Gaël et al.
   - **Tags**: Superconductivity, Scanning tunneling microscopy, magnetic chain
   - **Desc**: Here, we provide all original data used in the manuscript "Direct signatures of d-level hybridization and dimerization in magnetic adatom chains on a superconductor"

   **Comment**: Nanonis file format

---

54. **STM image of quasiparticle interferences on twisted graphene bilayers**

   - **DOI**: 10.5281/zenodo.17360113
   - **URL**: [https://doi.org/10.5281/zenodo.17360113](https://doi.org/10.5281/zenodo.17360113)
   - **Date**: 2025-10-15
   - **Access**: open
   - **License**: CC BY 4.0
   - **By**: Renard, Vincent
   - **Desc**: The dataset contains the STM measurements of quasiparticle interferences near a defect. Each image contains three channels : topography, dI/dV and current (bothforward and backward). Each image contains metadata indicating the measurement conditions

   **Comment**: Nanonis file format

---

55. **Revealing band-hybrid Cooper pairs on the surface of a superconductor with spin-orbit coupling**

   - **DOI**: 10.5281/zenodo.17202182
   - **URL**: [https://doi.org/10.5281/zenodo.17202182](https://doi.org/10.5281/zenodo.17202182)
   - **Date**: 2025-09-25
   - **Access**: open
   - **License**: CC BY 4.0
   - **By**: Pascual, Jose Ignacio
   - **Desc**: OPEN DATASET of the publication "Revealing band-hybrid Cooper pairs on the surface of a superconductor with spin-orbit coupling" including Scanning Tunneling Microscopy and Spectroscopy results.

   **Comment**: Nanonis file format

---

65. **Dataset for "An Alternative Chlorine-Assisted Optimization of CdS/Sb2Se3 Solar Cells: Towards Understanding of Chlorine Incorporation Mechanism"**

   - **DOI**: 10.5281/zenodo.14196316
   - **URL**: [https://doi.org/10.5281/zenodo.14196316](https://doi.org/10.5281/zenodo.14196316)
   - **Date**: 2024-11-21
   - **Access**: open
   - **License**: CC BY 4.0
   - **By**: Kuliček, Jaroslav, Bouzek, Karel, Paušová, Šárka
   - **Tags**: VZ3, CVUT, 214 021, 214 023, Kelvin probe, CdS/Sb2Se3, solar cells, SEM
   - **Desc**: The current strategies in the development of Sb2Se3 thin film solar cells involve fabrication and optimization of superstrate and substrate device architectures, with the preferable choice for TiO2 and CdS heterojunction layers. For CdS-based superstrate cells, several studies reported the necessity to apply CdCl2 or other metal halide-based post-deposition treatment (PDT), highlighting improvement of CdS/Sb2Se3 device efficiency. However, the need, effect, and mechanism of such PDT are very often not described. Additionally, the fact that many groups have not succeeded in demonstrating its benefits suggests that this strategy is not straightforward, requiring a deeper understanding towards a more unified concept. The present study proposes an alternative approach to the challenging CdCl2 PDT of CdS in CdS/Sb2Se3 device, involving controllable Cl incorporation in CdS films by systematically varying the concentration of NH4Cl in the CBD precursor solution from 1 to 8 mM. Structural and electrical characterizations are correlated with advanced measurements of Scanning Kelvin Probe, surface photovoltage, and atomic force microscopy to understand the impact of Cl incorporation on the properties of CdS films and CdS/Sb2Se3 devices. The validity of Cl incorporation in the CdS lattice and interdiffusion processes at the CdS-Sb2Se3 interface is confirmed by secondary ion mass spectrometry analysis. It is demonstrated that incorporation of 1 mM of NH4Cl, as a Cl source in CBD CdS, can boost the PCE of CdS/Sb2Se3 by ~20 %. With this approach, we offer new perspectives on the optimization methodology for Cl-based CdS/Sb2Se3 device processing and complementary understanding of the physiochemistry behind these processes.

   **Comment**: It has some .dat and .txt files

---

66. **Nucleation-Limited Kinetics of GaAs Nanostructures Grown by Selective Area Epitaxy: Implications for Shape Engineering in Optoelectronics Devices**

   - **DOI**: 10.5281/zenodo.13595509
   - **URL**: [https://doi.org/10.5281/zenodo.13595509](https://doi.org/10.5281/zenodo.13595509)
   - **Date**: 2024-08-12
   - **Access**: open
   - **License**: CC BY 4.0
   - **By**: Zendrini, Michele, Piazza, Valerio, Fontcuberta i Morral, Anna et al.
   - **Tags**: SAE, MOVPE, GaAs, Nanowires, Growth kinetics
   - **Desc**: This dataset corresponds to the following manuscript: Zendrini, M., Dubrovskii, V., Rudra, A., Dede, D., Fontcuberta i Morral, A., Piazza, V. “Nucleation-Limited Kinetics of GaAs Nanostructures Grown by Selective Area Epitaxy: Implications for Shape Engineering in Optoelectronics Devices” ACS Applied Nano Materials 7,16 (2024): 19065–19074 DOI: doi.org/10.1021/acsanm.4c02765 The dataset contains raw SEM images in .tif format for all the arrays of nanowires and nanomembranes discussed in the paper. The dataset also contains the AFM scans in .xyz format for all the arrays of nanowires and nanomembranes. The data for the morphological analysis are extracted from the SEM images and the AFM scans and they are collected in two separate .txt files for NWs and NMs.

   **Comment**: .spm dataset from bruker.

---

## Datasets with Unknown or Unsupported File Formats

*Scientifically relevant SPM datasets whose file formats are currently not supported by the parser (e.g., `.jpk`, `.par`, `.mtrx`, `.h5`, `.flt`) or require further investigation.*

4. **PiF-IR data of PMIS-C8 monolayer films on nanostructured and planar Au substrates, complementary AFM, FTIR/ATR and BAM data and calculated PMIS-C8 spectra**

   - **DOI**: 10.5281/zenodo.18060234
   - **URL**: [https://doi.org/10.5281/zenodo.18060234](https://doi.org/10.5281/zenodo.18060234)
   - **Date**: 2025-12-26
   - **Access**: open
   - **License**: CC BY 4.0
   - **By**: James, Ayona, Ali, Maryam, Ye, Zekai et al.
   - **Tags**: mid-IR photo-induced force microscopy, photothermal imaging, infrared spectroscopy, Langmuir-Blodgett films, monolayer
   - **Desc**: Raw data sets for Manuscript: Title: Effect of hybrid field coupling in nanostructured surfaces on anisotropic signal detection in nanoscale infrared spectroscopic imaging methods Autors: Ayona James,a,b Maryam Ali,a,b Zekai Ye,b Phan Thi Yen Nhi,a,b Sharon Xavi,a Mashiat Huq,a Sajib Barua,a,b Meng Luo,a Yisak Tsegazab,a,b Anna Elmanova,a,b Robin Schneider,b Olga Ustimenko,c Sarmiza-Elena Stanca,b Marco Diegel,b Andrea Dellith,b Uwe Hübner,b Christoph Krafft,a,b Jasmin Finkelmeyer,b Maximilian Hupfer,a,b Kalina Peneva,c,d,e Matthias Zeisberger,b Christin David,f,g Martin Presselt,a,b and Daniela Täuber*a,b a Institute of Physical Chemistry (IPC), Friedrich Schiller University Jena, 07743 Jena, Germany. b Leibniz Institute of Photonic Technology (LIPHT), 07745 Jena, Germany. c Institute of Organic and Macromolecular Chemistry (IOMC), Friedrich Schiller University Jena, 07743 Jena, Germany. d Jena Center of Soft Matter (JCSM), Friedrich Schiller University Jena, 07743 Jena, Germany. e Center for Energy and Environmental Chemistry Jena (CEEC Jena), Friedrich Schiller University Jena, 07743 Jena, Germany. f Institute of Condensed Matter Theory and Solid State Optics (IFTO), Friedrich Schiller University Jena, 07743 Jena, Germany. g University of Applied Sciences Landshut, 84036 Landshut, Germany. Content: Mid-infrared photo-induced force microscopy (PiF-IR) of oriented monolayer perylene (PMIS-C8) films on planar and nanostructured Au substrates (single point spectra, single frequency images, hyperspectral imaging); Atomic force microscopy (AFM) images of monolyer perylene films and plain Au substrates; Brewster Angle Microscopy (BAM) images acquired during Langmuir-Blodgett film deposition of the alkylated perylene derviate (PMIS-C8) on water; complementary infrared spectra of PMIS-C8 (FTIR & ATR) and calculated polarization-resolved IR spectra of PMIS-C8 together with interactive 3D visualizations allowing inspection of static atomic displacement vectors and dynamic animations of vibrational motions. PiF-IR spectra & single frequency scans (Figures 1a,b, S4): PMIS-C8 on evaporated Au, pos1: 251120_PMIS-C8_0001_spectra.zip (Figures 1a, S4a) PMIS-C8 on planar Au, pos2: 250619_PMIS-C8_0001_spectra.zip (Figures 1b, S4b, S5a-c) PMIS-C8 on planar Au, pos1: 250618_PMIS-C8_0001_spectra.zip (Figure S4c) PMIS-C8 on evaporated Au, pos2 including PDMS: 251121_PMIS-C8_0001_spectra.zip (Figure S4d) FTIR & ATR spectra (ATR-FTR.zip, Figure 1c): FTIR on Bruker microscope: BRUKER_FTIR_pmisc8.dpt FTIR on Agilent microscope: ftir_pmisc8.csv - ftir_WaterVapor.csv = ftir_pmisc8-WaterVapor.csv ATR: atr_WaterVapor.csv, atr_pmisc8-WaterVapor.csv, and corrected spectrum: atr_pmisc8-WaterVapor_ATcorr.csv Calculated spectra (Calculated_PMIS-C8_Spectra.zip, Figures 1d-f): Mode frequencies & intensities including x,y,z-components: ir_summary_all_modes.txt Line broadened spectra including x,y,z-components: spectra_fwhm_10.txt Interactive list of calculated modes, frequencies and total intensities: index.html Interactive molecular structure: interactive_molecule_export.html Interactive stick spectrum: interactive_spectrum.html 2 folders with associated files for animations and data sets BAM (BAM_Deposition_PMISC8.zip, Figure S1): Deposition of PMIS-C8 solution on water surface AFM (AFM.zip, Figures S2, S3): AFM_plain_evaporated-Au (Figure S2a) AFM_plain_planar-Au (Figure S2b) AFM_PMISC8_planar-Au (Figures S3a,b) AFM_PMISC8_evaporated-Au (Figures S3c,d) PIF-IR hyperspectral and single frequency scans (Figures 2-4, S4-6): PiF-IR hyperspectrum PMIS-C8 on evaporated Au: PiF-IR_PMISC8_evaporated-Au_hypir.zip (Figure 2) PiF-IR single frequency scan on evaporated Au, position of hyperspectrum: 251120_PMIS-C8_0002_scan.zip (Figure 2) 3 subsequent PiF-IR single frequency scans on evaporated Au: 251121_PMIS-C8_0002-4_scans.zip (Figure 4) PiF-IR hyperspectrum PMIS-C8 on planar Au: 250618_PMIS-C8_0004_hypir.zip (Figures 3, S5g-i) 2 subsequent PiF-IR single frequency scans on planar Au: 250618_PMIS-C8_0002-3_scans.zip (Figure 3, S5d-f, S6a) 2 subsequent PiF-IR single frequency scans on planar Au, pos 2: 250619_PMIS-C8_0002-3_scans.zip (Figure S6b)

   **Comment**: Unknow file format for AFM experiment, e.g., PMIS2-C8_ML2_p2_5__040925144712.SIG_HEIGHT_SENSOR_BKW.FLT

---

5. **Data set for the manuscript "Local Networks of Electrical Conductance in Hybrid Gold Nanoparticle-Polymer Films"**

   - **DOI**: 10.5281/zenodo.17350453
   - **URL**: [https://doi.org/10.5281/zenodo.17350453](https://doi.org/10.5281/zenodo.17350453)
   - **Date**: 2025-10-14
   - **Access**: open
   - **License**: CC BY 4.0
   - **By**: Das, Sukanya, Bennewitz, Roland, Kraus, Tobias et al.
   - **Desc**: Atomic Force Microscopy (AFM) original data files for the figures in the paper indicated. All data is in the format of the manufacturer of the instrument NanoWizard3 (Bruker). Data can be edited for example by the open source software Gwyddion.

   **Comment**: Datafile of type jpk. cafm_-1.2V_setpoint0.26V small area.jpk

---

8. **Dataset for  Blue Laser for Production of Carbon Dots**

   - **DOI**: 10.5281/zenodo.17423992
   - **URL**: [https://doi.org/10.5281/zenodo.17423992](https://doi.org/10.5281/zenodo.17423992)
   - **Date**: 2024-10-03
   - **Access**: open
   - **License**: CC BY 4.0
   - **By**: Cutroneo, Mariapompea
   - **Desc**: The PCL + CDs composites were studied using attenuated total reflectance coupled with Fourier transform infrared spectroscopy (ATR-FTIR) and were monitored using a JASCO Model 4600 spectrophotometer working in the (400–4000) cm −1 wavenumber range. The luminescence of the produced CDs was observed using the Avantes AvaSpec-2048-USB2 optical spectrometer. The luminescence was monitored in the transmission mode in the region 200–800 nm. The exciting UV light source operating at 365 nm and at a fluence of about 100 mJ/cm 2 illuminated the front of the cuvette containing the CD suspension at a 10 cm distance and at 0°, while the fiber connected to the spectrometer was located on the back of the cuvette at a 1 mm distance and at 180°. The silicon cuts 1 cm × 1 cm in size were covered with drops of CD suspension and dried in air overnight. The formed films were studied by AFM. A dimension ICON AFM system (Bruker Corp., Bremen, Germany) operating in the ScanAsyst imaging mode in air has been employed. A commercial silicon Tip and SCANASYST, in air mode, with a spring constant of 0.4 N/m, supported 3 μm 2 scanning. The identification of the CDs was carried out using AFM images recorded and processed using NanoScope Analysis 1.80 with 32-bit software.

   **Comment**: Unknown datastructure from a dimension ICON AFM system (Bruker Corp., Bremen, Germany)

---

17. **Dataset of Scanning Tunneling Microscopy (STM) images of graphene on nickel**

   - **DOI**: 10.5281/zenodo.7664070
   - **URL**: [https://doi.org/10.5281/zenodo.7664070](https://doi.org/10.5281/zenodo.7664070)
   - **Date**: 2021-12-24
   - **Access**: open
   - **License**: CC BY 4.0
   - **By**: Tommaso Rodani, Elda Osmenaj, Alberto Cazzaniga et al.
   - **Tags**: graphene, nickel, scanning tunneling microscopy, surface, chemical, vapour, deposition, doping
   - **Desc**: STM images presented in the dataset were recorded by the STRAS research group using a Omicron Variable Temperature STM (VT-STM) microscope, in the TASC laboratory of the CNR-IOM in Trieste.

   **Comment**: Unknow file format: 43586.par

---

18. **Dataset supplementing journal article "Design of an FPGA-Based Controller for Fast Scanning Probe Microscopy" in Sensors 2024**

   - **DOI**: 10.5281/zenodo.13744336
   - **URL**: [https://doi.org/10.5281/zenodo.13744336](https://doi.org/10.5281/zenodo.13744336)
   - **Date**: 2024-09-11
   - **Access**: open
   - **License**: CC BY 4.0
   - **By**: Gregorat, Leonardo, Cautero, Marco, Carrato, Sergio et al.
   - **Desc**: Dataset supplementing journal article "Design of an FPGA-Based Controller for Fast Scanning Probe Microscopy" in Sensors 2024. Fast imaging measurements showed in Figure 9 of the article: 9a: Fast STM of a static Pt5 cluster on a Fe3O4(001) magnetite surface, taken at room temperature in a UHV chamber with an Omicron VT-AFM microscope at 4 frames/s; pixel resolution 100x100 pixels; image size 8x8 nm2. 9b: Fast STM of a Pd-octaethylporphyrin monolayer on a Au(111) surface under electrolyte (phosphate buffer, pH= 7, Ar-saturated), taken with a Beetle-type EC-STM at 12 frames/s (EWE = +0.65 vs RHE, Ub = +0.4 V vs WE); pixel resolution 120x120 pixels; image size 8x8 nm2. 9c: Fast AFM images of a Mikromasch TGX1 test grating with a 3 μm pitch and a 130 nm height, taken in contact mode with an Asylum Research/Oxford Instruments MFP-3D microscope (Mikromasch NSC36 probe - 0.6 N/m cantilever) at 4 frames/s; pixel resolution 100x100 pixels.

   **Comment**: Omicron machine (Omicron VT-AFM microscope): Unknow data structure  FS_231026_009.h56.7 MB, FS_231026_009.h5_meta.

---

20. **Dataset of Scanning Tunneling Microscopy (STM) images of model surfaces for elementary steps in catalytic reactions**

   - **DOI**: 10.5281/zenodo.10886977
   - **URL**: [https://doi.org/10.5281/zenodo.10886977](https://doi.org/10.5281/zenodo.10886977)
   - **Date**: 2024-03-27
   - **Access**: open
   - **License**: CC BY 4.0
   - **By**: Rodani, Tommaso, Mirco Panighel, Cristina Africh et al.
   - **Tags**: scanning tunneling microscopy, surface, catalytic reactions
   - **Desc**: STM images presented in the dataset were recorded by the STRAS research group using a Omicron Variable Temperature STM (VT-STM) microscope, in the TASC laboratory of the CNR-IOM in Trieste. This work has been done within the NFFA-DI project funded by the European Union – NextGenerationEU - Missione 4, “Istruzione e Ricerca” – Componente 2, “Dalla ricerca all'impresa” – Linea di investimento 3.1,“Fondo per la realizzazione di un sistema integrato di infrastrutture di ricerca e innovazione” – Azione 3.1.1, “Creazione di nuove IR o potenziamento di quelle esistenti che concorrono agli obiettivi di Eccellenza Scientifica di Horizon Europe e costituzione di reti”.

   **Comment**: Unknow file format, __[__104365.tf__](http://104365.tf)__, 104399.par from Omicron Variable Temperature STM (VT-STM) microscope

---

22. **Data for: Hidden non-collinear spin-order induced topological surface states**

   - **DOI**: 10.5061/dryad.280gb5mv3
   - **URL**: [https://doi.org/10.5061/dryad.280gb5mv3](https://doi.org/10.5061/dryad.280gb5mv3)
   - **Date**: 2024-03-15
   - **Access**: open
   - **License**: CC0 1.0 (Public Domain)
   - **By**: Huang, Zengle, Yi, Hemian, Kaplan, Daniel et al.
   - **Tags**: Scanning tunneling microscopy
   - **Desc**: Rare-earth monopnictides are a family of materials simultaneously displaying complex magnetism, strong electronic correlation, and topological band structure. The recently discovered emergent arc-like surface states in these materials have been attributed to the multi-wave-vector antiferromagnetic order, yet the direct experimental evidence has been elusive. Here we report the observation of non-collinear antiferromagnetic order with multiple modulations using spin-polarized scanning tunneling microscopy. Moreover, we discover a hidden spin-rotation transition of single-to-multiple modulations 2 K below the Neel temperature. The hidden transition coincides with the onset of the surface state splitting observed by our angle-resolved photoemission spectroscopy measurements. Single modulation gives rise to a band inversion with induced topological surface states in a local momentum region while the full Brillouin zone carries trivial topological indices, and multiple modulation further splits the surface bands via non-collinear spin tilting, as revealed by our calculations. The direct evidence of the non-collinear spin order in NdSb not only clarifies the mechanism of the emergent topological surface states but also opens up a new paradigm of control and manipulation of band topology with magnetism.

   **Comment**: Uknow file: NbSb-spinpolarized-4K-20220826_0001.mtrx

---

35. **Visualizing Nanoscale Charge-Flow in Multi-Dimensional WSe2/GaAs vertical diodes**

   - **DOI**: 10.5281/zenodo.17121837
   - **URL**: [https://doi.org/10.5281/zenodo.17121837](https://doi.org/10.5281/zenodo.17121837)
   - **Date**: 2025
   - **Access**: open
   - **License**: Unknown
   - **By**: Zendrini, Michele, Piazza, Valerio
   - **Tags**: Electron beam induced current, WSe2, GaAs nanostructures
   - **Desc**: This dataset corresponds to the following manuscript: Zendrini, M., Blags, C., Wodzislawski, K. A., Rudra, A., Banerjee, M., Fontcuberta i Morral, A., Piazza, V. “Nanoscale electrical mapping of multi-dimensional WSe2/GaAs vertical diodes” Submitted (2025) DOI: The dataset contains raw EBIC images in .tif format for all the integrations of WSe2 flakes on top of planar and nanostructured (NMs and NXs) substrates discussed in the paper. The dataset also contains the AFM scans in .spm format for all the integrations. The data for the electrical analysis are extracted from the EBIC images as discussed in the main manuscript and supporting information. The data for morphological characterization are extracted from the AFM scans.

   **Comment**: Uknow file format: EBIC_Plan_nDoped_Zoom1_Vb0V.tif

---

43. **Accommodating a Hexagonal Zeta-phase Mn2N Film on a Cubic MgO (001) Substrate**

   - **DOI**: 10.5281/zenodo.11043571
   - **URL**: [https://doi.org/10.5281/zenodo.11043571](https://doi.org/10.5281/zenodo.11043571)
   - **Date**: 2024-04-22
   - **Access**: open
   - **License**: CC BY 4.0
   - **By**: Shrestha, Ashok
   - **Desc**: The figures associated with this paper can be derived from the following raw data set: Figure 2.opju: This file contains the numerical data that can be used to generate line profiles shown in the Figure 2. It consist of two set of data for Figure 2(a) and Figure2(b). The data set are clearly labelled. This fie can be opened using Origin software. Figure 3.opju: This file contains three set of raw data for Fig.3(a), Fig.3(b), and Fig.3(c) used in the mauscript. Those data set can be opened using Origin software. Figure 5.opju: The raw data for XRD and AES are given in this file. This file contains two sheets and are labellled properly. This also can be opend using Origin software. Figure 6(a).SM4/ Figure 6(c).SM4/Figure 6(d).SM4/: The raw data for STM images shown in Fig. 6 are given in the .SM4 format. It can be opened in WSxM software or other SPM mage processing software. These files are not drift and scale corrected. To do the drift correction in the image we used corel draw sotware and scanner calibration factors were applied for scale correction. Figure 7.xlsx: The numerical data for surface formation enery plot given in Fig. 7 is given in this file. It can be opened in Excel/Origin software. Figure 8(b).cube/ Figure 8(d).cube: The raw file for the simulated STm images are given in these files. These files can be opened in Vesta software.

---

46. **Dataset supplementing the journal article describing the pyfastspm Python package**

   - **DOI**: 10.5281/zenodo.7371527
   - **URL**: https://doi.org/10.5281/zenodo.7371527
   - **Date**: 2022-11-28
   - **Access**: open
   - **License**: CC BY 4.0
   - **By**: Karl Briegel, Felix Riccius, Jakob Filser et al.
   - **Desc**: This dataset represents a fast scanning tunneling microscopy image sequence, acquired with the FAST SPM module, showing a reduced Fe3O4(001) surface observed at 657 K during oxygen exposure. This is used as example dataset in the journal article describing the pyfastspm Python package (SoftwareX 21 (2023) 101269, Figure 3 and 4, Supporting Information).

---

49. **Data files for "Antiferromagnetism and Kekulé valence bond order in the honeycomb optical Su-Schrieffer-Heeger-Hubbard model"**

   - **DOI**: 10.5281/zenodo.18803936
   - **URL**: [https://doi.org/10.5281/zenodo.18803936](https://doi.org/10.5281/zenodo.18803936)
   - **Date**: 2026-02-27
   - **Access**: open
   - **License**: CC BY 4.0
   - **By**: Malkaruge Costa, Sohan, Cohen-Stead, Benjamin, Johnston, Steven
   - **Desc**: Data files for "Antiferromagnetism and Kekul{\'e} valence bond order in the honeycomb optical Su-Schrieffer-Heeger-Hubbard model." Authors: S. Malkaruge Costa , B. Cohen-Stead, and S. Johnston Paper abstract: The precise role of electron-phonon (e-ph) coupling in graphene and related materials on a honeycomb lattice is not yet fully understood, despite extensive research on these systems. Here, we perform sign-problem-free determinant quantum Monte Carlo simulations of the optical Su-Schrieffer-Heeger (oSSH)-Hubbard model on the honeycomb lattice, focusing on the parameters relevant to graphene. Performing finite-size scaling analyzes, we obtain the model’s ground state phase diagram, which includes the semi-metal (SM), Kekulé Valence Bond Solid (KVBS), and antiferromagnetic (AFM) phases, as well as indications of a small KVBS/AFM coexistence region. We find that a weak to moderate Hubbard repulsion, tuned toward the SM–AFM critical value in the pure honeycomb Hubbard model, enhances KVBS correlations and can even stabilize the KVBS phase. Estimating the effective parameters for graphene places it in the SM region of the phase diagram, but near the SM-KVBS phase boundary. Notably, we predict that increasing either the on-site Hubbard repulsion or the e-ph coupling strength drives graphene toward the KVBS phase rather than the AFM phase, highlighting a synergistic effect that can be exploited to further control the remarkable properties of graphene and related materials. DOI: https://doi.org/10.1103/8p79-4r7x Preprint: https://arxiv.org/abs/2511.21440

   **Comment**: Uknow file format

---

51. **Impact of structural heterogeneities in hierarchically grown microribbons on 2D WS2 monolayer on the measured local hydrogen evolution activity on Au substrate**

   - **DOI**: 10.5281/zenodo.17733854
   - **URL**: [https://doi.org/10.5281/zenodo.17733854](https://doi.org/10.5281/zenodo.17733854)
   - **Date**: 2025-11-27
   - **Access**: open
   - **License**: CC BY 4.0
   - **By**: Adofo, Laud Anim, Mendoza, Alejandro Esteban Perez, Joo, Miran et al.
   - **Tags**: 2D material, transition metal dichalcogenides, microribbons, hydrogen evolution reaction, scanning electrochemical cell microscopy
   - **Desc**: This dataset contains all raw data supporting the study investigating the local electrocatalytic activity of two-dimensional WS₂ monolayers and microribbons toward the hydrogen evolution reaction (HER) and the influence of structural and electronic heterogeneity on the measured electrochemical current. CVD-grown WS₂ flakes comprising monolayer regions and microribbon features were locally characterized using scanning electrochemical cell microscopy (SECCM). The spatially resolved electrochemical measurements were correlated with Raman spectroscopy, photoluminescence (PL) mapping, atomic force microscopy (AFM), and Kelvin probe force microscopy (KPFM) to establish direct structure–property–activity relationships. Differences in HER activity were observed between monolayer domains and microribbon regions, revealing pronounced spatial heterogeneity across the WS₂ surface. All raw and processed SECCM, Raman, PL, AFM, KPFM, and SEM data, together with associated metadata and custom MATLAB post-processing scripts, are included to enable full reproducibility of the analysis and to facilitate further quantitative investigation of local electrocatalytic behavior in 2D WS₂ systems.

   **Comment**: Unknow file format

---

57. **Raw data for article "Electronic transport experiments through free-standing graphene nanoribbons performed with atomic-scale control"**

   - **DOI**: 10.5281/zenodo.15148049
   - **URL**: [https://doi.org/10.5281/zenodo.15148049](https://doi.org/10.5281/zenodo.15148049)
   - **Date**: 2025-04-04
   - **Access**: open
   - **License**: CC BY 4.0
   - **By**: Friedrich, Niklas
   - **Desc**: Vertspec data recorded during formation of a GNR transport junction with an STM. STM image of a GNR used in a STM transport experiment and corresponding tip trajectory. Differential conductance data with GNR suspended between tip and substrate of an STM.

   **Comment**: Unknown file format

---

59. **Stabilizing Light-Responsive Azobenzene Films in Aqueous Environment with Thin Polymer Coatings**

   - **DOI**: 10.5281/zenodo.15995751
   - **URL**: [https://doi.org/10.5281/zenodo.15995751](https://doi.org/10.5281/zenodo.15995751)
   - **Date**: 2025-07-17
   - **Access**: open
   - **License**: CC BY 4.0
   - **By**: Isomäki, Mari, Kääriäinen, Lotta, Fedele, Chiara et al.
   - **Tags**: Azobenzene, parylene C, PDMS, surface relief grating, coating, thin film, cell culture substrate
   - **Desc**: This is the dataset containing raw data for a research article “Stabilizing Light-Responsive Azobenzene Films in Aqueous Environment with Thin Polymer Coatings”, submitted to “Soft Matter” journal. All the results presented in the article are based on the data included in this dataset. The data includes material characterization with atomic force microscopy (AFM), digital holographic microscope (DHM), profilometry, UV-Vis spectrophotometry, different optical microscopes (polarized optical microscope, light microscope, confocal microscope) and diffraction efficiency (DE) measurements. Both raw data and analyzed data are included in the datasets. All datasets include README.txt file, which provide additional info about the experimental settings and data analysis.

   **Comment**: Has a .spm file and an unknown file format.

---

61. **Code and Data for Cross-Modal Characterization of Thin Film MoS2 Using Generative Models**

   - **DOI**: 10.5281/zenodo.15533400
   - **URL**: [https://doi.org/10.5281/zenodo.15533400](https://doi.org/10.5281/zenodo.15533400)
   - **Date**: 2025-05-28
   - **Access**: open
   - **License**: CC BY 4.0
   - **By**: Moses, Isaiah A., Reinhart, Wesley
   - **Tags**: Raman Spectroscopy, Photoluminescence, Atomic Force Microscopy, Cross- Modal Learning, Autoencoder, Thin Film MoS2
   - **Desc**: This package contains data and code used in the manuscript "Cross-Modal Characterization of Thin Film MoS2 Using Generative Models" by Isaiah A. Moses et al. It consists of atomic force microscopy, Raman spectroscopy, and photoluminescence spectra of MoCVD-grown thin film MoS2. The codes are written in Python, and we have included some notebooks as well. The associated unprocessed data is available from the link https://data.2dccmip.org/Fwfn8olOmPsM and in the paper.

   **Comment**: Needs observation to detect the .txt file source

---

62. **FAIR Dataset of Defected Graphene with STM Images and Transport Properties**

   - **DOI**: 10.5281/zenodo.15520157
   - **URL**: [https://doi.org/10.5281/zenodo.15520157](https://doi.org/10.5281/zenodo.15520157)
   - **Date**: 2025-05-26
   - **Access**: open
   - **License**: CC BY 4.0
   - **By**: Vozza, Mario, Forni, Tommaso, Mercuri, Francesco
   - **Tags**: FAIR Metrics, FAIR Principles
   - **Desc**: This HDF5 (application/x-hdf5 ) dataset organizes data for graphene flakes. At the root level, global metadata and documentation are stored. Each flake is identified by an index and split into two groups: OptGeom (optimized geometry) and OptGeomElectrodes (geometry in an electrode setup). The OptGeom group contains the flake's atomic numbers, coordinates, number of atoms, and inertia tensor, with attributes such as formation energy. The OptGeomElectrodes group includes similar structural data but adds calculated properties like total energy, ionization potential (IP), electron affinity (EA), band gap, transport current, and STM images. In the folder we can find the extended metadata in the format json-ld FAIR metadata JSON-LD file (application/ld+json) Access condition: Open access Machine-readable: http://f-uji.net/vocab/access_condition/open

   **Comment**: H5 file

---

63. **Dataset of the publication: Atomic Force Microscopy beyond Topography: Chemical Sensing of 2D Material Surfaces through Adhesion Measurements**

   - **DOI**: 10.5281/zenodo.14222590
   - **URL**: [https://doi.org/10.5281/zenodo.14222590](https://doi.org/10.5281/zenodo.14222590)
   - **Date**: 2024-11-26
   - **Access**: open
   - **License**: CC BY 4.0
   - **By**: Forment-Aliaga, Alicia
   - **Tags**: RTMM, UIMM, Transition metal chalcogenides, MnPS3, 2D materials, AFM, adhesion properties
   - **Desc**: Dataset of the publication: Atomic Force Microscopy beyond Topography: Chemical Sensing of 2D Material Surfaces through Adhesion Measurements DOI: 10.1021/acsami.3c19254 I. Brotons-Alcázar, Jason. S. Terreblanche, S. Giménez-Santamarina, G. M. Gutiérrez-Finol, K. S. Ryder, A. Forment-Aliaga, E. Coronado, ACS Appl. Mater. Interfaces 2024 , 16 , 19711.

   **Comment**: Unknown file format,  Figure 5a.tif

---

68. **Data - 2D Co-Directed Metal–Organic Networks Featuring Strong Antiferromagnetism and Perpendicular Anisotropy**

   - **DOI**: 10.5281/zenodo.14179239
   - **URL**: [https://doi.org/10.5281/zenodo.14179239](https://doi.org/10.5281/zenodo.14179239)
   - **Date**: 2021-11
   - **Access**: open
   - **License**: Unknown
   - **By**: Parreiras, Sofia O., Martín-Fuentes, Cristina, Moreno, Daniel et al.
   - **Desc**: STM images, STS data, XAS/XMCD/XMD data. The software to open the STP files is WSxM.

   **Comment**: Unknown dataset

---

69. **Data - Lanthanide metal–organic network featuring strong perpendicular magnetic anisotropy**

   - **DOI**: 10.5281/zenodo.14196376
   - **URL**: [https://doi.org/10.5281/zenodo.14196376](https://doi.org/10.5281/zenodo.14196376)
   - **Date**: 2023-02
   - **Access**: open
   - **License**: Unknown
   - **By**: Parreiras, Sofia O., Moreno, Daniel, Mathialagan, Shanmugasibi K. et al.
   - **Desc**: (i) Multiplet calculations for TDA+Er; (ii) Point charges for multiplet calculations for TDA+Er; (iii) STM images; (iv) STS data; (v) XAS, XMCD and XLD data for TDA+Er

   **Comment**: Unknown dataset

---

## Datasets Not of Interest

*Datasets explicitly rejected: life/bio/food science, fisheries, no actual data files, or only raw images without metadata.*

3. **AFM images of information-carrying DNA origami nanostructures before and after 40 freeze–thaw cycles**

   - **DOI**: 10.5281/zenodo.18609746
   - **URL**: https://doi.org/10.5281/zenodo.18609746
   - **Date**: 2026-02-20
   - **Access**: open
   - **License**: CC BY 4.0
   - **By**: Li, Xinyang, Keller, Adrian
   - **Desc**: Twist-corrected rectangular DNA origami nanostructures (DONs) containing five biotin (Bt) modifications were exposed to 40 freeze-thaw (F/T) cycles (RT <-> −25 °C or −80 °C) using two strategies. Glycerol was added to achieve final concentrations of 0 mM, 10 mM, and 100 mM. Strategy I. Streptavidin (SAv) was freshly prepared from a 1 g L -1 stock solution in HPLC-grade water and added to the DON samples (in 1× TAE + 10 mM MgCl 2 ) to reach a final SAv concentration of 500 nM, corresponding to a tenfold molar excess over the total Bt sites. The samples were incubated for 30 min at room temperature and subsequently subjected to F/T cycling. Afterwards, 10 µL of DON/SAv solution were deposited on freshly cleaved mica and subsequently covered with 90 µL of 1× TAE + 10 mM MgCl 2 to reach a final DON and SAv concentration of 1 nM and 50 nM, respectively. The sample was incubated for 5 min to allow adsorption, after which the surfaces were rinsed three times with 3 mL of HPLC-grade water to remove unbound material and dried under argon (1 bar) prior to AFM imaging. Strategy II. F/T cycling of DONs (in 1× TAE + 10 mM MgCl 2 ) was performed in the absence of SAv. After F/T cycling of , 10 µL of DON solution were deposited on freshly cleaved mica and subsequently covered with 90 µL of 1× TAE + 10 mM MgCl 2 to reach a final DON concentration of 1 nM. After 5 min adsorption, the surface was rinsed three times with 3 mL HPLC-grade water and dried under argon (1 bar). 99 µL of fresh 1× TAE + 10 mM MgCl 2 were then applied to the mica surface, after which 1 µL of 5 µM SAv solution was added to reach a final concentration of 50 nM. The sample was incubated for 30 min at room temperature, rinsed again three times with 3 mL HPLC-grade water, and dried under argon (1 bar). Each sample (200 µL) was sealed in polypropylene PCR tubes and stored at −25 °C. For F/T cycling, each cycle consisted of freezing at −25 °C for at least 20 min followed by 20 min thawing at room temperature. A total of 40 cycles were performed. For one additional experiment using strategy II, F/T cycling was performed at −80 °C, with each cycle consisting of freezing at −80 °C for at least 8 min followed by 10 min thawing at room temperature. All samples were imaged in air using a Bruker Dimension Icon operated in ScanAsyst mode with ScanAsyst-Air cantilevers. Images were recorded at a scan size of 2 × 2 µm² with 1024 × 1024 pixels and a line rate of 1 Hz.

   **Comment**: We are not interested in BioScience experiments

---

6. **Dataset for Polyvinylalcohol Composite Filled with Carbon Dots Produced by Laser Ablation in Liquids**

   - **DOI**: 10.5281/zenodo.17424121
   - **URL**: [https://doi.org/10.5281/zenodo.17424121](https://doi.org/10.5281/zenodo.17424121)
   - **Date**: 2024-05-13
   - **Access**: open
   - **License**: CC BY 4.0
   - **By**: Cutroneo, Mariapompea
   - **Desc**: The prepared suspension was transferred to a quartz cuvette to be analyzed by UV-VIS spectrometer (Avantes BV, Apeldoorn, the Netherlands) to prove its luminescence. Cuvettes containing PBS and PBS+CDs, both illuminated by room light and illuminated by UV light at 365 nm wavelength. The suspension of PBS+CDs lights up in a blue color under UV light, suggesting emission at a wavelength of 450–495 nm. For morphological analysis of nanoscale structures, atomic force microscopy (AFM) is considered a powerful tool. Its widespread use is attributed to its accurate 2D and 3D reconstruction of sample topography at a relatively low cost and within a short time. AFM was carried out using a Dimension ICON AFM system (Bruker Corp., Bremen, Germany), operating in the PeakForce QNM (Quantitative Nanoscale Mechanical) imaging mode in air. Further equipment includes a commercial commercial silicon tip using using the SCANASYST in air mode with spring constant of 0.4 N/m and scan size of of 33 µm2 . UV-VIS absorption were performed using JASCO-600 a wavelength between 200 and 800 nm. ATR-FTIR spectra were taken using JASCO-7600 at 400-4000 cm-1.

   **Comment**: Not interested: It has only the image data, no metadata or instrument setup.

---

7. **Dataset for Insulator material deposited with Molybdenum disulphide prospective for sensing application**

   - **DOI**: 10.5281/zenodo.17424222
   - **URL**: [https://doi.org/10.5281/zenodo.17424222](https://doi.org/10.5281/zenodo.17424222)
   - **Date**: 2024-11-27
   - **Access**: open
   - **License**: CC BY 4.0
   - **By**: Cutroneo, Mariapompea
   - **Desc**: The primary target of molybdenum disulfide (MoS 2 ) crystal 99.995 % with a size of about 0.5 cm × 1.0 cm × 0.2 mm and a density of 5.06 g/cm 3 at 15 °C has been purchased from Sigma Aldrich. T he deposition of the adopted insulators occurred in a vacuum of about 7.6·10 -3 mbar inside a vacuum chamber . A Q-switching Nd: YAG laser operating at a wavelength of 1064 nm, a pulse duration of 5 ns, was used at a repetition rate of 10 Hz and 30 minutes of irradiation time . The laser beam passed through a 50 cm lens to focus the beam to a diameter of 0.5 mm on a solid target of MoS 2 placed in a rotating carrousel to avoid deep ablation which could modify the laser density. A fresh target surface was always exposed to the incident laser light. The distance between the window of incoming laser and the target is of 22 cm. The volume of the vacuum chamber is about 52 liters. The energy of the laser pulse was 600 mJ and the laser incidence angle was 45° on the surface of the target corresponding to a laser fluence of about 76 J/cm 2 . When the laser fluence overcame the ablation threshold of the MoS 2 , ions, besides other particles, atoms, and clusters, were ejected. A Tencor P-10 has been employed as a surface profiler to measure the crater size and shape formed on the surface of the MoS 2 after one laser shot to evaluate the amount of removed material during the laser irradiation. A mass quadrupole spectrometer QMG F3 220 PrismaPlus (MQS) from Pfeiffer Vacuum was used to detect the emitted atoms and molecules from the laser ablation of a target of MoS 2 in vacuum. Typically, the spectrometer detects the emission of the gas produced in the vacuum chamber. This spectrometer detects masses ranging between 1amu and 300 amu, with a sensitivity lower than 1 ppm and a mass resolution better than 1 amu. The MQS is equipped with a SEM detector with a power supply of 1100 V . The masses of interest have been selected as follows: 18 ( H 2 O ), 32 (S), 48 (SO), 64 ( S 2 ), 96 (Mo), 112 (MoO), 128 (MoS), 160 ( MoS 2 ) amu. The MQS detects the emitted atoms and molecules as a function of the time at the laser switching on and 1 Hz laser repetition rate. The Attenuated Total Reflectance – Fourier Transform Infrared (ATR-FTIR) spectroscopy using a Jasco 4700 and UV-VIS spectroscopy by means a Jasco V750 spectrophotometers, have been employed to analyze the alteration of the presence of specific functional groups, the changes of the chemical structure and of the optical transmittance in the polymer after the deposition of MoS 2 . The control of the quality of the deposited MoS 2 has been explored by Atomic Force Microscope (AFM) analysis. The accomplishment of the surface average roughness (Ra) and the mean roughness parameter (RMS) was performed using a Dimension ICON- Bruker Corp. has been used . T he 3D images with scan size of 1 m m have been captured using an exposure time of 1s, and processed by NanoScope Analysis software . The monitoring of the electrical capacitance alteration was performed by the I–V characteristic curve through frequency dependence measurements of the output voltage of a high-pass filter at the constant current of 0.5 mA for pristine samples and 0.1 mA . A metallic mask containing two stripes at distance of 1 mm each other and width of 10 mm was used to assist the production of two gold electrodes 50 nm thick sputtered on the composite surface. The resistivity of the used resistor was 1 M W . The voltage response was recorded over frequencies ranging between 20kHz and 100 kHz. The alternating current (AC) with sinusoidal waveform was generated using a Keithley 6221 current source. The AC voltage vs frequency was monitored by a Tektronix TDS5104B. oscilloscope. Commercial ceramic capacitor of 2.6 pF. 6.8 pF and 12 pF have been used to display the corresponding voltage frequency. In the experimental configuration shown in Figure 2 the prepared composite or the used commercial ceramic capacitor are alternatively positioned.

   **Comment**: Not interested: It has only the image data, no metadata or instrument setup.

---

9. **AFM BioMed 2025 - AFM Data- Bacteriorhodopsin Membrane Imaging**

   - **DOI**: 10.5281/zenodo.17105214
   - **URL**: https://doi.org/10.5281/zenodo.17105214
   - **Date**: 2025-09-12
   - **Access**: open
   - **License**: CC BY 4.0
   - **By**: Heath, George R
   - **Tags**: AFM, Bacteriorhodopsin
   - **Desc**: Seleted raw AFM Images of Bacteriorhodopsin membranes captured during the practicals sessions of the Membrane Imaging sessions of the AFM BioMed 2025 Summer school. Data captured using FastScan D probes in tapping mode on a Bruker FastScan AFM in the Pyne lab at the University of Sheffield.

   **Comment**: Not interested in life science

---

10. **Atomic force microscopy (AFM) images of streptavidin-decorated DNA origami rectangles**

   - **DOI**: 10.5281/zenodo.15370091
   - **URL**: https://doi.org/10.5281/zenodo.15370091
   - **Date**: 2025-05-09
   - **Access**: open
   - **License**: CC BY 4.0
   - **By**: Rabbe, Lukas, Keller, Adrian
   - **Tags**: DNA origami, DNA nanotechnology, Streptavidin, Biotin, Protein arrays
   - **Desc**: AFM images of twist-corrected DNA origami rectangles with different arrangements of biotin modifications (9 plus 3 marker positions and 20 plus 3 marker positions) after exposure to streptavidin at different concentrations (static at a fixed concentration and with stepwise increases in concentration at 5 min intervals until the final concentration was reached). AFM imaging was performed in air on mica surfaces using a Dimension Icon (Bruker) operated in ScanAsyst mode with ScanAsyst-Air cantilevers (nominal tip radius 2 nm, Bruker). Images were recorded at a size of 1 x 1 µm 2 , a resolution of 1024 x 1024 px, and a line rate of 1 Hz.

   **Comment**: Not interested in life science

---

11. **AFM and XPS datasets for DNA origami adsorption at single-crystalline TiO2 surfaces**

   - **DOI**: 10.5281/zenodo.15369685
   - **URL**: https://doi.org/10.5281/zenodo.15369685
   - **Date**: 2025-05-09
   - **Access**: open
   - **License**: CC BY 4.0
   - **By**: Keller, Adrian, Xu, Xiaodan, Golebiowska, Sandra
   - **Desc**: Atomic force microscopy (AFM) images recorded in the dry state of DNA origami triangles adsorbed on TiO2(001), TiO2(110), and TiO2(111) surfaces under different conditions as indicated. Native surface oxided (SiO2) of silicon wafers was used as a control. AFM imaging was performed using a Bruker Dimension Icon operated in ScanAsyst mode with SCANASYST-AIR cantilevers (Bruker). Images were acquired with a scan size of 2 × 2 µm² at a resolution of 1024 × 1024 pixels. X-ray photoelectron spectroscopy (XPS) of the different TiO2 surfaces prior to DNA origami adsorption. XPS measurements were conducted in ultra-high vacuum (base pressure better than 10-10 mbar) using an Omicron ESCA+ system (Omicron NanoTechnology) with a monochromatic Al Kα (1486.7 eV) X-ray source and a hemispherical energy analyzer. The source-analyzer angle was 102°, while the take-off angle of the detected photoelectrons was set to 30° with respect to the surface plane. A pass energy of 100 eV, a step size of 0.5 eV, and a dwell time of 0.1 s were used for survey spectra. A pass energy of 20 eV, a step size of 0.1 eV, and a dwell time of 0.5 s were used for high-resolution core-level spectra. Neutralization was done using simultaneous irradiation with a low energy electron beam (2 eV). Prior to DNA origami adsorption and XPS analysis (dataset "After Cleaning"), the substrates were soaked in Hellmanex III solution (Hellma GmbH) for two hours, rinsed thoroughly with HPLC-grade water (Carl Roth) and subsequently dried under a stream of argon. The cleaned substrates were treated with an O2 plasma (diener Zepto, diener electronic) for 1 minute to create a hydrophilic, hydroxyl-rich surface. For the XPS dataset "After MgCl2", the TiO2 surfaces were additionally incubated for 10 min in 5 mM MgCl2 solution (in water). To avoid any Mg2+ desorption, the surfaces were not washed after incubation but blow-dried in a high-pressure stream of argon.

   **Comment**: Not interested in life science

---

13. **High-speed atomic force microscopy images of DNA origami triangles adsorbing at mica surfaces**

   - **DOI**: 10.5281/zenodo.14275812
   - **URL**: https://doi.org/10.5281/zenodo.14275812
   - **Date**: 2024-12-04
   - **Access**: open
   - **License**: CC BY 4.0
   - **By**: Pothineni, Bhanu, Barner, Jörg, Keller, Adrian
   - **Desc**: Each folder corresponds to a different DNA origami concentration as indicated. Imaging was performed using a JPK Nanowizard ULTRA Speed 3 (Bruker) with USC F0.3-k0.3 cantilevers (NanoWorld). The DNA origami triangles were suspended in 1x TAE (pH 8.5) containing 10 mM CaCl 2 and 75 mM NaCl. For the first 10 min, images were recorded with 1 x 1 µm² scan size at a line rate of 200 Hz and a resolution of 200 x 200 pixels resulting in a frame rate of 1 fps. After about 10 min, the resolution was increased to 400 x 400 pixels, lowering the frame rate to 0.5 fps. After about another 15 min, overview images 4 x 4 µm² in size were recorded at a line rate of 20 Hz and a resolution of 2048 x 2048 pixels.

   **Comment**: Not interested in life science

---

14. **Atomic force microscopy (AFM) images of DNA origami rectangles**

   - **DOI**: 10.5281/zenodo.15147607
   - **URL**: https://doi.org/10.5281/zenodo.15147607
   - **Date**: 2025-04-04
   - **Access**: open
   - **License**: CC BY 4.0
   - **By**: Tomm, Emilia, Keller, Adrian
   - **Tags**: DNA origami, Recycling, Sustainability, Cost reduction
   - **Desc**: AFM images of bare DNA origami rectangles on mica that were assembled at different staple excess (2x to 10x). Images .jpk were recorded in air using a JPK Nanowizard Ultra Speed (JPK Instruments) operated in intermittent contact mode with HQ:NSC/Al BS cantilevers (75 kHz, 2.8 N/m) from MikroMasch (NanoAndMore). Images .spm were recoreded in air using a Bruker Dimension ICON in ScanAsyst PeakForce Tapping mode with SCANASYST-AIR cantilevers (70 kHz , 0.4 N/m). AFM images of biotinylated DNA origami rectangles after up to five (1b to 5b) consecutive folding reactions with staples recovered fromt he previous folding reactions. The DNA origami rectangles were adsorbed on mica and subsequently exposed to streptavidin (215 µM, 30 min) to visualize the presence of the biotinylated staples. Images were recorded in air using a Bruker Dimension ICON in ScanAsyst PeakForce Tapping mode with SCANASYST-AIR cantilevers (70 kHz , 0.4 N/m).

   **Comment**: Not interested in life science

---

19. **Mechanism for Vipp1 spiral formation, ring biogenesis and membrane repair**

   - **DOI**: 10.5281/zenodo.13149421
   - **URL**: [https://doi.org/10.5281/zenodo.13149421](https://doi.org/10.5281/zenodo.13149421)
   - **Date**: 2024-08-01
   - **Access**: open
   - **License**: MIT-LICENSE
   - **By**: Merino, Andrea, Naskar, Souvik, Espadas, Javier et al.
   - **Desc**: Here , we collect an image dat aset of Vipp1 polymerization dynamics on supported lipid bilayers using atomic force microscopy ( AFM ) . A JPK NanoWizard Ultraspeed AFM (Bruker and JPK BioAFM ) equipped with USC-F0.3-k0.3-10 cantilevers with spring constant of 0.3N nm−1, resonance frequency of about 300 kHz (Nanoworld), was employed for image acquisition. The AFM was operated in tapping mode with a cantilever oscil l ation frequency near to 150kHz. Both topographic and phase images were analysed using JPKSPM Data Processing, ImageJ, and WSxM software .

   **Comment**: Not interested on life science.

---

24. **Data from: Mechanical morphotype switching as an adaptive response in Mycobacteria**

   - **DOI**: 10.5061/dryad.cvdncjt90
   - **URL**: https://doi.org/10.5061/dryad.cvdncjt90
   - **Date**: 2023-11-29
   - **Access**: open
   - **License**: CC0 1.0 (Public Domain)
   - **By**: Eskandarian, Haig Alexander, Chen, Yu-Xiang
   - **Tags**: Atomic force microscopy, Long-Term Time-Lapse Atomic Force Microscopy, LTTL-AFM, Mycobacterium smegmatis, Cell Surface Stiffness, TnSeq, Transposon mutagenesis, Transposon insertion mutagenesis
   - **Desc**: Invading microbes face a myriad of cidal mechanisms of phagocytes that inflict physical damage to microbial structures. How intracellular bacterial pathogens adapt to these stresses is not fully understood. Here, we report a new virulence mechanism by which changes to the mechanical stiffness of the mycobacterial cell surface confers refraction to killing during infection. Long-Term Time-Lapse Atomic Force Microscopy was used to reveal a process of “mechanical morphotype switching” in mycobacteria exposed to host intracellular stress. A “soft” mechanical morphotype switch enhances tolerance to intracellular macrophage stress, including cathelicidin. Both pharmacologic treatment, with bedaquiline, and a genetic mutant lacking uvrA modified the basal mechanical state of mycobacteria into a “soft” mechanical morphotype, enhancing survival in macrophages. Our study proposes microbial cell mechanical adaptation as a critical axis for surviving host-mediated stressors.

   **Comment**: Not interested in life science.

---

25. **AFM Dataset on HeLa cells**

   - **DOI**: 10.5281/zenodo.8342121
   - **URL**: https://doi.org/10.5281/zenodo.8342121
   - **Date**: 2023-07-28
   - **Access**: open
   - **License**: CC BY 4.0
   - **By**: Javier Lopez Alonso
   - **Tags**: AFM, Microrheology, HeLa, Force Maps
   - **Desc**: Dataset acquired using a NanoWizard III (Bruker, Santa Barbara, CA, USA) on 40 HeLa cells using a SAA-SPH-5UM AFM probe (Bruker, Santa Barbara, CA, USA). The dataset includes force maps (20 cells) and microrheological measurements (20 cells) acquired on HeLa cells. Additionally this dataset includes: - Force settings used to acquired the data - Data used to characterize the piezo lag - Data used to characterize the viscous drag - Results obtained from PyFMLab, MATLAB routines and JPKDP

   **Comment**: Not interested in life science.

---

26. **Global monthly catches from tuna fisheries by 1° and 5° grids (1950-2024) (FIRMS level 0)**

   - **DOI**: 10.5281/zenodo.20364497
   - **URL**: https://doi.org/10.5281/zenodo.20364497
   - **Date**: 2026-05-24
   - **Access**: open
   - **License**: CC BY 4.0
   - **By**: FIRMS Global Tuna Atlas Technical Working Group
   - **Tags**: fishery, marine fishery, fishery resource, fish stock, commercial fishery, fisheries management, fishery data, fishery statistics
   - **Desc**: We compiled a comprehensive dataset of geo-referenced catches from global tuna fisheries available at a spatial resolution of 1° and 5° grid areas. This dataset was created by harmonizing public domain data from the five tuna Regional Fisheries Management Organizations (t-RFMOs) for the period 1950-2023. Under the auspices of the Fisheries and Resources Monitoring System (FIRMS) of the United Nations Food and Agriculture Organization (FAO), we developed a systematic data flow process in collaboration with the t-RFMO Secretariats. This process involved the implementation of a data exchange format adhering to the standards of the FAO Coordinating Working Party on Fishery Statistics (CWP), facilitating the seamless integration of data into the dataset. Geo-referenced catch data from tuna fisheries are reported in either the number of fish or live-weight equivalent (metric tonnes), with some strata providing catches in both units. The catches primarily represent the quantities of retained fish either landed or transhipped at sea and in ports. The data are stratified by year, month, fishing fleet, fishing gear, fishing mode, 1° or 5° grid area of longitude and latitude, and taxon. The dataset encompasses 49 medium- and large-sized pelagic species found in both neritic and oceanic habitats of the world's oceans. This includes 15 species of tunas, 10 species of billfish, 7 species of Spanish mackerels, 2 species of bonitos, and wahoo. Despite uncertainties and incomplete data due to under-reporting, the dataset also includes reported catches for 14 species of pelagic sharks and rays that may be either targeted or incidentally caught in tuna and tuna-like fisheries. The dataset serves as a benchmark for the monitoring and assessment of both artisanal and industrial fisheries from over 116 fishing fleets across 115 countries that have exploited tuna and tuna-like species for subsistence and commercial purposes over more than seven decades.

   **Comment**: Not interested in life science.

---

27. **Global monthly catches from tuna fisheries by 5° grid (1950-2024) (FIRMS level 0)**

   - **DOI**: 10.5281/zenodo.20364387
   - **URL**: https://doi.org/10.5281/zenodo.20364387
   - **Date**: 2026-05-24
   - **Access**: open
   - **License**: CC BY 4.0
   - **By**: FIRMS Global Tuna Atlas Technical Working Group
   - **Tags**: fishery, marine fishery, fishery resource, fish stock, commercial fishery, fisheries management, fishery data, fishery statistics
   - **Desc**: We compiled a comprehensive dataset of geo-referenced catches from global tuna fisheries available on a spatial resolution of 5° grid areas. This dataset was created by harmonizing public domain data from the five tuna Regional Fisheries Management Organizations (t-RFMOs) for the period 1950-2024. Under the auspices of the Fisheries and Resources Monitoring System (FIRMS) of the United Nations Food and Agriculture Organization (FAO), we developed a systematic data flow process in collaboration with the t-RFMO Secretariats. This process involved the implementation of a data exchange format adhering to the standards of the FAO Coordinating Working Party on Fishery Statistics (CWP), facilitating the seamless integration of data into the dataset. Geo-referenced catch data from tuna fisheries are reported in either the number of fish or live-weight equivalent (metric tonnes), with some strata providing catches in both units. The catches primarily represent the quantities of retained fish either landed or transhipped at sea and in ports. The data are stratified by year, month, fishing fleet, fishing gear, fishing mode, 5° grid area of longitude and latitude, and taxon. The dataset encompasses 49 medium- and large-sized pelagic species found in both neritic and oceanic habitats of the world's oceans. This includes 15 species of tunas, 10 species of billfish, 7 species of Spanish mackerels, 2 species of bonitos, and wahoo. Despite uncertainties and incomplete data due to under-reporting, the dataset also includes reported catches for 14 species of pelagic sharks and rays that may be either targeted or incidentally caught in tuna and tuna-like fisheries. The dataset serves as a benchmark for the monitoring and assessment of both artisanal and industrial fisheries from over 116 fishing fleets across 115 countries that have exploited tuna and tuna-like species for subsistence and commercial purposes over more than seven decades.

   **Comment**: Not interested in life science.

---

28. **Global monthly catches from tuna surface fisheries by 1° grid (1958-2024) (FIRMS level 0)**

   - **DOI**: 10.5281/zenodo.20364254
   - **URL**: https://doi.org/10.5281/zenodo.20364254
   - **Date**: 2026-05-24
   - **Access**: open
   - **License**: CC BY 4.0
   - **By**: FIRMS Global Tuna Atlas Technical Working Group
   - **Tags**: fishery, marine fishery, fishery resource, fish stock, commercial fishery, fisheries management, fishery data, fishery statistics
   - **Desc**: We compiled a comprehensive dataset of geo-referenced catches from global tuna fisheries that use fishing gears set at the water's surface. This dataset was created by harmonizing public domain data from the five tuna Regional Fisheries Management Organizations (t-RFMOs) for the period 1958-2024. Under the auspices of the Fisheries and Resources Monitoring System (FIRMS) of the United Nations Food and Agriculture Organization (FAO), we developed a systematic data flow process in collaboration with the t-RFMO Secretariats. This process involved the implementation of a data exchange format adhering to the standards of the FAO Coordinating Working Party on Fishery Statistics (CWP), facilitating the seamless integration of data into the dataset. Geo-referenced catch data from tuna surface fisheries are reported in either the number of fish or live-weight equivalent (metric tonnes), with some strata providing catches in both units. The catches primarily represent the quantities of retained fish either landed or transhipped at sea and in ports. The data are stratified by year, month, fishing fleet, fishing gear, fishing mode, 1° grid area of longitude and latitude, and taxon. The dataset encompasses 42 medium- and large-sized pelagic species found in both neritic and oceanic habitats of the world's oceans. This includes 14 species of tunas, 9 species of billfish, 4 species of Spanish mackerels, 2 species of bonitos, and wahoo. Despite uncertainties and incomplete data due to under-reporting, the dataset also includes reported catches for 12 species of pelagic sharks and rays that may be either targeted or incidentally caught in tuna and tuna-like fisheries. The dataset serves as a benchmark for the monitoring and assessment of both artisanal and industrial fisheries using surrounding nets, gillnets, entangling nets, and pole-and-lines from over 74 fishing fleets across 70 countries that have exploited tuna and tuna-like species for subsistence and commercial purposes over more than six decades.

   **Comment**: Not interested in life science.

---

29. **Global annual catches from tuna fisheries (1918-2024) (FIRMS level 0)**

   - **DOI**: 10.5281/zenodo.20364152
   - **URL**: https://doi.org/10.5281/zenodo.20364152
   - **Date**: 2026-05-24
   - **Access**: open
   - **License**: CC BY 4.0
   - **By**: FIRMS Global Tuna Atlas Technical Working Group
   - **Tags**: fishery, marine fishery, fishery resource, fish stock, commercial fishery, fisheries management, fishery data, fishery statistics
   - **Desc**: We constructed the most comprehensive dataset of nominal catches from global tuna fisheries by compiling and harmonizing public domain data from the five tuna Regional Fisheries Management Organizations (t-RFMOs) for the period 1918-2024. Under the auspices of the Fisheries and Resources Monitoring System (FIRMS) of the United Nations Food and Agriculture Organization (FAO),we developed a systematic data flow process in collaboration with the t-RFMO Secretariats. This process involved the implementation of a data exchange format adhering to the standards of the FAO Coordinating Working Party on Fishery Statistics (CWP),facilitating the seamless integration of data into the dataset. Nominal catch data are expressed in live-weight equivalent (metric tonnes) and primarily represent the quantities of retained fish either landed or transhipped at sea and in ports. In recent years,data from fisheries in the Atlantic and Western-Central Pacific Oceans have partially included amounts of fish discarded dead. The data are stratified by year,fishing fleet,fishing gear,large spatial area,and taxon. The dataset encompasses 50 medium- and large-sized pelagic species found in both neritic and oceanic habitats of the world's oceans. This includes 15 species of tunas,10 species of billfish,8 species of Spanish mackerels,2 species of bonitos,and wahoo. In 2024,the global catch for these species was estimated to exceed 7.1 million metric tonnes. Despite uncertainties and incomplete data due to under-reporting,the dataset also includes reported catches for 14 species of pelagic sharks and rays that may be either targeted or incidentally caught in tuna and tuna-like fisheries. The total reported catch of these elasmobranch species was approximately 123,000 metric tonnes in 2024. The dataset serves as a benchmark for the monitoring and assessment of both artisanal and industrial fisheries from over 162 fishing fleets across 160 countries that have exploited tuna and tuna-like species for subsistence and commercial purposes over more than seven decades.

   **Comment**: Not interested in life science.

---

36. **Raw data for the article "Synthesis and characterization of phase-separated extracellular condensates in interactions with cells"**

   - **DOI**: 10.5281/zenodo.15638559
   - **URL**: https://doi.org/10.5281/zenodo.15638559
   - **Date**: 2025-06-11
   - **Access**: open
   - **License**: CC BY 4.0
   - **By**: Naghilou, Aida, Mashaghi, Alireza
   - **Desc**: Biomolecular condensates formed through liquid-liquid phase separation play key roles in intracellular organization and signaling, yet their function in extracellular environments remains largely unexplored. Here, we establish a model using heparan sulfate, a key component of the extracellular matrix, to study extracellular condensate-cell interactions. We develop a methodology based on scanning probe microscopy (SPM) to quantify rheological properties of these extracellular condensates as well as their adhesion forces with cellular surfaces. Our findings and methodology open new avenues for understanding the organizational roles of condensates beyond cellular boundaries. This repository includes the data files related to this study as well as the Mathematica codes for SPM analysis (Github Link). Users are requested to cite: Naghilou et al., Chemical Engineering Journal, 164551 (2025) https://doi.org/10.1016/j.cej.2025.164551

   **Comment**: Not interested in bioscience

---

39. **Base électronique de productions orales d'apprenants macédoniens de la langue française FRANCORAL**

   - **DOI**: 10.5281/zenodo.14541061
   - **URL**: [https://doi.org/10.5281/zenodo.14541061](https://doi.org/10.5281/zenodo.14541061)
   - **Date**: 2024-12-21
   - **Access**: open
   - **License**: CC BY 4.0
   - **By**: Saints Cyril and Methodius University of Skopje, Kasaposka-Chadlovska, Milena
   - **Desc**: La base électronique de productions orales d'apprenants macédoniens de la langue française FRANCORAL a été créée dans le cadre d'un projet de recherche mené par un groupe de chercheurs de l'Université « Sts. Cyrille et Méthode » de Skopje et financé par le Rectorat de cette Université (le code du projet est: NIP.UKIM.23-24.19). Elle représente la première collection électronique des productions orales d'étudiants macédoniens en français au niveau universitaire. Son objectif principal est de fournir un matériel linguistique authentique qui servirait de fondement empirique à des études quantitatives et qualitatives sur l'apprentissage du français par les locuteurs macédoniens. La base comprend 131 enregistrements oraux provenant de trente-deux étudiants en français de la Faculté de philologie « Blaze Koneski » de Skopje. Sur la plateforme Zenodo, un fichier au format zip est joint, contenant deux fichiers distincts : « Productions orales » et « Informations sur les participants ». Le premier fichier contient 4 dossiers séparés, organisés selon les stimuli utilisés pour réaliser les enregistrements (description de photo (32 enregistrements), dialogue (28 enregistrements), lecture de texte (43 enregistrements), monologue (28 enregistrements)). Les dossiers contiennent les enregistrements audio et les transcriptions correspondantes. Chaque transcription comprend une liste de symboles utilisés. Les enregistrements ont été effectués dans les laboratoires de la Faculté de philologie « Blaze Koneski » à Skopje, à l'aide d'un équipement technique et informatique adapté. Les données collectées pourront être expoitées pour faire des recherches dans des domaines variés tels que la méthodologie et la didactique du FLE, la phonologie, la morphosyntaxe, la sémantique, la pragmatique ou la grammaire contrastive. L'analyse des erreurs en production orale contribuera à l'élaboration de programmes de FLE spécifiquement conçus pour répondre aux besoins et aux caractéristiques des apprenants macédoniens.

---

40. **A dataset on "Coating of self-sensing AFM cantilevers with boron-doped nanocrystalline diamond films at low temperatures"**

   - **DOI**: 10.5281/zenodo.12654928
   - **URL**: [https://doi.org/10.5281/zenodo.12654928](https://doi.org/10.5281/zenodo.12654928)
   - **Date**: 2024-07-04
   - **Access**: open
   - **License**: CC BY 4.0
   - **By**: Potocký, Štěpán, Kuliček, Jaroslav, Ukraintsev, Egor et al.
   - **Tags**: nanocrystalline  diamond, boron-doping, microwave  plasma  CVD, self-sensing probes
   - **Desc**: The data set to paper: Coating of self-sensing AFM cantilevers with boron-doped nanocrystalline diamond at low temperatures Štěpán Potocký1*, Jaroslav Kuliče1k, Egor Ukraintsev1, Ondřej Novotný2, Alexander Kromka3, and Bohuslav Rezek1 1 Faculty of Electrical Engineering, Czech Technical University in Prague, Technická 2, 16627 Prague, Czech Republic 2 NenoVision s.r.o., Purkyňova 649, 61200 Brno, Czech Republic 3 Institute of Physics, Czech Academy of Sciences, Prague 6, Czech Republic *corresponding author: potocky@fel.cvut.cz Data manager: Kristýna Dostálová: dostalovak@fzu.cz Date of data collection: 1. 10. 2023 - 31. 3. 2024 All the data showed in the pictures are provided in X-Y format with described sample. Always, the respective figure to which the data belong is provided in high resolution. The data are in the following formats: Figure 1: pdf Figure 2: pdf Figure 3: pdf, csv Figure 4: pdf, csv, gwy Figure 5: pdf, gwy Figure S1: pdf Figure S2: pdf The comma separated values file (csv) always contain the description of the columns in the first row. Gwy correspond to free Gwyddion SPM data analysis software (gwyddion.net). In case of composed image the name of the file corresponds to the corresponding figure. Data acquistion and processing is provided in the Experimental part in the publication: DOI:10.1002/pssa.202400553.

   **Comment**: Only array data and image PDF

---

41. **Typhoon effect on pelagic ecosystem**

   - **DOI**: 10.5061/dryad.0zpc8673n
   - **URL**: [https://doi.org/10.5061/dryad.0zpc8673n](https://doi.org/10.5061/dryad.0zpc8673n)
   - **Date**: 2024-07-06
   - **Access**: open
   - **License**: CC0 1.0 (Public Domain)
   - **By**: Chen, Chung-Chi
   - **Tags**: Marine and aquatic sciences, Phytoplankton, Bacterioplankton, Typhoons
   - **Desc**: This dataset contains data collected onboard the R/V Ocean Researcher I during the pre-typhoon (July 6–8, 2018) and post-typhoon (July 13–16, 2018) periods across transects T1 (i.e., Sts. 5, 35, and 34) and T2 (i.e., Sts. 4, 3, 2, 1, and 1A) in the southern East China Sea described in the paper: “ C.-C. Chen, C.-h. Hsieh, Y.-H. Cheng, W.-J. Huang, W.-C. Chou, F.-K. Shiah, G.-C. Gong (2023). Effect of a tropical cyclone on the pelagic ecosystem of a continental shelf , Limnology and Oceanography (submitted) “. Main results of this study included fifteen figures as described in the paper, and please refer it for further details.

   **Comment**: Irrelevant dataset

---

44. **Effet des tensioactifs biosourcés sur les propriétés catalytiques des nanoparticules d'argent pour la réduction de l'éosine Y**

   - **DOI**: 10.5281/zenodo.10575544
   - **URL**: https://doi.org/10.5281/zenodo.10575544
   - **Date**: 2024-01-28
   - **Access**: open
   - **License**: CC BY-SA 4.0
   - **By**: Ramona, Gaétan, Naboulet, Gaëlle, Thomas, Grégoire
   - **Desc**: Le développement de synthèses vertes de nanoparticules métalliques à base de surfactants biosourcés représente un enjeu important. Les nanoparticules métalliques sont largement utilisées pour catalyser des réactions de réduction de composés organiques en jouant le rôle de support pour le transfert d’électron. Ce projet a pour objectif de comparer deux voies de synthèse : une conventionnelle et une verte; en termes de taille et d’activité catalytique. Deux synthèses de nanoparticules d’argent avec des citrates et des tensioactifs biosourcés issus du fenugrec ont été réalisées. Pour chaque synthèse deux concentrations différentes de surfactant ont été utilisées. Des Ag NPs de taille 115 nm à 75 nm selon la concentration en citrate ont été obtenues. Les caractérisations par TEM et AFM des nanoparticules d’argent à base de fenugrec montrent des particules sphériques de taille 6 nm et 20 nm confinées dans une matrice carbonée probablement issue du fenugrec. Des mesures de taille en DLS et NTA qui correspondraient à ces structures organiques et non aux nanoparticules d’argent attendues ont également été obtenues. Pour chacune des deux synthèses, les nanoparticules ne présentent aucune activité catalytique pour la réduction de l’éosine Y par NaBH4 comme le souligne des suivis cinétiques en déclin d’absorbance et de fluorescence. Pour le fenugrec, le manque d'accessibilité de la surface des nanoparticules d’argent bloquée par la structure carbonée du fenugrec pourrait expliquer cette absence de pouvoir catalytique.

---

45. **Fonctionnalisation de nanoparticules magnétiques  Fe3O4 par du polyéthylène glycol : synthèse et caractérisation**

   - **DOI**: 10.5281/zenodo.10568963
   - **URL**: https://doi.org/10.5281/zenodo.10568963
   - **Date**: 2024-01-25
   - **Access**: open
   - **License**: CC BY 4.0
   - **By**: Antony Laurent, Enzo Lecointre
   - **Desc**: Les ferrofluides fonctionnalisés par du polyéthylène glycol (PEG) sont depuis plusieurs années utilisés dans pour le traitement du cancer. Il présente de meilleures propriétés thérapeutiques que la présence seule de ferrofluides. Dans cette étude, l’impact du taux de fonctionnalisation de ferrofluides par du PEG est étudié ici. Pour ce faire, deux formulations de ferrofluides ont été réalisées dans les mêmes conditions en solution aqueuse puis, chacune a été mélangée avec une concentration de PEG-4000 différente (0,04 g.ml-1 et 0,08 g.ml-1). Les deux formulations ont été caractérisées par DLS, NTA, zétamétrie, AFM et MET. Elles ont permis de trouver une taille de nanoparticules pour les ferrofluides de 18,1 nm (MET), de 17 nm (AFM) pour les ferrofluides-PEG-4000#1 et de 13,2 nm (AFM) pour les ferrofluides-PEG-4000#2 avec respectivement des agrégats de 160, 45 et 40 nm (AFM). Ces analyses ont permis de montrer que l’on n’a pas obtenu des ferrofluides-PEG, mais une encapsulation de ferrofluides dans le PEG-4000. Ainsi, cette étude a permis de montrer une polydispersité en taille et de forme dans les nanoparticules entre les ferrofluides et les ferrofluides-PEG. Les résultats obtenus ont permis de montrer que la concentration de PEG, avait un impact sur la taille des NPs, et plus précisément qu’elle réduisait leur taille. De plus, l’observation des ferrofluides-PEG-4000 a permis de montrer leur encapsulation et leur stabilité.

---

50. **Dataset for the article "Nanoscale Structure-Function Mapping of Boron-Doped "Classic" and Dendritic Carbon Nanowalls"**

   - **DOI**: 10.5281/zenodo.18596714
   - **URL**: [https://doi.org/10.5281/zenodo.18596714](https://doi.org/10.5281/zenodo.18596714)
   - **Date**: 2026-02-10
   - **Access**: embargoed
   - **License**: CC BY 4.0
   - **By**: Ukraintsev, Egor
   - **Tags**: Nano-FTIR, SECCM, carbon nanowalls, boron doping, surface photovoltage, electrochemical mapping, near-field spectroscopy, nanoscale morphology
   - **Desc**: Dataset for the article "Nanoscale Structure-Function Mapping of Boron-Doped “Classic” and Dendritic Carbon Nanowalls" Noah Al-Shamery, Rafael A. Vicente, Thorsten Gölz, Andreas Tittl, Jaroslav Kuliček, Bohuslav Rezek, Michał Sobaszek, Pooi See Lee, Robert Bogdanowicz, Patrick R. Unwin, Anna Dettlaff School of Materials Science and Engineering, Nanyang Technological University, 50 Nanyang Avenue, Singapore 639798, Singapore Department of Chemistry, University of Warwick, CV4 7AL Coventry, United Kingdom Department of Physical-Chemistry, Universidade Estadual de Campinas (UNICAMP), R. Josué de Castro, s/n, Cidade Universitária, Campinas 13083-970, Brazil Center for Innovation on New Energies (CINE), R. Michel Debrun, s/n, Prédio Amarelo, Campinas 13083-841, Brazil Fakultät für Physik, Nano Institute Munich & Center for NanoScience (CeNS), Ludwig-Maximilians-Universität, Königinstr. 10, 80539, Munich, Germany Czech Technical University in Prague, Faculty of Electrical Engineering, Technická 2, Prague 6, Czechia Gdańsk University of Technology, Faculty of Electronics, Telecommunications and Informatics, Narutowicza 11/12, 80-233 Gdańsk, Poland Gdańsk University of Technology, Faculty of Chemistry, 11/12 Narutowicza Str., 80-233, Gdańsk, Poland Figure 2. Raman mapping and spectral results of B:CNW and D:CNW: a) D‑band peak map, b) Raman spectra of bulk carbon nanowalls, and c) G‑band peak map. Figure 3. Time‑resolved WF for the B:CNW and D:CNW electrodes measured in the dark and under simulated sunlight illumination. Figure.4. WF mapping for samples B:CNW and D:CNW in the dark (a) and simulated sunlight (b) conditions. (c) Surface photovoltage mapping at the same location. Table 1. Summary of carbon nanowalls WF in the dark and SPV. Figure S1. Deconvoluted Raman spectra of B:CNW and D:CNW. Figure S2. Hyperspectral Raman maps of B:CNW and D:CNW in the a) D‑band and b) G‑band peaks, acquired over areas of 15×15 μm², 5×5 μm², and 2.5×2.5 μm². Figure S3. Hyperspectral Raman maps of B:CNW and D:CNW in the a) G´‑band and b) 2D´‑band peaks, acquired over areas of 15×15 μm², 5×5 μm², and 2.5×2.5 μm².. Abstract: Understanding how nanoscale structure influences functionality in carbon-based materials is critical for advancing their use in sensing, catalysis, and energy storage. Here, we investigate boron-doped carbon nanowalls (B:CNW) and dendritic carbon nanowalls (D:CNW) using a correlative, multimodal approach that combines nano-FTIR spectroscopy, atomic force microscopy (AFM), Raman mapping, Kelvin probe work function (WF) and surface photovoltage (SPV) measurements, and scanning electrochemical cell microscopy (SECCM). Far-field Raman and FTIR confirm the expected graphitic and boron-related signatures, while nano-FTIR and AFM reveal pronounced apex-to-margin contrasts in local chemistry and morphology, including apex-specific boron modes in D:CNW and additional carbonyl species at B:CNW margins. Raman mapping links these nanoscale features to differences in wall packing density and porosity.. WF/SPV mapping shows that D:CNW possesses a higher and more spatially uniform WF together with a predominantly positive SPV, indicative of efficient photogenerated hole accumulation, whereas B:CNW exhibits a broader WF distribution and weaker, heterogeneous SPV response. SECCM measurements further demonstrate that B:CNW behaves as a largely homogeneous nanoscale electrode, while D:CNW displays apex-dominated, highly wettable regions that locally amplify electrochemical currents. Together, these results provide a coherent structure–function picture in which B:CNW offers spatially uniform electrochemical behaviour suited to reproducible, large-area sensing, whereas D:CNW provides an energetically favourable and locally intensified interface for highly sensitive, apex-driven detection. The correlative methodology outlined here yields transferable design rules for tailoring doped nanocarbon architectures in optoelectronic and electrochemical devices. Keywords: Nano-FTIR, SECCM, carbon nanowalls, boron doping, surface photovoltage, electrochemical mapping, near-field spectroscopy, nanoscale morphology, photoelectrochemical sensors, structure-function relationships

   **Comment**: No dataset

---

52. **Dataset for 'Amyloid fibril-nanocellulose interactions and self-assembly'**

   - **DOI**: 10.5281/zenodo.17828112
   - **URL**: https://doi.org/10.5281/zenodo.17828112
   - **Date**: 2025-12-05
   - **Access**: open
   - **License**: CC BY 4.0
   - **By**: Nystrom, Gustav
   - **Desc**: Amyloid fibrils from inexpensive food proteins and nanocellulose are renewable and biodegradable materials with broad ranging applications, such as water purification, bioplastics and biomaterials. To improve the mechanical properties of hybrid amyloid-nanocellulose materials, their colloidal interactions need to be understood and tuned. A combination of turbidity and zeta potential measurements, rheology and atomic force microscopy point to the importance of electrostatic interactions. These interactions lead to entropy-driven polyelectrolyte complexation for positively charged hen egg white lysozyme (HEWL) amyloids with negatively charged nanocellulose. The complexation increased the elasticity of the amyloid network by cross-linking individual fibrils. Scaling laws suggest different contributions to elasticity depending on nanocellulose morphology: cellulose nanocrystals induce amyloid bundling and network formation, while cellulose nanofibrils contribute to a second network. The contribution of the amyloids to the elasticity of the entire network structure is independent of nanocellulose morphology and agrees with theoretical scaling laws. Finally, strong and almost transparent hybrid amyloid-nanocellulose gels were prepared in a slow self-assembly started from repulsive co-dispersions above the isoelectric point of the amyloids, followed by dialysis to decrease the pH and induce amyloid-nanocellulose attraction and cross-linking. In summary, the gained knowledge on colloidal interactions provides an important basis for the design of functional biohybrid materials based on these two biopolymers.

   **Comment**: Not interested Food science

---

56. **Datasets for manuscript: Hybrid Dielectric-Graphene SERS metasurfaces for anti- body sensing**

   - **DOI**: 10.5281/zenodo.17023716
   - **URL**: [https://doi.org/10.5281/zenodo.17023716](https://doi.org/10.5281/zenodo.17023716)
   - **Date**: 2025-09-01
   - **Access**: open
   - **License**: CC BY 4.0
   - **By**: Pinilla-Cienfuegos, Elena
   - **Tags**: Dielectric metasurfaces, Graphene, Surface-enhanced Raman spectroscopy (SERS), Antibody sensing, Biosensors
   - **Desc**: Dataset corresponding to the AFM, Raman measurements and COMSOL simulations.

   **Comment**: Life science not interested

---

58. **Data for "Which chromium-sulfur compounds exist as 2D material?"**

   - **DOI**: 10.5281/zenodo.16614226
   - **URL**: [https://doi.org/10.5281/zenodo.16614226](https://doi.org/10.5281/zenodo.16614226)
   - **Date**: 2025-07-30
   - **Access**: open
   - **License**: CC BY 4.0
   - **By**: Safeer, Affan, Ghorbani-Asl, Mahdi, Jolie, Wouter et al.
   - **Tags**: chromium sulfide, single-layer 2D material, molecular beam-epitaxy, scanning tunneling microscopy, density functional theory
   - **Desc**: This repository contains the data and source code associated with the paper: *Which chromium-sulfur compounds exist as 2D material?*. Experimental setup STM and STS were carried out at a base operating temperature of T = 1.7 K after in-situ transfer from the preparation chamber. STS was performed with the lock-in technique. STM images were taken in constant current mode. Computational setup First-principles calculations were carried out using the code VASP. Further information in the README files.

   **Comment**: Only array data no metadata. Not interested.

---

60. **The electrical, photo-catalytic and sensory properties of graphene oxide and polyimide implanted by low and medium energy silver ions**

   - **DOI**: 10.5281/zenodo.15631026
   - **URL**: [https://doi.org/10.5281/zenodo.15631026](https://doi.org/10.5281/zenodo.15631026)
   - **Date**: 2025-06-10
   - **Access**: restricted
   - **License**: CC BY 4.0
   - **By**: Novák, Josef
   - **Tags**: ion implnatation, graphene oxide, polyimide, RBS, photocatalysis properties, electric properties, low energy implnatation, medium energy implnatation
   - **Desc**: Precise control of electrical conductivity, humidity sensitivity, and photocatalytic activity in polymeric and carbon-based materials is essential for advancing technologies in environmental sensing, flexible electronics, and photocatalytic systems. Conventional chemical modification methods often lack spatial precision, introduce impurities, and risk structural degradation. Ion implantation provides a controllable alternative for tuning surface properties at the nanoscale, enabling the targeted introduction of functional species without chemical reagents. This work investigates the effects of low-energy (20 keV) and medium-energy (1.5 MeV) Ag⁺ ion implantation on the electrical, sensory, and photocatalytic properties of graphene oxide (GO) and polyimide (PI). Implantations were carried out with fluences ranging from 3.75×10 12 cm -2 to 1×10 16 cm -2 . Silver ions offer excellent electrical, catalytic, and plasmonic characteristics, making them ideal for multifunctional enhancement of GO and PI. Elemental and structural changes induced by implantation were analyzed using Rutherford Backscattering Spectroscopy (RBS), Elastic Recoil Detection Analysis (ERDA), Raman spectroscopy, Fourier Transform Infrared Spectroscopy (FTIR), and X-ray Photoelectron Spectroscopy (XPS). Surface morphology was assessed via Atomic Force Microscopy (AFM). Electrical properties as a function of air humidity were evaluated using a two-point method, and photocatalytic activity was tested by monitoring the UV-induced decomposition of Rhodamine B. The results demonstrate that ion implantation significantly reduces surface resistivity and enhances both the photocatalytic activity and humidity sensitivity of GO and PI. The most pronounced improvements occurred at higher fluences, where defect generation and partial deoxygenation contributed to optimal performance. Ion implantation thus represents an effective approach for tuning the multifunctional behavior of polymer systems.

   **Comment**: No dataset

---

64. **Data Grids for examples in Probe Particle Atomic Force Microscopy simulation program (ppafm)**

   - **DOI**: 10.5281/zenodo.14222456
   - **URL**: [https://doi.org/10.5281/zenodo.14222456](https://doi.org/10.5281/zenodo.14222456)
   - **Date**: 2024-11-26
   - **Access**: open
   - **License**: CC BY 4.0
   - **By**: Hapala, Prokop
   - **Desc**: These files are used for running the examples for [ppafm](https://github.com/Probe-Particle/ppafm/) program. The grids are stored in in [.xsf](http://www.xcrysden.org/doc/XSF.html) and [.cube](https://paulbourke.net/dataformats/cube/) format. The data set compiles both the new examples used in paper [Advancing scanning probe microscopy simulations: A decade of development in probe-particle models](https://www.sciencedirect.com/science/article/pii/S0010465524002649) as well as older examples. Notice that the structure does not exactly reflect the directory structure in the [example folder of ppafm](https://github.com/Probe-Particle/ppafm/tree/main/examples) to prevent possible redudancy, but is instead flatenized and sorted by molecules.

   **Comment**: Most probably simulation data, there are some other unknown dataset, and probably some .spm data from bruker

---

67. **RAW data - Boric acid modified polydopamine and nanocolumnar hydrogenated TiO2 nanocomposite with improved photocatalytic performance. Appl. Surf. Sci. 2025, 686, 162118. DOI: 10.1016/j.apsusc.2024.162118 - AFM - ICONBruker - CNBM UAM - BAPDA/H:TiO2**

   - **DOI**: 10.5281/zenodo.13756858
   - **URL**: [https://doi.org/10.5281/zenodo.13756858](https://doi.org/10.5281/zenodo.13756858)
   - **Date**: 2024-09-13
   - **Access**: open
   - **License**: CC BY 4.0
   - **By**: Szewczyk, Jakub
   - **Desc**: This repository contains RAW data for the experiment described in the publication: Jakub Szewczyk, Tim Tjardts, Fabian Symalla, Igor Iatsunskyi, Franz Faupel, Cenk Aktas, Emerson Coy, Salih Veziroglu, Boric acid modified polydopamine and nanocolumnar hydrogenated TiO2 nanocomposite with improved photocatalytic performance. Applied Surface Science 2025, 686, 162118. The remaining data supporting this study's findings are available from the corresponding author upon reasonable request. The raw AFM data is posted here in the open-access model.

   **Comment**: No dataset

---

---

# Creative Commons License Reference

Creative Commons (CC) licenses are built from four elements — **BY** (Attribution), **SA** (ShareAlike), **NC** (NonCommercial), **ND** (NoDerivatives) — combined into the seven licenses below, ranging from most to least permissive.

| License | Full Name | Commercial Use | Derivatives | Share-Alike Required |
|---------|-----------|:--------------:|:-----------:|:--------------------:|
| **CC0** | Public Domain Dedication | ✅ | ✅ Any | ❌ |
| **CC BY 4.0** | Attribution 4.0 International | ✅ | ✅ Any | ❌ |
| **CC BY-SA 4.0** | Attribution-ShareAlike 4.0 | ✅ | ✅ Must use same license | ✅ |
| **CC BY-NC 4.0** | Attribution-NonCommercial 4.0 | ❌ | ✅ Any | ❌ |
| **CC BY-NC-SA 4.0** | Attribution-NonCommercial-ShareAlike 4.0 | ❌ | ✅ Must use same license | ✅ |
| **CC BY-ND 4.0** | Attribution-NoDerivatives 4.0 | ✅ | ❌ (only verbatim copies) | ❌ |
| **CC BY-NC-ND 4.0** | Attribution-NonCommercial-NoDerivatives 4.0 | ❌ | ❌ (only verbatim copies) | ❌ |

## Description of Each License

**CC0 (Public Domain Dedication)**
The creator waives all copyright. Anyone can copy, modify, distribute, and perform the work, even for commercial purposes, without asking permission. Commonly used for datasets where maximum reuse is desired.

**CC BY 4.0 — Attribution**
The most permissive CC license with a copyright. You may share and adapt the material for any purpose, including commercially, as long as you give appropriate credit to the original author, link to the license, and indicate if changes were made.

**CC BY-SA 4.0 — Attribution-ShareAlike**
Same as CC BY, but any derivative work must be distributed under the identical license. This "copyleft" clause ensures the open nature propagates to all derivatives. Used by Wikipedia.

**CC BY-NC 4.0 — Attribution-NonCommercial**
Share and adapt freely, but only for non-commercial purposes. Commercial use requires separate permission from the rights holder. Common in academic datasets where authors want to prevent commercial exploitation.

**CC BY-NC-SA 4.0 — Attribution-NonCommercial-ShareAlike**
Combines NC and SA restrictions: non-commercial use only, and derivatives must carry the same license. The most restrictive license still permitting adaptation.

**CC BY-ND 4.0 — Attribution-NoDerivatives**
You may redistribute the work commercially or non-commercially, but you must share it verbatim — no remixing, transforming, or building upon it. Commonly used when authors want wide distribution but full control over the integrity of the work.

**CC BY-NC-ND 4.0 — Attribution-NonCommercial-NoDerivatives**
The most restrictive CC license. Only verbatim, non-commercial redistribution with credit is allowed. No derivatives, no commercial use. Sometimes called "download and share only."

## Which License Is Best for Research Data?

For open scientific datasets intended for reuse and reproducibility, **CC BY 4.0** or **CC0** are recommended by most data repositories (including Zenodo). Both allow other researchers to download, reuse, and build upon the data in publications and tools.

> **Note:** Most Zenodo datasets in this investigation use **CC BY 4.0** as the default open license.
