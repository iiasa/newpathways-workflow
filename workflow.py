from pathlib import Path
import re

import pyam
from pyam.utils import escape_regexp
from nomenclature import DataStructureDefinition, RegionProcessor, process, CodeList


here = Path(__file__).absolute().parent


def main(df: pyam.IamDataFrame) -> pyam.IamDataFrame:
    """Project/instance-specific workflow for scenario processing"""

    # Import the definitions
    definition = DataStructureDefinition(here / "definitions")

    # Validate against the allowed scenario names and assign meta indicators
    for scenario in df.scenario:
        # Get the scenario code
        code = _match_code(definition.scenario, scenario)
        if code is None:
            raise ValueError(f"Scenario '{scenario}' not registered for this project.")

        # Check that model(s) are registered for the scenario
        model = df.model if len(df.model) == 1 else df.filter(scenario=scenario).model
        if not set(model).issubset(code.extra_attributes["model"]):
            raise ValueError(
                f"Model '{_format(model)}' not registered for scenario '{scenario}'."
            )

        # Assign meta indicators for the scenario
        rows = df.meta.index.get_level_values("scenario") == scenario
        for key, value in code.extra_attributes["meta_indicators"].items():
            df.meta.loc[rows, key] = value

    # Run the validation and region-processing
    processor = RegionProcessor.from_directory(path=here / "mappings", dsd=definition)
    return process(df, definition, processor=processor)


def _match_code(code_list: CodeList, value: str):
    for name, code in code_list.items():
        pattern = re.compile(escape_regexp(name) + "$")
        if re.match(pattern, value):
            return code


def _format(values: list) -> str:
    return ", ".join(values)
