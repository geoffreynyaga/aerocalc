# aerocalc

aerocalc v0.11 python3 version (converted using 2to3 tool)

original aerocalc:

- homepage: https://kilohotel.com/python/aerocalc/
- pypi website: https://pypi.python.org/pypi/AeroCalc/0.11

AeroCalc 0.11
Aeronautical Engineering Calculations

AeroCalc is a pure python package that performs various aeronautical engineering calculations. Currently it provides airspeed conversions, static source error correction calculations, standard atmosphere calculations and unit conversions.

## Installation

Download the files https://github.com/chengdi123000/aerocalc/archive/v0.11-py3.tar.gz, decompress it and use `setup.py` to install.

```bash
wget https://github.com/chengdi123000/aerocalc/archive/v0.11-py3.tar.gz
tar xf v0.11-py3.tar.gz
cd aerocalc-0.11-py3
python setup.py install

```

## Testing

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
├── aerocalc
│   ├── __pycache__
│   └── test
├──  <b>htmlcov</b>
└── venv
</pre>

Open up the folder and open the `index.html` in your browser to see this information.
