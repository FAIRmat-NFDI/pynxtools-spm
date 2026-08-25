#!/usr/bin/env python3
"""
Script to add attributes to HDF5 files.

This script opens an HDF5 file, navigates to a specified dataset or group path,
adds or overwrites an attribute, and closes the file.

Usage:
    python overwrite_a_hdf5_file.py <h5_file> <dataset_path> <attr_name> <attr_value> [--type TYPE]

Example:
    python overwrite_a_hdf5_file.py data.h5 /entry/current_backward long_name "Backward Current" --type str
    python overwrite_a_hdf5_file.py data.h5 /entry/measurement gain 1.5 --type float
    python overwrite_a_hdf5_file.py data.h5 /entry count 42 --type int
"""

import h5py
import argparse
import sys
from pathlib import Path


def add_attribute_to_hdf5(
    h5_file: str,
    dataset_path: str,
    attr_name: str,
    attr_value: str,
    attr_type: str = "str",
) -> None:
    """
    Add or overwrite an attribute in an HDF5 file at a given dataset/group path.

    Parameters
    ----------
    h5_file : str
        Path to the HDF5 file
    dataset_path : str
        Path to the dataset or group (e.g., '/entry/current_backward')
    attr_name : str
        Name of the attribute to add
    attr_value : str
        Value of the attribute (will be converted based on attr_type)
    attr_type : str
        Data type for the attribute: 'str', 'int', 'float', 'bool'
        Default is 'str'

    Raises
    ------
    FileNotFoundError
        If the HDF5 file does not exist
    KeyError
        If the dataset/group path does not exist in the file
    ValueError
        If the attribute type is invalid or conversion fails
    """

    # Check if file exists
    h5_path = Path(h5_file)
    if not h5_path.exists():
        raise FileNotFoundError(f"HDF5 file not found: {h5_file}")

    # Convert attribute value based on type
    # Explicit union annotation: mypy would otherwise infer the type from the
    # first assignment below (int) and reject the float/str branches.
    converted_value: str | int | float | bool
    try:
        if attr_type.lower() == "int":
            converted_value = int(attr_value)
        elif attr_type.lower() == "float":
            converted_value = float(attr_value)
        elif attr_type.lower() == "bool":
            converted_value = attr_value.lower() in ("true", "1", "yes", "on")
        elif attr_type.lower() == "str":
            converted_value = str(attr_value)
        else:
            raise ValueError(
                f"Unsupported attribute type: {attr_type}. "
                "Supported types: str, int, float, bool"
            )
    except (ValueError, AttributeError) as e:
        raise ValueError(f"Failed to convert '{attr_value}' to type {attr_type}: {e}")

    # Open HDF5 file and add attribute
    try:
        with h5py.File(h5_file, "r+") as hdf5_file:
            # Check if dataset/group path exists
            if dataset_path not in hdf5_file:
                raise KeyError(
                    f"Dataset/group path '{dataset_path}' not found in {h5_file}. "
                    f"Available paths: {list(hdf5_file.keys())}"
                )

            # Get the dataset or group
            target = hdf5_file[dataset_path]

            # Add or overwrite the attribute
            target.attrs[attr_name] = converted_value

            print(
                f"✓ Successfully added attribute '{attr_name}' = {converted_value!r} "
                f"(type: {attr_type}) to '{dataset_path}' in {h5_file}"
            )

    except h5py.Error as e:
        raise RuntimeError(f"HDF5 error while processing {h5_file}: {e}")


def main():
    """Parse command-line arguments and execute the script."""
    parser = argparse.ArgumentParser(
        description="Add attributes to HDF5 files",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Add a string attribute
  python overwrite_a_hdf5_file.py data.h5 /entry/current_backward long_name "Backward Current"
  
  # Add a float attribute with explicit type
  python overwrite_a_hdf5_file.py data.h5 /entry/measurement gain 1.5 --type float
  
  # Add an integer attribute
  python overwrite_a_hdf5_file.py data.h5 /entry count 42 --type int
  
  # Add a boolean attribute
  python overwrite_a_hdf5_file.py data.h5 /entry/flag enabled true --type bool
        """,
    )

    parser.add_argument("h5_file", help="Path to the HDF5 file")
    parser.add_argument(
        "dataset_path",
        help="Path to the dataset or group (e.g., /entry/current_backward)",
    )
    parser.add_argument("attr_name", help="Name of the attribute to add")
    parser.add_argument("attr_value", help="Value of the attribute")
    parser.add_argument(
        "--type",
        dest="attr_type",
        default="str",
        choices=["str", "int", "float", "bool"],
        help="Data type for the attribute (default: str)",
    )

    args = parser.parse_args()

    try:
        add_attribute_to_hdf5(
            h5_file=args.h5_file,
            dataset_path=args.dataset_path,
            attr_name=args.attr_name,
            attr_value=args.attr_value,
            attr_type=args.attr_type,
        )
    except (FileNotFoundError, KeyError, ValueError, RuntimeError) as e:
        print(f"✗ Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"✗ Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
