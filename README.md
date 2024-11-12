# Predicting Pulsed-Laser Deposition SrTiO3 Homoepitaxy Growth Dynamics using High-Speed RHEED

This repository contains code and data for the paper **Predicting Pulsed-Laser Deposition SrTiO3 Homoepitaxy Growth Dynamics using High-Speed Reflection High-Energy Electron Diffraction**. The study presents a high-speed platform for capturing in situ RHEED dynamics to analyze the growth kinetics of SrTiO3 (STO) homoepitaxy with a temporal resolution greater than 500 Hz, advancing the potential for real-time analysis of surface crystallinity during pulsed-laser deposition (PLD).

## Project Overview

Pulsed-laser deposition (PLD) is essential for growing complex oxides with controlled stoichiometry. In this work, we leverage high-speed RHEED to capture surface dynamics at speeds much faster than conventional video-rate cameras (60-120 Hz). Using an open-source analysis package that fits diffraction spots to 2D Gaussians, we can extract single-pulse surface reconstruction kinetics for the (001)-oriented STO system.

This repository includes the following:
- Code to process high-speed RHEED data by fitting diffraction spots.
- Scripts to analyze surface crystallinity and model single-pulse intensity decay.
- Example data from homoepitaxially deposited STO surfaces with various terminations.
- Results demonstrating the influence of substrate step width and termination on adatom deposition kinetics.

## Key Features

- **High-Speed RHEED Analysis**: Capture in situ surface crystallinity at >500 Hz.
- **Gaussian Fitting**: Fit diffraction spots to 2D Gaussians for single-pulse surface kinetics.
- **Exponential Decay Modeling**: Use exponential functions to model intensity decay correlated with surface termination.
- **Dynamic Growth Insights**: Understand how surface termination and step width affect growth mechanisms in real time.

## Repository Structure

- `data/`: Example high-speed RHEED data for STO homoepitaxy. Data is Available on from Zenodo via DOI 10.5281/zenodo.7934968.
- `notebooks/`: Scripts for data processing, Gaussian fitting, and exponential modeling.
- `src/`: Source code for RHEED data analysis.
- `README.md`: This readme file.

## Installation

Clone the repository and install dependencies. The code requires Python 3.10+ and the following packages:

```bash
git clone https://github.com/yig319/Predicting-Pulsed-Laser-Deposition-SrTiO3-Homoepitaxy-Growth-Dynamics-using-RHEED.git
cd Predicting-Pulsed-Laser-Deposition-SrTiO3-Homoepitaxy-Growth-Dynamics-using-RHEED
pip install -r requirements.txt
