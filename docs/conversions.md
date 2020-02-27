## Area Conversion

This module is used to convert areas between various units.

> `Convert area values between ft**2, in**2, m**2, km**2, sm**2 and nm**2.`

```python
def area_conv(Area, from_units=default_area_units, to_units=default_area_units):
    """
    NOTE:  The incoming value is first converted to ft**2, then it is converted to
           desired return value.
    """
    ...
    return converted area
```

NB: The units default to those specified in default_units.py

#### Examples:

`Convert 1 ft**2 to inches**2, with ft\*\*2 already defined as the default units:`

```shell
> area_conv(1, to_units = 'in**2')
144.0
```

`Convert 288 square inches to square feet, with ft**2 already defined as the default units:`

```bash
> area_conv(288, from_units = 'in\*\*2')
2.0
```

`Convert 10 square metres to square inches:`

```bash
> area_conv(1000, from_units = 'm**2', to_units = 'in**2')
1550003.1000061999
```

## Density Conversion

This function is used to convert density values between e.g `kg/m**3, slug/ft**3 and lb/ft**3.`

```python
def density_conv(Density, from_units, to_units):
"""
    The incoming value is first converted to kg/m**3, then it is converted
    to desired return value.
    """
    ...
    return converted_density

```

> #### NB: There are <b>`NO`</b> default units. Both the from_units and the to_units <b>`MUST`</b> be specified.

Example:

`Convert 1.225 kg per metre cubed to lb per foot cubed:`

```bash
> density_conv(1.225, from_units = 'kg/m**3', to_units = 'lb/ft**3')
0.076474253491112101
```

## Force Conversion

Convert force values between lb and N.

```python
def force_conv(Force, from_units=default_weight_units, to_units=default_weight_units):
    """
    The incoming value is first converted to N, then it is converted to the
    desired return value.
    """
    ...
    return converted_force

```

## Length Conversion

`Convert length values between ft, in, m, km, sm and nm.`

```python
def len_conv(L, from_units=default_length_units, to_units=default_length_units):
    """
    The incoming value is first converted to ft, then it is converted to
    desired return value.

    The units default to those specified in default_units.py
    """
    ...
    return converted_length
```

### Examples:

`Convert 5280 ft to statute miles, with feet already defined as the default units:`

```bash
> len_conv(5280, to_units = 'sm')
  1.0
```

`Convert 1 nautical mile to feet, with feet already defined as the default units:`

```bash
> len_conv(1, from_units = 'nm')
  6076.1154855643044
```

`Convert 1000 metres to kilometres:`

```bash
> len_conv(1000, from_units = 'm', to_units = 'km')
  0.99999999999999989
```

## Power Conversion

`Convert power values between horsepower, ft-lb/mn, ft-lb/s, watts, kilowatts, BTU/hr and BTU/mn.`

```python
def power_conv(P, from_units=default_power_units, to_units=default_power_units):
    """
    The incoming value is first converted to hp, then it is converted to the
    desired return value.
    """
    ...
    return converted_power
```

<b>The units default to those specified in default_units.py</b>

## Pressure Conversion

`Convert pressure values between inches of HG, mm of HG, psi, lb/ft^2, hpa and mb.`

```python
def press_conv(P, from_units=default_press_units, to_units=default_press_units):
    """


    The incoming value is first converted to Pa, then it is converted to
    desired return value.
    The units default to those specified in default_units.py

    """
    ...
    return converted_pressure
```

### Examples:

`Convert 1013.25 hpa to default pressure units:`

```bash
> press_conv(1013.25, from_units = 'hpa')
29.921331923765198
```

`Convert 29.9213 default pressure units to mm of HG:`

```bash
> press_conv(29.9213, to_units = 'mm HG')
760.00128931459176
```

`Convert 2116.22 lb per sq. ft to lb per sq. inch:`

```bash
> press_conv(2116.22, from_units = 'psf', to_units = 'psi')
14.695973160069311
```

## Speed Conversion

`Convert speed values between kt, mph, km/h, m/s and ft/s.`

```python
def speed_conv(S, from_units=default_speed_units, to_units=default_speed_units):
    """
    The incoming value is first converted to kt, then it is converted to
    desired return value.
    The units default to those specified in default_units.py
    """
    ...
    return converted_speed
```

### Example:

`Convert 230 mph to kt:`

```bash
> speed_conv(230, from_units = 'mph', to_units = 'kt')
199.86453563714903
```

## Temperature Conversion

> Converts absolute temperature values between deg C, F, K and R.

> NOTE: This function should <b>NOT</b> be used for relative temperature conversions,
> i.e. `temperature differences.`

```python
def temp_conv(T, from_units=default_temp_units, to_units=default_temp_units):
    """
    The incoming value is first converted to deg K, then it is converted to
    desired return value.
    The units default to those specified in default_units.py

    """
    return converted_temperature
```

### Examples:

`Convert 32 deg F to deg C, with deg C as the default units:`

```bash
> temp_conv(32, from_units = 'F')
> 0.0
```

`Convert 100 deg C to deg F, with deg C as the default units:`

```bash
> temp_conv(100, to_units = 'F')
> 212.0
```

`Convert 59 deg F to deg K`

```bash
> temp_conv(59, from_units = 'F', to_units = 'K')
> 288.14999999999998
```

## Volume Conversions

> <b>`Convert volume values between USG, ImpGal (Imperial gallons), l (litres), ft**3, in**3, m**3, km**3, sm**3 and nm**3.`</b>

```python
def vol_conv(V, from_units=default_vol_units, to_units=default_vol_units):
    """
    The incoming value is first converted to ft**3, then it is converted to
    desired return value.

    The units default to those specified in default_units.py

    Examples:


    """
    return converted_volume
```

`Convert 1 cubic foot to US gallons, with cubic feet already defined as the default units:`

```bash
> vol_conv(1, to_units = 'USG')
7.4805194804946105
```

`Convert 1 Imperial gallon to cubic feet, with cubic feet already defined as the default units:`

```shell
> vol_conv(1, from_units = 'ImpGal')

0.16054365323600001
```

`Convert 10 US gallon to litres:`

```bash
> vol_conv(10, from_units = 'USG', to_units = 'l')
37.854117840125852
```

## Weight Conversion

> Convert weight values between lb and kg.
>
> ### `Purists will yell that lb is a unit of weight, and kg is a unit of mass.`
>
> ### `Get over it!!!!!`

```python
def wt_conv(W, from_units=default_weight_units, to_units=default_weight_units):
    """
    The incoming value is first converted to kg, then it is converted to the
    desired return value.

    The units default to those specified in default_units.py
    """
    return converted_weight
```

## AVGAS Conversion

> Convert aviation gasoline between units of lb, US Gallon (USG),
> Imperial Gallon (Imp Gal), litres (l) and kg, assuming nominal
> density for aviation gasoline of 6.01 lb per USG.

```
    Note: it was difficult to find authoritative values for aviation gasoline
    density. Conventional wisdom is that aviation gasoline has a density of
    6 lb/USG. The Canada Flight Supplement provides densities of:
    temp density density density
    (deg C) (lb/USG) (lb/ImpGal) (lb/l)
    -40     6.41     7.68        1.69
    -20     6.26     7.50        1.65
    0       6.12     7.33        1.62
    15      6.01     7.20        1.59
    30      5.90     7.07        1.56

    However, the Canada Flight Supplement does not provide a source for its
    density data.  And, the values for the different volume units are not
    completly consistent, as they don't vary by exactly the correct factor.
    For example, if the density at 15 deg C is 6.01 lb/USG, we would expect
    the density in lb/ImpGal to be 7.22, (given that 1 ImpGal = 1.201 USG)
    yet the Canada Flight Supplement has 7.20.

    The only authoritative source for aviation gasoline density that was
    found on the web was the \"Air BP Handbook of Products\" on the British
    Petroleum (BP) web site:

    <http://www.bp.com/liveassets/bp_internet/aviation/air_bp/STAGING/local_assets/downloads_pdfs/a/air_bp_products_handbook_04004_1.pdf>

    It provides the following density data valid at 15 deg C (the BP document
    only provides density in kg/m**3 - the density in lb/USG were calculated
    by Kevin Horton):

    Avgas    density     density
    Type    (kg/m**3)    (lb/USG)
    80       690          5.76
    100      695          5.80
    100LL    715          5.97

    The available aviation gasoline specifications do not appear to define an
    allowable density range.  They do define allowable ranges for various
    parametres of the distillation process - the density of the final product
    will vary depending on where in the allowable range the refinery is run.
    Thus there will be some variation in density from refinery to refinery.

    This function uses the 15 deg C density values provided by BP, with the
    variation with temperature provided in the Canada Flight Supplement.

    The grade may be specified as \"80\", \"100\" or \"100LL\".  It defaults to
    \"100LL\" if it is not specified.

```

```python
def avgas_conv(
AG,
from_units=default_avgas_units,
to_units=default_avgas_units,
temp=15,
temp_units="C",
grade="nominal",
):
    """
    The units default to those specified in default_units.py
    The temperature defaults to 15 deg C if it is not specified.
    """

    return converted_avgas
```
