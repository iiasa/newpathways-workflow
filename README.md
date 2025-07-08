# NEWPATHWAYS Scenario Processing Workflow

Copyright 2025 IIASA and the NEWPATHWAYS consortium

[![Code style: ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

<img src="images/newpathways_logo.svg" height="80" align="right" alt="SPARCCLE Project Logo">

## Background

The NEWPATHWAYS project aims to inform solutions to strengthen climate action by developing and analysing next-generation Paris-aligned global and national low-emission transformation pathways for the Global Stocktake in 2028.

Visit https://newpathways.eu for more info!

## Overview

This repository contains the workflow and configuration for the EU project NEWPATHWAYS.

> [!TIP]
> For *users not comfortable working with GitHub repositories and yaml files*,
> the definitions for this project are available for download as an xlsx spreadsheet
> at [https://files.ece.iiasa.ac.at/newpathways/newpathways-template.xlsx](https://files.ece.iiasa.ac.at/newpathways/newpathways-template.xlsx).

### Project nomenclature and model registration

This projects uses the variables region definitions from the
https://github.com/iamconsortium/common-definitions project.

To register a model, add the native-region definition and mappings
to common-definitions and then import them for this project by adding 
the region-hierarchy and the model name(s) to the file `nomenclature.yaml`.

## Funding acknowledgement

<img src="images/eu_logo.jpg" width="80" height="54" align="left" alt="EU logo">

Funded by the European Union. Views and opinions expressed are however those of the author(s) only and do not necessarily reflect those of the European Union or the European Climate, Infrastructure and Environment Executive Agency (CINEA). Neither the European Union nor the granting authority can be held responsible for them.
