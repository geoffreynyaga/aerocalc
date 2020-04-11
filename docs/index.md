# Welcome to aerocalc3 ✈️🧮 documentation

[![Netlify Status](https://api.netlify.com/api/v1/badges/fb968472-9209-45c9-a9e6-dfc8fc8bc92d/deploy-status)](https://app.netlify.com/sites/aerocalc3/deploys)

> #### aerocalc3 Aeronautical Engineering Calculations
>
> aerocalc3 is a python utility package that performs various aeronautical engineering calculations.
>
> Currently it provides:
>
> - airspeed conversions,
> - static source error correction calculations
> - standard atmosphere calculations and
> - unit conversions.

[Full Documentation ](https://aerocalc3.netlify.com)

> - Homepage: https://aerocalc3.netlify.com
> - pypi website: https://pypi.org/project/aerocalc3/

[GitHub Pages](https://geoffreynyaga.github.io/aerocalc/)

## Table of Contents

> [Airspeed Conversions Docs ↗️](docs/airspeed.md)

> [Default Values Docs ↗️](docs/defaults.md)

> [Physical Properties (density, pressure etc) Conversion Docs ↗️](docs/conversions.md)

> ### Original aerocalc:
>
> For original documentation visit [kilohotel](https://kilohotel.com/python/aerocalc/.)

## Installation 📥

```bash
pip install aerocalc3==0.10
```

#### Alternatively:

Download the files `https://github.com/geoffreynyaga/aerocalc/archive/v_01.tar.gz`, decompress it and use `setup.py` to install.

```bash
wget https://github.com/geoffreynyaga/aerocalc/archive/v_01.tar.gz

tar xf v0.11-py3.tar.gz

cd aerocalc-0.11-py3

python setup.py install
```

## Project layout

```
    .
    ├── aerocalc # Source code folder.
    │   └── tests
    ├── docs # The documentation directory.
    ├── htmlcov # Test coverage folder.
    ├── site # Documentation build for deployment.
    │   ├── about
    │   ├── css
    │   ├── fonts
    │   ├── img
    │   ├── js
    │   └── search
    └── venv # Your generated virtual environment.
```

## Testing 🧪🧪

The projects uses pytest and black as the formatting option. The tests also check for consistencies on code format.

To initiate tests follow the steps below:

1. Its advised to create a virtual environment

```bash
virtualenv venv
```

2. Activate the environent. For Linux/MacOS users use the command below

```bash
source venv/bin/activate
```

for windows users

```bash
cd venv/Scripts

activate.bat
```

3. Install the requirements

```shell
pip install -r requirements.txt
```

4. Run the pytest command

```bash
pytest
```

The testing results will be displayed and there will also be a `htmlcov` folder generated inside the project that will contain the code coverage details.

<pre>
├── aerocalc3
│   ├── __pycache__
│   └── test
├──  <b>htmlcov</b>
└── venv
</pre>

Open up the folder and open the `index.html` in your browser to see this information.
