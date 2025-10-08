# Scanning Probe Microscopy (SPM)

Scanning Probe Microscopy (SPM) is a high resolution imaging technique used to study material surface at nano scale. The technique can take on a wide range form of experiments catagorized by operating environment (e.g., ambient, valcuum) and setup, type of interaction between prob and specimen, number of probe and actuation modes, etc. Therfore, there are many subteniques, like STM (Scanning Tunneling Microscopy), AFM (Atomic Force Microscopy), STS (Scanning Probe Spectroscopy). Thses complex experiments require complex setup of instruments provided by different technology companies which turns out diverse data model (mostly unstructured) and data format. How can we compare the diversed data model and data format? Can we interprete the data in a common data model and format accessible to all SPM community? Does the proposed data model follow FAIR data principle?

We have developed community driven standard application definition, using NeXus[link_goes_here] data format, for SPM[link_goes_here] subdomains e.g., STM[link_goes here], STS[link_goes_here], AFM[link_goes_here] and a few base classes to describe instrument components (e.g. Lock-in[link-goes-here], Cantilever[link-goes-here]). Based on our data model, we build the data workflow that connects the data from experiment generated raw files to the standard application definition inscribed in a HDF5 file (as we are using NeXus data format in HDF5 file, later on we also call it NeXus file with '.nxs' extension).
TODO: mention one can use `NXspm` for any sub technique do not warranty the validataion of the parsed data.

## __SPM Readers__
The SPM reader(s) is plugin of material science reader framwork `pynxtools`[`link_goes_here`] and anchors a bundle of readers from STM, STS and AFM. The prime purpose of the readers is to transform data from measurement files into by the SPM community supported schema (NeXus applications and base classes) which allows experimentalists to store, organize, search, analyze, and share experimental data in NOMAD (as plugin `pynxtools-spm` is integrated with [NOMAD](https://nomad-lab.eu/nomad-lab/)) research data management (RDM) platform. 

The SPM reader is plugin of material science reader framwork `pynxtools`[`link_goes_here`] and anchors a bundle of readers from STM, STS and AFM. The readers follow a [common structure](link_to_common_code_structure) that shall allow to extend reader orchestra by including new readers of different SPM subtechnique (e.g. SPSTM). For each type of techniques (e.g., STM, STS, and AFM), there might be multiple vendors (e.g., Nanonis, Omicron) and each vendor favors different data format and data model. Therefore, each reader is designed to be modular and configurable to adapt different data format and data model. These allows to integrate more and more data format and data model from different vendors without changing the reader structure.


To understand the reader structure, one might start understanding the design pattern of the application degintions `NXspm[link_goes_here]`, `NXstm[link_goes_here]`, `NXsts[link_goes_here]`, and `NXafm[link_goes_here]` on the [FAIRmat NeXus Proposal](https://fairmat-nfdi.github.io/nexus_definitions/) page or in the [GitHub repository].

### __Reader Members of `pynxtools-spm` reader orchestra__
`pynxtools-spm` includes three readers:

- STS reader
- STM reader
- AFM reader

The `section`, `sub_sections`, and `quantities` refer to the root level entitiy (behaves like a `group`), `group`, and `field` of the NeXus definition, respectively. The given schema ELN can be read as follows, `stm` ELN has direct fields `default`, `definition` and direct groups `Instrument`, `Sample`, with each group optionally containing nested `group`s and `field`s.

This type of ELN needs to be used if the reader is run from the command line. To know which fields and groups refer to which type of data, one needs to read the NeXus definition on the [FAIRmat NeXus Proposal](https://fairmat-nfdi.github.io/nexus_definitions/classes/contributed_definitions/NXsts.html#nxsts) page or in the [GitHub repository](https://github.com/FAIRmat-NFDI/nexus_definitions/blob/fairmat/contributed_definitions/NXsts.nxdl.xml).


#### __STS reader__

The `STS` reader builds on the [NXsts](link from nexus-fairmat page) application definition and needs an experimental file, a config file and a eln (eln stands for electronic lab notebook) file to transform the experiment generated data (from raw files) and user provided data (from ELN) into NeXus file [NXsts](link from nexus-fairmat page) according to the application concepts.

#### __STM Reader__
The STM reader is a part of `pynxtools-spm` package and builds on the [NXstm](link from nexus-fairmat page) application definition and needs an experimental file, a config file and a eln (eln stands for electronic lab notebook) file to transform the experiment generated data (from raw files) and user provided data (from ELN) into NeXus file according to the [NXstm](link from nexus-fairmat page) application concepts.

#### __AFM Reader__
The AFM reader is a part of `pynxtools-spm` package and builds on the [NXafm](link from nexus-fairmat page) application definition and needs an experimental file, a config file and a eln (eln stands for electronic lab notebook) file to transform the experiment generated data (from raw files) and user provided data (from ELN) into NeXus file according to the [NXafm](link from nexus-fairmat page) application concepts.

!!! Warning 
  The config file is a map from the data model of raw file to the data model inscribed in correspoding application definition, which infers raw files from different software version or different vendor require different config files. Most likely, the path is path to the raw data file needs to be updated in the config file. 

### __Supported Vendor files and Formats__
Readers support the following vendor files and formats.

- __STS__
    - Nanonis `STS` files
        - Extension: `.dat`
- __STM__
    - Nanonis `STM` files
        - Extension: `.sxm`
    - Omicron `STM` files
        - Extension: `.sm4`
- __AFM__
    - Nanonis `AFM` files
        - Extension: `.sxm`

### __Input files__
The readers mainly need three input files to transform the data into the `NXsts`, `NXstm`, and `NXafm` application definitions for `STS`, `STM`, and `AFM` techniques, respectively. The three input files are - 

#### __Experimental file__ 
The experimental file is the raw data file generated by the instrument software e.g., (`.dat` for Nanonis `STS` files).

#### __Config file__ 
The config file is a `json` file which maps between the data model (unstructure data) of the raw data file and the data model inscribed in the (e.g., `NXsts`) application definition. Note that, as a intermediate step the corresponding parser generates a data object (e.g., Python dictionary) developing slash separated string key mapping to the value. In the config file, the key string path is used as a path refering the data in raw file. To know how to read this config file and modify it, please follow `Config File` in  [Work with Reader](../how-to-guides/how-to-act-with-reader.md) guide.

=== "Config File Nanonis (STS)"
    <div class="scrollable">
    ```json
    {
        "ENTRY[entry]": {
            "@default": { "raw_path": "@default:current_filter" },
            "definition": { "@version": "" },
            "start_time": {
            "raw_path": "/Start time/value"
            },
            "end_time": {
            "raw_path": "/Saved Date/value"
            },
            "INSTRUMENT[instrument]": {
            "lockin_amplifier": {
                "modulation_status": {
                "raw_path": "/Lock-in/Lock-in status/value"
                },
                "reference_frequency": {
                "raw_path": "/Lock-in/Frequency/value",
                "@units": "/Lock-in/Frequency/unit"
                },
                "modulation_signal": {
                "raw_path": "@default:Current"
                },
                "demodulated_signal": {
                "raw_path": "@default:Current"
                },
                "reference_amplitude": {
                "raw_path": "/Lock-in/Amplitude/value",
                "@units": "/Lock-in/Modulated signal/Bias/unit"
                },
                "demodulated_frequency": "",
                "demodulated_amplitude": "",
                "demodulator_channels": "",
                "recorded_channels": "",
                "active_channel": {
                "raw_path": ""
                },
                "flip_sign": "",
                "low_passN": [
                {
                    "d1": {
                    "raw_path": "/Lock-in/LP Filter Cutoff D1/value",
                    "@units": "/Lock-in/LP Filter Cutoff D1/unit"
                    }
                },
                {
                    "d2": {
                    "raw_path": "/Lock-in/LP Filter Cutoff D2/value",
                    "@units": "/Lock-in/LP Filter Cutoff D2/unit"
                    }
                }
                ],
                "lp_filter_orderN": [
                {
                    "d1": { "raw_path": "/Lock-in/LP Filter Order D1/value" },
                    "d2": { "raw_path": "/Lock-in/LP Filter Order D2/value" }
                }
                ],
                "high_passN": [
                {
                    "d1": {
                    "raw_path": "/Lock-in/HP Filter Cutoff D1/value",
                    "@units": "/Lock-in/HP Filter Cutoff D1/unit"
                    }
                },
                {
                    "d2": {
                    "raw_path": "/Lock-in/HP Filter Cutoff D2/value",
                    "@units": "/Lock-in/HP Filter Cutoff D2/unit"
                    }
                }
                ],
                "hp_filter_orderN": [
                { "d1": { "raw_path": "/Lock-in/HP Filter Order D1/value" } },
                { "d2": { "raw_path": "/Lock-in/HP Filter Order D2/value" } }
                ],
                "ref_offset_phaseN[ref_offset_phase_n]": [
                {
                    "d1": {
                    "raw_path": "/Lock-in/Reference phase D1/value",
                    "@units": "/Lock-in/Reference phase D1/unit"
                    }
                },
                {
                    "d2": {
                    "raw_path": "/Lock-in/Reference phase D2/value",
                    "@units": "/Lock-in/Reference phase D2/unit"
                    }
                }
                ],
                "harmonic_orderN[harmonic_order_n]": [
                { "d1": { "raw_path": "/Lock-in/Harmonic D1/value" } },
                { "d2": { "raw_path": "/Lock-in/Harmonic D2/value" } }
                ],
                "dc_offset_valueN": [
                {
                    "d1": {
                    "raw_path": "",
                    "@units": ""
                    }
                },
                {
                    "d2": {
                    "raw_path": "",
                    "@units": ""
                    }
                }
                ]
            },
            "real_time_controller": {
                "fabrication": {
                "model": {
                    "raw_path": "/NanonisMain/RT Release/value"
                }
                },
                "frequency": {
                "raw_path": "/NanonisMain/RT Frequency/value",
                "@units": "/NanonisMain/RT Frequency/unit"
                },
                "acquisition_time": {
                "raw_path": "/NanonisMain/Acquisition Period/value",
                "@units": "/NanonisMain/Acquisition Period/unit"
                },
                "animation_time": {
                "raw_path": "/NanonisMain/Animations Period/value",
                "@units": "/NanonisMain/Animations Period/unit"
                },
                "measurement_time": {
                "raw_path": "/NanonisMain/Measurements Period/value",
                "@units": "/NanonisMain/Measurements Period/unit"
                },
                "indication_time": {
                "raw_path": "/NanonisMain/Indicators Period/value",
                "@units": "/NanonisMain/Indicators Period/unit"
                }
            },
            "bias_spectroscopy_environment": {
                "SPM_BIAS_SPECTROSCOPY[bias_spectroscopy]": {
                "measurement_type": "",
                "SPM_POSITIONER[spm_positioner]": {
                    "z_controller": {
                    "feedback_on": {
                        "raw_path": "/Z-Controller/Controller status/value"
                    },
                    "set_point": {
                        "raw_path": "/Z-Controller/Setpoint/value",
                        "@units": "/Z-Controller/Setpoint unit/value"
                    },
                    "tip_lift": {
                        "raw_path": "/Z-Controller/TipLift/value",
                        "@units": "/Z-Controller/TipLift/unit"
                    },
                    "z": {
                        "raw_path": "/Z-Controller/Z/value",
                        "@units": "/Z-Controller/Z/unit"
                    },
                    "K_i": {
                        "raw_path": "/Z-Controller/I gain/value"
                    },
                    "K_p": {
                        "raw_path": "/Z-Controller/P gain/value"
                    },
                    "D_t": {
                        "raw_path": "/Z-Controller/Time const/value",
                        "@units": "/Z-Controller/Time const/unit"
                    },
                    "controller_label": {
                        "raw_path": "/Z-Controller/Controller name/value"
                    },
                    "z_offset_value": {
                        "raw_path": "/Bias Spectroscopy/Z offset/value",
                        "@units": "/Bias Spectroscopy/Z offset/unit"
                    }
                    }
                },
                "BIAS_SWEEP[bias_sweep]": {
                    "#note": "This group will be handled in _construct_bias_sweep_grp.",
                    "scan_type": "",
                    "settling_time": {
                    "raw_path": "/Bias Spectroscopy/Settling time/value",
                    "@units": "/Bias Spectroscopy/Settling time/unit"
                    },
                    "first_settling_time": {
                    "raw_path": "/Bias Spectroscopy/1st Settling time/value",
                    "@units": "/Bias Spectroscopy/1st Settling time/unit"
                    },
                    "end_settling_time": {
                    "raw_path": "/Bias Spectroscopy/End Settling time/value",
                    "@units": "/Bias Spectroscopy/End Settling time/unit"
                    },
                    "max_slew_rate": {
                    "raw_path": "/Bias Spectroscopy/Max Slew rate/value",
                    "@units": "/Bias Spectroscopy/Max Slew rate/unit"
                    },
                    "final_z": "",
                    "total_spectroscopy_time": "",
                    "number_of_sweeps": {
                    "raw_path": "/Bias Spectroscopy/Number of sweeps/value"
                    },
                    "scan_region": {
                    "scan_range_bias": "",
                    "scan_offset_bias": {
                        "raw_path": ["/Bias/Offset/value"],
                        "@units": "/Bias/Offset/unit"
                    },
                    "scan_angleN[scan_angle_n]": "",
                    "scan_start_bias": {
                        "raw_path": "/Bias Spectroscopy/Sweep Start/value",
                        "@units": "/Bias Spectroscopy/Sweep Start/unit"
                    },
                    "scan_end_bias": {
                        "raw_path": "/Bias Spectroscopy/Sweep End/value",
                        "@units": "/Bias Spectroscopy/Sweep End/unit"
                    }
                    },
                    "linear_sweep": {
                    "scan_speed": "",
                    "scan_time": "",
                    "forward_speedN[forward_speed]": {
                        "raw_path": "/Scan/speed forw./value",
                        "@units": "/Scan/speed forw./unit"
                    },
                    "backward_speedN[backward_speed]": {
                        "raw_path": "/Scan/speed backw./value",
                        "@units": "/Scan/speed backw./unit"
                    },
                    "scan_points_bias": {
                        "raw_path": "/Bias Spectroscopy/Num Pixel/value"
                    },
                    "step_size_bias": "",
                    "reset_bias": "",
                    "backward_sweep": "",
                    "DATA[scan_data]": [
                        {
                        "data": {
                            "name": "current",
                            "raw_path": "/dat_mat_components/LI Demod 1 X/value",
                            "@units": "/dat_mat_components/LI Demod 1 X/unit",
                            "@long_name": "Lockin Demod 1X"
                        },
                        "0": {
                            "name": "voltage",
                            "raw_path": [
                            "/dat_mat_components/Bias calc/value",
                            "/dat_mat_components/Bias/value"
                            ],
                            "@units": [
                            "/dat_mat_components/Bias calc/unit",
                            "/dat_mat_components/Bias/unit"
                            ],
                            "@long_name": "Bias Voltage"
                        },
                        "title": { "raw_path": "@default:Lockin Signal 1X" },
                        "grp_name": "Lockin Demod 1X"
                        },
                        {
                        "data": {
                            "name": "Lockin Demod 1Y",
                            "raw_path": "/dat_mat_components/LI Demod 1 Y/value",
                            "@units": "/dat_mat_components/LI Demod 1 Y/unit"
                        },
                        "0": {
                            "name": "Bias Voltage",
                            "raw_path": [
                            "/dat_mat_components/Bias calc/value",
                            "/dat_mat_components/Bias/value"
                            ],
                            "@units": [
                            "/dat_mat_components/Bias calc/unit",
                            "/dat_mat_components/Bias/unit"
                            ]
                        },
                        "title": { "raw_path": "@default:Lockin Signal 1Y" },
                        "grp_name": "Lockin Demod 1Y"
                        },
                        {
                        "data": {
                            "name": "Lockin Demod 2X",
                            "raw_path": "/dat_mat_components/LI Demod 2 X/value",
                            "@units": "/dat_mat_components/LI Demod 2 X/unit"
                        },
                        "0": {
                            "name": "Bias Voltage",
                            "raw_path": [
                            "/dat_mat_components/Bias calc/value",
                            "/dat_mat_components/Bias/value"
                            ],
                            "@units": [
                            "/dat_mat_components/Bias calc/unit",
                            "/dat_mat_components/Bias/unit"
                            ]
                        },
                        "title": { "raw_path": "@default:Lockin Signal 2X" },
                        "grp_name": "Lockin Demod 2X"
                        },
                        {
                        "data": {
                            "name": "Lockin Demod 2Y",
                            "raw_path": "/dat_mat_components/LI Demod 2 Y/value",
                            "@units": "/dat_mat_components/LI Demod 2 Y/unit"
                        },
                        "0": {
                            "name": "Bias Voltage",
                            "raw_path": [
                            "/dat_mat_components/Bias calc/value",
                            "/dat_mat_components/Bias/value"
                            ],
                            "@units": [
                            "/dat_mat_components/Bias calc/unit",
                            "/dat_mat_components/Bias/unit"
                            ]
                        },
                        "title": { "raw_path": "@default:Lockin Signal 2Y" },
                        "grp_name": "Lockin Demod 2Y"
                        },
                        {
                        "data": {
                            "name": "Lockin Demod 1X_filter",
                            "raw_path": "/dat_mat_components/LI Demod 1 X [filt]/value",
                            "@units": "/dat_mat_components/LI Demod 1 X [filt]/unit"
                        },
                        "0": {
                            "name": "Bias Voltage",
                            "raw_path": [
                            "/dat_mat_components/Bias [filt]/value",
                            "/dat_mat_components/Bias calc/value",
                            "/dat_mat_components/Bias/value"
                            ],
                            "@units": [
                            "/dat_mat_components/Bias calc/unit",
                            "/dat_mat_components/Bias/unit"
                            ]
                        },
                        "title": { "raw_path": "@default:Lockin Demod 1X(filter)" },
                        "grp_name": "Lockin_Demod_1X_filter"
                        },
                        {
                        "data": {
                            "name": "Lockin Demod 1Y_filter",
                            "raw_path": "/dat_mat_components/LI Demod 1 Y [filt]/value",
                            "@units": "/dat_mat_components/LI Demod 1 Y [filt]/unit"
                        },
                        "0": {
                            "name": "Bias Voltage",
                            "raw_path": [
                            "/dat_mat_components/Bias [filt]/value",
                            "/dat_mat_components/Bias calc/value",
                            "/dat_mat_components/Bias/value"
                            ],
                            "@units": [
                            "/dat_mat_components/Bias calc/unit",
                            "/dat_mat_components/Bias/unit"
                            ]
                        },
                        "title": { "raw_path": "@default:Lockin Demod 1Y(filter)" },
                        "grp_name": "Lockin_Demod_1Y_filter"
                        },
                        {
                        "data": {
                            "name": "Lockin Demod 2X_filter",
                            "raw_path": "/dat_mat_components/LI Demod 2 X [filt]/value",
                            "@units": "/dat_mat_components/LI Demod 2 X [filt]/unit"
                        },
                        "0": {
                            "name": "Bias Voltage",
                            "raw_path": [
                            "/dat_mat_components/Bias [filt]/value",
                            "/dat_mat_components/Bias calc/value",
                            "/dat_mat_components/Bias/value"
                            ],
                            "@units": [
                            "/dat_mat_components/Bias calc/unit",
                            "/dat_mat_components/Bias/unit"
                            ]
                        },
                        "title": { "raw_path": "@default:Lockin Demod 2X(filter)" },
                        "grp_name": "Lockin_Demod_2X_filter"
                        },
                        {
                        "data": {
                            "name": "Lockin Demod 2Y_filter",
                            "raw_path": "/dat_mat_components/LI Demod 2 Y [filt]/value",
                            "@units": "/dat_mat_components/LI Demod 2 Y [filt]/unit"
                        },
                        "0": {
                            "name": "Bias Voltage",
                            "raw_path": [
                            "/dat_mat_components/Bias [filt]/value",
                            "/dat_mat_components/Bias calc/value",
                            "/dat_mat_components/Bias/value"
                            ],
                            "@units": [
                            "/dat_mat_components/Bias calc/unit",
                            "/dat_mat_components/Bias/unit"
                            ]
                        },
                        "title": { "raw_path": "@default:Lockin Demod 2Y(filter)" },
                        "grp_name": "Lockin_Demod_2Y_filter"
                        }
                    ]
                    }
                },
                "CIRCUIT[circuit]": ""
                },
                "independent_controllers": "",
                "measurement_sensors": ""
            },
            "current_sensorTAG[current_sensor]": {
                "current": {
                "raw_path": "/Current/Current/value",
                "@units": "/Current/Current/unit"
                },
                "calibration": {
                "calibration_parameters": {
                    "coefficient": {
                    "raw_path": "/Current/Calibration/value",
                    "@units": "/Current/Calibration/unit"
                    }
                }
                },
                "offset_value": {
                "raw_path": "/Current/Offset/value",
                "@units": "/Current/Offset/unit"
                },
                "AMPLIFIER[amplifier]": {
                "current_gain": { "raw_path": "" }
                }
            },
            "piezo_sensor": {
                "piezo_configuration": {
                "calibration": {
                    "calibration_type": {
                    "raw_path": "@default:active"
                    },
                    "calibration_date": {
                    "raw_path": ""
                    },
                    "rangeN[range_n]": { "x": "", "y": "", "z": "" },
                    "calibration_parameters": {
                    "coefficientN[coefficient_n]": [
                        {
                        "x": {
                            "raw_path": "/Piezo Configuration/Calib. X/value",
                            "@units": "/Piezo Configuration/Calib. X/unit"
                        }
                        },
                        {
                        "y": {
                            "raw_path": "/Piezo Configuration/Calib. Y/value",
                            "@units": "/Piezo Configuration/Calib. Y/unit"
                        }
                        },
                        {
                        "z": {
                            "raw_path": "/Piezo Configuration/Calib. Z/value",
                            "@units": "/Piezo Configuration/Calib. Z/unit"
                        }
                        }
                    ],
                    "second_order_correctionN[second_order_correction_n]": [
                        {
                        "x": {
                            "raw_path": "/Piezo Configuration/2nd order corr X/value",
                            "@units": "/Piezo Configuration/2nd order corr X/unit"
                        }
                        },
                        {
                        "y": {
                            "raw_path": "/Piezo Configuration/2nd order corr Y/value",
                            "@units": "/Piezo Configuration/2nd order corr Y/unit"
                        }
                        }
                    ]
                    },
                    "driftN[drift_n]": [
                    {
                        "x": {
                        "raw_path": "/Piezo Configuration/Drift X/value",
                        "@units": "/Piezo Configuration/Drift X/unit"
                        }
                    },
                    {
                        "y": {
                        "raw_path": "/Piezo Configuration/Drift Y/value",
                        "@units": "/Piezo Configuration/Drift Y/unit"
                        }
                    },
                    {
                        "z": {
                        "raw_path": "/Piezo Configuration/Drift Z/value",
                        "@units": "/Piezo Configuration/Drift Z/unit"
                        }
                    }
                    ],
                    "hv_gainN[hv_gain_n]": [
                    { "x": { "raw_path": "/Piezo Configuration/HV Gain X/value" } },
                    { "y": { "raw_path": "/Piezo Configuration/HV Gain Y/value" } },
                    { "z": { "raw_path": "/Piezo Configuration/HV Gain Z/value" } }
                    ],
                    "tiltN[tilt_n]": [
                    {
                        "x": {
                        "raw_path": "/Piezo Configuration/Tilt X/value",
                        "@units": "/Piezo Configuration/Tilt X/unit"
                        }
                    },
                    {
                        "y": {
                        "raw_path": "/Piezo Configuration/Tilt Y/value",
                        "@units": "/Piezo Configuration/Tilt Y/unit"
                        }
                    },
                    {
                        "z": {
                        "raw_path": "/Piezo Configuration/Tilt Z/value",
                        "@units": "/Piezo Configuration/Tilt Z/unit"
                        }
                    }
                    ],
                    "drift_correction_status": {
                    "raw_path": [
                        "/Piezo Configuration/Drift correction status/value",
                        "/Piezo Calibration/Drift correction status/value"
                    ]
                    }
                },
                "piezo_material": {
                    "curvature_radiusN": [
                    {
                        "x": {
                        "raw_path": "/Piezo Configuration/Curvature radius X/value",
                        "@units": "/Piezo Configuration/Curvature radius X/unit"
                        }
                    },
                    {
                        "y": {
                        "raw_path": "/Piezo Configuration/Curvature radius Y/value",
                        "@units": "/Piezo Configuration/Curvature radius Y/unit"
                        }
                    },
                    {
                        "z": {
                        "raw_path": "/Piezo Configuration/Curvature radius Z/value",
                        "@units": "/Piezo Configuration/Curvature radius Z/unit"
                        }
                    }
                    ]
                }
                },
                "SPM_POSITIONER[spm_positioner]": "",
                "x": { "raw_path": "/X/value", "@units": "/X/unit" },
                "y": { "raw_path": "/Y/value", "@units": "/Y/unit" },
                "z": { "raw_path": "/Z/value", "@units": "/Z/unit" },
                "AXISoffset_value[x_offset_value]": {
                "x": "",
                "y": "",
                "z": ""
                }
            },
            "sample_bias_voltage": {
                "bias_voltage": {
                "raw_path": "/Bias/Bias/value",
                "@units": "/Bias/Bias/unit"
                },
                "calibration": {
                "calibration_parameters": {
                    "coefficient": {
                    "raw_path": "/Bias/Calibration/value",
                    "@units": "/Bias/Calibration/unit"
                    }
                }
                }
            },
            "SCAN_ENVIRONMENT[scan_environment]": {
                "identifier_environment": {
                "raw_path": "/Scan/series name/value"
                },
                "cryo_bottom_temperature": { "@units": "" },
                "cryo_shield_temperature": { "@units": "" },
                "head_temperature": {
                "raw_path": "/Temperature 1/Temperature 1/value",
                "@units": "/Temperature 1/Temperature 1/unit"
                },
                "cryo_shield_temperature_sensor": "@default_link:/ENTRY[entry]/INSTRUMENT[instrument]/cryo_shield_temperature_sensor",
                "cryo_bottom_temperature_sensor": "@default_link:/ENTRY[entry]/INSTRUMENT[instrument]/cryo_bottom_temperature_sensor",
                "head_temperature_sensor": "@default_link:/ENTRY[entry]/INSTRUMENT[instrument]/head_temperature_sensor"
            },
            "cryo_shield_temperature_sensor": {
                "temp_offset_value": "",
                "TEMPERATUREchannel[temperature_channel]": "",
                "calibration": {
                "calibration_parameters": {
                    "coefficient": ""
                }
                },
                "temperature_calibration": { "coefficients": "" },
                "DATA[data]": ""
            },
            "cryo_bottom_temperature_sensor": {
                "temp_offset_value": "",
                "TEMPERATUREchannel[temperature_channel]": "",
                "calibration": {
                "calibration_parameters": {
                    "coefficient": ""
                }
                },
                "temperature_calibration": { "coefficients": "" },
                "DATA[data]": ""
            },
            "sample_temperature_sensor": {
                "temp_offset_value": "",
                "TEMPERATUREchannel[temperature_channel]": "",
                "calibration": {
                "calibration_parameters": {
                    "coefficient": ""
                }
                },
                "temperature_calibration": { "coefficients": "" },
                "DATA[data]": ""
            },
            "head_temperature_sensor": {
                "temp_offset_value": "",
                "TEMPERATUREchannel[temperature_channel]": "",
                "calibration": {
                "calibration_parameters": {
                    "coefficient": ""
                }
                },
                "temperature_calibration": { "coefficients": "" },
                "DATA[data]": [
                {
                    "data": {
                    "name": "temperature1",
                    "raw_path": "/dat_mat_components/Temperature 1/value",
                    "@units": "/dat_mat_components/Temperature 1/unit"
                    },
                    "0": {
                    "name": "Bias Voltage",
                    "raw_path": [
                        "/dat_mat_components/Bias calc/value",
                        "/dat_mat_components/Bias/value"
                    ],
                    "@units": [
                        "/dat_mat_components/Bias calc/unit",
                        "/dat_mat_components/Bias/unit"
                    ],
                    "axis_ind": 0
                    },
                    "title": { "raw_path": "@default:Bias Spectroscopy Temperature1" },
                    "grp_name": "temperature1"
                },
                {
                    "data": {
                    "name": "temperature1_filter",
                    "raw_path": "/dat_mat_components/Temperature 1 [filt]/value",
                    "@units": "/dat_mat_components/Temperature 1 [filt]/unit"
                    },
                    "0": {
                    "name": "Bias Voltage",
                    "raw_path": [
                        "/dat_mat_components/Bias calc/value",
                        "/dat_mat_components/Bias/value"
                    ],
                    "@units": [
                        "/dat_mat_components/Bias calc/unit",
                        "/dat_mat_components/Bias/unit"
                    ],
                    "axis_ind": 0
                    },
                    "title": {
                    "raw_path": "@default:Bias Spectroscopy Temperature1(filter)"
                    },
                    "grp_name": "temperature1_filter"
                }
                ]
            }
            },
            "DATA[data]": [
            {
                "data": {
                "name": "Current",
                "raw_path": "/dat_mat_components/Current/value",
                "@units": "/dat_mat_components/Current/unit"
                },
                "0": {
                "name": "Bias Voltage",
                "raw_path": [
                    "/dat_mat_components/Bias calc/value",
                    "/dat_mat_components/Bias/value"
                ],
                "@units": [
                    "/dat_mat_components/Bias calc/unit",
                    "/dat_mat_components/Bias/unit"
                ]
                },
                "title": { "raw_path": "@default:Bias Spectroscopy" },
                "grp_name": "current"
            },
            {
                "data": {
                "name": "Current_filter",
                "raw_path": "/dat_mat_components/Current [filt]/value",
                "@units": "/dat_mat_components/Current [filt]/unit"
                },
                "0": {
                "name": "Bias Voltage",
                "raw_path": [
                    "/dat_mat_components/Bias [filt]/value",
                    "/dat_mat_components/Bias calc/value",
                    "/dat_mat_components/Bias/value"
                ],
                "@units": [
                    "/dat_mat_components/Bias calc/unit",
                    "/dat_mat_components/Bias/unit"
                ],
                "axis_ind": 0
                },
                "title": { "raw_path": "@default:Bias Spectroscopy(filter)" },
                "grp_name": "Current_filter"
            },
            {
                "data": {
                "name": "Current_filter",
                "raw_path": "/dat_mat_components/Current [filt]/value",
                "@units": "/dat_mat_components/Current [filt]/unit"
                },
                "0": {
                "name": "Bias Voltage",
                "raw_path": [
                    "/dat_mat_components/Bias [filt]/value",
                    "/dat_mat_components/Bias calc/value",
                    "/dat_mat_components/Bias/value"
                ],
                "@units": [
                    "/dat_mat_components/Bias calc/unit",
                    "/dat_mat_components/Bias/unit"
                ]
                },
                "title": { "raw_path": "@default:Bias Spectroscopy(filter)" },
                "grp_name": "Current_filter"
            },
            {
                "data": {
                "name": "Current_backward",
                "raw_path": "/dat_mat_components/Current [bwd]/value",
                "@units": "/dat_mat_components/Current [bwd]/unit"
                },
                "0": {
                "name": "Bias Voltage",
                "raw_path": [
                    "/dat_mat_components/Bias [filt]/value",
                    "/dat_mat_components/Bias calc/value",
                    "/dat_mat_components/Bias/value"
                ],
                "@units": [
                    "/dat_mat_components/Bias calc/unit",
                    "/dat_mat_components/Bias/unit"
                ]
                },
                "title": { "raw_path": "@default:Bias Spectroscopy(Backward)" },
                "grp_name": "Current_Backward"
            }
            ],
            "reproducibility_indicators": {
            "current": "@default_link:/ENTRY[entry]/INSTRUMENT[instrument]/current_sensor/current",
            "current_gain": "@default_link:/ENTRY[entry]/INSTRUMENT[instrument]/current_sensor/AMPLIFIER[amplifier]/current_gain",
            "current_offset": "@default_link:/ENTRY[entry]/INSTRUMENT[instrument]/current_sensor/current_offset",
            "bias_sweep": "@default_link:/ENTRY[entry]/INSTRUMENT[instrument]/bias_spectroscopy_environment/BIAS_SPECTROSCOPY[bias_spectroscopy]/BIAS_SWEEP[bias_sweep]",
            "reference_frequency": "@default_link:/ENTRY[entry]/INSTRUMENT[instrument]/lockin_amplifier/reference_frequency",
            "modulation_signal": "@default_link:/ENTRY[entry]/INSTRUMENT[instrument]/lockin_amplifier/modulation_signal"
            },
            "resolution_indicators": {
            "head_temperature": "@default_link:/ENTRY[entry]/INSTRUMENT[instrument]/scan_environment/head_temperature",
            "cryo_bottom_temperature": "@default_link:/ENTRY[entry]/INSTRUMENT[instrument]/scan_environment/cryo_bottom_temperature",
            "cryo_shield_temperature": "@default_link:/ENTRY[entry]/INSTRUMENT[instrument]/scan_environment/cryo_shield_temperature",
            "bias_sweep": "@default_link:/ENTRY[entry]/INSTRUMENT[instrument]/bias_spectroscopy_environment/BIAS_SPECTROSCOPY[bias_spectroscopy]/BIAS_SWEEP[bias_sweep]",
            "reference_frequency": "@default_link:/ENTRY[entry]/INSTRUMENT[instrument]/lockin_amplifier/reference_frequency",
            "modulation_signal": "@default_link:/ENTRY[entry]/INSTRUMENT[instrument]/lockin_amplifier/modulation_signal"
            }
        }
    }
    ```
    </div>
=== "Config File Nanonis (STM)"
    <div class="scrollable">
    ```json
    {
        "ENTRY[entry]": {
            "@default": { "raw_path": "@default:current_backward" },
            "identifier_collection": "",
            "start_time": {
            "#note": "Handled in function _set_start_end_time"
            },
            "end_time": {
            "#note": "Handled in function _set_start_end_time"
            },
            "scan_mode": "",
            "scan_type": "",
            "experiment_description": { "raw_path": "/COMMENT" },
            "INSTRUMENT[instrument]": {
            "SCAN_ENVIRONMENT[scan_environment]": {
                "head_temperature": {
                "raw_path": "/Temperature 1/Temperature 1",
                "@units": "@default:K"
                },
                "cryo_bottom_temperature": "",
                "cryo_shield_temperature": "",
                "identifier_environment": { "raw_path": "/Scan/series name" },
                "SPM_SCAN_CONTROL[spm_scan_control]": {
                "scanTAG[scan_name]": { "raw_path": "/Scan/series name" },
                "meshSCAN[mesh_scan]": {
                    "backward_speedN[backward_speed_n]": {
                    "#note": "Derived in construct_scan_pattern_grp",
                    "raw_path": "/Scan/speed backw.",
                    "@units": "/Scan/speed backw./@unit"
                    },
                    "forward_speedN[forward_speed_n]": {
                    "#note": "Derived in construct_scan_pattern_grp",
                    "raw_path": "/Scan/speed forw.",
                    "@units": "/Scan/speed forw./@unit"
                    },
                    "scan_speedN[scan_speed_n]": "",
                    "channelNAME[scan_name_n]": "",
                    "scan_pointsN[scan_points_n]": {
                    "#note": "Derived in construct_scan_pattern_grp",
                    "raw_path": "/SCAN/PIXELS",
                    "@units": ""
                    },
                    "steppingN[stepping_n]": [
                    {
                        "_x": {
                        "raw_path": "@default:1",
                        "@units": ""
                        }
                    },
                    {
                        "_y": {
                        "raw_path": "@default:1",
                        "@units": ""
                        }
                    }
                    ],
                    "step_sizeN[step_size_n]": [
                    { "x": { "raw_path": "", "@units": "" } },
                    { "y": { "raw_path": "", "@units": "" } }
                    ],
                    "scan_time": "",
                    "continuousN[continuous]": {
                    "raw_path": "@default:True"
                    }
                },
                "scan_region": {
                    "scan_angleN[scan_angle_n]": {
                    "raw_path": "/SCAN/ANGLE",
                    "@units": "@default:deg"
                    },
                    "scan_offset_valueN[scan_offset_value_n]": {
                    "#note": "Derived in function 'construct_scan_region_grp'.",
                    "raw_path": "/SCAN/OFFSET",
                    "@units": "/Z-Controller/Z/@unit"
                    },
                    "scan_rangeN[scan_range_n]": {
                    "#note": "Derived in function 'construct_scan_region_grp'.",
                    "raw_path": "/SCAN/RANGE",
                    "@units": "/Z-Controller/Z/@unit"
                    },
                    "scan_startN[scan_start_n]": {
                    "raw_path": "",
                    "@units": ""
                    },
                    "scan_endN[scan_end_n]": {
                    "raw_path": "",
                    "@units": ""
                    }
                },
                "scan_time_start": "",
                "scan_time_end": "",
                "independent_scan_axes": {
                    "#note": "Handled in function _construct_nxscan_controllers",
                    "raw_path": "/SCAN/DIR",
                    "@units": ""
                },
                "scan_resolutionN[scan_resolution_n]": "",
                "accuracyN[accuracy_n]": "",
                "scan_type": { "raw_path": "@default:mesh", "@units": "" },
                "scan_control_type": {
                    "raw_path": "@default:continuous",
                    "@units": ""
                }
                },
                "cryo_shield_temperature_sensor": "@default_link:/ENTRY[entry]/INSTRUMENT[instrument]/cryo_shield_temperature_sensor",
                "cryo_bottom_temperature_sensor": "@default_link:/ENTRY[entry]/INSTRUMENT[instrument]/cryo_bottom_temperature_sensor",
                "head_temperature_sensor": "@default_link:/ENTRY[entry]/INSTRUMENT[instrument]/head_temperature_sensor"
            },
            "voltage_sensorTAG[voltage_sensor]": {
                "voltage": {
                "raw_path": "",
                "@units": ""
                },
                "voltage_offset_value": {
                "raw_path": "",
                "@units": ""
                },
                "calibration": {
                "calibration_parameters": {
                    "coefficient": ""
                },
                "calibration_time": ""
                },
                "AMPLIFIER[amplifier]": {
                "voltage_gain": {
                    "raw_path": ""
                }
                }
            },
            "current_sensorTAG[current_sensor]": {
                "current": {
                "raw_path": "/Current/Current",
                "@units": "/Current/Current/@unit"
                },
                "offset_value": {
                "raw_path": "/Current/Offset",
                "@units": "/Current/Offset/@unit"
                },
                "calibration": {
                "calibration_parameters": {
                    "coefficient": {
                    "raw_path": "/Current/Calibration",
                    "@units": "/Current/Calibration/@unit"
                    }
                },

                "calibration_time": ""
                },
                "AMPLIFIER[amplifier]": {
                "current_gain": {
                    "raw_path": ""
                }
                }
            },
            "lockin_amplifier": {
                "reference_frequency": {
                "raw_path": "/Lock-in/Frequency",
                "@units": "@default:Hz"
                },
                "reference_amplitude": {
                "raw_path": "",
                "@units": ""
                },
                "reference_phase": {
                "raw_path": "",
                "@units": ""
                },
                "modulation_signal": {
                "raw_path": "/Lock-in/Modulated signal"
                },
                "demodulated_signal": {
                "raw_path": "/Lock-in/Demodulated signal"
                },
                "modulation_status": { "raw_path": "/Lock-in/Lock-in status" },
                "demodulated_frequency": "",
                "demodulated_amplitude": "",
                "demodulator_channels": "",
                "recorded_channels": "",
                "active_channel": {
                "raw_path": ""
                },
                "flip_sign": "",
                "low_passN": [
                {
                    "d1": {
                    "raw_path": "/Lock-in/LP Filter Cutoff D1",
                    "@units": "/Lock-in/LP Filter Cutoff D1/@unit"
                    }
                },
                {
                    "d2": {
                    "raw_path": "/Lock-in/LP Filter Cutoff D2",
                    "@units": "/Lock-in/LP Filter Cutoff D2/@unit"
                    }
                }
                ],
                "lp_filter_orderN": [
                {
                    "d1": { "raw_path": "" },
                    "d2": { "raw_path": "" }
                }
                ],
                "high_passN": [
                {
                    "d1": {
                    "raw_path": "/Lock-in/HP Filter Cutoff D1",
                    "@units": "/Lock-in/HP Filter Cutoff D1/@unit"
                    }
                },
                {
                    "d2": {
                    "raw_path": "/Lock-in/HP Filter Cutoff D2",
                    "@units": "/Lock-in/HP Filter Cutoff D2/@unit"
                    }
                }
                ],
                "hp_filter_orderN": [
                { "d1": { "raw_path": "" } },
                { "d2": { "raw_path": "" } }
                ],
                "ref_offset_phaseN[ref_offset_phase_n]": [
                {
                    "d1": {
                    "raw_path": "/Lock-in/Reference phase D1",
                    "@units": "/Lock-in/Reference phase D1/@unit"
                    }
                },
                {
                    "d2": {
                    "raw_path": "/Lock-in/Reference phase D2",
                    "@units": "/Lock-in/Reference phase D2/@unit"
                    }
                }
                ],
                "harmonic_orderN[harmonic_order_n]": [
                { "d1": { "raw_path": "/Lock-in/Harmonic D1" } },
                { "d2": { "raw_path": "/Lock-in/Harmonic D2" } }
                ],
                "dc_offset_valueN": [
                {
                    "d1": {
                    "raw_path": "",
                    "@units": ""
                    }
                },
                {
                    "d2": {
                    "raw_path": "",
                    "@units": ""
                    }
                }
                ]
            },
            "bias_spectroscopy_environment": {
                "SPM_BIAS_SPECTROSCOPY[spm_bias_spectroscopy]": {
                "measurement_type": "",
                "SPM_POSITIONER[spm_positioner]": {
                    "z_controller": {
                    "z_average_time": {
                        "raw_path": "/Bias Spectroscopy/Z Avg time",
                        "@units": "/Bias Spectroscopy/Z Avg time/@unit"
                    },
                    "z_controller_time": {
                        "raw_path": "/Bias Spectroscopy/Z control time",
                        "@units": "/Bias Spectroscopy/Z control time/@unit"
                    },
                    "z_controller_hold": {
                        "raw_path": "/Bias Spectroscopy/Z-controller hold"
                    },
                    "final_z": {
                        "raw_path": ""
                    },
                    "z_offset_value": {
                        "raw_path": "/Bias Spectroscopy/Z offset",
                        "@units": "/Bias Spectroscopy/Z offset/@unit"
                    }
                    }
                },
                "BIAS_SWEEP[bias_sweep]": {
                    "#note": "handled in _construct_bias_sweep_grp function",
                    "scan_type": "",
                    "settling_time": {
                    "raw_path": "/Bias Spectroscopy/Settling time",
                    "@units": "/Bias Spectroscopy/Settling time/@unit"
                    },
                    "first_settling_time": {
                    "raw_path": "/Bias Spectroscopy/1st Settling time",
                    "@units": "/Bias Spectroscopy/1st Settling time/@unit"
                    },
                    "end_settling_time": {
                    "raw_path": "/Bias Spectroscopy/End Settling time",
                    "@units": "/Bias Spectroscopy/End Settling time/@unit"
                    },
                    "max_slew_rate": {
                    "raw_path": "/Bias Spectroscopy/Max Slew rate",
                    "@units": "/Bias Spectroscopy/Max Slew rate/@unit"
                    },
                    "final_z": "",
                    "total_spectroscopy_time": "",
                    "sweep_number": {
                    "raw_path": "/Bias Spectroscopy/Number of sweeps"
                    },
                    "scan_region": {
                    "scan_range_bias": "",
                    "scan_offset_bias": {
                        "raw_path": "/Bias/Offset",
                        "@units": "/Bias/Offset/@unit"
                    },
                    "scan_angleN[scan_angle_n]": "",
                    "scan_start_bias": {
                        "raw_path": "/Bias Spectroscopy/Sweep Start",
                        "@units": "/Bias Spectroscopy/Sweep Start/@unit"
                    },
                    "scan_end_bias": {
                        "raw_path": "/Bias Spectroscopy/Sweep End",
                        "@units": "/Bias Spectroscopy/Sweep End/@unit"
                    }
                    },
                    "linear_sweep": {
                    "scan_speed": "",
                    "scan_time": "",
                    "forward_speedN[forward_speed]": "",
                    "backward_speedN[backward_speed]": "",
                    "scan_points_bias": {
                        "raw_path": "/Bias Spectroscopy/Num Pixel"
                    },
                    "step_size_bias": "",
                    "reset_bias": "",
                    "backward_sweep": {
                        "raw_path": "/Bias Spectroscopy/backward sweep"
                    },
                    "SCAN_DATA[scan_data]": ""
                    }
                },
                "CIRCUIT[circuit]": ""
                }
            },
            "height_piezo_sensor": {
                "piezo_configuration": {
                "calibration": {
                    "calibration_type": {
                    "raw_path": "@default:active"
                    },
                    "calibration_date": {
                    "raw_path": ""
                    },
                    "rangeN[range_n]": { "x": "", "y": "", "z": "" },
                    "calibratedAXIS[calibrated_n]": [
                    { "x": "" },
                    { "y": "" },
                    { "z": "" }
                    ],
                    "calibration_parameters": {
                    "coefficientN[coefficient_n]": [
                        {
                        "x": {
                            "raw_path": "/Piezo Configuration/Calib. X",
                            "@units": "/Piezo Configuration/Calib. X/@unit"
                        }
                        },
                        {
                        "y": {
                            "raw_path": "/Piezo Configuration/Calib. Y",
                            "@units": "/Piezo Configuration/Calib. Y/@unit"
                        }
                        },
                        {
                        "z": {
                            "raw_path": "/Piezo Configuration/Calib. Z",
                            "@units": "/Piezo Configuration/Calib. Z/@unit"
                        }
                        }
                    ],
                    "second_order_correctionN[second_order_correction_n]": [
                        {
                        "x": {
                            "raw_path": "/Piezo Configuration/2nd order corr X",
                            "@units": "/Piezo Configuration/2nd order corr X/@unit"
                        }
                        },
                        {
                        "y": {
                            "raw_path": "/Piezo Configuration/2nd order corr Y",
                            "@units": "/Piezo Configuration/2nd order corr Y/@unit"
                        }
                        },
                        {
                        "z": {
                            "raw_path": "/Piezo Configuration/2nd order corr Z",
                            "@units": "/Piezo Configuration/2nd order corr Z/@unit"
                        }
                        }
                    ]
                    },
                    "calibration_name": {
                    "raw_path": "/Piezo Configuration/Active Calib."
                    },
                    "driftN[drift_n]": [
                    {
                        "x": {
                        "raw_path": "/Piezo Configuration/Drift X",
                        "@units": "/Piezo Configuration/Drift X/@unit"
                        }
                    },
                    {
                        "y": {
                        "raw_path": "/Piezo Configuration/Drift Y",
                        "@units": "/Piezo Configuration/Drift Y/@unit"
                        }
                    },
                    {
                        "z": {
                        "raw_path": "/Piezo Configuration/Drift Z",
                        "@units": "/Piezo Configuration/Drift Z/@unit"
                        }
                    }
                    ],
                    "drift_correction_status": {
                    "raw_path": [
                        "/Piezo Configuration/Drift correction status",
                        "/Piezo Calibration/Drift correction status"
                    ]
                    },
                    "hv_gainN[hv_gain_n]": [
                    { "x": { "raw_path": "/Piezo Configuration/HV Gain X" } },
                    { "y": { "raw_path": "/Piezo Configuration/HV Gain Y" } },
                    { "z": { "raw_path": "/Piezo Configuration/HV Gain Z" } }
                    ],
                    "tiltN[tilt_n]": [
                    {
                        "x": {
                        "raw_path": "/Piezo Configuration/Tilt X",
                        "@units": "/Piezo Configuration/Tilt X/@unit"
                        }
                    },
                    {
                        "y": {
                        "raw_path": "/Piezo Configuration/Tilt Y",
                        "@units": "/Piezo Configuration/Tilt X/@unit"
                        }
                    },
                    {
                        "z": {
                        "raw_path": "/Piezo Configuration/Tilt Z",
                        "@units": "/Piezo Configuration/Tilt X/@unit"
                        }
                    }
                    ]
                },
                "piezo_material": {
                    "curvature_radiusN": [
                    {
                        "x": {
                        "raw_path": "/Piezo Configuration/Curvature radius X",
                        "@units": "/Piezo Configuration/Curvature radius X/@unit"
                        }
                    },
                    {
                        "y": {
                        "raw_path": "/Piezo Configuration/Curvature radius Y",
                        "@units": "/Piezo Configuration/Curvature radius Y/@unit"
                        }
                    },
                    {
                        "z": {
                        "raw_path": "/Piezo Configuration/Curvature radius Z",
                        "@units": "/Piezo Configuration/Curvature radius Z/@unit"
                        }
                    }
                    ]
                }
                },
                "SPM_POSITIONER[spm_positioner]": {
                "z_controller": {
                    "K_i": { "raw_path": "/Z-Controller/P gain" },
                    "K_p": { "raw_path": "/Z-Controller/I gain" },
                    "set_point": {
                    "raw_path": "/Z-Controller/Setpoint",
                    "@units": "/Z-Controller/Setpoint/@unit"
                    },
                    "D_t": {
                    "raw_path": "/Z-Controller/Time const",
                    "@units": "/Z-Controller/Time const/@unit"
                    },
                    "tip_lift": {
                    "raw_path": "/Z-Controller/TipLift",
                    "@units": "/Z-Controller/TipLift/@unit"
                    },
                    "z": {
                    "raw_path": "/Z-Controller/Z",
                    "@units": "/Z-Controller/Z/@unit"
                    },
                    "feedback_on": {
                    "raw_path": "/Z-Controller/Controller status"
                    },
                    "switch_off_delay": {
                    "raw_path": "/Z-Controller/Switch off delay",
                    "@units": "/Z-Controller/Switch off delay/@unit"
                    },
                    "z_offset_value": "",
                    "controller_label": { "raw_path": "/Z-Controller/Controller name" }
                }
                },
                "x": "",
                "y": "",
                "z": {
                "raw_path": "/Z-Controller/Z",
                "@units": "/Z-Controller/Z/@unit"
                },
                "AXISoffset_value[x_offset_value]": {
                "x": "",
                "y": "",
                "z": ""
                }
            },
            "real_time_controller": {
                "fabrication": {
                "model": {
                    "raw_path": "/NanonisMain/RT Release/value"
                }
                },
                "frequency": {
                "raw_path": "/NanonisMain/RT Frequency",
                "@units": "/NanonisMain/RT Frequency/@unit"
                },
                "acquisition_time": {
                "raw_path": "/NanonisMain/Acquisition Period",
                "@units": "/NanonisMain/Acquisition Period/@unit"
                },
                "animation_time": {
                "raw_path": "/NanonisMain/Animations Period",
                "@units": "/NanonisMain/Animations Period/@unit"
                },
                "measurement_time": {
                "raw_path": "/NanonisMain/Measurements Period",
                "@units": "/NanonisMain/Measurements Period/@unit"
                },
                "indication_time": {
                "raw_path": "/NanonisMain/Indicators Period",
                "@units": "/NanonisMain/Indicators Period/@unit"
                }
            },
            "sample_bias_voltage": {
                "bias_voltage": {
                "raw_path": "/Bias/Bias",
                "@units": "/Bias/Bias/@unit"
                },
                "bias_offset_value": {
                "raw_path": "/Bias/Offset",
                "@units": "/Bias/Offset/@unit"
                },
                "calibration": {
                "calibration_parameters": {
                    "coefficient": {
                    "raw_path": "/Bias/Calibration",
                    "@units": "/Bias/Calibration/@unit"
                    }
                },
                "calibration_time": ""
                }
            }
            },
            "PROCESS[process]": { "program": "" },
            "SAMPLE[sample]": { "name": "" },
            "USER[user]": {
            "address": "",
            "affiliation": "",
            "email": "",
            "name": "",
            "orcid": "",
            "telephone_number": ""
            },
            "DATA[data]": [
            {
                "data": {
                "name": "z",
                "raw_path": "/Z/forward",
                "@units": "@default:m"
                },
                "title": {
                "raw_path": "@default:Height Plot of STM Experiment (Foward Direction)"
                },
                "grp_name": "z_forward"
            },
            {
                "data": {
                "name": "z",
                "raw_path": "/Z/backward",
                "@units": "@default:m"
                },
                "title": {
                "raw_path": "@default:Height Plot of STM Experiment (Backward Direction)"
                },
                "grp_name": "z_backward"
            },
            {
                "data": {
                "name": "current",
                "raw_path": "/Current/forward",
                "@units": "@default:A"
                },
                "title": {
                "raw_path": "@default:Current Plot of STM Experiment (Foward Direction)"
                },
                "grp_name": "current_forward"
            },
            {
                "data": {
                "name": "current",
                "raw_path": "/Current/backward",
                "@units": "@default:A"
                },
                "title": {
                "raw_path": "@default:Current Plot of STM Experiment (Backward Direction)"
                },
                "grp_name": "current_backward"
            }
            ],
            "reproducibility_indicators": {
            "current": "@default_link:/ENTRY[entry]/INSTRUMENT[instrument]/current_sensor/current",
            "current_gain": "@default_link:/ENTRY[entry]/INSTRUMENT[instrument]/current_sensor/AMPLIFIER[amplifier]/current_gain",
            "current_offset": "@default_link:/ENTRY[entry]/INSTRUMENT[instrument]/current_sensor/current_offset",
            "bias_sweep": "@default_link:/ENTRY[entry]/INSTRUMENT[instrument]/bias_spectroscopy_environment/BIAS_SPECTROSCOPY[bias_spectroscopy]/BIAS_SWEEP[bias_sweep]",
            "reference_frequency": "@default_link:/ENTRY[entry]/INSTRUMENT[instrument]/lockin_amplifier/reference_frequency",
            "modulation_signal": "@default_link:/ENTRY[entry]/INSTRUMENT[instrument]/lockin_amplifier/modulation_signal"
            },
            "resolution_indicators": {
            "head_temperature": "@default_link:/ENTRY[entry]/INSTRUMENT[instrument]/scan_environment/head_temperature",
            "cryo_bottom_temperature": "@default_link:/ENTRY[entry]/INSTRUMENT[instrument]/scan_environment/cryo_bottom_temperature",
            "cryo_shield_temperature": "@default_link:/ENTRY[entry]/INSTRUMENT[instrument]/scan_environment/cryo_shield_temperature",
            "bias_sweep": "@default_link:/ENTRY[entry]/INSTRUMENT[instrument]/bias_spectroscopy_environment/BIAS_SPECTROSCOPY[bias_spectroscopy]/BIAS_SWEEP[bias_sweep]",
            "reference_frequency": "@default_link:/ENTRY[entry]/INSTRUMENT[instrument]/lockin_amplifier/reference_frequency",
            "modulation_signal": "@default_link:/ENTRY[entry]/INSTRUMENT[instrument]/lockin_amplifier/modulation_signal"
            }
        }
    }
    ```
    </div>
=== "Config File Nanonis (AFM)"
    <div class="scrollable">
    ```json
    {
        "ENTRY[entry]": {
            "@default": {
            "raw_path": "@default:amplitude_backward"
            },
            "definition": { "@version": null },
            "identifier_collection": "",
            "entry_identifier": "",
            "start_time": {
            "#note": "Handled in function _set_start_end_time"
            },
            "end_time": {
            "#note": "Handled in function _set_start_end_time"
            },
            "scan_mode": "",
            "scan_type": "",
            "identifier_experiment": { "identifier": "" },
            "experiment_description": { "raw_path": "/COMMENT" },
            "INSTRUMENT[instrument]": {
            "SPM_CANTILEVER[spm_cantilever]": {
                "cantilever_oscillator": {
                "reference_amplitude": {
                    "raw_path": "/Oscillation Control/Amplitude Setpoint",
                    "@units": "/Oscillation Control/Amplitude Setpoint/@unit"
                },
                "reference_frequency": {
                    "raw_path": "/Oscillation Control/Center Frequency",
                    "@units": "/Oscillation Control/Center Frequency/@unit"
                },
                "reference_phase": {
                    "raw_path": "/Oscillation Control/Reference Phase",
                    "@units": "/Oscillation Control/Reference Phase/@unit"
                },
                "frequency_bandwidth": {
                    "raw_path": "/Oscillation Control/Range",
                    "@units": "/Oscillation Control/Range/@unit"
                },
                "frequency_harmonic": { "raw_path": "/Oscillation Control/Harmonic" },
                "frequency_shift": {
                    "raw_path": "/Oscillation Control/FrequencyShift",
                    "@units": "/Oscillation Control/FrequencyShift/@unit"
                },
                "frequency_cutoff": {
                    "raw_path": "/Oscillation Control/Cut off frq",
                    "@units": "/Oscillation Control/Cut off frq/@unit"
                },
                "target_amplitude": "",
                "active_frequency": ""
                },
                "cantilever_config": {
                "amplitude_excitation": {
                    "raw_path": "/Oscillation Control/Excitation",
                    "@units": "/Oscillation Control/Excitation/@unit"
                },
                "spring_constant": {
                    "raw_path": "/Oscillation Control/PLL-Setup amplitude/spring_constant",
                    "@units": "/Oscillation Control/PLL-Setup amplitude/spring_constant/@unit"
                }
                },
                "phase_positioner": {
                "actuator": {
                    "feedback": {
                    "K_p": {
                        "raw_path": "/Oscillation Control/Phase P gain"
                    },
                    "K_i": {
                        "raw_path": "/Oscillation Control/Phase I gain"
                    },
                    "K_d": "",
                    "D_t": ""
                    }
                }
                },
                "amplitude_positioner": {
                "actuator": {
                    "feedback": {
                    "K_p": {
                        "raw_path": "/Oscillation Control/Amplitude P gain"
                    },
                    "K_i": {
                        "raw_path": "/Oscillation Control/Amplitude I gain"
                    },
                    "K_d": "",
                    "D_t": ""
                    }
                }
                }
            },
            "phase_lock_loop": {
                "loop_filter": {
                "Kf_coefficient": {
                    "raw_path": "/Oscillation Control/PLL-Setup Q-Factor",
                    "@units": "/Oscillation Control/Sensitivity/@unit"
                }
                },
                "frequency_bandwidth": {
                "raw_path": "/Oscillation Control/PLL-Setup Demod. Bandwidth Amp",
                "@units": "/Oscillation Control/PLL-Setup Demod. Bandwidth Amp/@unit"
                },
                "phase_bandwidth": {
                "raw_path": "/Oscillation Control/PLL-Setup Demod. Bandwidth Pha",
                "@units": "/Oscillation Control/PLL-Setup Demod. Bandwidth Pha/@unit"
                }
            },
            "lockin_amplifier": {
                "reference_frequency": {
                "raw_path": "/Lock-in/Frequency",
                "@units": "@default:Hz"
                },
                "modulation_signal": {
                "raw_path": "/Lock-in/Modulated signal"
                },
                "demodulated_signal": {
                "raw_path": "/Lock-in/Demodulated signal"
                },
                "modulation_status": { "raw_path": "/Lock-in/Lock-in status" },
                "demodulated_frequency": "",
                "demodulated_amplitude": "",
                "demodulator_channels": "",
                "recorded_channels": "",
                "ref_offset_phaseN[ref_offset_phase_n]": {
                "raw_path": "/Lock-in/Reference phase",
                "@units": "/Lock-in/Reference phase/@unit"
                },
                "harmonic_orderN[harmonic_order_n]": {
                "raw_path": "/Lock-in/Harmonic"
                }
            },
            "bias_spectroscopy_environment": {
                "BIAS_SPECTROSCOPY[bias_spectroscopy]": {
                "bias_sweep": {
                    "linear_sweep": {
                    "reset_bias": null,
                    "scan_points_bias": null,
                    "step_size_bias": { "@units": null }
                    },
                    "scan_region": {
                    "scan_end_bias": { "@units": null },
                    "scan_offset_bias": { "@units": null },
                    "scan_range_bias": { "@units": null },
                    "scan_start_bias": { "@units": null }
                    },
                    "settling_time": { "@units": null }
                }
                },
                "independent_controllers": null,
                "measurement_sensors": null
            },
            "head_temperature_sensor": null,
            "cryo_shield_temperature_sensor": null,
            "cryo_bottom_temperature_sensor": null,
            "height_piezo_sensor": {
                "piezo_configuration": {
                "calibration": {
                    "calibration_type": {
                    "raw_path": "@default:active"
                    },
                    "calibration_date": {
                    "raw_path": ""
                    },
                    "calibration_parameters": {
                    "coefficientN[coefficient_n]": [
                        {
                        "x": {
                            "raw_path": "/Piezo Calibration/Calib. X",
                            "@units": "/Piezo Calibration/Calib. X/@unit"
                        }
                        },
                        {
                        "y": {
                            "raw_path": "/Piezo Calibration/Calib. Y",
                            "@units": "/Piezo Calibration/Calib. Y/@unit"
                        }
                        },
                        {
                        "z": {
                            "raw_path": "/Piezo Calibration/Calib. Z",
                            "@units": "/Piezo Calibration/Calib. Z/@unit"
                        }
                        }
                    ],
                    "second_order_correctionN[second_order_correction_n]": [
                        {
                        "x": {
                            "raw_path": "/Piezo Calibration/2nd order corr X",
                            "@units": "/Piezo Calibration/2nd order corr X/@unit"
                        }
                        },
                        {
                        "y": {
                            "raw_path": "/Piezo Calibration/2nd order corr Y",
                            "@units": "/Piezo Calibration/2nd order corr Y/@unit"
                        }
                        },
                        {
                        "z": {
                            "raw_path": "/Piezo Calibration/2nd order corr Z",
                            "@units": "/Piezo Calibration/2nd order corr Z/@unit"
                        }
                        }
                    ]
                    },
                    "calibration_name": {
                    "raw_path": "/Piezo Calibration/Active Calib."
                    },
                    "driftN[drift_n]": [
                    {
                        "x": {
                        "raw_path": "/Piezo Calibration/Drift X",
                        "@units": "/Piezo Calibration/Drift X/@unit"
                        }
                    },
                    {
                        "y": {
                        "raw_path": "/Piezo Calibration/Drift Y",
                        "@units": "/Piezo Calibration/Drift Y/@unit"
                        }
                    },
                    {
                        "z": {
                        "raw_path": "/Piezo Calibration/Drift Z",
                        "@units": "/Piezo Calibration/Drift Z/@unit"
                        }
                    }
                    ],
                    "drift_correction_status": {
                    "raw_path": [
                        "/Piezo Configuration/Drift correction status",
                        "/Piezo Calibration/Drift correction status"
                    ]
                    },
                    "hv_gainN[hv_gain_n]": [
                    { "x": { "raw_path": "/Piezo Calibration/HV Gain X" } },
                    { "y": { "raw_path": "/Piezo Calibration/HV Gain Y" } },
                    { "z": { "raw_path": "/Piezo Calibration/HV Gain Z" } }
                    ],
                    "tiltN[tilt_n]": [
                    {
                        "x": {
                        "raw_path": "/Piezo Calibration/Tilt X",
                        "@units": "/Piezo Calibration/Tilt X/@unit"
                        }
                    },
                    {
                        "y": {
                        "raw_path": "/Piezo Calibration/Tilt Y",
                        "@units": "/Piezo Calibration/Tilt X/@unit"
                        }
                    }
                    ]
                },
                "piezo_material": {
                    "curvature_radiusN": [
                    {
                        "x": {
                        "raw_path": "/Piezo Calibration/Curvature radius X",
                        "@units": "/Piezo Calibration/Curvature radius X/@unit"
                        }
                    },
                    {
                        "y": {
                        "raw_path": "/Piezo Calibration/Curvature radius Y",
                        "@units": "/Piezo Calibration/Curvature radius Y/@unit"
                        }
                    }
                    ]
                }
                },
                "SPM_POSITIONER[spm_positioner]": {
                "z_controller": {
                    "K_i": { "raw_path": "/Z-Controller/P gain" },
                    "K_p": { "raw_path": "/Z-Controller/I gain" },
                    "set_point": {
                    "raw_path": "/Z-Controller/Setpoint",
                    "@units": "/Z-Controller/Setpoint unit"
                    },
                    "D_t": {
                    "raw_path": "/Z-Controller/Time const",
                    "@units": "/Z-Controller/Time const/@unit"
                    },
                    "tip_lift": {
                    "raw_path": "/Z-Controller/TipLift",
                    "@units": "/Z-Controller/TipLift/@unit"
                    },
                    "z": {
                    "raw_path": "/Z-Controller/Z",
                    "@units": "/Z-Controller/Z/@unit"
                    },
                    "feedback_on": {
                    "raw_path": "/Z-Controller/Controller status"
                    },
                    "switch_off_delay": {
                    "raw_path": "/Z-Controller/Switch off delay",
                    "@units": "/Z-Controller/Switch off delay/@unit"
                    },
                    "controller_label": { "raw_path": "/Z-Controller/Controller name" }
                },
                "z_offset_value": "",
                "tip_position_z": ""
                },
                "x": { "@units": null },
                "y": { "@units": null },
                "z": {
                "raw_path": "/Z-Controller/Z",
                "@units": "/Z-Controller/Z/@unit"
                }
            },
            "SCAN_ENVIRONMENT[scan_environment]": {
                "head_temperature": {
                "raw_path": "/Temperature 1/Temperature 1",
                "@units": "@default:K"
                },
                "cryo_bottom_temperature": null,
                "cryo_shield_temperature": null,
                "identifier_environment": { "raw_path": "/Scan/series name" },
                "SPM_SCAN_CONTROL[spm_scan_control]": {
                "scanTAG[scan_name]": { "raw_path": "/Scan/series name" },
                "scan_region": {
                    "scan_angleN[scan_angle_n]": {
                    "raw_path": "/SCAN/ANGLE",
                    "@units": "@default:deg"
                    },
                    "scan_offset_valueN[scan_offset_value_n]": {
                    "#note": "Derived in function 'construct_scan_region_grp'.",
                    "raw_path": "/SCAN/OFFSET",
                    "@units": "/Z-Controller/Z/@unit"
                    },
                    "scan_rangeN[scan_range_n]": {
                    "#note": "Derived in function 'construct_scan_region_grp'.",
                    "raw_path": "/SCAN/RANGE",
                    "@units": "/Z-Controller/Z/@unit"
                    }
                },
                "meshSCAN[mesh_scan]": {
                    "backward_speedN[backward_speed_n]": {
                    "#note": "Derived in construct_scan_pattern_grp",
                    "raw_path": "/Scan/speed backw.",
                    "@units": "/Scan/speed backw./@unit"
                    },
                    "forward_speedN[forward_speed_n]": {
                    "#note": "Derived in construct_scan_pattern_grp",
                    "raw_path": "/Scan/speed forw.",
                    "@units": "/Scan/speed forw./@unit"
                    },
                    "scan_speedN[scan_speed_n]": "",
                    "channelNAME[scan_name_n]": "",
                    "scan_pointsN[scan_points_n]": {
                    "#note": "Derived in construct_scan_pattern_grp",
                    "raw_path": "/SCAN/PIXELS",
                    "@units": ""
                    },
                    "steppingN[stepping_n]": [
                    {
                        "_x": {
                        "raw_path": "@default:1",
                        "@units": ""
                        }
                    },
                    {
                        "_y": {
                        "raw_path": "@default:1",
                        "@units": ""
                        }
                    }
                    ],
                    "step_sizeN[step_size_n]": { "raw_path": "", "@units": "" },
                    "scan_time": "",
                    "DATA[scan_data]": [
                    {
                        "data": {
                        "name": "imput_4",
                        "raw_path": "/Input_4/forward",
                        "@units": "/DATA/INFO/Input_4/Unit"
                        },
                        "title": {
                        "raw_path": "@default:Input-4 Plot of AFM Experiment (Forward Direction)"
                        },
                        "grp_name": "input_4_forward"
                    },
                    {
                        "data": {
                        "name": "imput_4",
                        "raw_path": "/Input_4/backward",
                        "@units": "/DATA/INFO/Input_4/Unit"
                        },
                        "title": {
                        "raw_path": "@default:Input-4 Plot of AFM Experiment (Backward Direction)"
                        },
                        "grp_name": "input_4_backward"
                    },
                    {
                        "data": {
                        "name": "lix_1_omega",
                        "raw_path": "/LIX_1_omega/forward",
                        "@units": "/DATA/INFO/LIX_1_omega/Unit"
                        },
                        "title": {
                        "raw_path": "@default:Lockin X-1 Plot of AFM Experiment (Forward Direction)"
                        },
                        "grp_name": "lix_1_omega_forward"
                    },
                    {
                        "data": {
                        "name": "lix_1_omega",
                        "raw_path": "/LIX_1_omega/backward",
                        "@units": "/DATA/INFO/LIX_1_omega/Unit"
                        },
                        "title": {
                        "raw_path": "@default:Lockin X-1 Plot of AFM Experiment (Backward Direction)"
                        },
                        "grp_name": "lix_1_omega_backward"
                    },
                    {
                        "data": {
                        "name": "liy_1_omega",
                        "raw_path": "/LIY_1_omega/forward",
                        "@units": "/DATA/INFO/LIY_1_omega/Unit"
                        },
                        "title": {
                        "raw_path": "@default:Lockin Y-1 Plot of AFM Experiment (Forward Direction)"
                        },
                        "grp_name": "liy_1_omega_forward"
                    },
                    {
                        "data": {
                        "name": "liy_1_omega",
                        "raw_path": "/LIY_1_omega/backward",
                        "@units": "/DATA/INFO/LIY_1_omega/Unit"
                        },
                        "title": {
                        "raw_path": "@default:Lockin Y-1 Plot of AFM Experiment (Backward Direction)"
                        },
                        "grp_name": "liy_1_omega_backward"
                    },
                    {
                        "data": {
                        "name": "frequency_shift",
                        "raw_path": "/Frequency_Shift/forward",
                        "@units": "/DATA/INFO/Frequency_Shift/Unit"
                        },
                        "title": {
                        "raw_path": "@default:Frequency Shift Plot of AFM Experiment (Forward Direction)"
                        },
                        "grp_name": "frequency_shift_forward"
                    },
                    {
                        "data": {
                        "name": "frequency_shift",
                        "raw_path": "/Frequency_Shift/backward",
                        "@units": "/DATA/INFO/Frequency_Shift/Unit"
                        },
                        "title": {
                        "raw_path": "@default:Frequency Shift Plot of AFM Experiment (Backward Direction)"
                        },
                        "grp_name": "frequency_shift_backward"
                    }
                    ]
                },
                "independent_scan_axes": {
                    "#note": "Derived in scan pattern group.",
                    "raw_path": "/SCAN/DIR",
                    "@units": ""
                },
                "scan_resolutionN[scan_resolution_n]": "",
                "accuracyN": "",
                "scan_type": { "raw_path": "@default:mesh", "@units": "" },
                "scan_control_type": {
                    "raw_path": "@default:continuous",
                    "@units": ""
                }
                },
                "cryo_shield_temperature_sensor": "@default_link:/ENTRY[entry]/INSTRUMENT[instrument]/cryo_shield_temperature_sensor",
                "cryo_bottom_temperature_sensor": "@default_link:/ENTRY[entry]/INSTRUMENT[instrument]/cryo_bottom_temperature_sensor",
                "head_temperature_sensor": "@default_link:/ENTRY[entry]/INSTRUMENT[instrument]/head_temperature_sensor"
            },
            "real_time_controller": {
                "fabrication": {
                "model": {
                    "raw_path": "/NanonisMain/RT Release/value"
                }
                },
                "frequency": {
                "raw_path": "/NanonisMain/RT Frequency",
                "@units": "/NanonisMain/RT Frequency/@unit"
                },
                "acquisition_time": {
                "raw_path": "/NanonisMain/Acquisition Period",
                "@units": "/NanonisMain/Acquisition Period/@unit"
                },
                "animation_time": {
                "raw_path": "/NanonisMain/Animations Period",
                "@units": "/NanonisMain/Animations Period/@unit"
                },
                "measurement_time": {
                "raw_path": "/NanonisMain/Measurements Period",
                "@units": "/NanonisMain/Measurements Period/@unit"
                },
                "indication_time": {
                "raw_path": "/NanonisMain/Indicators Period",
                "@units": "/NanonisMain/Indicators Period/@unit"
                }
            },
            "sample_bias_voltage": {
                "bias_voltage": {
                "raw_path": "/Bias/Bias",
                "@units": "/Bias/Bias/@unit"
                },
                "bias_offset_value": {
                "raw_path": "/Bias/Offset",
                "@units": "/Bias/Offset/@unit"
                },
                "calibration": {
                "calibration_parameters": {
                    "coefficient": {
                    "raw_path": "/Bias/Calibration",
                    "@units": "/Bias/Calibration/@unit"
                    }
                },
                "calibration_time": ""
                }
            }
            },
            "DATA[data]": [
            {
                "data": {
                "name": "z",
                "raw_path": "/Z/forward",
                "@units": "/DATA/INFO/Z/Unit"
                },
                "title": {
                "raw_path": "@default:Height Plot of AFM Experiment (Foward Direction)"
                },
                "grp_name": "z_forward"
            },
            {
                "data": {
                "name": "z",
                "raw_path": "/Z/backward",
                "@units": "/DATA/INFO/Z/Unit"
                },
                "title": {
                "raw_path": "@default:Height Plot of AFM Experiment (Backward Direction)"
                },
                "grp_name": "z_backward"
            },
            {
                "data": {
                "name": "excitation",
                "raw_path": "/Excitation/forward",
                "@units": "/DATA/INFO/Excitation/Unit"
                },
                "title": {
                "raw_path": "@default:Excitation Plot of AFM Experiment (Forward Direction)"
                },
                "grp_name": "excitation_forward"
            },
            {
                "data": {
                "name": "excitation",
                "raw_path": "/Excitation/backward",
                "@units": "/DATA/INFO/Excitation/Unit"
                },
                "title": {
                "raw_path": "@default:Excitation Plot of AFM Experiment (Backward Direction)"
                },
                "grp_name": "excitation_backward"
            },
            {
                "data": {
                "name": "phase",
                "raw_path": "/Phase/Forward",
                "@units": "/DATA/INFO/Phase/Unit"
                },
                "title": {
                "raw_path": "@default:Phase Plot of AFM Experiment (Forward Direction)"
                },
                "grp_name": "phase_forward"
            },
            {
                "data": {
                "name": "phase",
                "raw_path": "/Phase/Backward",
                "@units": "/DATA/INFO/Phase/Unit"
                },
                "title": {
                "raw_path": "@default:Phase Plot of AFM Experiment (Backward Direction)"
                },
                "grp_name": "phase_backward"
            },
            {
                "data": {
                "name": "current",
                "raw_path": "/Current/forward",
                "@units": "/DATA/INFO/Current/Unit"
                },
                "title": {
                "raw_path": "@default:Current Plot of AFM Experiment (Forward Direction)"
                },
                "grp_name": "current_forward"
            },
            {
                "data": {
                "name": "current",
                "raw_path": "/Current/backward",
                "@units": "/DATA/INFO/Current/Unit"
                },
                "title": {
                "raw_path": "@default:Current Plot of AFM Experiment (Backward Direction)"
                },
                "grp_name": "current_backward"
            }
            ],
            "reproducibility_indicators": {
            "cantilever_head_temperature": "@default_link:/ENTRY[entry]/INSTRUMENT[instrument]/scan_environment/head_temperature",
            "cryo_bottom_temperature": "@default_link:/ENTRY[entry]/INSTRUMENT[instrument]/scan_environment/cryo_bottom_temperature",
            "cryo_shield_temperature": "@default_link:/ENTRY[entry]/INSTRUMENT[instrument]/scan_environment/cryo_shield_temperature",
            "cantilever_oscillator": "@default_link:/ENTRY[entry]/INSTRUMENT[instrument]/cantilever_spm/cantilever_oscillator"
            },
            "resolution_indicators": {
            "cantilever_head_temperature": "@default_link:/ENTRY[entry]/INSTRUMENT[instrument]/scan_environment/head_temperature",
            "cryo_bottom_temperature": "@default_link:/ENTRY[entry]/INSTRUMENT[instrument]/scan_environment/cryo_bottom_temperature",
            "cryo_shield_temperature": "@default_link:/ENTRY[entry]/INSTRUMENT[instrument]/scan_environment/cryo_shield_temperature",
            "oscillator_excitation": "@default_link:/ENTRY[entry]/INSTRUMENT[instrument]/cantilever_spm/cantilever_config/amplitude_excitation",
            "amplitude_excitation": "@default_link:/ENTRY[entry]/INSTRUMENT[instrument]/phase_lock_loop/amplitude_excitation"
            }
        }
    }
    ```
    </div>

#### __ELN Schema file__ 
The ELN schema file is a `yaml` file which describes the metadata of the experiment. To know how to read this ELN schema file and modify it, please follow section `ELN Schema File` [Work with Reader](../how-to-guides/how-to-act-with-reader.md) guide. This file only usable in [NOMAD](link_goes_here) RDM system.

=== "ELN Schema file (STS)"
    <div class="scrollable">
    ```yaml
    definitions:
        name: An ELN example for STS (Scanning Tunneling Spectroscopy).
        sections:
            sts:
            base_sections:
                - pynxtools.nomad.dataconverter.NexusDataConverter
                - nomad.datamodel.data.EntryData
            m_annotations:
                template:
                reader: spm
                nxdl: NXsts
                eln:
                hide: []
            quantities:
                default:
                type: str
                m_annotations:
                    eln:
                    component: StringEditQuantity
                description: |
                    The name of the NXdata group that comes as child of the entry group for default plot visualization
                    to be displayed upon the entry of NeXus file.
                definition:
                type:
                    type_kind: Enum
                    type_data:
                    - NXsts
                m_annotations:
                    eln:
                    component: EnumEditQuantity
                description: |
                    Name of the definitions from NeXus app def designed for STS experiments, one can use 
                    NXsts or NXspm, but NXsts is recommended.
                experiment_technique:
                type:
                    type_kind: Enum
                    type_data:
                    - STS
                m_annotations:
                    eln:
                    component: EnumEditQuantity
                description: |
                    Name of the technique used for the experiment, e.g. STS.
                experiment_description:
                type: str
                m_annotations:
                    eln:
                    component: RichTextEditQuantity
                description: |
                    Descriptive comments for this experiment, added by the experimenter in eln or 
                    coming from the output file, e.g. Comment01 SYNC & Filter LP 8order WITHDRAW
                    600 steps, locked Au(111), 50pA, 100 mV set point, 1mV DCA, 973Hz,138
                    1st H, -84 2nd H.
                identifier_experiment: 
                type: str
                m_annotations:
                    eln:
                    component: StringEditQuantity
                description: |
                    An unique identifier fot the experiment. e.g. the identifier
                    could be specific for a lab or experiment team.
                identifier_collection: 
                type: str
                m_annotations:
                    eln:
                    component: StringEditQuantity
                description: |
                    An unique identifier of a collection. Use this
                    if the experiment if part of a collection of experiments
            sub_sections:
                User:
                section:
                    m_annotations:
                    eln:
                        overview: true
                    quantities:
                    name:
                        type: str
                        m_annotations:
                        eln:
                            component: StringEditQuantity
                        description: |
                        Name of the user who performed the experiment.
                    affiliation:
                        type: str
                        shape: "*"
                        m_annotations:
                        eln:
                            component: StringEditQuantity
                        description: |
                        Affiliation of the user who performed the experiment.
                    email:
                        type: str
                        shape: "*"
                        m_annotations:
                        eln:
                            component: StringEditQuantity
                        description: |
                        List of emails from users who performed the experiment.
                Instrument:
                section:
                    m_annotations:
                    eln:
                        overview: true
                    sub_sections:
                    hardware:
                        section:
                        m_annotations:
                            eln:
                            overview: true
                        quantities:
                            name:
                            type: str
                            m_annotations:
                                eln:
                                component: StringEditQuantity
                            description: |
                                Name of the hardware. (e.g. Nanonis).
                            vendor:
                            type: str
                            m_annotations:
                                eln:
                                component: StringEditQuantity
                            description: |
                                Name of the manufacturer of the hardware (e.g. Nanonis).
                            model:
                            type: str
                            m_annotations:
                                eln:
                                component: StringEditQuantity
                            description: |
                                Version or model of the component named by the manufacturer (e.g. Generic 5e).
                            model/@version:
                            type: str
                            m_annotations:
                                eln:
                                component: StringEditQuantity
                            description: |
                                If model has a distinquishable version (e.g. BP5e).
                    software:
                        section:
                        m_annotations:
                            eln:
                            overview: true
                        quantities:
                            vendor:
                            type: str
                            m_annotations:
                                eln:
                                component: StringEditQuantity
                            description: |
                                Name of the manufacturer of the software.
                            name:
                            type: str
                            m_annotations:
                                eln:
                                component: StringEditQuantity
                            description: |
                                Name of the software. (e.g. Nanonis).
                            model:
                            type: str
                            m_annotations:
                                eln:
                                component: StringEditQuantity
                            description: |
                                Version or model, required to choose correct file parser, of the component named 
                                by the manufacturer (e.g. Generic 5e).
                                Note that model should be exactly the same as the one in the experiment file.
                            model/@version:
                            type: str
                            m_annotations:
                                eln:
                                component: StringEditQuantity
                            description: |
                                If model has a distinquishable version (e.g. BP5e).
                    lockin_amplifier:
                        section:
                        m_annotations:
                            eln:
                            overview: true
                        quantities:
                            modulation_signal:
                            type: str
                            m_annotations:
                                eln:
                                component: StringEditQuantity
                            description: |
                                Type of the signal either in voltage or current.
                            flip_sign:
                            type: np.float64
                            m_annotations:
                                eln:
                                component: NumberEditQuantity
                            description: |
                                The sign (1 or -1) that defines the sign of the lock-in current.
                                The calibration procedure with retracted tip is normally performed
                                to compensate for the signal phase delay in SPM. The procedure 
                                yields two possible solutions, this number should be equal to 1 or -1
                                depending on which solution is chosen (this concept mainly used in 
                                STS experiments, e.g. in Nanonis machine).
                    Scan_environment:
                        section:
                        m_annotations:
                            eln:
                            overview: true
                        quantities:
                            head_temperature:
                            type: np.float64
                            unit: kelvin
                            m_annotations:
                                eln:
                                component: NumberEditQuantity
                                defaultDisplayUnit: K
                            description: |
                                Temperature of STM head. Note: At least one field from head_temperature,
                                cryo_bottom_temperature and cryo_shield_temperature must be provided.
                            cryo_bottom_temperature:
                            type: np.float64
                            unit: kelvin
                            m_annotations:
                                eln:
                                component: NumberEditQuantity
                                defaultDisplayUnit: K
                            description: |
                                Temperature of the cold tail of the cryostat. Note: 
                                At least one field from head_temperature, cryo_bottom_temperature and cryo_shield_temperature must be provided.
                            cryo_shield_temperature:
                            type: np.float64
                            unit: kelvin
                            m_annotations:
                                eln:
                                component: NumberEditQuantity
                                defaultDisplayUnit: K
                            description: |
                                Temperature of liquid nitrogen shield. Note: At
                                least one field from head_temperature, cryo_bottom_temperature and cryo_shield_temperature must be provided.
                Sample:
                section:
                    m_annotations:
                    eln: 
                        overview: true
                    quantities:
                    name:
                        type: str
                        m_annotations:
                        eln:
                            component: StringEditQuantity
                        description: |
                        Name of the sample.
                    chemical_formula:
                        type: str
                        m_annotations:
                        eln:
                            component: StringEditQuantity
                        description: |
                        The chemical formula specified using CIF conventions.
                        Abbreviated version of CIF standard:
                        
                        * Only recognized element symbols may be used.
                        * Each element symbol is followed by a 'count' number. A count of '1' may be omitted.
                        * A space or parenthesis must separate each cluster of (element symbol + count).
                        * Where a group of elements is enclosed in parentheses, the multiplier for the
                            group must follow the closing parentheses. That is, all element and group
                            multipliers are assumed to be printed as subscripted numbers.
                        * Unless the elements are ordered in a manner that corresponds to their chemical
                            structure, the order of the elements within any group or moiety depends on
                            whether or not carbon is present.
                        * If carbon is present, the order should be:
                        
                            - C, then H, then the other elements in alphabetical order of their symbol.
                            - If carbon is not present, the elements are listed purely in alphabetic order of their symbol.
                            
                        * This is the *Hill* system used by Chemical Abstracts.
                    description:
                        type: str
                        m_annotations:
                        eln:
                            component: RichTextEditQuantity
                        description: |
                        Description of the sample or sample preparation.
                    sub_sections:
                    Sample_component:
                        section:
                        m_annotations:
                            eln:
                            overview: true
                        description: |
                            A sample component is a part of the sample that is of interest.
                            For example, a sample component could be a layer of a multilayer sample.
                        quantities:
                            name:
                            type: str
                            m_annotations:
                                eln:
                                component: StringEditQuantity
                            description: |
                                Name of the sample component.
                            identifier_component:
                            type: str
                            m_annotations:
                                eln:
                                component: StringEditQuantity
                            description: |
                                An unique identifier for the sample component.
                            chemical_formula:
                            type: str
                            m_annotations:
                                eln:
                                component: StringEditQuantity
                            description: |
                                The chemical formula specified using CIF conventions.
                                Abbreviated version of CIF standard:
                                
                                * Only recognized element symbols may be used.
                                * Each element symbol is followed by a 'count' number. A count of '1' may be omitted.
                                * A space or parenthesis must separate each cluster of (element symbol + count).
                                * Where a group of elements is enclosed in parentheses, the multiplier for the
                                group must follow the closing parentheses. That is, all element and group
                                multipliers are assumed to be printed as subscripted numbers.
                                * Unless the elements are ordered in a manner that corresponds to their chemical
                                structure, the order of the elements within any group or moiety depends on
                                whether or not carbon is present.
                                * If carbon is present, the order should be:
                                
                                - C, then H, then the other elements in alphabetical order of their symbol.
                                - If carbon is not present, the elements are listed purely in alphabetic order of their symbol.
                                
                                * This is the *Hill* system used by Chemical Abstracts.
                            description:
                            type: str
                            m_annotations:
                                eln:
                                component: RichTextEditQuantity
                            description: |
                                Description of the sample component or sample preparation.
                    history:
                        section:
                        m_annotations:
                            eln:
                            overview: true
                        sub_sections:
                            Note:
                            section:
                                m_annotations:
                                eln:
                                    overview: true
                                description: |
                                Notes about the sample history.
                                quantities:
                                description:
                                    type: str
                                    m_annotations:
                                    eln:
                                        component: RichTextEditQuantity
                                    description: |
                                    Title of an image or other details of the note.                          
                        quantities:
                            identifier_history:
                            type: str
                            m_annotations:
                                eln:
                                component: StringEditQuantity
                            description: |
                                Identifier for sample history.
    ```
    </div>
=== "ELN Schema File (STM)"
    <div class="scrollable">
    ```yaml
    definitions:
        name: An ELN example for STM (Scanning Tunneling Microscopy).
        sections:
            stm:
            base_sections:
                - pynxtools.nomad.dataconverter.NexusDataConverter
                - nomad.datamodel.data.EntryData
            m_annotations:
                template:
                reader: spm
                nxdl: NXstm
                eln:
                hide: []
            quantities:
                default:
                type: str
                m_annotations:
                    eln:
                    component: StringEditQuantity
                description: |
                    The name of the NXdata group that comes as child of the entry group for default plot visualization
                    to be displayed upon the entry of NeXus file.
                definition:
                type:
                    type_kind: Enum
                    type_data:
                    - NXstm
                m_annotations:
                    eln:
                    component: EnumEditQuantity
                description: |
                    Name of the definitions from NeXus app def designed for STM experiments,
                    e.g. NXstm.
                experiment_technique:
                type:
                    type_kind: Enum
                    type_data:
                    - STM
                m_annotations:
                    eln:
                    component: EnumEditQuantity
                description: |
                    Name of the technique used for the experiment, e.g. STM. 
                scan_mode:
                type:
                    type_kind: Enum
                    type_data:
                    - constant height
                    - constant current
                m_annotations:
                    eln:
                    component: EnumEditQuantity
                description: |
                    Type of the scan mode to define the type of the interaction between 
                    the tip and the sample.
                experiment_description:
                type: str
                m_annotations:
                    eln:
                    component: RichTextEditQuantity
                description: |
                    Descriptive comments for this experiment, added by the experimenter in eln or 
                    coming from the output file, e.g. Comment01 SYNC & Filter LP 8order WITHDRAW
                    600 steps, locked Au(111), 50pA, 100 mV set point, 1mV DCA, 973Hz,138
                    1st H, -84 2nd H.
                identifier_experiment: 
                type: str
                m_annotations:
                    eln:
                    component: StringEditQuantity
                description: |
                    An unique identifier fot the experiment. e.g. the identifier
                    could be specific for a lab or experiment team.
                identifier_collection: 
                type: str
                m_annotations:
                    eln:
                    component: StringEditQuantity
                description: |
                    An unique identifier of a collection. Use this
                    if the experiment if part of a collection of experiments
            sub_sections:
                User:
                section:
                    m_annotations:
                    eln:
                        overview: true
                    quantities:
                    name:
                        type: str
                        m_annotations:
                        eln:
                            component: StringEditQuantity
                        description: |
                        Name of the user who performed the experiment.
                    affiliation:
                        type: str
                        shape: "*"
                        m_annotations:
                        eln:
                            component: StringEditQuantity
                        description: |
                        Affiliation of the user who performed the experiment.
                    email:
                        type: str
                        shape: "*"
                        m_annotations:
                        eln:
                            component: StringEditQuantity
                        description: |
                        List of emails from users who performed the experiment.
                Instrument:
                section:
                    m_annotations:
                    eln:
                        overview: true
                    sub_sections:
                    hardware:
                        section:
                        m_annotations:
                            eln:
                            overview: true
                        quantities:
                            name:
                            type: str
                            m_annotations:
                                eln:
                                component: StringEditQuantity
                            description: |
                                Name of the hardware. (e.g. Nanonis).
                            vendor:
                            type: str
                            m_annotations:
                                eln:
                                component: StringEditQuantity
                            description: |
                                Name of the manufacturer of the hardware (e.g. Nanonis).
                            model:
                            type: str
                            m_annotations:
                                eln:
                                component: StringEditQuantity
                            description: |
                                Version or model of the component named by the manufacturer (e.g. Nanonis).
                            model/@version:
                            type: str
                            m_annotations:
                                eln:
                                component: StringEditQuantity
                            description: |
                                If model has a distinquishable version (e.g. BP5e).
                    software:
                        section:
                        m_annotations:
                            eln:
                            overview: true
                        quantities:
                            name:
                            type: str
                            m_annotations:
                                eln:
                                component: StringEditQuantity
                            description: |
                                Name of the software. (e.g. Nanonis).
                            vendor:
                            type: str
                            m_annotations:
                                eln:
                                component: StringEditQuantity
                            description: |
                                Name of the manufacturer of the software (e.g. Nanonis).
                            model:
                            type: str
                            m_annotations:
                                eln:
                                component: StringEditQuantity
                            description: |
                                Version or model, required to choose correct file parser, of the component named 
                                by the manufacturer (e.g. Generic 5e). 
                                Note that the model should be exactly the same as in the experiment file.
                            model/@version:
                            type: str
                            m_annotations:
                                eln:
                                component: StringEditQuantity
                            description: |
                                If model has a distinquishable version (e.g. BP5e).
                    height_piezo_sensor:
                        section:
                        m_annotations:
                            eln:
                            overview: true
                        sub_sections:
                            piezo_configuration:
                            section:
                                m_annotations:
                                eln:
                                    overview: true
                                sub_sections:
                                piezo_material:
                                    section:
                                    m_annotations:
                                        eln:
                                        overview: true
                                    quantities:
                                        identifier_piezo_material:
                                        type: str
                                        m_annotations:
                                            eln:
                                            component: StringEditQuantity
                                        description: |
                                            An unique identifier for the piezo material.              
                    lockin_amplifier:
                        section:
                        m_annotations:
                            eln:
                            overview: true
                        quantities:
                            modulation_signal:
                            type: str
                            m_annotations:
                                eln:
                                component: StringEditQuantity
                            description: |
                                Type of the signal either in voltage or current.
                    Scan_environment:
                        section:
                        m_annotations:
                            eln:
                            overview: true
                        quantities:
                            head_temperature:
                            type: np.float64
                            unit: kelvin
                            m_annotations:
                                eln:
                                component: NumberEditQuantity
                                defaultDisplayUnit: K
                            description: |
                                Temperature of STM head. Note: At least one field from head_temperature,
                                cryo_bottom_temperature and cryo_shield_temperature must be provided.
                                At least one field from head_temperature, cryo_bottom_temperature and cryo_shield_temperature must be provided.
                            cryo_bottom_temperature:
                            type: np.float64
                            unit: kelvin
                            m_annotations:
                                eln:
                                component: NumberEditQuantity
                                defaultDisplayUnit: K
                            description: |
                                Temperature of the cold tail of the cryostat. Note: 
                                At least one field from head_temperature, cryo_bottom_temperature and cryo_shield_temperature must be provided.
                            cryo_shield_temperature:
                            type: np.float64
                            unit: kelvin
                            m_annotations:
                                eln:
                                component: NumberEditQuantity
                                defaultDisplayUnit: K
                            description: |
                                Temperature of liquid nitrogen shield. Note: At
                                least one field from head_temperature, cryo_bottom_temperature and cryo_shield_temperature must be provided.
                Sample:
                section:
                    m_annotations:
                    eln: 
                        overview: true
                    quantities:
                    name:
                        type: str
                        m_annotations:
                        eln:
                            component: StringEditQuantity
                        description: |
                        Name of the sample.
                    chemical_formula:
                        type: str
                        m_annotations:
                        eln:
                            component: StringEditQuantity
                        description: |
                        The chemical formula specified using CIF conventions.
                        Abbreviated version of CIF standard:
                        
                        * Only recognized element symbols may be used.
                        * Each element symbol is followed by a 'count' number. A count of '1' may be omitted.
                        * A space or parenthesis must separate each cluster of (element symbol + count).
                        * Where a group of elements is enclosed in parentheses, the multiplier for the
                            group must follow the closing parentheses. That is, all element and group
                            multipliers are assumed to be printed as subscripted numbers.
                        * Unless the elements are ordered in a manner that corresponds to their chemical
                            structure, the order of the elements within any group or moiety depends on
                            whether or not carbon is present.
                        * If carbon is present, the order should be:
                        
                            - C, then H, then the other elements in alphabetical order of their symbol.
                            - If carbon is not present, the elements are listed purely in alphabetic order of their symbol.
                            
                        * This is the *Hill* system used by Chemical Abstracts.
                    description:
                        type: str
                        m_annotations:
                        eln:
                            component: RichTextEditQuantity
                        description: |
                        Description of the sample or sample preparation.
                    sub_sections:
                    Sample_component:
                        section:
                        m_annotations:
                            eln:
                            overview: true
                        description: |
                            A sample component is a part of the sample that is of interest.
                            For example, a sample component could be a layer of a multilayer sample.
                        quantities:
                            name:
                            type: str
                            m_annotations:
                                eln:
                                component: StringEditQuantity
                            description: |
                                Name of the sample component.
                            identifier_component:
                            type: str
                            m_annotations:
                                eln:
                                component: StringEditQuantity
                            description: |
                                An unique identifier for the sample component.
                            chemical_formula:
                            type: str
                            m_annotations:
                                eln:
                                component: StringEditQuantity
                            description: |
                                The chemical formula specified using CIF conventions.
                                Abbreviated version of CIF standard:
                                
                                * Only recognized element symbols may be used.
                                * Each element symbol is followed by a 'count' number. A count of '1' may be omitted.
                                * A space or parenthesis must separate each cluster of (element symbol + count).
                                * Where a group of elements is enclosed in parentheses, the multiplier for the
                                group must follow the closing parentheses. That is, all element and group
                                multipliers are assumed to be printed as subscripted numbers.
                                * Unless the elements are ordered in a manner that corresponds to their chemical
                                structure, the order of the elements within any group or moiety depends on
                                whether or not carbon is present.
                                * If carbon is present, the order should be:
                                
                                - C, then H, then the other elements in alphabetical order of their symbol.
                                - If carbon is not present, the elements are listed purely in alphabetic order of their symbol.
                                
                                * This is the *Hill* system used by Chemical Abstracts.
                            description:
                            type: str
                            m_annotations:
                                eln:
                                component: RichTextEditQuantity
                            description: |
                                Description of the sample component or sample preparation.
                    history:
                        section:
                        m_annotations:
                            eln:
                            overview: true
                        sub_sections:
                            Note:
                            section:
                                m_annotations:
                                eln:
                                    overview: true
                                description: |
                                Notes about the sample history.
                                quantities:
                                description:
                                    type: str
                                    m_annotations:
                                    eln:
                                        component: RichTextEditQuantity
                                    description: |
                                    Title of an image or other details of the note.                          
                        quantities:
                            identifier_history:
                            type: str
                            m_annotations:
                                eln:
                                component: StringEditQuantity
                            description: |
                                Identifier for sample history.
    ```
    </div>
=== "ELN Schema File (AFM)"
    <div class="scrollable">
    ```yaml
    definitions:
        name: Atomic Force Microscopy (AFM) ELN Examples
        sections:
            afm:
            base_sections:
                - pynxtools.nomad.dataconverter.NexusDataConverter
                - nomad.datamodel.data.EntryData
            m_annotations:
                template:
                reader: spm
                nxdl: NXafm
                eln:
                hide: []
            quantities:
                default:
                type: str
                m_annotations:
                    eln:
                    component: StringEditQuantity
                description: |
                    The name of the NXdata group that comes as child of the entry group for default plot
                    to be displayed upon the entry of NeXus file.
                definition:
                type:
                    type_kind: Enum
                    type_data:
                    - NXafm
                m_annotations:
                    eln:
                    component: EnumEditQuantity
                description: |
                    Name of the definitions from NeXus app def designed for STS experiments, one can use 
                    NXsts or NXspm, but NXsts is recommended.
                experiment_technique:
                type:
                    type_kind: Enum
                    type_data:
                    - AFM
                m_annotations:
                    eln:
                    component: EnumEditQuantity
                description: |
                    Name of the technique used for the experiment, e.g. AFM.
                scan_mode:
                type:
                    type_kind: Enum
                    type_data:
                    - contact mode
                    - tapping mode
                    - non-contact mode
                    - Kelvin probe
                    - electric force
                m_annotations:
                    eln:
                    component: EnumEditQuantity
                description: |
                    Mode of scan in AFM experiment.
                experiment_description:
                type: str
                m_annotations:
                    eln:
                    component: RichTextEditQuantity
                description: |
                    Descriptive comments for this experiment, added by the experimenter in eln or 
                    coming from the output file, e.g. Comment01 SYNC & Filter LP 8order WITHDRAW
                    600 steps, locked Au(111), 50pA, 100 mV set point, 1mV DCA, 973Hz,138
                    1st H, -84 2nd H.
                identifier_experiment: 
                type: str
                m_annotations:
                    eln:
                    component: StringEditQuantity
                description: |
                    An unique identifier fot the experiment. e.g. the identifier
                    could be specific for a lab or experiment team.

                identifier_collection: 
                type: str
                m_annotations:
                    eln:
                    component: StringEditQuantity
                description: |
                    An unique identifier of a collection. Use this
                    if the experiment if part of a collection of experiments
            sub_sections:
                User:
                repeats: True
                section:
                    m_annotations:
                    eln:
                        overview: true
                    quantities:
                    name:
                        type: str
                        m_annotations:
                        eln:
                            component: StringEditQuantity
                        description: |
                        Name of the user who performed the experiment.
                    affiliation:
                        type: str
                        shape: "*"
                        m_annotations:
                        eln:
                            component: StringEditQuantity
                        description: |
                        Affiliation of the user who performed the experiment.
                    email:
                        type: str
                        shape: "*"
                        m_annotations:
                        eln:
                            component: StringEditQuantity
                        description: |
                        List of emails from users who performed the experiment.
                Instrument:
                section:
                    m_annotations:
                    eln:
                        overview: true
                    sub_sections:
                    hardware:
                        section:
                        m_annotations:
                            eln:
                            overview: true
                        quantities:
                            vendor:
                            type: str
                            m_annotations:
                                eln:
                                component: StringEditQuantity
                            description: |
                                Name of the vendor of the hardware. (e.g. Nanonis).
                            name:
                            type: str
                            m_annotations:
                                eln:
                                component: StringEditQuantity
                            description: |
                                Name of the hardware. (e.g. Nanonis).
                            model:
                            type: str
                            m_annotations:
                                eln:
                                component: StringEditQuantity
                            description: |
                                Version or model of the component named by the manufacturer (e.g. Nanonis).
                            model/@version:
                            type: str
                            m_annotations:
                                eln:
                                component: StringEditQuantity
                            description: |
                                If model has a distinquishable version (e.g. BP5e).
                    software:
                        section:
                        m_annotations:
                            eln:
                            overview: true
                        quantities:
                            vendor:
                            type: str
                            m_annotations:
                                eln:
                                component: StringEditQuantity
                            description: |
                                Name of the vendor of the software. (e.g. Nanonis).
                            name:
                            type: str
                            m_annotations:
                                eln:
                                component: StringEditQuantity
                            description: |
                                Name of the software. (e.g. Nanonis).
                            model:
                            type: str
                            m_annotations:
                                eln:
                                component: StringEditQuantity
                            description: |
                                Version or model of the component named by the manufacturer (e.g. Generic 4).
                                Note that this should be exacty the same as in experiment file.
                            model/@version:
                            type: str
                            m_annotations:
                                eln:
                                component: StringEditQuantity
                            description: |
                                If model has a distinquishable version (e.g. BP5e).
                    height_piezo_sensor:
                        section:
                        m_annotations:
                            eln:
                            overview: true
                        sub_sections:
                            piezo_configuration:
                            section:
                                m_annotations:
                                eln:
                                    overview: true
                                sub_sections:
                                piezo_material:
                                    section:
                                    m_annotations:
                                        eln:
                                        overview: true
                                    quantities:
                                        identifier_piezo_material:
                                        type: str
                                        m_annotations:
                                            eln:
                                            component: StringEditQuantity
                                        description: |
                                            An unique identifier for the piezo material.
                    Scan_environment:
                        section:
                        m_annotations:
                            eln:
                            overview: true
                        quantities:
                            head_temperature:
                            type: np.float64
                            unit: kelvin
                            m_annotations:
                                eln:
                                component: NumberEditQuantity
                                defaultDisplayUnit: K
                            description: |
                                Temperature of STM head. Note: At least one field from head_temperature,
                                cryo_bottom_temperature and cryo_shield_temperature must be provided.
                                At least one field from tip_temperature, cryo_bottom_temperature and cryo_shield_temperature must be provided.
                            cryo_bottom_temperature:
                            type: np.float64
                            unit: kelvin
                            m_annotations:
                                eln:
                                component: NumberEditQuantity
                                defaultDisplayUnit: K
                            description: |
                                Temperature of the cold tail of the cryostat. Note: 
                                At least one field from tip_temperature, cryo_bottom_temperature and cryo_shield_temperature must be provided.
                            cryo_shield_temperature:
                            type: np.float64
                            unit: kelvin
                            m_annotations:
                                eln:
                                component: NumberEditQuantity
                                defaultDisplayUnit: K
                            description: |
                                Temperature of liquid nitrogen shield. Note: At
                                least one field from head_temperature, cryo_bottom_temperature and cryo_shield_temperature must be provided.
                Sample:
                section:
                    m_annotations:
                    eln: 
                        overview: true
                    quantities:
                    name:
                        type: str
                        m_annotations:
                        eln:
                            component: StringEditQuantity
                        description: |
                        Name of the sample.
                    chemical_formula:
                        type: str
                        m_annotations:
                        eln:
                            component: StringEditQuantity
                        description: |
                        The chemical formula specified using CIF conventions.
                        Abbreviated version of CIF standard:
                        
                        * Only recognized element symbols may be used.
                        * Each element symbol is followed by a 'count' number. A count of '1' may be omitted.
                        * A space or parenthesis must separate each cluster of (element symbol + count).
                        * Where a group of elements is enclosed in parentheses, the multiplier for the
                            group must follow the closing parentheses. That is, all element and group
                            multipliers are assumed to be printed as subscripted numbers.
                        * Unless the elements are ordered in a manner that corresponds to their chemical
                            structure, the order of the elements within any group or moiety depends on
                            whether or not carbon is present.
                        * If carbon is present, the order should be:
                        
                            - C, then H, then the other elements in alphabetical order of their symbol.
                            - If carbon is not present, the elements are listed purely in alphabetic order of their symbol.
                            
                        * This is the *Hill* system used by Chemical Abstracts.
                    description:
                        type: str
                        m_annotations:
                        eln:
                            component: RichTextEditQuantity
                        description: |
                        Description of the sample or sample preparation.
                    sub_sections:
                    Sample_component:
                        section:
                        m_annotations:
                            eln:
                            overview: true
                        description: |
                            A sample component is a part of the sample that is of interest.
                            For example, a sample component could be a layer of a multilayer sample.
                        quantities:
                            name:
                            type: str
                            m_annotations:
                                eln:
                                component: StringEditQuantity
                            description: |
                                Name of the sample component.
                            identifier_component:
                            type: str
                            m_annotations:
                                eln:
                                component: StringEditQuantity
                            description: |
                                An unique identifier for the sample component.
                            chemical_formula:
                            type: str
                            m_annotations:
                                eln:
                                component: StringEditQuantity
                            description: |
                                The chemical formula specified using CIF conventions.
                                Abbreviated version of CIF standard:
                                
                                * Only recognized element symbols may be used.
                                * Each element symbol is followed by a 'count' number. A count of '1' may be omitted.
                                * A space or parenthesis must separate each cluster of (element symbol + count).
                                * Where a group of elements is enclosed in parentheses, the multiplier for the
                                group must follow the closing parentheses. That is, all element and group
                                multipliers are assumed to be printed as subscripted numbers.
                                * Unless the elements are ordered in a manner that corresponds to their chemical
                                structure, the order of the elements within any group or moiety depends on
                                whether or not carbon is present.
                                * If carbon is present, the order should be:
                                
                                - C, then H, then the other elements in alphabetical order of their symbol.
                                - If carbon is not present, the elements are listed purely in alphabetic order of their symbol.
                                
                                * This is the *Hill* system used by Chemical Abstracts.
                            description:
                            type: str
                            m_annotations:
                                eln:
                                component: RichTextEditQuantity
                            description: |
                                Description of the sample component or sample preparation.
                    history:
                        section:
                        m_annotations:
                            eln:
                            overview: true
                        sub_sections:
                            Note:
                            section:
                                m_annotations:
                                eln:
                                    overview: true
                                description: |
                                Notes about the sample history.
                                quantities:
                                description:
                                    type: str
                                    m_annotations:
                                    eln:
                                        component: RichTextEditQuantity
                                    description: |
                                    Title of an image or other details of the note.                          
                        quantities:
                            identifier_history:
                            type: str
                            m_annotations:
                                eln:
                                component: StringEditQuantity
                            description: |
                                Identifier for sample history.
    ```
    </div>

#### __ELN YAML File__ 
The ELN YAML file is a human created ELN and can be used to run reader in Jupyter notebook or local Python environment. For more details please follow the section `ELN YAML File` in [Work with Reader](../how-to-guides/how-to-act-with-reader.md) guide.

=== "Eln YAML File (STS)"
    <div class="scrollable">
    ```yaml
    Sample:
        name: diPAMY
        History:
            Note:
            description: The experiment was run in Carlos' Lab.
        Sample_component:
            chemical_formula: Au(KAl3Si3O12H2)
            description: 'Substrate:
                        Two layers stack: Au-Mica'
            name: Au(Mica)
        default: current_filter_grad
        definition: NXsts
        scan_mode: constant height
        experiment_description: 'The experiment with
        Bias: -50mA
        Setpoint: 25pA'
        Instrument:
        hardware:
            model: Generic5e
            model/@version: 5
            name: Nanonis
            vendor: Nanonis
        lockin_amplifier:
            flip_sign: -1.0
            modulation_signal: Current
        Scan_environment:
            head_temperature:
            unit: K
            value: 10.0
        software:
            model: Generic5e
            model/@version: 5
            name: Nanonis
            vendor: Nanonis
        experiment_technique: STS
        identifier_collection: Au_mica_2023_Y_A_diPAMY_154-211C_370C_1min_385C_30min_400C_1min_400C_30min_415_30min_430_30min_11min_30min_30min_20230419_
        identifier_experiment: Au_mica_2023_Y_A_diPAMY_154-211C_370C_1min_385C_30min_400C_1min_400C_30min_415_30min_430_30min_11min_30min_30min_20230416_20230420
        User:
        affiliation:
        - Name 1
        - Name 2
        - Name 3
        email:
        - name3@physik.hu-berlin.de
        - name2@physik.hu-berlin.de
        - name4@physik.hu-berlin.de
        - name5@physik.hu-berlin.de
        name: name5
    ```
    </div>
=== "Eln YAML File (STM)"
    <div class="scrollable">
    ```yaml
    Sample:
        History:
            Note:
            description: Sample History goes here.
        name: diPAMY
        chemical_formula: Au(KAl3Si3012H2)
        description: 'Substrate: Stack of two layers: Au(111) on Mica'

        default: current_forward
        definition: NXstm
        experiment_description: 'Experiment with
        Bias: -50mV
        Setpoint: 25pA'
        Instrument:
        hardware:
            model: Generic 5
            model/@version: 5
            name: Nanonis
            vendor: Nanonis
        software:
            vendor: Nanonis
            name: Nanonis
            model: Generic 5
            model/@version: 5
        experiment_technique: STM
        identifier_collection: D:\Data\20230428\Au_mica_2023_Y_A_diPAMY_154-211C_370C_1min_385C_30min_400C_1min_400C_30min_415_30min_430_30min_11min_30min_30min_20230419
        identifier_experiment: D:\Data\20230428\Au_mica_2023_Y_A_diPAMY_154-211C_370C_1min_385C_30min_400C_1min_400C_30min_415_30min_430_30min_11min_30min_30min_20230419_1min_0420_30min_0425_30min_195.sxm
        scan_mode: constant current
        User:
        affiliation:
        - Rubel Mozumder
        - Dr. Cojal González, José David
        - Dr. Carlos-Andres Palma
        email:
        - ycjin@physik.hu-berlin.de
        - rubel.mozumder@physik.hu-berlin.de
        - cojal@physik.hu-berlin.de
        - palma@physik.hu-berlin.de
        name: Yichen Jin
    ```
    </div>
=== "Eln YAML File (AFM)"
    <div class="scrollable">
    ```yaml
    Instrument:
        hardware:
            model: Generic 4
            model/@version: '4'
            name: Nanonis
            vendor: Nanonis
        software:
            model: Generic 4
            model/@version: '4'
            name: Nanonis
            vendor: Nanonis
        Sample:
        Sample_component:
            chemical_formula: ' KAl₂(AlSi₃O₁₀)(OH)₂)'
            description: <p>Gold on Mica.</p>
            name: Au(Mica)
        History:
            Note:
            description: "Demo description: This sample is used in Palma's lab."
        name: diPAMY
        default: current_forward
        definition: NXafm
        experiment_description: <p>An demo NeXus example for AFM.&nbsp;</p>
        experiment_technique: AFM
        identifier_collection: D:\\Data\\123306
        identifier_experiment: D:\\Data\\123306\A151216.123306-02602
        scan_mode: tapping mode
        User:
        - affiliation:
        - Dr. Cojal González, José David (HU)
        - Prof. Carlos-Andres Palma (HU)
        email:
        - cojal@physik.hu-berlin.de
        - palma@physik.hu-berlin.de
        - mozumder@physik.hu-berlin.de
        name: Rubel Mozumder
    ```
    </div>