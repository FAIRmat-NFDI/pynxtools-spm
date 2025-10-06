# TODO
1. Update the ci/cd with the pyprojectoml file script.
2. Update afm reader write data to the height_piezo_sensor and XY_piezo_sensor instead of piezo_sensor.
3. Add calibration temperature in the all calibration especially for piezo_config_spm base class.
4. Write a drive_frequency and drive_amplitude instead of the reference_frequency and reference_amplitude in cantilever_oscillator.
5. Rethink for cantilever_spm class baseed on the new piezo_sensor and XY_piezo_sensor if it is possible.
6. Use a field called dc_offset_N for channels in NXlockin_amplifier.
7. Expand voltage sensor in STM experiment: 
    - In STM experiment, topography measurement, the height of the tip is being changed upon the applied voltage change with constant current output. So, there are two bias voltages: one is the fixed voltage (offset) and the other is the variable voltage (applied to the sample) in addition to the fixed voltage.
    - Use also the same voltage in the sample environment.
8. In the RHKattributes.json file, for each of the scan there are some keywords-value pairs that we may also collect from the `.sm4`.

    ```
        "long_name": "Topography Backward",
        "units": "m",
        "scaling_factor": 1.0,
        "offset": 0.0,
        "start_time": "2024-01-24T16:27:57.000",
        "notes": "",
        "interpretation": "image",
        "bias": -0.029999995604157448,
        "bias_units": "V",
        "setpoint": -1e-09,
        "setpoint_units": "A",
        "feedback_active": true,
        "feedback_pgain": 1e-10,
        "scan_angle": 0.0,
        "time_per_point": 0.0001896237808978185,
        "filename": "STM_sm4/VT240124_A1_0003.sm4"
    ```
9. ✅ Question for Omicron SM4 STM file:
    - How to define the scan area from the available metadata?
        In a typical scan called `topography`, in the scan matrix, X-axis spans from `0.00000000e+00` to `4.99023443e-08`
        and Y-axis spans from `0.00000000e+00` to `4.99023443e-08`. But there no metadata available to define the scan area. At least I can not figure it out.

        Metadata map:

        {'RHK_PRMdata': '',
        'RHK_PageID': 19581,
        'RHK_PageDataType': 0,
        'RHK_PageDataTypeName': 'RHK_DATA_IMAGE',
        'RHK_PageSourceType': 0,
        'RHK_PageSourceTypeName': 'RHK_SOURCE_RAW',
        'RHK_MinorVer': 6,
        'RHK_Signature': 'STiMage 005.004 1',
        'RHK_PageType': 1,
        'RHK_PageTypeName': 'RHK_PAGE_TOPOGRAPHIC',
        'RHK_DataSubSource': 0,
        'RHK_LineType': 0,
        'RHK_LineTypeName': 'RHK_LINE_NOT_A_LINE',
        'RHK_Xcorner': 0,
        'RHK_Ycorner': 0,
        'RHK_Xsize': 512, ❓❓ Number of pixels in X direction
        'RHK_Ysize': 512, ❓❓ Number of pixels in Y direction
        'RHK_ImageType': 0,
        'RHK_ImageTypeName': 'RHK_IMAGE_NORMAL',
        'RHK_ScanType': 1,
        'RHK_ScanTypeName': 'RHK_SCAN_LEFT',
        'RHK_GroupId': 0,
        'RHK_MinZvalue': 0,
        'RHK_MaxZvalue': 0,
        'RHK_Xscale': -9.765625e-11,  ❓❓ What is the meaning of this value? what is the unit?
        'RHK_Yscale': 9.765625e-11,   ❓❓     ""
        'RHK_Zscale': -7.9139135e-16, ❓❓     ""
        'RHK_XYscale': 0.0,    ❓❓ What is the meaning of this value? what is the unit?
        'RHK_Xoffset': -2.25e-07,
        'RHK_Yoffset': 0.0,
        'RHK_Zoffset': 0.0,
        'RHK_Period': 0.00016412816, ❓❓ What is the meaning of this value? what is the unit?
        'RHK_Bias': -1.0,
        'RHK_Current': -4e-10,
        'RHK_Angle': 0.0,
        'RHK_GridXsize': 0,
        'RHK_GridYsize': 0,
        'RHK_Label': 'Topography',
        'RHK_SystemText': '',
        'RHK_SessionText': '',
        'RHK_UserText': '',
        'RHK_FileName': './from_dario/VT220120_A2_0001.sm4',
        'RHK_Date': '01/20/22',
        'RHK_Time': '16:07:09',
        'RHK_Xunits': 'm',
        'RHK_Yunits': 'm',
        'RHK_Zunits': 'm',
        'RHK_Xlabel': '',
        'RHK_Ylabel': 'Topography',
        'RHK_StatusChannelText': '',
        'RHK_CompletedLineCount': 512,
        'RHK_OverSamplingCount': 0,
        'RHK_SlicedVoltage': '',
        'RHK_PLLProStatus': '',
        'RHK_SetpointUnit': 'A',
        'RHK_CH1DriveValue': -1.0,
        'RHK_CH1DriveValueUnits': 'V',
        'RHK_CH2DriveValue': 0.0,
        'RHK_CH2DriveValueUnits': 'V',
        'RHK_DateTime': '2022-01-20T16:07:09.000',
        'RHK_ImageDrift_Filetime': 132871648294581297,
        'RHK_ImageDrift_DriftOptionType': 2,
        'RHK_ImageDrift_DriftOptionTypeName': 'RHK_DRIFT_EACH_LOCATION',
        'RHK_ImageDrift_Time': 86.13445,
        'RHK_ImageDrift_dX': 0.0,
        'RHK_ImageDrift_dY': 0.0,
        'RHK_ImageDrift_CumulativeX': 0.0,
        'RHK_ImageDrift_CumulativeY': 0.0,
        'RHK_ImageDrift_VectorX': 0.0,
        'RHK_ImageDrift_VectorY': 0.0,
        'RHK_PiezoSensitivity_TubeX': -5.866e-08,
        'RHK_PiezoSensitivity_TubeY': 5.866e-08,
        'RHK_PiezoSensitivity_TubeZ': -1.133e-08,
        'RHK_PiezoSensitivity_TubeZOffset': 1.133e-08,
        'RHK_PiezoSensitivity_ScanX': 0.0,
        'RHK_PiezoSensitivity_ScanY': 0.0,
        'RHK_PiezoSensitivity_ScanZ': 0.0,
        'RHK_PiezoSensitivity_Actuator': 0.0,
        'RHK_PiezoSensitivity_TubeXUnit': 'm/V',
        'RHK_PiezoSensitivity_TubeYUnit': 'm/V',
        'RHK_PiezoSensitivity_TubeZUnit': 'm/V',
        'RHK_PiezoSensitivity_TubeZOffsetUnit': 'm/V',
        'RHK_PiezoSensitivity_ScanXUnit': '',
        'RHK_PiezoSensitivity_ScanYUnit': '',
        'RHK_PiezoSensitivity_ScanZUnit': '',
        'RHK_PiezoSensitivity_ActuatorUnit': '',
        'RHK_PiezoSensitivity_TubeCalibration': '300K',
        'RHK_PiezoSensitivity_ScanCalibration': '',
        'RHK_PiezoSensitivity_ActuatorCalibration': '',
        'RHK_ScanProcessor_XSlopeCompensation': -0.19,
        'RHK_ScanProcessor_YSlopeCompensation': 0.0,
        'RHK_ScanProcessor_XSlopeCompensationUnit': '%',
        'RHK_ScanProcessor_YSlopeCompensationUnit': '%',
        'RHK_CH1Drive_MasterOscillator': 1,
        'RHK_CH1Drive_Amplitude': 0.009999998845,
        'RHK_CH1Drive_Frequency': 1200.0,
        'RHK_CH1Drive_PhaseOffset': 0.0,
        'RHK_CH1Drive_HarmonicFactor': 1.0,
        'RHK_CH1Drive_AmplitudeUnit': 'V',
        'RHK_CH1Drive_FrequencyUnit': 'Hz',
        'RHK_CH1Drive_PhaseOffsetUnit': 'deg',
        'RHK_CH1Drive_ReservedUnit': '',
        'RHK_CH2Drive_MasterOscillator': 0,
        'RHK_CH2Drive_Amplitude': 0.0,
        'RHK_CH2Drive_Frequency': 0.0,
        'RHK_CH2Drive_PhaseOffset': 0.0,
        'RHK_CH2Drive_HarmonicFactor': 0.0,
        'RHK_CH2Drive_AmplitudeUnit': 'V',
        'RHK_CH2Drive_FrequencyUnit': 'Hz',
        'RHK_CH2Drive_PhaseOffsetUnit': 'deg',
        'RHK_CH2Drive_ReservedUnit': '',
        'RHK_Lockin0_NonMasterOscillator': 1,
        'RHK_Lockin0_Frequency': 0.0,
        'RHK_Lockin0_HarmonicFactor': 1.0,
        'RHK_Lockin0_PhaseOffset': 0.9999998565,
        'RHK_Lockin0_FilterCutoffFrequency': '',
        'RHK_Lockin0_FreqUnit': '',
        'RHK_Lockin0_PhaseUnit': '',
        'RHK_ZPI_SetPoint': -4e-10,
        'RHK_ZPI_ProportionalGain': 1e-10,
        'RHK_ZPI_IntegralGain': 2.2e-06,
        'RHK_ZPI_LowerBound': -1.6995e-06,
        'RHK_ZPI_UpperBound': 1.6995e-06,
        'RHK_ZPI_FeedbackType': 'Logarithmic',
        'RHK_ZPI_SetPointUnit': 'A',
        'RHK_ZPI_ProportionalGainUnit': 'm',
        'RHK_ZPI_IntegralGainUnit': 'm/s',
        'RHK_ZPI_OutputUnit': 'm',
        'RHK_LowPassFilter1_CutoffFrequency': 100.0,
        'RHK_LowPassFilter1_CutoffFrequencyUnits': 'kHz'
        }
        ```

10. Send some other questions to Dario.
    1. In the RHKattributes.json file, there are four dictionary containers:
     `Topography_forward`, `Topography_backward` (constant current mode), `current_forward` and `current_backward` (constant height mode). Therefore, two setpoints would refers to the current and other two would refers to the height.

            ?? But I see that all of them are related to the current.??

11. For omicron make the multiple scan_control for topography and current measurements.

12. Write NXdata and map that NXdata to in NXdata in scan_control in the NXscan. And store the NXdata to be linked to the NXdata in NXscan control.
13. Include data in ELN:
    - tip_temp
    - cryo_temp
    - piezo_temp
    - Remove scan_name from scan_environment

14. Fix links   
    1. <group name="current_sensor" type="NXsensor" optional="true"></group>
    2. <group name="voltage_sensor" type="NXsensor" optional="true"></group>
    3. <group name="piezo_sensor" type="NXsensor" optional="true"></group>
    4. <group name="sample_bias_voltage" type="NXsensor"></group>

15. Make sample hisroty optional=True in the NXsample.
    <group name="history" type="NXhistory">
        <doc>
            A set of physical processes that occurred to the sample prior/during experiment.
        </doc>
    </group>

16. Rename all the partial fields in the NXscan_control. spm_scan_region and spm_scan_pattern.
    e.g., speed_N 
