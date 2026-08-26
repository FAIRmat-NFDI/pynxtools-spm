from pynxtools.dataconverter.nexus_tree import NexusNode

from pynxtools.dataconverter.helpers import generate_template_from_nxdl
from pynxtools.dataconverter.nexus_tree import *
from pynxtools.dataconverter.template import Template
from pynxtools.dataconverter.nexus_tree import generate_tree_from

# import template
from pynxtools.dataconverter.template import Template
import copy


## Template class
## ==========================================
class KeyProperty:
    """
    A class to represent the key of the Template class.

    The class is intended to have private attributes:
        NXtype: group, field, or attribute
        NXdataType: INT, FLOAT, according to the nexus data type
        NXunits: NX_LENGTH, NX_TIME, NX_CURRENT, or m, power, etc.
    """

    prop_name = None
    _prop_name = None

    def __set_name__(self, owner, name):
        """Set the name of the property."""
        self.prop_name = name
        self._prop_name = f"_{name}"

    def __get__(self, instance, owner):
        """Get the value of the property."""
        return getattr(instance, self._prop_name, None)

    def __set__(self, instance, value):
        """Set the value of the property."""
        if not isinstance(value, KeyObject):
            raise TypeError(f"Expected KeyObject, got {type(value)}")
        setattr(instance, self._prop_name, value)

    # def __setitem__(self, key, value):
    #     """Set the value of the property."""
    #     if not isinstance(value, KeyObject):
    #         raise TypeError(f"Expected KeyObject, got {type(value)}")

    #     setattr(self, key, value)

class KeyObject:
    """
    A class to represent the key of the Template class.

    The class is intended to have private attributes:
        NXtype: group, field, or attribute
        NXdataType: INT, FLOAT, according to the nexus data type
        NXunits: NX_LENGTH, NX_TIME, NX_CURRENT, or m, power, etc.
    """

    nx_name = KeyProperty()
    nx_class = KeyProperty()
    nx_units = KeyProperty()
    nx_dtype = KeyProperty()
    # None  # data  type
    nx_name_type = KeyProperty()
    nx_optionality = KeyProperty()
    value = KeyProperty()
    nx_node = None

    def __init__(
        self,
        nx_node,
        concept_value=None,
    ):
        # TODO remove the node
        self.nx_node = nx_node
        self.value = concept_value

        if self.nx_node.type == "group":
            self.nx_class = self.nx_node.nx_class
            self.nx_dtype = None
        elif self.nx_node.type in ("field", "attribute"):
            self.nx_class = None
            self.nx_dtype = self.nx_node.nx_dtype
            if units := getattr(self.nx_node, "unit", None):
                self._nx_units = units
        # elif self.nx_node.type == "choice":
        # Not implemented yet
        self.nx_name = self.nx_node.name
        self.nx_name_type = self.nx_node.name_type
        self.nx_optionality = self.nx_node.optionality

    def __repr__(self):
        """Returns a unique string representation for the KeyObject object."""
        return self.value

    def __eq__(self, value):
        self.value = value

    def __getattr__(self, name):
        """Handles how attributes are accessed from the KeyObject object."""
        if name in self.__dict__:
            return getattr(self, name)
        else:
            raise AttributeError(
                f"'{self.__class__.__name__}' object has no attribute '{name}'"
            )

    def __setattr__(self, name, value):
        """Handles how attributes are set within the KeyObject object."""
        if name in self.__dict__:
            setattr(self, name, value)
        else:
            raise AttributeError(
                f"'{self.__class__.__name__}' object has no attribute '{name}'"
            )


class DescriptedTemplate(dict):
    """
    A Template object to control and separate template paths according to optionality.
    """

    def __init__(self, template=None, **kwargs):
        super().__init__(**kwargs)
        if isinstance(template, Template):
            self.optional: dict = copy.deepcopy(template["optional"])
            self.recommended: dict = copy.deepcopy(template["recommended"])
            self.required: dict = copy.deepcopy(template["required"])
            self.undocumented: dict = copy.deepcopy(template["undocumented"])
            self.optional_parents: list = copy.deepcopy(template["optional_parents"])
            # self.lone_groups: dict = copy.deepcopy(template["lone_groups"])
        else:
            self.optional: dict = {}  # type: ignore[no-redef]
            self.recommended: dict = {}  # type: ignore[no-redef]
            self.required: dict = {}  # type: ignore[no-redef]
            self.undocumented: dict = {}  # type: ignore[no-redef]
            self.optional_parents: list = []  # type: ignore[no-redef]
            self.lone_groups: list = []  # type: ignore[no-redef, assignment]
            if isinstance(template, dict):
                self.undocumented: dict = copy.deepcopy(template)  # type: ignore[no-redef]

        # self.overwrite_keys = overwrite_keys

    def get_accumulated_dict(self):
        """Returns a dictionary of all the optionalities merged into one."""
        return {
            **self.optional,
            **self.recommended,
            **self.required,
            **self.undocumented,
        }

    def __repr__(self):
        """Returns a unique string representation for the Template object."""
        return self.get_accumulated_dict().__repr__()

    def __setitem__(self, key, value):
        """Handles how values are set within the Template object."""
        if isinstance(value, dict):
            pass
        elif isinstance(value, KeyObject):
            # If value is an KeyObject, store it in the dictionary
            opt = None
            if not (opt := value.nx_optionality):
                self.optional[key] = value
            elif opt == "recommended":
                self.recommended[key] = value
            elif opt == "required":
                self.required[key] = value
            else:  # opt == "undocumented"
                self.undocumented[key] = value
            raise KeyError(
                f"Node does not have proper optionality value."
                f"Has {value.nx_optionality} but should be one"
                f" of [optional, recommended, required, undocumented]"
            )
        else:
            self.undocumented[key] = value
        # return super().__setitem__(key, value)

    def __getitem__(self, key):
        """Handles how values are accessed from the Template object."""
        # Try setting item in all else throw error. Does not append to default.
        if key in self.required:
            return self.required[key]
        elif key in self.optional:
            return self.optional[key]
        elif key in self.recommended:
            return self.recommended[key]
        elif key in self.undocumented:
            return self.undocumented[key]
        if key in ("optional", "recommended", "required", "undocumented"):
            return getattr(self, key)

        # if key in ("required", "optional", "recommended", "undocumented"):
        #     return self.get_optionality(key)
        raise KeyError(
            "Only paths starting with '/' or one of [optional_parents, "
            "lone_groups, required, optional, recommended, undocumented] can be used."
        )


# Create Template from NeXusNode Tree
def add_template_key_from(nx_node, template, parent_path=""):
    key = None
    unit = None
    if nx_node.type == "attribute":
        leaf_part = (
            f"{nx_node.name}[{nx_node.name}]" if nx_node.variadic else nx_node.name
        )
        key = f"{parent_path}/@{leaf_part}"
    elif nx_node.type == "field":
        leaf_part = (
            f"{nx_node.name}[{nx_node.name}]" if nx_node.variadic else nx_node.name
        )
        key = f"{parent_path}/{leaf_part}"
        if hasattr(nx_node, "unit") and nx_node.unit:
            unit = f"{key}/@units"
    elif nx_node.type == "group":
        leaf_part = f"{nx_node.name}[{nx_node.name}]"
        key = f"{parent_path}/{leaf_part}"
    if key:
        template[nx_node.optionality][key] = KeyObject(nx_node)
    if unit:
        template[nx_node.optionality][unit] = nx_node.unit
    return key


# TODO: appdef tree
def build_template_from_nexus_tree(appdef_root, template, parent_path=""):
    """
    Build a template from the nexus tree.
    """
    for child in appdef_root.children:
        key = add_template_key_from(child, template, parent_path)
        if not key:
            continue
        build_template_from_nexus_tree(child, template, key)


# template = Template()
# build_template_from_nexus_tree(spmT, template)
# template_old = Template()

# root, _ = get_nxdl_root_and_path(spm_appdef)
# generate_template_from_nxdl(
#     root=root,
#     template=template_old,
# )
# print(' #### check optional missing keys')
# template_ = template
# template_old_ = template_old
# def check_missing():
#     for key, _ in template_['optional'].items():
#         if key not in template_old_['optional']:
#             print(f"OPTIONAL Missing key in template_old: {key}")
#     print(' #### check required missing keys')
#     for key, _ in template_['required'].items():
#         if key not in template_old_['required']:
#             print(f"REQUIRED: Missing key in template_old: {key}")

tempate = DescriptedTemplate()
spm = "NXspm"

spmT = generate_tree_from(spm)

build_template_from_nexus_tree(appdef_root=spmT, template=tempate)

xx = "hello"