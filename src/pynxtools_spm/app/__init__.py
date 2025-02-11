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

# schema = "pynxtools.nomad.schema.NeXus.Spm"
# schema = "pynxtools.nomad.schema.Spm"

schema = "pynxtools.nomad.schema.Root"

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
                    items=[
                        Menu(
                            title="elements",
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
                        )
                    ],
                ),
                Menu(
                    title="Reproducibilty Parameters",
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
                                    x="data.ENTRY.experiment_instrument.scan_environment.tip_temp__field#pynxtools.nomad.schema.Root#float",
                                ),
                            ],
                        ),
                        Menu(
                            title="Cryo Bottom Temperature",
                            show_header=True,
                            items=[
                                MenuItemHistogram(
                                    x="data.ENTRY.experiment_instrument.scan_environment.cryo_bottom_temp__field#pynxtools.nomad.schema.Root#float",
                                ),
                            ],
                        ),
                        Menu(
                            title="Cryo Shield Temperature",
                            show_header=True,
                            items=[
                                MenuItemHistogram(
                                    x="data.ENTRY.experiment_instrument.scan_environment.cryo_shield_temp__field#pynxtools.nomad.schema.Root#float",
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
                                    x="data.ENTRY.experiment_instrument.lockin_amplifier.reference_amplitude__field#pynxtools.nomad.schema.Root#float",
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
                                    x="data.ENTRY.experiment_instrument.bias_spectroscopy_environment.bias_spectroscopy.bias_sweep.scan_region.scan_start_bias__field#pynxtools.nomad.schema.Root#float",
                                ),
                            ],
                        ),
                        Menu(
                            title="Scan Bias (End)",
                            show_header=True,
                            items=[
                                MenuItemHistogram(
                                    x="data.ENTRY.experiment_instrument.bias_spectroscopy_environment.bias_spectroscopy.bias_sweep.scan_region.scan_end_bias__field#pynxtools.nomad.schema.Root#float",
                                ),
                            ],
                        ),
                        Menu(
                            title="Sweep Number",
                            show_header=True,
                            items=[
                                MenuItemHistogram(
                                    x="data.ENTRY.experiment_instrument.bias_spectroscopy_environment.bias_spectroscopy.bias_sweep.sweep_number__field#pynxtools.nomad.schema.Root#float",
                                ),
                            ],
                        ),
                    ],
                ),
                Menu(
                    title="Resolution Parameters",
                ),
                Menu(
                    title="Temperature",
                    show_header=True,
                    # indentation with respect to the previous Menu Resolution Parameters
                    indentation=1,
                    items=[
                        Menu(
                            title="Tip Temperature",
                            indentation=1,
                            show_header=True,
                            items=[
                                MenuItemHistogram(
                                    x="data.ENTRY.experiment_instrument.scan_environment.tip_temp__field#pynxtools.nomad.schema.Root#float",
                                ),
                            ],
                        )
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
                    "quantity": "data.ENTRY.start_time__field#pynxtools.nomad.schema.Root#datetime",
                    "title": "Start Time",
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
                    "quantity": "entry_type",
                    "title": "Entry Type",
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
                    "quantity": "data.ENTRY.definition__field#pynxtools.nomad.schema.Root#str",
                    "title": "Definition",
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
                    "quantity": "results.material.elements",
                    "title": "Periodic Table",
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
                    "quantity": "data.ENTRY.experiment_instrument.scan_environment.tip_temp__field#pynxtools.nomad.schema.Root#float",
                    "title": "Tip Temperature (Scan Environment)",
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
                    "quantity": "data.ENTRY.experiment_instrument.scan_environment.cryo_bottom_temp__field#pynxtools.nomad.schema.Root#float",
                    "title": "Cryo Bottom Temperature (Scan Environment)",
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
                    "quantity": "data.ENTRY.experiment_instrument.scan_environment.cryo_shield_temp__field#pynxtools.nomad.schema.Root#float",
                    "title": "Cryo Shield Temperature (Scan Environment)",
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
                    "quantity": "data.ENTRY.experiment_instrument.lockin_amplifier.reference_amplitude__field#pynxtools.nomad.schema.Root#float",
                    "title": "Reference Amplitude (Lockin Amplifier)",
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
                    "quantity": "data.ENTRY.experiment_instrument.bias_spectroscopy_environment.bias_spectroscopy.bias_sweep.scan_region.scan_start_bias__field#pynxtools.nomad.schema.Root#float",
                    "title": "Scan Start Bias (Bias Spectroscopy)",
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
                    "quantity": "data.ENTRY.experiment_instrument.bias_spectroscopy_environment.bias_spectroscopy.bias_sweep.scan_region.scan_end_bias__field#pynxtools.nomad.schema.Root#float",
                    "title": "Scan End Bias (Bias Spectroscopy)",
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
                    "quantity": "data.ENTRY.experiment_instrument.bias_spectroscopy_environment.bias_spectroscopy.bias_sweep.sweep_number__field#pynxtools.nomad.schema.Root#float",
                    "title": "Sweep Number (Bias Spectroscopy)",
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
                    "quantity": "data.ENTRY.experiment_instrument.bias_spectroscopy_environment.bias_spectroscopy.positioner_spm.z_controller.z_average_time__field#pynxtools.nomad.schema.Root#int",
                    "title": "Z Average Time (Bias Spectroscopy)",
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
                    "quantity": "data.ENTRY.experiment_instrument.bias_spectroscopy_environment.bias_spectroscopy.circuit.acquisition_time__field#pynxtools.nomad.schema.Root#float",
                    "title": "Acquisition Time (Bias Spectroscopy)",
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
                    "quantity": "data.ENTRY.experiment_instrument.bias_spectroscopy_environment.bias_spectroscopy.circuit.animation_time__field#pynxtools.nomad.schema.Root#float",
                    "title": "Animation Time (Bias Spectroscopy)",
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
                    "quantity": "data.ENTRY.experiment_instrument.current_sensor.current__field#pynxtools.nomad.schema.Root#float",
                    "title": "Current (Current Sensor)",
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
                    "quantity": "data.ENTRY.experiment_instrument.sample_bias_votage.bias_voltage__field#pynxtools.nomad.schema.Root#float",
                    "title": "Bias Voltage (Sample Bias Voltage)",
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
                    "quantity": "data.ENTRY.experiment_instrument.sample_bias_votage.bias_offset__field#pynxtools.nomad.schema.Root#float",
                    "title": "Bias Offset (Sample Bias Voltage)",
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
                    "quantity": "data.ENTRY.experiment_instrument.sample_bias_votage.bias_calibration.coefficients__field#pynxtools.nomad.schema.Root#float",
                    "title": "Bias Calibration Coefficients (Sample Bias Voltage)",
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
                    "quantity": "data.ENTRY.experiment_instrument.current_sensor.current_offset__field#pynxtools.nomad.schema.Root#float",
                    "title": "Current Offset (Current Sensor)",
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
                    "quantity": "data.ENTRY.experiment_instrument.current_sensor.amplifier.current_gain__field#pynxtools.nomad.schema.Root#float",
                    "title": "Current Gain (Current Sensor)",
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
                    "quantity": "data.ENTRY.experiment_instrument.current_sensor.current_calibration.coefficients__field#pynxtools.nomad.schema.Root#float",
                    "title": "Current Calibration Coefficients (Current Sensor)",
                    "layout": {
                        "xxl": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 9, "x": 8},
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
                    "quantity": "data.ENTRY.experiment_instrument.bias_spectroscopy_environment.bias_spectroscopy.positioner_spm.z_offset__field#pynxtools.nomad.schema.Root#float",
                    "title": "Z Offset (Bias Spectroscopy)",
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
                    "quantity": "data.ENTRY.experiment_instrument.bias_spectroscopy_environment.bias_spectroscopy.bias_sweep.end_settling_time__field#pynxtools.nomad.schema.Root#float",
                    "title": "Bias Sweep End Settling Time (Bias Spectroscopy)",
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
                    "quantity": "data.ENTRY.experiment_instrument.bias_spectroscopy_environment.bias_spectroscopy.bias_sweep.first_settling_time__field#pynxtools.nomad.schema.Root#float",
                    "title": "First Settling Time (Bias Spectroscopy)",
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
                    "quantity": "data.ENTRY.experiment_instrument.bias_spectroscopy_environment.bias_spectroscopy.bias_sweep.final_z__field#pynxtools.nomad.schema.Root#float",
                    "title": "Final Z (Bias Spectroscopy)",
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
                    "quantity": "data.ENTRY.experiment_instrument.bias_spectroscopy_environment.bias_spectroscopy.positioner_spm.z_controller.z_controller_hold__field#pynxtools.nomad.schema.Root#float",
                    "title": "Z Controller Hold (Bias Spectroscopy)",
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
                    "quantity": "data.ENTRY.experiment_instrument.bias_spectroscopy_environment.bias_spectroscopy.positioner_spm.controller_name__field#pynxtools.nomad.schema.Root#float",
                    "title": "Controller Name (Bias Spectroscopy)",
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
                    "quantity": "data.ENTRY.experiment_instrument.piezo_sensor.positioner_spm.z_controller.k_i_value__field#pynxtools.nomad.schema.Root#float",
                    "title": "K_I (Piezo PID Controller)",
                    "layout": {
                        "xxl": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 23, "x": 24},
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
                    "quantity": "data.ENTRY.experiment_instrument.piezo_sensor.positioner_spm.z_controller.k_p_value__field#pynxtools.nomad.schema.Root#float",
                    "title": "K_P (Piezo PID Controller)",
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
                    "quantity": "data.ENTRY.experiment_instrument.piezo_sensor.positioner_spm.z_controller.k_t_value__field#pynxtools.nomad.schema.Root#float",
                    "title": "K_T (Piezo PID Controller)",
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
                    "quantity": "data.ENTRY.experiment_instrument.piezo_sensor.positioner_spm.z_controller.switch_off_delay__field#pynxtools.nomad.schema.Root#float",
                    "title": "Switch Off Delay (Piezo PID Controller)",
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
                    "quantity": "data.ENTRY.experiment_instrument.piezo_sensor.positioner_spm.z_controller.tip_lift__field#pynxtools.nomad.schema.Root#float",
                    "title": "Tip Lift (Piezo PID Controller)",
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
                    "quantity": "data.ENTRY.experiment_instrument.bias_spectroscopy_environment.bias_spectroscopy.circuit.measurement_time__field#pynxtools.nomad.schema.Root#float",
                    "title": "Measurement Time (Bias Spectroscopy)",
                    "layout": {
                        "xxl": {"minH": 3, "minW": 3, "h": 3, "w": 8, "y": 30, "x": 0},
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
                    "quantity": "data.ENTRY.experiment_instrument.bias_spectroscopy_environment.bias_spectroscopy.circuit.indicators_period__field#pynxtools.nomad.schema.Root#float",
                    "title": "Indicators Period (Bias Spectroscopy)",
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
                    "quantity": "data.ENTRY.experiment_instrument.bias_spectroscopy_environment.bias_spectroscopy.bias_sweep.max_slew_rate__field#pynxtools.nomad.schema.Root#float",
                    "title": "Max Slew Rate (Bias Spectroscopy)",
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
                    "quantity": "data.ENTRY.experiment_instrument.bias_spectroscopy_environment.bias_spectroscopy.positioner_spm.z_controller.z_controller_time__field#pynxtools.nomad.schema.Root#float",
                    "title": "Z Controller Time (Bias Spectroscopy)",
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
