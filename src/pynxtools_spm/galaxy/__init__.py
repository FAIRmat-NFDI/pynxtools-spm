"""Files for the Galaxy ELN tools: the ELN rules and the LLM instructions per NeXus definition.

See https://github.com/FAIRmat-NFDI/pynxtools-spm/issues/131.
"""

from pathlib import Path

GALAXY_DIR = Path(__file__).parent
ELN_RULES_FILE = GALAXY_DIR / "eln_rules.yaml"
