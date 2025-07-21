from spym import RHKsm4


class Sm4Omicron(SPMParser):
    """
    Parser for Omicron SM4 STM files.
    """

    def __init__(self, file_path):
        super().__init__(file_path)

    def parse(self):
        """
        Parse the Omicron SM4 STM file and return the parsed data.
        
        RHKsm4 Object:
            RHKsm4 object is a container containing RHKpage (can be called scan page) object
            each of the page has object public attributes
                - attrs --> has all the metadata for each scan
                - label --> label for each scan page
                - data  --> 2D matrix image data
                - coords --> list of coordinates for each image data
        
        Returns:
            parsed data object (RHKsm4) object containing all the parsed data.
        """

        rhk_file_obj = RHKsm4(self.file_path)

        # Process the parsed data as needed
        # For example, you can convert it to a specific format or extract certain fields

        sm4_data_dict = {}

        return rhk_file_obj

    def get_stm_raw_file_info():
        ...