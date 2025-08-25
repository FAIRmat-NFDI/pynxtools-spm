# TODO
1. Update the ci/cd with the pyprojectoml file script.
2. Update afm reader write data to the height_piezo_sensor and XY_piezo_sensor instead of piezo_sensor.
3. Add calibration temperature in the all calibration especially for piezo_config_spm base class.
4. Write a drive_frequency and drive_amplitude instead of the reference_frequency and reference_amplitude in cantilever_oscillator.
5. Rethink for cantilever_spm class baseed on the new piezo_sensor and XY_piezo_sensor if it is possible.
6. Use a field called dc_offset_N for channels in NXlockin_amplifier.