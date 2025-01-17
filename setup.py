from setuptools import find_packages, setup
from typing import List


def get_requirements() -> List[str]:
    requirement_list: List[str] = []
    try:
        with open("requirements.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()

                if requirement and requirement != "-e .":
                    requirement_list.append(requirement)

    except FileNotFoundError:
        print("requirements.txt file not found")


setup(
    name="ai-assistant",
    version="0.0.1",
    author="Mohammad Shuaib",
    author_email="mohammadshuaib3455@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)
