from setuptools import setup, find_packages

setup(
    name="sto_rheed",
    version="0.1",
    description="Repository for Predicting Pulsed-Laser Deposition SrTiO3 Homoepitaxy Growth Dynamics using High-Speed Reflection High-Energy Electron Diffraction project",
    author="Yichen Guo",
    package_dir={"": "src"},
    packages=find_packages(where="src"),  # Will include all packages under 'src'
    install_requires=[],  # Add dependencies if needed, e.g., ['numpy']
)
