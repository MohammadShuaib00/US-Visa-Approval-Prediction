import os
import sys
from setuptools import find_packages, setup
from typing import List
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)

def get_requirements(file_path: str = "requirements.txt") -> List[str]:
    requirement_list = []
    try:
        logging.info("Reading the requirements.txt file")
        with open(file_path, "r") as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement and requirement != "-e .":  # Skip editable installs
                    requirement_list.append(requirement)
        logging.info("requirements.txt file has been read successfully")
        return requirement_list  
    except Exception as e:
        logging.error(f"Error reading the requirements file: {e}")

# Setup function for the package
setup(
    name="usvisaapprovalpredict",
    version="0.0.1",
    author="Mohammad Shuaib",
    author_email="mohammadshuaib3455@gmail.com",
    description="US Visa Approval Prediction",
    packages=find_packages(),
    install_requires=get_requirements() 
)
