#!/usr/bin/env python3
"""
A default configuration file for Nanonis STM data from SXM file.
"""

# -*- coding: utf-8 -*-
#
# Copyright The NOMAD Authors.
#
# This file is part of NOMAD. See https://nomad-lab.eu for further info.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

_nanonis_stm_sxm_generic_5e = {
    "ENTRY[entry]": {
        "@default": {"raw_path": "@default:current_backward"},
        "collection_identifier": "",
        "definition": "",
        "end_time": "",
        "entry_identifier": "",
        "start_time": "",
        "scan_mode": "",
        "scan_type": "",
        "experiment_identifier": {"identifier": ""},
        "experiment_description": {"raw_path": "/COMMENT"},
        "experiment_instrument": {
            "scan_environment": {
                "tip_temp": {
                    "raw_path": "/Temperature 1/Temperature 1",
                    "@units": "@default:K",
                },
                "cryo_bottom_temp": "",
                "cryo_shield_temp": "",
                "scan_name": {"raw_path": "/Scan/series name"},
                "SCAN_CONTROL[scan_control]": {
                    "scan_name": {"raw_path": "/Scan/series name"},
                    "mesh_SCAN[mesh_scan]": {
                        "backward_speed_N[backward_speed_n]": {
                            "#note": "Derived in construct_scan_pattern_grp",
                            "raw_path": "/Scan/speed backw.",
                            "@units": "/Scan/speed backw./@unit",
                        },
                        "forward_speed_N[forward_speed_n]": {
                            "#note": "Derived in construct_scan_pattern_grp",
                            "raw_path": "/Scan/speed forw.",
                            "@units": "/Scan/speed forw./@unit",
                        },
                        "scan_speed_N[scan_speed_n]": "",
                        "channel_NAME_N[scan_name_n]": "",
                        "scan_points_N[scan_points_n]": {
                            "#note": "Derived in construct_scan_pattern_grp",
                            "raw_path": "/SCAN/PIXELS",
                            "@units": "",
                        },
                        "stepping_N[stepping_n]": {
                            "raw_path": "@default:1",
                            "@units": "",
                        },
                        "step_size_N[step_size_n]": {"raw_path": "", "@units": ""},
                        "scan_time": "",
                        "SCAN_data[scan_data]": "",
                    },
                    "scan_region": {
                        "scan_angle_N[scan_angle_n]": {
                            "raw_path": "/SCAN/ANGLE",
                            "@units": "@default:deg",
                        },
                        "scan_offset_N[scan_offset_n]": {
                            "#note": "Derived in function 'construct_scan_region_grp'.",
                            "raw_path": "/SCAN/OFFSET",
                            "@units": "/Z-Controller/Z/@unit",
                        },
                        "scan_range_N[scan_range_n]": {
                            "#note": "Derived in function 'construct_scan_region_grp'.",
                            "raw_path": "/SCAN/RANGE",
                            "@units": "/Z-Controller/Z/@unit",
                        },
                    },
                    "scan_time_start": "",
                    "scan_time_end": "",
                    "independent_scan_axes": {
                        "#note": "Handled in function _construct_nxscan_controllers",
                        "raw_path": "/SCAN/DIR",
                        "@units": "",
                    },
                    "scan_resolution_N": "",
                    "accuracy_N": "",
                    "scan_type": {"raw_path": "@default:mesh", "@units": ""},
                    "scan_control_type": {
                        "raw_path": "@default:continuous",
                        "@units": "",
                    },
                },
                "SENSOR[sensor]": {
                    "calibration_time": "",
                    "run_control": "",
                    "value": "",
                    "value_timestamp": "",
                },
                "independent_controllers": "",
                "measurement_sensors": "",
                "cryo_shield_temp_sensor": {
                    "calibration_time": "",
                    "run_control": "",
                    "value": "",
                    "value_timestamp": "",
                },
                "cryo_temp_sensor": {
                    "calibration_time": "",
                    "run_control": "",
                    "value": "",
                    "value_timestamp": "",
                },
                "tip_temp_sensor": {
                    "calibration_time": "",
                    "run_control": "",
                    "value": "",
                    "value_timestamp": "",
                },
            },
            "current_sensor": {
                "current": {
                    "raw_path": "/Current/Current",
                    "@units": "/Current/Current/@unit",
                },
                "current_offset": {
                    "raw_path": "/Current/Offset",
                    "@units": "/Current/Offset/@unit",
                },
                "current_calibration": {
                    "coefficients": {
                        "raw_path": "/Current/Calibration",
                        "@units": "/Current/Calibration/@unit",
                    },
                    "calibration_time": "",
                },
                "AMPLIFIER[amplifier]": {"current_gain": {"raw_path": "/Current/Gain"}},
            },
            "LOCKIN[lockin]": {
                "reference_frequency": {
                    "raw_path": "/Lock-in/Frequency",
                    "@units": "@default:Hz",
                },
                "modulation_signal_type": {
                    "raw_path": "/Lock-in/Modulated signal",
                    "@units": "/Lock-in/Modulated signal/@unit",
                },
                "demodulated_signal": {
                    "raw_path": "/Lock-in/Demodulated signal",
                    "@units": "/Lock-in/Demodulated signal/@unit",
                },
                "modulation_status": {"raw_path": "/Lock-in/Lock-in status"},
                "demodulated_frequency": "",
                "demodulated_amplitude": "",
                "demodulator_channels": "",
                "recorded_channels": "",
                "low_pass_N": [
                    {
                        "d1": {
                            "raw_path": "/Lock-in/LP Filter Cutoff D1",
                            "@units": "/Lock-in/LP Filter Cutoff D1/@unit",
                        }
                    },
                    {
                        "d2": {
                            "raw_path": "/Lock-in/LP Filter Cutoff D2",
                            "@units": "/Lock-in/LP Filter Cutoff D2/@unit",
                        }
                    },
                ],
                "lp_filter_order_N": [
                    {
                        "d1": {"raw_path": "/Lock-in/LP Filter Order D1"},
                        "d2": {"raw_path": "/Lock-in/LP Filter Order D2"},
                    }
                ],
                "hi_pass_N": [
                    {
                        "d1": {
                            "raw_path": "/Lock-in/HP Filter Cutoff D1",
                            "@units": "/Lock-in/HP Filter Cutoff D1/@unit",
                        }
                    },
                    {
                        "d2": {
                            "raw_path": "/Lock-in/HP Filter Cutoff D2",
                            "@units": "/Lock-in/HP Filter Cutoff D2/@unit",
                        }
                    },
                ],
                "hp_filter_order_N": [
                    {"d1": {"raw_path": "/Lock-in/HP Filter Order D1"}},
                    {"d2": {"raw_path": "/Lock-in/HP Filter Order D2"}},
                ],
                "ref_phase_N[ref_phase_n]": [
                    {
                        "d1": {
                            "raw_path": "/Lock-in/Reference phase D1",
                            "@units": "/Lock-in/Reference phase D1/@unit",
                        }
                    },
                    {
                        "d2": {
                            "raw_path": "/Lock-in/Reference phase D2",
                            "@units": "/Lock-in/Reference phase D2/@unit",
                        }
                    },
                ],
                "harmonic_order_N[harmonic_order_n]": [
                    {"d1": {"raw_path": "/Lock-in/Harmonic D1"}},
                    {"d2": {"raw_path": "/Lock-in/Harmonic D2"}},
                ],
            },
            "bias_spectroscopy_environment": {
                "BIAS_SPECTROSCOPY[bias_spectroscopy]": {
                    "measurement_type": "",
                    "POSITIONER_SPM[positioner_spm]": {
                        "z_controller": {
                            "z_average_time": {
                                "raw_path": "/Bias Spectroscopy/Z Avg time",  #
                                "@units": "/Bias Spectroscopy/Z Avg time/@unit",
                            },
                            "z_controller_time": {
                                "raw_path": "/Bias Spectroscopy/Z control time",
                                "@units": "/Bias Spectroscopy/Z control time/@unit",
                            },
                            "z_controller_hold": {
                                "raw_path": "/Bias Spectroscopy/Z-controller hold",
                            },
                            "record_final_z": {
                                "raw_path": "/Bias Spectroscopy/Record final Z",
                            },
                        },
                        "z_offset": {
                            "raw_path": "/Bias Spectroscopy/Z offset",
                            "@units": "/Bias Spectroscopy/Z offset/@unit",
                        },
                    },
                    "bias_sweep": {
                        "scan_type": "",
                        "settling_time": {
                            "raw_path": "/Bias Spectroscopy/Settling time",
                            "@units": "/Bias Spectroscopy/Settling time/@unit",
                        },
                        "first_settling_time": {
                            "raw_path": "/Bias Spectroscopy/1st Settling time",
                            "@units": "/Bias Spectroscopy/1st Settling time/@unit",
                        },
                        "end_settling_time": {
                            "raw_path": "/Bias Spectroscopy/End Settling time",
                            "@units": "/Bias Spectroscopy/End Settling time/@unit",
                        },
                        "max_slew_rate": {
                            "raw_path": "/Bias Spectroscopy/Max Slew rate",
                            "@units": "/Bias Spectroscopy/Max Slew rate/@unit",
                        },
                        "final_z": "",
                        "total_spectroscopy_time": "",
                        "sweep_number": {
                            "raw_path": "/Bias Spectroscopy/Number of sweeps"
                        },
                        "scan_region": {
                            "scan_range_bias": "",
                            "scan_offset_bias": "",
                            "scan_angle_N[scan_angle_n]": "",
                            "scan_start_bias": {
                                "raw_path": "/Bias Spectroscopy/Sweep Start",
                                "@units": "/Bias Spectroscopy/Sweep Start/@unit",
                            },
                            "scan_end_bias": {
                                "raw_path": "/Bias Spectroscopy/Sweep End",
                                "@units": "/Bias Spectroscopy/Sweep End/@unit",
                            },
                        },
                        "linear_sweep": {
                            "scan_speed": "",
                            "scan_time": "",
                            "forward_speed_bias": "",
                            "backward_speed_bias": "",
                            "scan_points_bias": {
                                "raw_path": "/Bias Spectroscopy/Num Pixel",
                            },
                            "step_size_bias": "",
                            "reset_bias": "",
                            "backward_weep": {
                                "raw_path": "/Bias Spectroscopy/backward sweep"
                            },
                            "SCAN_data[scan_data]": "",
                        },
                    },
                    "CIRCUIT[circuit]": "",
                },
                "current_sensor": {  # TODO: ADD it to NXstm
                    "AMPLIFIER[amplifier]": {"current_gain": ""},
                    "current": "",
                    "current_calibration": {
                        "calibration_time": "",
                        "coefficients": "",
                    },
                    "current_offset": "",
                },
            },
            "piezo_sensor": {
                "peizo_configuration": {
                    "calibration": {
                        "calibration_type": {
                            "raw_path": "@default:active",
                        },
                        "calibration_coefficient_N[calibration_coefficient_n]": [
                            {
                                "X": {
                                    "raw_path": "/Piezo Configuration/Calib. X",
                                    "@units": "/Piezo Configuration/Calib. X/@unit",
                                }
                            },
                            {
                                "Y": {
                                    "raw_path": "/Piezo Configuration/Calib. Y",
                                    "@units": "/Piezo Configuration/Calib. Y/@unit",
                                }
                            },
                            {
                                "Z": {
                                    "raw_path": "/Piezo Configuration/Calib. Z",
                                    "@units": "/Piezo Configuration/Calib. Z/@unit",
                                },
                            },
                        ],
                        "2nd_order_correction_N[2nd_order_correction_n]": [
                            {
                                "X": {
                                    "raw_path": "/Piezo Configuration/2nd order corr X",
                                    "@units": "/Piezo Configuration/2nd order corr X/@unit",
                                }
                            },
                            {
                                "Y": {
                                    "raw_path": "/Piezo Configuration/2nd order corr Y",
                                    "@units": "/Piezo Configuration/2nd order corr Y/@unit",
                                }
                            },
                            {
                                "Z": {
                                    "raw_path": "/Piezo Configuration/2nd order corr Z",
                                    "@units": "/Piezo Configuration/2nd order corr Z/@unit",
                                }
                            },
                        ],
                        "calibration_name": {
                            "raw_path": "/Piezo Configuration/Active Calib."
                        },
                        "drift_N[drift_n]": [
                            {
                                "X": {
                                    "raw_path": "/Piezo Configuration/Drift X",
                                    "@units": "/Piezo Configuration/Drift X/@unit",
                                }
                            },
                            {
                                "Y": {
                                    "raw_path": "/Piezo Configuration/Drift Y",
                                    "@units": "/Piezo Configuration/Drift Y/@unit",
                                }
                            },
                            {
                                "Z": {
                                    "raw_path": "/Piezo Configuration/Drift Z",
                                    "@units": "/Piezo Configuration/Drift Z/@unit",
                                }
                            },
                        ],
                        "drift_correction_status": {
                            "raw_path": [
                                "/Piezo Configuration/Drift correction status",
                                "/Piezo Calibration/Drift correction status",
                            ]
                        },
                        "hv_gain_N[hv_gain_n]": [
                            {"X": {"raw_path": "/Piezo Configuration/HV Gain X"}},
                            {"Y": {"raw_path": "/Piezo Configuration/HV Gain Y"}},
                            {"Z": {"raw_path": "/Piezo Configuration/HV Gain Z"}},
                        ],
                        "tilt_N[tilt_n]": [
                            {
                                "X": {
                                    "raw_path": "/Piezo Configuration/Tilt X",
                                    "@units": "/Piezo Configuration/Tilt X/@unit",
                                }
                            },
                            {
                                "Y": {
                                    "raw_path": "/Piezo Configuration/Tilt Y",
                                    "@units": "/Piezo Configuration/Tilt X/@unit",
                                }
                            },
                            {
                                "Z": {
                                    "raw_path": "/Piezo Configuration/Tilt Z",
                                    "@units": "/Piezo Configuration/Tilt X/@unit",
                                }
                            },
                        ],
                    },
                    "piezo_material": {
                        "curvature_radius_N": [
                            {
                                "x": {
                                    "raw_path": "/Piezo Configuration/Curvature radius X",
                                    "@units": "/Piezo Configuration/Curvature radius X/@unit",
                                }
                            },
                            {
                                "y": {
                                    "raw_path": "/Piezo Configuration/Curvature radius Y",
                                    "@units": "/Piezo Configuration/Curvature radius Y/@unit",
                                }
                            },
                            {
                                "z": {
                                    "raw_path": "/Piezo Configuration/Curvature radius Z",
                                    "@units": "/Piezo Configuration/Curvature radius Z/@unit",
                                }
                            },
                        ]
                    },
                },
                "POSITIONER_SPM[positioner_spm]": {
                    "z_controller": {
                        "K_i_value[k_i_value]": {"raw_path": "/Z-Controller/P gain"},
                        "K_p_value[k_p_value]": {"raw_path": "/Z-Controller/I gain"},
                        "setpoint": {
                            "raw_path": "/Z-Controller/Setpoint",
                            "@units": "/Z-Controller/Setpoint unit",
                        },
                        "switch_off_delay": "",
                        "K_t_const[k_t_const]": {
                            "raw_path": "/Z-Controller/Time const",
                            "@units": "/Z-Controller/Time const/@unit",
                        },
                        "tip_lift": {
                            "raw_path": "/Z-Controller/TipLift",
                            "@units": "/Z-Controller/TipLift/@unit",
                        },
                        "z": {
                            "raw_path": "/Z-Controller/Z",
                            "@units": "/Z-Controller/Z/@unit",
                        },
                    },
                    "z_offset": "",
                    "tip_position_z": "",
                    "controller_name": {"raw_path": "/Z-Controller/Controller name"},
                    "controller_status": {
                        "raw_path": "/Z-Controller/Controller status"
                    },
                    "switch_off_delay": {
                        "raw_path": "/Z-Controller/Switch off delay",
                        "@units": "/Z-Controller/Switch off delay/@unit",
                    },
                },
                "x": "",
                "y": "",
                "z": "",
            },
            "real_time_controller": {
                "rcs_frequency": {
                    "raw_path": "/NanonisMain/RT Frequency",
                    "@units": "/NanonisMain/RT Frequency/@unit",
                },
                "rcs_model": {
                    "raw_path": "/NanonisMain/RT Release",
                },
                "acquisition_time": {
                    "raw_path": "/NanonisMain/Acquisition Period",
                    "@units": "/NanonisMain/Acquisition Period/@unit",
                },
                "animation_time": {
                    "raw_path": "/NanonisMain/Animations Period",
                    "@units": "/NanonisMain/Animations Period/@unit",
                },
                "measurement_time": {
                    "raw_path": "/NanonisMain/Measurements Period",
                    "@units": "/NanonisMain/Measurements Period/@unit",
                },
                "indicators_period": {
                    "raw_path": "/NanonisMain/Indicators Period",
                    "@units": "/NanonisMain/Indicators Period/@unit",
                },
            },
            "sample_bias_votage": {
                "bias_voltage": {
                    "raw_path": "/Bias/Bias",
                    "@units": "/Bias/Bias/@unit",
                },
                "bias_offset": {
                    "raw_path": "/Bias/Offset",
                    "@units": "/Bias/Offset/@unit",
                },
                "bias_calibration": {
                    "coefficients": {
                        "raw_path": "/Bias/Calibration",
                        "@units": "/Bias/Calibration/@unit",
                    },
                    "calibration_time": "",
                },
            },
        },
        "PROCESS[process]": {"program": ""},
        "SAMPLE[sample]": {"name": ""},
        "USER[user]": {
            "address": "",
            "affiliation": "",
            "email": "",
            "name": "",
            "orcid": "",
            "telephone_number": "",
        },
        "DATA[data]": [
            {
                "data": {
                    "name": "z",
                    "raw_path": "/Z/forward",
                    "@units": "@default:m",
                },
                # Syntax Note: If axis will be provided use the following structure
                # "0": {
                #     "name": "Bias Voltage",
                #     "raw_path": [
                #         "/Excitation/forward",
                #         "/dat_mat_components/Bias/value",
                #     ],
                #     "@units": [
                #         "/dat_mat_components/Bias calc/unit",
                #         "/dat_mat_components/Bias/unit",
                #     ],
                #     # "@long_name": "Bias Voltage",
                # },
                "@title": "Height Plot of STM Experiment (Foward Direction)",
                "grp_name": "z_forward",
            },
            {
                "data": {
                    "name": "z",
                    "raw_path": "/Z/backward",
                    "@units": "@default:m",
                },
                "@title": "Height Plot of STM Experiment (Backward Direction)",
                "grp_name": "z_backward",
            },
            {
                "data": {
                    "name": "current",
                    "raw_path": "/Current/forward",
                    "@units": "@default:A",
                },
                "@title": "Current Plot of STM Experiment (Foward Direction)",
                "grp_name": "current_forward",
            },
            {
                "data": {
                    "name": "current",
                    "raw_path": "/Current/backward",
                    "@units": "@default:A",
                },
                "@title": "Current Plot of STM Experiment (Backward Direction)",
                "grp_name": "current_backward",
            },
        ],
        "reproducibility_indicators": {
            "current": "",
            "current_gain": "",
            "current_offset": "",
            "reference_frequency": "",
            "modulation_signal_type": "",
        },
        "resolution_indicators": {
            "reference_frequency": "",
            "modulation_signal_type": "",
        },
    }
}