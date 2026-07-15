Along-Track Footprint Analysis of Multi-Mission Satellite Altimetry

A Python-based research software module for characterizing spatial sampling patterns of multi-mission satellite altimetry observations and evaluating effective along-track resolution over ocean and inland water surfaces.

Overview
Satellite altimetry observations are collected along repeated satellite ground tracks with mission-dependent spatial sampling characteristics. Understanding the effective observation spacing is essential for reliable construction of along-track water-level time series, multi-mission integration, and geophysical interpretation of satellite-derived observations.

This project provides an automated workflow for analyzing the spatial sampling characteristics (satellite footprint) of Level-2 along-track altimetry observations from multiple satellite missions. The software calculates observation spacing along satellite tracks, identifies irregular sampling caused by missing records or data gaps, and estimates the effective spatial resolution of each mission within a selected study region.

The framework has been designed as a preprocessing module for larger satellite altimetry processing workflows, including water-level time-series generation, multi-mission harmonization, tidal analysis, and climate-related variability studies. 

-------------------------------------------------------------------------------------------------------------------------------------------------------------


Project Objective

This project analyzes the spatial sampling characteristics (satellite footprint) of multi-mission satellite altimetry over a study region, such as the Caspian Sea.

The analysis is performed using Level-2 (L2) along-track altimetry products downloaded from the AVISO+ data distribution service. The user specifies the ground track (pass) numbers to be analyzed. For each selected pass, the program processes every available observation cycle for all selected satellite missions.

For each mission, the along-track distance between consecutive observations is computed for every available pass and cycle.

A stepwise 3-sigma outlier detection procedure is then applied to identify and remove abnormal spacing caused by missing records, data gaps, or other irregular observations. Distance statistics are calculated after each outlier removal step.

The Remaining group in the final statistics table represents the nominal observation spacing after all detected outliers have been removed. These values provide a realistic estimate of the effective spatial sampling of each satellite mission over the study area.

Besides characterizing the satellite footprint, this analysis is an important preprocessing step for future applications. In particular, it provides a reliable assessment of observation spacing before constructing along-track water level time series, where irregular sampling intervals and missing observations may influence the quality of the resulting time series.

⸻

Input Data

The analysis uses multi-mission Level-2 (L2) along-track satellite altimetry products downloaded from the AVISO+ data distribution service.

The user provides:

* A list of ground track (pass) numbers.
* A list of satellite missions to be processed.

The directory structure is organized as follows:

Data/
│
├── Pass_016/
│   ├── TOPEX-POSEIDON/
│   │   ├── cycle_001.txt
│   │   ├── cycle_002.txt
│   │   └── ...
│   │
│   ├── JASON-1/
│   ├── JASON-2/
│   └── JASON-3/
│
├── Pass_017/
│   └── ...
│
└── ...

Each mission directory contains one text file for every observation cycle.

Each input file contains four numeric columns without a header:

Column	Description
1	Latitude
2	Longitude
3	Sea Surface Height (SSH)
4	Time

⸻

Processing Workflow

The processing sequence is:

1. Read all cycle files for each selected pass.
2. Read all selected satellite missions.
3. Compute the along-track distance between consecutive observations.
4. Merge all observations belonging to the same mission.
5. Apply stepwise 3-sigma outlier detection.
6. Compute descriptive statistics for each filtering step.
7. Export the statistics table.

⸻

Output

For each satellite mission, the package produces:

* Stepwise 3-sigma outlier detection results.
* Distance statistics table including:
    * Number of observations
    * Mean distance
    * Standard deviation
    * Minimum distance
    * Maximum distance
    * Median distance

The final Remaining group represents the nominal observation spacing after removing all detected outliers.

⸻

Current Project Structure

main.py
project1.py
reader.py
distance.py
outlier.py

⸻

Python Requirements

* Python 3.11 or newer
* pandas
* numpy

⸻

Future Development

This module serves as the preprocessing stage for subsequent analyses, including:

* Along-track water level time series construction.
* Multi-mission time series integration.
* Bias correction between satellite missions.
* Long-term water level monitoring.
* Tidal Modeling
* ...
