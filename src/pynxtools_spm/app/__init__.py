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
#

from nomad.config.models.plugins import AppEntryPoint
from nomad.config.models.ui import (
    App,
    Column,
    Menu,
    MenuItemTerms,
    MenuItemPeriodicTable,
    MenuItemHistogram,
    SearchQuantities,
)


schema = "pynxtools.nomad.schema.Root"

map_concept_to_full_quantities = {
    "Start Time": f"data.ENTRY.start_time__field#{schema}#datetime",
    "Entry Type": "entry_type",
    "Definition": f"data.ENTRY.definition__field#{schema}#str",
    "Periodic Table": "results.material.elements",
    "Tip Temperature (Scan Environment)": f"data.ENTRY.experiment_instrument.scan_environment.tip_temp__field#{schema}#float",
    "Cryo Bottom Temperature (Scan Environment)": f"data.ENTRY.experiment_instrument.scan_environment.cryo_bottom_temp__field#{schema}#float",
    "Cryo Shield Temperature (Scan Environment)": f"data.ENTRY.experiment_instrument.scan_environment.cryo_shield_temp__field#{schema}#float",
    "Reference Amplitude (Lockin Amplifier)": f"data.ENTRY.experiment_instrument.lockin_amplifier.reference_amplitude__field#{schema}#float",
    "Scan Start Bias (Bias Spectroscopy)": f"data.ENTRY.experiment_instrument.bias_spectroscopy_environment.bias_spectroscopy.bias_sweep.scan_region.scan_start_bias__field#{schema}#float",
    "Scan End Bias (Bias Spectroscopy)": f"data.ENTRY.experiment_instrument.bias_spectroscopy_environment.bias_spectroscopy.bias_sweep.scan_region.scan_end_bias__field#{schema}#float",
    "Sweep Number (Bias Spectroscopy)": f"data.ENTRY.experiment_instrument.bias_spectroscopy_environment.bias_spectroscopy.bias_sweep.sweep_number__field#{schema}#float",
    "Z Average Time (Bias Spectroscopy)": f"data.ENTRY.experiment_instrument.bias_spectroscopy_environment.bias_spectroscopy.positioner_spm.z_controller.z_average_time__field#{schema}#int",
    "Acquisition Time (Bias Spectroscopy)": f"data.ENTRY.experiment_instrument.bias_spectroscopy_environment.bias_spectroscopy.circuit.acquisition_time__field#{schema}#float",
    "Animation Time (Bias Spectroscopy)": f"data.ENTRY.experiment_instrument.bias_spectroscopy_environment.bias_spectroscopy.circuit.animation_time__field#{schema}#float",
    "Current (Current Sensor)": f"data.ENTRY.experiment_instrument.current_sensor.current__field#{schema}#float",
    "Bias Voltage (Sample Bias Voltage)": f"data.ENTRY.experiment_instrument.sample_bias_votage.bias_voltage__field#{schema}#float",
    "Bias Offset (Sample Bias Voltage)": f"data.ENTRY.experiment_instrument.sample_bias_votage.bias_offset__field#{schema}#float",
    "Bias Calibration Coefficients (Sample Bias Voltage)": f"data.ENTRY.experiment_instrument.sample_bias_votage.bias_calibration.coefficients__field#{schema}#float",
    "Current Offset (Current Sensor)": f"data.ENTRY.experiment_instrument.current_sensor.current_offset__field#{schema}#float",
    "Current Gain (Current Sensor)": f"data.ENTRY.experiment_instrument.current_sensor.current_gain__field#{schema}#float",
    "Current Calibration Coefficients (Current Sensor)": f"data.ENTRY.experiment_instrument.current_sensor.current_calibration.coefficients__field#{schema}#float",
    "Z Offset (Bias Spectroscopy)": f"data.ENTRY.experiment_instrument.bias_spectroscopy_environment.bias_spectroscopy.positioner_spm.z_controller.z_offset__field#{schema}#float",
    "Bias Sweep End Settling Time (Bias Spectroscopy)": f"data.ENTRY.experiment_instrument.bias_spectroscopy_environment.bias_spectroscopy.bias_sweep.end_settling_time__field#{schema}#float",
    "First Settling Time (Bias Spectroscopy)": f"data.ENTRY.experiment_instrument.bias_spectroscopy_environment.bias_spectroscopy.first_settling_time__field#{schema}#float",
    "Final Z (Bias Spectroscopy)": f"data.ENTRY.experiment_instrument.bias_spectroscopy_environment.bias_spectroscopy.bias_sweep.final_z__field#{schema}#float",
    "Z Controller Hold (Bias Spectroscopy)": f"data.ENTRY.experiment_instrument.bias_spectroscopy_environment.bias_spectroscopy.positioner_spm.z_controller_hold__field#{schema}#float",
    # TODO: Make the type str of the below quanity and check why its not working
    "Controller Name (Bias Spectroscopy)": f"data.ENTRY.experiment_instrument.bias_spectroscopy_environment.bias_spectroscopy.positioner_spm.name__field#{schema}#float",
    "K_I (Piezo PID Controller)": f"data.ENTRY.experiment_instrument.piezo_sensor.positioner_spm.z_controller.k_i_value__field#{schema}#float",
    "K_P (Piezo PID Controller)": f"data.ENTRY.experiment_instrument.piezo_sensor.positioner_spm.z_controller.k_p_value__field#{schema}#float",
    "K_T (Piezo PID Controller)": f"data.ENTRY.experiment_instrument.piezo_sensor.positioner_spm.z_controller.k_t_value__field#{schema}#float",
    "Switch Off Delay (Piezo PID Controller)": f"data.ENTRY.experiment_instrument.piezo_sensor.positioner_spm.z_controller.switch_off_delay__field#{schema}#float",
    "Tip Lift (Piezo PID Controller)": f"data.ENTRY.experiment_instrument.piezo_sensor.positioner_spm.z_controller.tip_lift__field#{schema}#float",
    "Measurement Time (Bias Spectroscopy)": f"data.ENTRY.experiment_instrument.bias_spectroscopy_environment.bias_spectroscopy.circuit.measurement_time__field#{schema}#float",
    "Indicators Period (Bias Spectroscopy)": f"data.ENTRY.experiment_instrument.bias_spectroscopy_environment.bias_spectroscopy.circuit.indicators_period__field#{schema}#float",
    "Max Slew Rate (Bias Spectroscopy)": f"data.ENTRY.experiment_instrument.bias_spectroscopy_environment.bias_spectroscopy.bias_sweep.max_slew_rate__field#{schema}#float",
    "Z Controller Time (Bias Spectroscopy)": f"data.ENTRY.experiment_instrument.bias_spectroscopy_environment.bias_spectroscopy.positioner_spm.z_controller.z_controller_time__field#{schema}#float",
}

# import and times to add in search app
# STS:
# positoiner_spm.z_controller.set_point
# positioner_spm.z_controller.z
# positioner_spm.z_controller.z_offset
# piezo_sensor.x
# piezo_sensor.y
# piezo_sensor.z
# sample_bias_voltage.bias_voltage
# user.name
# user.affiliation
# lockin_aplifier.reference_amplitude
# lockin_amplifier.reference_frequency
# loackin_current_flip_sign
# current_sensor.current
# current_sensor.current_offset
# bias_spectroscopy_environment.bias_spectroscopy.bias_sweep.scan_region.scan_start_bias
# bias_spectroscopy_environment.bias_spectroscopy.bias_sweep.scan_region.scan_end_bias
# bias_spectroscopy_environment.bias_spectroscopy.bias_sweep.scan_region.scan_offset_bias
# bias_spectroscopy_environment.bias_spectroscopy.bias_sweep.linear_sweep.backward_speed
# bias_spectroscopy_environment.bias_spectroscopy.bias_sweep.linear_sweep.forward_speed

spm_app = AppEntryPoint(
    name="SpmApp",
    description="A Generic NOMAD App for SPM Experimetal Technique.",
    app=App(
        # Label of the App
        label="SPM",
        # Path used in the URL, must be unique
        path="spm_app",
        # Used to categorize apps in the explore menu
        category="Experiment",
        # Brief description used in the app menu
        description="A simple search app customized for SPM experimental technique.",
        # Longer description that can also use markdown
        readme="This is a simple App to support basic search for NeXus based SPM Experiment Entries.",
        # If you want to use quantities from a custom schema, you need to load
        # the search quantities from it first here. Note that you can use a glob
        # syntax to load the entire package, or just a single schema from a
        # package.
        search_quantities=SearchQuantities(
            include=[f"*#{schema}"],
        ),
        # Controls which columns are shown in the results table
        columns=[
            Column(quantity="entry_id", selected=True),
            Column(quantity="entry_type", selected=True),
            Column(
                title="definition",
                quantity=f"data.ENTRY[*].definition__field#{schema}",
                selected=True,
            ),
            Column(
                title="start_time",
                quantity=f"data.ENTRY[*].start_time__field#{schema}",
                selected=True,
            ),
            Column(
                title="title",
                quantity=f"data.ENTRY[*].title__field#{schema}",
                selected=True,
            ),
        ],
        # Dictionary of search filters that are always enabled for queries made
        # within this app. This is especially important to narrow down the
        # results to the wanted subset. Any available search filter can be
        # targeted here. This example makes sure that only entries that use
        # MySchema are included.
        filters_locked={"section_defs.definition_qualified_name": [schema]},
        # Controls the menu shown on the left
        menu=Menu(
            title="Filters",
            show_header=True,
            items=[
                Menu(
                    title="Material",
                    # items=[
                    #     Menu(
                    #         title="elements",
                    show_header=True,
                    items=[
                        MenuItemPeriodicTable(
                            quantity="results.material.elements",
                        ),
                        MenuItemTerms(
                            quantity="results.material.chemical_formula_hill",
                            width=6,
                            options=0,
                        ),
                        MenuItemTerms(
                            quantity="results.material.chemical_formula_iupac",
                            width=6,
                            options=0,
                        ),
                        MenuItemHistogram(
                            x="results.material.n_elements",
                        ),
                    ],
                    # )
                    # ],
                ),
                Menu(
                    title="Reproducibilty & Resolution Parameters",
                ),
                Menu(
                    title="Temperature",
                    show_header=True,
                    indentation=1,
                    items=[
                        Menu(
                            title="Tip Temperature",
                            show_header=True,
                            items=[
                                MenuItemHistogram(
                                    title="Tip Temperature test",
                                    x=map_concept_to_full_quantities[
                                        "Tip Temperature (Scan Environment)"
                                    ],
                                ),
                            ],
                        ),
                        Menu(
                            title="Cryo Bottom Temperature",
                            show_header=True,
                            items=[
                                MenuItemHistogram(
                                    title="Cryo Bottom Temperature test",
                                    x=map_concept_to_full_quantities[
                                        "Cryo Bottom Temperature (Scan Environment)"
                                    ],
                                ),
                            ],
                        ),
                        Menu(
                            title="Cryo Shield Temperature",
                            show_header=True,
                            items=[
                                MenuItemHistogram(
                                    x=map_concept_to_full_quantities[
                                        "Cryo Shield Temperature (Scan Environment)"
                                    ],
                                ),
                            ],
                        ),
                    ],
                ),
                Menu(
                    title="Lockin Amplifier",
                    indentation=1,
                    items=[
                        Menu(
                            title="Reference Amplitude",
                            show_header=True,
                            items=[
                                MenuItemHistogram(
                                    x=map_concept_to_full_quantities[
                                        "Reference Amplitude (Lockin Amplifier)"
                                    ],
                                ),
                            ],
                        ),
                    ],
                ),
                Menu(
                    title="Bias Spectroscopy",
                    indentation=1,
                    items=[
                        Menu(
                            title="Scan Bias (Start)",
                            show_header=True,
                            items=[
                                MenuItemHistogram(
                                    x=map_concept_to_full_quantities[
                                        "Scan Start Bias (Bias Spectroscopy)"
                                    ],
                                ),
                            ],
                        ),
                        Menu(
                            title="Scan Bias (End)",
                            show_header=True,
                            items=[
                                MenuItemHistogram(
                                    x=map_concept_to_full_quantities[
                                        "Scan End Bias (Bias Spectroscopy)"
                                    ],
                                ),
                            ],
                        ),
                        Menu(
                            title="Sweep Number",
                            show_header=True,
                            items=[
                                MenuItemHistogram(
                                    x=map_concept_to_full_quantities[
                                        "Sweep Number (Bias Spectroscopy)"
                                    ],
                                ),
                            ],
                        ),
                    ],
                ),
            ],
        ),
        # Controls the default dashboard shown in the search interface
        dashboard={
            "widgets": [
                {
                    "type": "histogram",
                    "show_input": False,
                    "autorange": True,
                    "nbins": 30,
                    "scale": "linear",
                    "title": "Start Time",
                    "quantity": map_concept_to_full_quantities["Start Time"],
                    "layout": {
                        "xxl": {
                            "minH": 3,
                            "minW": 3,
                            "h": 5,
                            "w": 16,
                            "y": 11,
                            "x": 16,
                        },
                        "xl": {"minH": 3, "minW": 3, "h": 4, "w": 12, "y": 0, "x": 0},
                        "lg": {"minH": 3, "minW": 3, "h": 4, "w": 12, "y": 0, "x": 0},
                        "md": {"minH": 3, "minW": 3, "h": 4, "w": 12, "y": 0, "x": 0},
                        "sm": {"minH": 3, "minW": 3, "h": 4, "w": 12, "y": 0, "x": 0},
                    },
                },
                {
                    "type": "terms",
                    "show_input": False,
                    "scale": "linear",
                    "title": "Entry Type",
                    "quantity": map_concept_to_full_quantities["Entry Type"],
                    "layout": {
                        "xxl": {"minH": 3, "minW": 3, "h": 8, "w": 4, "y": 8, "x": 32},
                        "xl": {"minH": 3, "minW": 3, "h": 8, "w": 4, "y": 0, "x": 12},
                        "lg": {"minH": 3, "minW": 3, "h": 8, "w": 4, "y": 0, "x": 12},
                        "md": {"minH": 3, "minW": 3, "h": 8, "w": 4, "y": 0, "x": 12},
                        "sm": {"minH": 3, "minW": 3, "h": 8, "w": 4, "y": 46, "x": 0},
                    },
                },
                {
                    "type": "terms",
                    "show_input": False,
                    "scale": "linear",
                    "title": "Definition",
                    "quantity": "data.ENTRY.definition__field#pynxtools.nomad.schema.Root#str",
                    "layout": {
                        "xxl": {"minH": 3, "minW": 3, "h": 8, "w": 4, "y": 0, "x": 32},
                        "xl": {"minH": 3, "minW": 3, "h": 8, "w": 4, "y": 0, "x": 16},
                        "lg": {"minH": 3, "minW": 3, "h": 8, "w": 4, "y": 0, "x": 16},
                        "md": {"minH": 3, "minW": 3, "h": 8, "w": 4, "y": 38, "x": 0},
                        "sm": {"minH": 3, "minW": 3, "h": 8, "w": 4, "y": 38, "x": 0},
                    },
                },
                {
                    "type": "periodic_table",
                    "scale": "linear",
                    "title": "Periodic Table",
                    "quantity": map_concept_to_full_quantities["Periodic Table"],
                    "layout": {
                        "xxl": {
                            "minH": 3,
                            "minW": 3,
                            "h": 11,
                            "w": 16,
                            "y": 0,
                            "x": 16,
                        },
                        "xl": {"minH": 3, "minW": 3, "h": 4, "w": 12, "y": 4, "x": 0},
                        "lg": {"minH": 3, "minW": 3, "h": 4, "w": 12, "y": 4, "x": 0},
                        "md": {"minH": 3, "minW": 3, "h": 4, "w": 12, "y": 4, "x": 0},
                        "sm": {"minH": 3, "minW": 3, "h": 4, "w": 12, "y": 4, "x": 0},
                    },
                },
                {
                    "type": "histogram",
                    "show_input": False,
                    "autorange": True,
                    "nbins": 30,
                    "scale": "linear",
                    "title": "Tip Temperature (Scan Environment)",
                    "quantity": map_concept_to_full_quantities[
                        "Tip Temperature (Scan Environment)"
                    ],
                    "layout": {
                        "xxl": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "xl": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "lg": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "md": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 35, "x": 0},
                        "sm": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 35, "x": 0},
                    },
                },
                {
                    "type": "histogram",
                    "show_input": False,
                    "autorange": True,
                    "nbins": 30,
                    "scale": "linear",
                    "title": "Cryo Bottom Temperature (Scan Environment)",
                    "quantity": map_concept_to_full_quantities[
                        "Cryo Bottom Temperature (Scan Environment)"
                    ],
                    "layout": {
                        "xxl": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 3, "x": 0},
                        "xl": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "lg": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "md": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 32, "x": 0},
                        "sm": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 32, "x": 0},
                    },
                },
                {
                    "type": "histogram",
                    "show_input": False,
                    "autorange": True,
                    "nbins": 30,
                    "scale": "linear",
                    "title": "Cryo Shield Temperature (Scan Environment)",
                    "quantity": map_concept_to_full_quantities[
                        "Cryo Shield Temperature (Scan Environment)"
                    ],
                    "layout": {
                        "xxl": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 6, "x": 0},
                        "xl": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "lg": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "md": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 29, "x": 0},
                        "sm": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 29, "x": 0},
                    },
                },
                {
                    "type": "histogram",
                    "show_input": False,
                    "autorange": True,
                    "nbins": 30,
                    "scale": "linear",
                    "title": "Reference Amplitude (Lockin Amplifier)",
                    "quantity": map_concept_to_full_quantities[
                        "Reference Amplitude (Lockin Amplifier)"
                    ],
                    "layout": {
                        "xxl": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 21, "x": 0},
                        "xl": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "lg": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "md": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 26, "x": 0},
                        "sm": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 26, "x": 0},
                    },
                },
                {
                    "type": "histogram",
                    "show_input": False,
                    "autorange": True,
                    "nbins": 30,
                    "scale": "linear",
                    "title": "Scan Start Bias (Bias Spectroscopy)",
                    "quantity": map_concept_to_full_quantities[
                        "Scan Start Bias (Bias Spectroscopy)"
                    ],
                    "layout": {
                        "xxl": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 9, "x": 0},
                        "xl": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "lg": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "md": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 23, "x": 0},
                        "sm": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 23, "x": 0},
                    },
                },
                {
                    "type": "histogram",
                    "show_input": False,
                    "autorange": True,
                    "nbins": 30,
                    "scale": "linear",
                    "title": "Scan End Bias (Bias Spectroscopy)",
                    "quantity": map_concept_to_full_quantities[
                        "Scan End Bias (Bias Spectroscopy)"
                    ],
                    "layout": {
                        "xxl": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 12, "x": 0},
                        "xl": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "lg": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "md": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 20, "x": 0},
                        "sm": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 20, "x": 0},
                    },
                },
                {
                    "type": "histogram",
                    "show_input": False,
                    "autorange": True,
                    "nbins": 30,
                    "scale": "linear",
                    "title": "Sweep Number (Bias Spectroscopy)",
                    "quantity": map_concept_to_full_quantities[
                        "Sweep Number (Bias Spectroscopy)"
                    ],
                    "layout": {
                        "xxl": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 15, "x": 0},
                        "xl": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "lg": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "md": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 17, "x": 0},
                        "sm": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 17, "x": 0},
                    },
                },
                {
                    "type": "histogram",
                    "show_input": False,
                    "autorange": True,
                    "nbins": 30,
                    "scale": "linear",
                    "title": "Z Average Time (Bias Spectroscopy)",
                    "quantity": map_concept_to_full_quantities[
                        "Z Average Time (Bias Spectroscopy)"
                    ],
                    "layout": {
                        "xxl": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 18, "x": 0},
                        "xl": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "lg": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "md": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 14, "x": 0},
                        "sm": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 14, "x": 0},
                    },
                },
                {
                    "type": "histogram",
                    "show_input": False,
                    "autorange": True,
                    "nbins": 30,
                    "scale": "linear",
                    "title": "Acquisition Time (Bias Spectroscopy)",
                    "quantity": map_concept_to_full_quantities[
                        "Acquisition Time (Bias Spectroscopy)"
                    ],
                    "layout": {
                        "xxl": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 27, "x": 0},
                        "xl": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "lg": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "md": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 11, "x": 0},
                        "sm": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 11, "x": 0},
                    },
                },
                {
                    "type": "histogram",
                    "show_input": False,
                    "autorange": True,
                    "nbins": 30,
                    "scale": "linear",
                    "title": "Animation Time (Bias Spectroscopy)",
                    "quantity": map_concept_to_full_quantities[
                        "Animation Time (Bias Spectroscopy)"
                    ],
                    "layout": {
                        "xxl": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 24, "x": 0},
                        "xl": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "lg": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "md": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 8, "x": 0},
                        "sm": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 8, "x": 0},
                    },
                },
                {
                    "type": "histogram",
                    "show_input": False,
                    "autorange": True,
                    "nbins": 30,
                    "scale": "linear",
                    "title": "Current (Current Sensor)",
                    "quantity": map_concept_to_full_quantities[
                        "Current (Current Sensor)"
                    ],
                    "layout": {
                        "xxl": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 8},
                        "xl": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "lg": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "md": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "sm": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                    },
                },
                {
                    "type": "histogram",
                    "show_input": False,
                    "autorange": True,
                    "nbins": 30,
                    "scale": "linear",
                    "title": "Bias Voltage (Sample Bias Voltage)",
                    "quantity": map_concept_to_full_quantities[
                        "Bias Voltage (Sample Bias Voltage)"
                    ],
                    "layout": {
                        "xxl": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 12, "x": 8},
                        "xl": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "lg": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "md": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "sm": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                    },
                },
                {
                    "type": "histogram",
                    "show_input": False,
                    "autorange": True,
                    "nbins": 30,
                    "scale": "linear",
                    "title": "Bias Offset (Sample Bias Voltage)",
                    "quantity": map_concept_to_full_quantities[
                        "Bias Offset (Sample Bias Voltage)"
                    ],
                    "layout": {
                        "xxl": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 15, "x": 8},
                        "xl": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "lg": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "md": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "sm": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                    },
                },
                {
                    "type": "histogram",
                    "show_input": False,
                    "autorange": True,
                    "nbins": 30,
                    "scale": "linear",
                    "title": "Bias Calibration Coefficients (Sample Bias Voltage)",
                    "quantity": map_concept_to_full_quantities[
                        "Bias Calibration Coefficients (Sample Bias Voltage)"
                    ],
                    "layout": {
                        "xxl": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 18, "x": 8},
                        "xl": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "lg": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "md": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "sm": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                    },
                },
                {
                    "type": "histogram",
                    "show_input": False,
                    "autorange": True,
                    "nbins": 30,
                    "scale": "linear",
                    "title": "Current Offset (Current Sensor)",
                    "quantity": map_concept_to_full_quantities[
                        "Current Offset (Current Sensor)"
                    ],
                    "layout": {
                        "xxl": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 3, "x": 8},
                        "xl": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "lg": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "md": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "sm": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                    },
                },
                {
                    "type": "histogram",
                    "show_input": False,
                    "autorange": True,
                    "nbins": 30,
                    "scale": "linear",
                    "title": "Current Gain (Current Sensor)",
                    "quantity": map_concept_to_full_quantities[
                        "Current Gain (Current Sensor)"
                    ],
                    "layout": {
                        "xxl": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 6, "x": 8},
                        "xl": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "lg": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "md": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "sm": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                    },
                },
                {
                    "type": "histogram",
                    "show_input": False,
                    "autorange": True,
                    "nbins": 30,
                    "scale": "linear",
                    "title": "Current Calibration Coefficients (Current Sensor)",
                    "quantity": map_concept_to_full_quantities[
                        "Current Calibration Coefficients (Current Sensor)"
                    ],
                    "layout": {
                        "xxl": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 9, "x": 8},
                        "xl": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "lg": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "md": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "sm": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                    },
                },
                ###
                {
                    "type": "histogram",
                    "show_input": False,
                    "autorange": True,
                    "nbins": 30,
                    "scale": "linear",
                    "title": "Z Offset (Bias Spectroscopy)",
                    "quantity": map_concept_to_full_quantities[
                        "Z Offset (Bias Spectroscopy)"
                    ],
                    "layout": {
                        "xxl": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 30, "x": 8},
                        "xl": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "lg": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "md": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "sm": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                    },
                },
                {
                    "type": "histogram",
                    "show_input": False,
                    "autorange": True,
                    "nbins": 30,
                    "scale": "linear",
                    "title": "Bias Sweep End Settling Time (Bias Spectroscopy)",
                    "quantity": map_concept_to_full_quantities[
                        "Bias Sweep End Settling Time (Bias Spectroscopy)"
                    ],
                    "layout": {
                        "xxl": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 24, "x": 8},
                        "xl": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "lg": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "md": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "sm": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                    },
                },
                {
                    "type": "histogram",
                    "show_input": False,
                    "autorange": True,
                    "nbins": 30,
                    "scale": "linear",
                    "title": "First Settling Time (Bias Spectroscopy)",
                    "quantity": map_concept_to_full_quantities[
                        "First Settling Time (Bias Spectroscopy)"
                    ],
                    "layout": {
                        "xxl": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 21, "x": 8},
                        "xl": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "lg": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "md": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "sm": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                    },
                },
                {
                    "type": "histogram",
                    "show_input": False,
                    "autorange": True,
                    "nbins": 30,
                    "scale": "linear",
                    "title": "Final Z (Bias Spectroscopy)",
                    "quantity": map_concept_to_full_quantities[
                        "Final Z (Bias Spectroscopy)"
                    ],
                    "layout": {
                        "xxl": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 27, "x": 8},
                        "xl": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "lg": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "md": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "sm": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                    },
                },
                {
                    "type": "histogram",
                    "show_input": False,
                    "autorange": True,
                    "nbins": 30,
                    "scale": "linear",
                    "title": "Z Controller Hold (Bias Spectroscopy)",
                    "quantity": map_concept_to_full_quantities[
                        "Z Controller Hold (Bias Spectroscopy)"
                    ],
                    "layout": {
                        "xxl": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 33, "x": 8},
                        "xl": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "lg": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "md": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "sm": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                    },
                },
                {
                    "type": "histogram",
                    "show_input": False,
                    "autorange": True,
                    "nbins": 30,
                    "scale": "linear",
                    "title": "Controller Name (Bias Spectroscopy)",
                    "quantity": map_concept_to_full_quantities[
                        "Controller Name (Bias Spectroscopy)"
                    ],
                    "layout": {
                        "xxl": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 26, "x": 16},
                        "xl": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "lg": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "md": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "sm": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                    },
                },
                {
                    "type": "histogram",
                    "show_input": False,
                    "autorange": True,
                    "nbins": 30,
                    "scale": "linear",
                    "title": "K_I (Piezo PID Controller)",
                    "quantity": map_concept_to_full_quantities[
                        "K_I (Piezo PID Controller)"
                    ],
                    "layout": {
                        "xxl": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 23, "x": 24},
                        "xl": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "lg": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "md": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "sm": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                    },
                },
                ##
                {
                    "type": "histogram",
                    "show_input": False,
                    "autorange": True,
                    "nbins": 30,
                    "scale": "linear",
                    "title": "K_P (Piezo PID Controller)",
                    "quantity": map_concept_to_full_quantities[
                        "K_P (Piezo PID Controller)"
                    ],
                    "layout": {
                        "xxl": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 20, "x": 24},
                        "xl": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "lg": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "md": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "sm": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                    },
                },
                {
                    "type": "histogram",
                    "show_input": False,
                    "autorange": True,
                    "nbins": 30,
                    "scale": "linear",
                    "title": "K_T (Piezo PID Controller)",
                    "quantity": map_concept_to_full_quantities[
                        "K_T (Piezo PID Controller)"
                    ],
                    "layout": {
                        "xxl": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 23, "x": 16},
                        "xl": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "lg": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "md": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "sm": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                    },
                },
                {
                    "type": "histogram",
                    "show_input": False,
                    "autorange": True,
                    "nbins": 30,
                    "scale": "linear",
                    "title": "Switch Off Delay (Piezo PID Controller)",
                    "quantity": map_concept_to_full_quantities[
                        "Switch Off Delay (Piezo PID Controller)"
                    ],
                    "layout": {
                        "xxl": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 17, "x": 24},
                        "xl": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "lg": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "md": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "sm": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                    },
                },
                {
                    "type": "histogram",
                    "show_input": False,
                    "autorange": True,
                    "nbins": 30,
                    "scale": "linear",
                    "title": "Tip Lift (Piezo PID Controller)",
                    "quantity": map_concept_to_full_quantities[
                        "Tip Lift (Piezo PID Controller)"
                    ],
                    "layout": {
                        "xxl": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 17, "x": 16},
                        "xl": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "lg": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "md": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "sm": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                    },
                },
                {
                    "type": "histogram",
                    "show_input": False,
                    "autorange": True,
                    "nbins": 30,
                    "scale": "linear",
                    "title": "Measurement Time (Bias Spectroscopy)",
                    "quantity": map_concept_to_full_quantities[
                        "Measurement Time (Bias Spectroscopy)"
                    ],
                    "layout": {
                        "xxl": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 30, "x": 0},
                        "xl": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "lg": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "md": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "sm": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                    },
                },
                ##
                {
                    "type": "histogram",
                    "show_input": False,
                    "autorange": True,
                    "nbins": 30,
                    "scale": "linear",
                    "title": "Indicators Period (Bias Spectroscopy)",
                    "quantity": map_concept_to_full_quantities[
                        "Indicators Period (Bias Spectroscopy)"
                    ],
                    "layout": {
                        "xxl": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 33, "x": 0},
                        "xl": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "lg": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "md": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "sm": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                    },
                },
                {
                    "type": "histogram",
                    "show_input": False,
                    "autorange": True,
                    "nbins": 30,
                    "scale": "linear",
                    "title": "Max Slew Rate (Bias Spectroscopy)",
                    "quantity": map_concept_to_full_quantities[
                        "Max Slew Rate (Bias Spectroscopy)"
                    ],
                    "layout": {
                        "xxl": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 26, "x": 24},
                        "xl": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "lg": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "md": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "sm": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                    },
                },
                {
                    "type": "histogram",
                    "show_input": False,
                    "autorange": True,
                    "nbins": 30,
                    "scale": "linear",
                    "title": "Z Controller Time (Bias Spectroscopy)",
                    "quantity": map_concept_to_full_quantities[
                        "Z Controller Time (Bias Spectroscopy)"
                    ],
                    "layout": {
                        "xxl": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 20, "x": 16},
                        "xl": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "lg": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "md": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                        "sm": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 0, "x": 0},
                    },
                },
            ]
        },
    ),
)

# data.ENTRY.experiment_instrument.scan_environment.cryo_bottom_temp__field#pynxtools.nomad.schema.Root#float

## Some Resolution histogram path
# data.ENTRY.experiment_instrument.scan_environment.tip_temp__field#pynxtools.nomad.schema.Root#float
# data.ENTRY.experiment_instrument.scan_environment.cryo_bottom_temp__field#pynxtools.nomad.schema.Root#float
# data.ENTRY.experiment_instrument.scan_environment.cryo_shield_temp__field#pynxtools.nomad.schema.Root#float

# data.ENTRY.experiment_instrument.bias_spectroscopy_environment.bias_spectroscopy.bias_sweep.scan_region.scan_end_bias__field#pynxtools.nomad.schema.Root#float
# data.ENTRY.experiment_instrument.bias_spectroscopy_environment.bias_spectroscopy.bias_sweep.scan_region.scan_start_bias__field#pynxtools.nomad.schema.Root#float
# data.ENTRY.experiment_instrument.bias_spectroscopy_environment.bias_spectroscopy.bias_sweep.sweep_number__field#pynxtools.nomad.schema.Root#float
# data.ENTRY.experiment_instrument.bias_spectroscopy_environment.bias_spectroscopy.positioner_spm.z_controller.z_average_time__field#pynxtools.nomad.schema.Root#int
# data.ENTRY.experiment_instrument.lockin_amplifier.reference_amplitude__field#pynxtools.nomad.schema.Root#float
# data.ENTRY.experiment_instrument.bias_spectroscopy_environment.bias_spectroscopy.circuit.acquisition_time__field#pynxtools.nomad.schema.Root#float
# data.ENTRY.experiment_instrument.bias_spectroscopy_environment.bias_spectroscopy.circuit.animation_time__field#pynxtools.nomad.schema.Root#float
# data.ENTRY.experiment_instrument.bias_spectroscopy_environment.bias_spectroscopy.circuit.measurement_time__field#pynxtools.nomad.schema.Root#float
# data.ENTRY.experiment_instrument.bias_spectroscopy_environment.bias_spectroscopy.circuit.indicators_period__field#pynxtools.nomad.schema.Root#float


## Some Reproducibility histogram path
# data.ENTRY.experiment_instrument.current_sensor.current__field#pynxtools.nomad.schema.Root#float
# data.ENTRY.experiment_instrument.current_sensor.current_offset__field#pynxtools.nomad.schema.Root#float
# data.ENTRY.experiment_instrument.current_sensor.amplifier.current_gain__field#pynxtools.nomad.schema.Root#float
# data.ENTRY.experiment_instrument.current_sensor.current_calibration.coefficients__field#pynxtools.nomad.schema.Root#float

# data.ENTRY.experiment_instrument.sample_bias_votage.bias_voltage__field#pynxtools.nomad.schema.Root#float
# data.ENTRY.experiment_instrument.sample_bias_votage.bias_offset__field#pynxtools.nomad.schema.Root#float
# data.ENTRY.experiment_instrument.sample_bias_votage.bias_calibration.coefficients__field#pynxtools.nomad.schema.Root#float

# data.ENTRY.experiment_instrument.bias_spectroscopy_environment.bias_spectroscopy.bias_sweep.first_settling_time__field#pynxtools.nomad.schema.Root#float
# data.ENTRY.experiment_instrument.bias_spectroscopy_environment.bias_spectroscopy.bias_sweep.end_settling_time__field#pynxtools.nomad.schema.Root#float
# data.ENTRY.experiment_instrument.bias_spectroscopy_environment.bias_spectroscopy.bias_sweep.final_z__field#pynxtools.nomad.schema.Root#float
# data.ENTRY.experiment_instrument.bias_spectroscopy_environment.bias_spectroscopy.bias_sweep.max_slew_rate__field#pynxtools.nomad.schema.Root#float
# data.ENTRY.experiment_instrument.bias_spectroscopy_environment.bias_spectroscopy.positioner_spm.z_controller.z_controller_hold__field#pynxtools.nomad.schema.Root#float
# data.ENTRY.experiment_instrument.bias_spectroscopy_environment.bias_spectroscopy.positioner_spm.z_controller.z_controller_time__field#pynxtools.nomad.schema.Root#float

# data.ENTRY.experiment_instrument.piezo_sensor.positioner_spm.z_controller.k_i_value__field#pynxtools.nomad.schema.Root#float
# data.ENTRY.experiment_instrument.piezo_sensor.positioner_spm.z_controller.k_p_value__field#pynxtools.nomad.schema.Root#float
# data.ENTRY.experiment_instrument.piezo_sensor.positioner_spm.z_controller.k_t_value__field#pynxtools.nomad.schema.Root#float
# data.ENTRY.experiment_instrument.piezo_sensor.positioner_spm.z_controller.switch_off_delay__field#pynxtools.nomad.schema.Root#float
# data.ENTRY.experiment_instrument.piezo_sensor.positioner_spm.z_controller.tip_lift__field#pynxtools.nomad.schema.Root#float

# Fix the type check why it does not work with str/string
# data.ENTRY.experiment_instrument.bias_spectroscopy_environment.bias_spectroscopy.positioner_spm.controller_name__field#pynxtools.nomad.schema.Root#string
# data.ENTRY.experiment_instrument.bias_spectroscopy_environment.bias_spectroscopy.positioner_spm.z_controller.z_controller_status__field#pynxtools.nomad.schema.Root#str
