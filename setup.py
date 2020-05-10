from setuptools import setup, find_packages

tests_require = [
    "flake8",
    "pytest",
    "pytest-cov",
    "pytest-datadir",
]

setup(
    name="nicethings",
    version="0.1.0",
    packages=find_packages("src"),
    package_dir={"": "src"},
    url="",
    license="MIT",
    author="qdd",
    author_email="qdd@eruditorum.dev",
    description="Tools for maintaining PEP-503 static sites",
    install_requires=[
        "attrs",
        "requests",
    ],
    tests_require=tests_require,
    extras_require={
        "tests": tests_require,
        "dev": [
            "black",
            "sphinx",
        ] + tests_require,
    },

)
