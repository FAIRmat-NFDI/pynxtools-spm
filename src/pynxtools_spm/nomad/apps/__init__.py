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

"""
SPM app backed by the generated Python metainfo (nexus_parser_v2).

The app targets the ``Spm`` application definition. ``Afm``, ``Stm`` and ``Sts``
entries derive from it, so they are matched through the inheritance mechanism.

Search depth
------------
NOMAD registers dynamically mapped quantities only down to a fixed sub-section
depth for allow-listed NeXus AppDefs.

- Topographic scan (``instrument.scan_environment.spm_scan_control.*``)
- Bias spectroscopy sweep (``instrument.bias_spectroscopy_environment.*``)
- Cantilever oscillator (``instrument.spm_cantilever.cantilever_oscillator.*``)
- Z controller (``instrument.*piezo_sensor.spm_positioner.z_controller.*``)
"""

from nomad.config.models.plugins import AppEntryPoint
from nomad.config.models.ui import (
    App,
    Column,
    Menu,
    MenuItemHistogram,
    MenuItemPeriodicTable,
    MenuItemTerms,
    MenuSizeEnum,
    SearchQuantities,
)

schema = "pynxtools.nomad.metainfo.applications.Spm"

map_concept_to_full_quantities = {
    # Entry level
    "Entry Type": "entry_type",
    "Definition": f"data.definition#{schema}",
    "Technique": f"data.experiment_technique#{schema}",
    "Scan Mode": f"data.scan_mode#{schema}",
    "Start Time": f"data.start_time#{schema}",
    "End Time": f"data.end_time#{schema}",
    "Experiment Description": f"data.experiment_description#{schema}",
    "Periodic Table": "results.material.elements",
    # Sample
    "Sample Name": f"data.sample.name#{schema}",
    "Sample Chemical Formula": f"data.sample.chemical_formula#{schema}",
    # User
    "User Name": f"data.user.name#{schema}",
    "User Affiliation": f"data.user.affiliation#{schema}",
    # Scan Environment
    "Head Temperature (Scan Environment)": (
        f"data.instrument.scan_environment.head_temperature#{schema}"
    ),
    "Cryo Bottom Temperature (Scan Environment)": (
        f"data.instrument.scan_environment.cryo_bottom_temperature#{schema}"
    ),
    "Cryo Shield Temperature (Scan Environment)": (
        f"data.instrument.scan_environment.cryo_shield_temperature#{schema}"
    ),
    # Instrument -> Hardware
    "Name (Hardware)": f"data.instrument.hardware.name#{schema}",
    "Model (Hardware)": f"data.instrument.hardware.model#{schema}",
    "Vendor (Hardware)": f"data.instrument.hardware.vendor#{schema}",
    # Instrument -> Software
    "Name (Software)": f"data.instrument.software.name#{schema}",
    "Model (Software)": f"data.instrument.software.model#{schema}",
    # Instrument -> Current Sensor
    "Current (Current Sensor)": f"data.instrument.current_sensorTAG.current#{schema}",
    "Current Offset (Current Sensor)": (
        f"data.instrument.current_sensorTAG.offset_value#{schema}"
    ),
    # Instrument -> Sample Bias Voltage
    "Bias voltage (Sample Bias Voltage)": (
        f"data.instrument.sample_bias_voltage.bias_voltage#{schema}"
    ),
    "Bias offset (Sample Bias Voltage)": (
        f"data.instrument.sample_bias_voltage.bias_offset_value#{schema}"
    ),
    # Instrument -> Piezo sensor
    "Piezo X (Piezo Sensor XYZ)": f"data.instrument.piezo_sensor.x#{schema}",
    "Piezo Y (Piezo Sensor XYZ)": f"data.instrument.piezo_sensor.y#{schema}",
    "Piezo Z (Piezo Sensor XYZ)": f"data.instrument.piezo_sensor.z#{schema}",
    # Instrument -> Lockin Amplifier
    "Reference Frequency (Lockin Amplifier)": (
        f"data.instrument.lockin_amplifier.reference_frequency#{schema}"
    ),
    "Reference Phase (Lockin Amplifier)": (
        f"data.instrument.lockin_amplifier.reference_phase#{schema}"
    ),
    "Reference Amplitude (Lockin Amplifier)": (
        f"data.instrument.lockin_amplifier.reference_amplitude#{schema}"
    ),
    "Demodulated signal (Lockin Amplifier)": (
        f"data.instrument.lockin_amplifier.demodulated_signal#{schema}"
    ),
    "Lockin Current Flip Sign (Lockin Amplifier)": (
        f"data.instrument.lockin_amplifier.flip_sign#{schema}"
    ),
}


# Sub-sections that repeat, i.e. that the archive stores as a list. Only these
# take a JMESPath projection in a column; the rest must not, or the cell
# resolves to null. Listed here rather than read from the section definitions,
# because importing the schema package from an app module is circular: the
# plugin machinery loads app entry points while the schema is still
# initialising. `test_as_column_matches_metainfo_repeats` asserts that this
# stays in sync with the generated metainfo.
REPEATING_SUB_SECTIONS = frozenset(
    {
        "instrument",
        "sample",
        "user",
        "scan_environment",
        "current_sensorTAG",
    }
)


def as_column(quantity: str) -> str:
    """Turn a filter quantity name into one usable as a results table column.

    Menu items aggregate over the search index and address a quantity by its
    plain name. Table cells instead extract a value from the returned archive
    data with JMESPath, which cannot step into a list implicitly. The projection
    must therefore match the schema exactly, in both directions::

        data.sample.name        -> null   (sample repeats, so it is a list)
        data.sample[*].name     -> ["..."]
        data.instrument.hardware[*].name -> null   (hardware does not repeat)

    Only some sub-sections repeat - ``instrument``, ``sample``, ``user``,
    ``scan_environment`` and ``current_sensorTAG`` do, while ``hardware``,
    ``software``, ``lockin_amplifier``, ``piezo_sensor`` and
    ``sample_bias_voltage`` do not. A projection is therefore inserted at every
    segment named in `REPEATING_SUB_SECTIONS` and nowhere else, at whatever
    depth it occurs.

    The projection is dropped again when the name is turned into an API request
    (``parseJMESPath`` in the GUI keeps only the field names), so filtering and
    sorting are unaffected. Names without a schema are returned unchanged.
    """
    path, separator, schema_suffix = quantity.partition("#")
    if not separator or not path.startswith("data."):
        return quantity

    segments = [
        f"{part}[*]" if part in REPEATING_SUB_SECTIONS else part
        for part in path.split(".")
    ]
    return f"{'.'.join(segments)}{separator}{schema_suffix}"


spm_app: AppEntryPoint = AppEntryPoint(
    name="SpmApp",
    description="A Generic NOMAD App for SPM Experiment Technique.",
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
        readme=(
            "Search app for SPM entries parsed by the annotation-based parser "
            "(nexus_parser_v2). Covers NXafm, NXstm and NXsts entries through "
            "their shared NXspm application definition."
        ),
        # Load the search quantities of the SPM application definition. The glob
        # syntax pulls in every quantity registered for this schema.
        search_quantities=SearchQuantities(
            include=[f"*#{schema}"],
        ),
        # Controls which columns are shown in the results table
        columns=[
            Column(search_quantity="entry_id", selected=True),
            Column(
                search_quantity=map_concept_to_full_quantities["Entry Type"],
                selected=True,
            ),
            Column(
                title="Definition",
                search_quantity=as_column(map_concept_to_full_quantities["Definition"]),
                selected=True,
            ),
            Column(
                title="Technique",
                search_quantity=as_column(map_concept_to_full_quantities["Technique"]),
                selected=True,
            ),
            Column(
                title="Start Time",
                search_quantity=as_column(map_concept_to_full_quantities["Start Time"]),
                selected=True,
            ),
            Column(
                title="Sample",
                search_quantity=as_column(
                    map_concept_to_full_quantities["Sample Name"]
                ),
                selected=True,
            ),
            Column(
                title="Author",
                search_quantity=as_column(map_concept_to_full_quantities["User Name"]),
                selected=False,
            ),
        ],
        # Only entries that use the SPM application definition are shown. Afm,
        # Stm and Sts derive from Spm, so they are included as well.
        filters_locked={"section_defs.definition_qualified_name": [schema]},
        # Controls the menu shown on the left
        menu=Menu(
            title="Filters",
            size=MenuSizeEnum.SM,
            show_header=True,
            items=[
                Menu(
                    title="Material",
                    size=MenuSizeEnum.XXL,
                    show_header=True,
                    items=[
                        MenuItemPeriodicTable(
                            search_quantity="results.material.elements",
                        ),
                        MenuItemTerms(
                            search_quantity="results.material.chemical_formula_hill",
                            width=6,
                            options=0,
                        ),
                        MenuItemTerms(
                            search_quantity="results.material.chemical_formula_iupac",
                            width=6,
                            options=0,
                        ),
                        MenuItemHistogram(
                            x="results.material.n_elements",
                        ),
                    ],
                ),
                Menu(
                    title="Experiment",
                    show_header=True,
                    items=[
                        MenuItemTerms(
                            title="Definition",
                            search_quantity=map_concept_to_full_quantities[
                                "Definition"
                            ],
                        ),
                        MenuItemTerms(
                            title="Technique",
                            search_quantity=map_concept_to_full_quantities["Technique"],
                        ),
                        MenuItemTerms(
                            title="Scan Mode",
                            search_quantity=map_concept_to_full_quantities["Scan Mode"],
                        ),
                        MenuItemTerms(
                            title="Entry Type",
                            search_quantity=map_concept_to_full_quantities[
                                "Entry Type"
                            ],
                        ),
                    ],
                ),
                Menu(
                    title="Scan Environment",
                ),
                Menu(
                    title="Temperature",
                    indentation=1,
                    show_header=True,
                    items=[
                        MenuItemHistogram(
                            title="Head Temperature",
                            x=map_concept_to_full_quantities[
                                "Head Temperature (Scan Environment)"
                            ],
                        ),
                        MenuItemHistogram(
                            title="Cryo Bottom Temperature",
                            x=map_concept_to_full_quantities[
                                "Cryo Bottom Temperature (Scan Environment)"
                            ],
                        ),
                        MenuItemHistogram(
                            title="Cryo Shield Temperature",
                            x=map_concept_to_full_quantities[
                                "Cryo Shield Temperature (Scan Environment)"
                            ],
                        ),
                    ],
                ),
                Menu(
                    title="Instrument",
                ),
                Menu(
                    title="Hardware",
                    indentation=1,
                    show_header=True,
                    items=[
                        MenuItemTerms(
                            title="Name",
                            search_quantity=map_concept_to_full_quantities[
                                "Name (Hardware)"
                            ],
                        ),
                        MenuItemTerms(
                            title="Model",
                            search_quantity=map_concept_to_full_quantities[
                                "Model (Hardware)"
                            ],
                        ),
                        MenuItemTerms(
                            title="Vendor",
                            search_quantity=map_concept_to_full_quantities[
                                "Vendor (Hardware)"
                            ],
                        ),
                    ],
                ),
                Menu(
                    title="Software",
                    indentation=1,
                    show_header=True,
                    items=[
                        MenuItemTerms(
                            title="Name",
                            search_quantity=map_concept_to_full_quantities[
                                "Name (Software)"
                            ],
                        ),
                        MenuItemTerms(
                            title="Model",
                            search_quantity=map_concept_to_full_quantities[
                                "Model (Software)"
                            ],
                        ),
                    ],
                ),
                Menu(
                    title="Current Sensor",
                    indentation=1,
                    show_header=True,
                    items=[
                        MenuItemHistogram(
                            title="Current",
                            x=map_concept_to_full_quantities[
                                "Current (Current Sensor)"
                            ],
                        ),
                        MenuItemHistogram(
                            title="Current Offset",
                            x=map_concept_to_full_quantities[
                                "Current Offset (Current Sensor)"
                            ],
                        ),
                    ],
                ),
                Menu(
                    title="Sample Bias Voltage",
                    indentation=1,
                    show_header=True,
                    items=[
                        MenuItemHistogram(
                            title="Bias Voltage",
                            x=map_concept_to_full_quantities[
                                "Bias voltage (Sample Bias Voltage)"
                            ],
                        ),
                        MenuItemHistogram(
                            title="Bias Offset",
                            x=map_concept_to_full_quantities[
                                "Bias offset (Sample Bias Voltage)"
                            ],
                        ),
                    ],
                ),
                Menu(
                    title="Piezo Sensor",
                    indentation=1,
                    show_header=True,
                    items=[
                        MenuItemHistogram(
                            title="x",
                            x=map_concept_to_full_quantities[
                                "Piezo X (Piezo Sensor XYZ)"
                            ],
                        ),
                        MenuItemHistogram(
                            title="y",
                            x=map_concept_to_full_quantities[
                                "Piezo Y (Piezo Sensor XYZ)"
                            ],
                        ),
                        MenuItemHistogram(
                            title="z",
                            x=map_concept_to_full_quantities[
                                "Piezo Z (Piezo Sensor XYZ)"
                            ],
                        ),
                    ],
                ),
                Menu(
                    title="Lockin Amplifier",
                    indentation=1,
                    show_header=True,
                    items=[
                        MenuItemHistogram(
                            title="Reference Frequency",
                            x=map_concept_to_full_quantities[
                                "Reference Frequency (Lockin Amplifier)"
                            ],
                        ),
                        MenuItemHistogram(
                            title="Reference Phase",
                            x=map_concept_to_full_quantities[
                                "Reference Phase (Lockin Amplifier)"
                            ],
                        ),
                        MenuItemHistogram(
                            title="Reference Amplitude",
                            x=map_concept_to_full_quantities[
                                "Reference Amplitude (Lockin Amplifier)"
                            ],
                        ),
                        MenuItemTerms(
                            title="Demodulated signal",
                            search_quantity=map_concept_to_full_quantities[
                                "Demodulated signal (Lockin Amplifier)"
                            ],
                        ),
                        MenuItemHistogram(
                            title="Lockin Current Flip Sign",
                            x=map_concept_to_full_quantities[
                                "Lockin Current Flip Sign (Lockin Amplifier)"
                            ],
                        ),
                    ],
                ),
                Menu(
                    title="Sample",
                    show_header=True,
                    items=[
                        MenuItemTerms(
                            title="Name",
                            search_quantity=map_concept_to_full_quantities[
                                "Sample Name"
                            ],
                        ),
                        MenuItemTerms(
                            title="Chemical Formula",
                            search_quantity=map_concept_to_full_quantities[
                                "Sample Chemical Formula"
                            ],
                        ),
                    ],
                ),
                Menu(
                    title="Author",
                    show_header=True,
                    items=[
                        MenuItemTerms(
                            title="Name",
                            search_quantity=map_concept_to_full_quantities["User Name"],
                        ),
                        MenuItemTerms(
                            title="Affiliation",
                            search_quantity=map_concept_to_full_quantities[
                                "User Affiliation"
                            ],
                        ),
                        MenuItemTerms(
                            title="Uploader",
                            search_quantity="authors.name",
                        ),
                    ],
                ),
            ],
        ),
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
                        "lg": {"minH": 3, "minW": 3, "h": 4, "w": 12, "y": 8, "x": 0},
                        "md": {"minH": 3, "minW": 3, "h": 4, "w": 12, "y": 0, "x": 0},
                        "sm": {"minH": 3, "minW": 3, "h": 4, "w": 12, "y": 0, "x": 0},
                    },
                },
                {
                    "type": "terms",
                    "show_input": False,
                    "scale": "linear",
                    "title": "Definition",
                    "quantity": map_concept_to_full_quantities["Definition"],
                    "layout": {
                        "xxl": {"minH": 3, "minW": 3, "h": 8, "w": 4, "y": 0, "x": 32},
                        "xl": {"minH": 3, "minW": 3, "h": 8, "w": 4, "y": 0, "x": 16},
                        "lg": {"minH": 3, "minW": 3, "h": 8, "w": 4, "y": 8, "x": 16},
                        "md": {"minH": 3, "minW": 3, "h": 8, "w": 4, "y": 38, "x": 0},
                        "sm": {"minH": 3, "minW": 3, "h": 8, "w": 4, "y": 38, "x": 0},
                    },
                },
                {
                    "type": "terms",
                    "show_input": False,
                    "scale": "linear",
                    "title": "Scan Mode",
                    "quantity": map_concept_to_full_quantities["Scan Mode"],
                    "layout": {
                        "xxl": {"minH": 3, "minW": 3, "h": 8, "w": 4, "y": 8, "x": 32},
                        "xl": {"minH": 3, "minW": 3, "h": 8, "w": 4, "y": 0, "x": 12},
                        "lg": {"minH": 3, "minW": 3, "h": 8, "w": 4, "y": 8, "x": 12},
                        "md": {"minH": 3, "minW": 3, "h": 8, "w": 4, "y": 0, "x": 12},
                        "sm": {"minH": 3, "minW": 3, "h": 8, "w": 4, "y": 46, "x": 0},
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
                        "lg": {"minH": 3, "minW": 3, "h": 8, "w": 18, "y": 0, "x": 0},
                        "md": {"minH": 3, "minW": 3, "h": 4, "w": 12, "y": 4, "x": 0},
                        "sm": {"minH": 3, "minW": 3, "h": 4, "w": 12, "y": 4, "x": 0},
                    },
                },
            ]
        },
    ),
)
