# class Concept:
#     def __set_name__(self, owner, conceptObj):
#         self.name = conceptObj.name
#         self._private_name = f"_{self.name}"
#         self._type = conceptObj.type # field, group, or attribute
#         self._dataType = conceptObj.dataType
#         self._units = conceptObj.units
#         self._value = None
#         self._curate_data = None
#     # Units may comes as /Entry/Instrument/Source/Beamline/energy/units
    
#     def curate_data(self, data):
#         """
#         Fit the data to the concept.
#         """
#         print('__curate_data__')
#         return data
    
#     def __get__(self, instance, owner):
#         """
#         Get the value of the concept.
#         """
#         print('__get__')
#         return getattr(instance, self._private_name, None)
    
#     def __set__(self, instance, value):
#         """
#         Set the value of the concept.
#         """
#         print('__set__')

#         setattr(instance, self._private_name, value)


class CustomObject:
    def __init__(self):
        self._data = {}

    def __getitem__(self, key):
        return self._data[key]

    def __setitem__(self, key, value):
        if isinstance(value, KeyObject):
            # If value is an KeyObject, store it in the dictionary
            self._data[key] = value
        else:
            # Modify value only, keep the locked type
            self._data[key]['value'] = value  # will raise if type mismatch

class KeyObject:
    """
    A class to represent the key of the Template class.

    The class is intended to have private attributes:
        NXtype: group, field, or attribute
        NXdataType: INT, FLOAT, according to the nexus data type
        NXunits: NX_LENGTH, NX_TIME, NX_CURRENT, or m, power, etc.
    """

    def __init__(self, value, value_type=None):
        self._locked_type = value_type or type(value)
        self.value = value

    def __getitem__(self, key):
        if key == 'type':
            print(f"__getitem__ key==type")
            return self._locked_type
        else:
            raise KeyError(f"Invalid key: {key}")

    def __setitem__(self, key, new_value):
        if key == 'type':
            print(f" __setitem__ key==type Change a type is not allowd.")
        if key == 'units':
            print(f"not implemented yet! ")
        if key == 'value':
            self.value = new_value

    def __iadd__(self, other):
        self.value += other
        return self

    def __repr__(self):
        return repr(self.value)
    
obj = CustomObject()
obj['a'] = KeyObject(50, float)

print(obj['a'])            # 50
print(obj['a']['type'])    # float

obj['a'] += 10           # OK
print(obj['a'])            # 60.0

obj['a'] = 80            # modifies .value, keeps float type
print(obj['a'])            # 80.0
