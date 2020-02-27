# AIRSPEED MODULE

INTRO:

> Perform various air speed conversions.
>
> Convert between Indicated Air Speed (IAS), Calibrated Air Speed (CAS),
> Equivalent Air Speed (EAS), True Air Speed (TAS) and mach number.
>
> Convert between pitot static system pressures and air speed.
>
> Provide interactive airspeed conversions when script is run directly, e.g.
> 'python airspeed.py'.

```
default_area_units = "ft**2"
default_power_units = "hp"
default_speed_units = "kt"
default_temp_units = "C"
default_weight_units = "lb"
default_press_units = "in HG"
default_density_units = "lb/ft**3"
default_length_units = "ft"
default_avgas_units = "lb"

P0 = 101325.0 # Pressure at sea level, pa

# speed of sound from http://www.edwards.af.mil/sharing/tech_pubs/Handbook-10%20March02.pdf

A0 = 340.2941 # speed of sound at sea level, std day, m/s

F = (1.25 ** 2.5 \* (2.4 ** 2.0) \*_ 2.5) _ 1.2

# F calculated by manipulating NASA RP 1046 pg 17

# F is used in some of the supersonic solution equations.
```

## delta pressure to speed

```python
def _dp2speed(
dp, Pref, Rhoref, press_units=default_press_units, speed_units=default_speed_units,
):
    ...
    return speed
```

## delta pressure to CAS

> `Return the CAS for a given differential pressure (the difference between the pitot and static pressures).`

```
The pressure units may be in inches of HG, mm of HG, psi, lb/ft^2,
hpa and mb.  The units are specified as: 'in HG', 'mm HG', 'psi',
'lb/in**2', 'psf', 'lb/ft**2 'hpa', 'mb' or 'pa'.

The speed units may be 'kt', 'mph', 'km/h', 'm/s' and 'ft/s'.
```

```python
def dp2cas(dp, press_units=default_press_units, speed_units=default_speed_units):
    """
    If the units are not specified, the units in default_units.py are used.

    """
    ...
    return cas
```

### Examples:

`Determine the CAS in kt that is equivalent to a differential pressure of 15 in HG:`

```bash
> dp2cas(15)
518.96637566127652

```

`Determine the CAS in mph that is equivalent to a differential pressure of 0.2 psi:`

```bash
> dp2cas(.2, press_units = 'psi', speed_units = 'mph')
105.88275188221526
```

## delta pressure and altitude to EAS

`Return the EAS for a given differential pressure (the difference between the pitot and static pressures) and altitude.`

```
    The pressure units may be in inches of HG, mm of HG, psi, lb/ft^2,
    hpa and mb.  The units are specified as: 'in HG', 'mm HG', 'psi',
    'lb/in**2', 'psf', 'lb/ft**2 'hpa', 'mb' or 'pa'.

    The speed units may be 'kt', 'mph', 'km/h', 'm/s' and 'ft/s'.

    The altitude may be in feet ('ft'), metres ('m'), kilometres ('km'),
    statute miles, ('sm') or nautical miles ('nm').
```

```python
def dp2eas(
dp,
altitude,
press_units=default_press_units,
speed_units=default_speed_units,
alt_units=default_alt_units,
):
    """
    If the units are not specified, the units in default_units.py are used.

    This first version only works for EAS < 661.48 kt.
    """
    ...
    return eas
```

## delta pressure, altitude and temperature to TAS

`Return the TAS for a given differential pressure (the difference between the pitot and static pressures) and altitude.`

```
The pressure units may be in inches of HG, mm of HG, psi, lb/ft^2,
    hpa and mb.  The units are specified as: 'in HG', 'mm HG', 'psi',
    'lb/in**2', 'psf', 'lb/ft**2 'hpa', 'mb' or 'pa'.

    The speed units may be 'kt', 'mph', 'km/h', 'm/s' and 'ft/s'.

    The altitude may be in feet ('ft'), metres ('m'), kilometres ('km'),
    statute miles, ('sm') or nautical miles ('nm').

    The temperature may be in deg C, F, K or R.
```

```python
def dp2tas(
dp,
altitude,
temp,
press_units=default_press_units,
speed_units=default_speed_units,
alt_units=default_alt_units,
temp_units=default_temp_units,
):
    """
    If the units are not specified, the units in default_units.py are used.

    This first version only works for TAS < 661.48 kt.
    """
    ...
    return tas
```

## speed to delta pressure

`Return a delta pressure (the difference between the pitot and static pressures) for a given speed. Subsonic equation.`

```python
def _speed2dp(
speed,
Pref,
Rhoref,
press_units=default_press_units,
speed_units=default_speed_units,
):
    ...
    return dp
```

## Super CAS to delta pressure

`Return the differential pressure (difference between pitot and static pressures) for a given CAS.`

```
This function only works for the following conditions: - CAS > 661.48 kt - speed in m/s - pressure in pa.
```

```python
def _super_cas2dp(mcas: float) -> float:
    ...
    return dp
```

## CAS to delta pressure

`Converts calibrated airspeed to differential pressure (difference between pitot and static pressures) for a given CAS`

```python
def cas2dp(
cas, speed_units=default_speed_units, press_units=default_press_units
) -> float:
"""
    Args:
        cas (float): calibrated airspeed
        speed_units (string, optional): kt', 'mph', 'km/h', 'm/s' or 'ft/s'. Defaults to default_speed_units.
        press_units (str, optional): inches of HG, mm of HG, psi, lb/ft^2,
                                hpa and mb.
                                The units are specified as: 'in HG',
                                'mm HG', 'psi','lb/in**2', 'psf', 'lb/ft**2 'hpa',
                                'mb' or 'pa'.
                                 Defaults to default_press_units.
    If the units are not specified, the units in default_units.py are used.

    """
    ...
    return dp
```

## EAS and altitude to delta pressure

`Return the differential pressure (difference between pitot and static pressures) for a given EAS.`

```
 The speed units may be 'kt', 'mph', 'km/h', 'm/s' and 'ft/s'.

    The pressure units may be in inches of HG, mm of HG, psi, lb/ft^2,
    hpa and mb.  The units are specified as: 'in HG', 'mm HG', 'psi',
    'lb/in**2', 'psf', 'lb/ft**2 'hpa', 'mb' or 'pa'.

    The altitude may be in feet ('ft'), metres ('m'), kilometres ('km'),
    statute miles, ('sm') or nautical miles ('nm').
```

```python
def eas2dp(
eas,
altitude,
speed_units=default_speed_units,
alt_units=default_alt_units,
press_units=default_press_units,
):
    """
    If the units are not specified, the units in default_units.py are used.

    This first version only works for CAS < 661.48 kt.
    """
    ...
    return dp
```

## TAS, altitude and temperature to delta pressure

`Return the differential pressure (difference between pitot and static pressures) for a given TAS.`

```The speed units may be 'kt', 'mph', 'km/h', 'm/s' and 'ft/s'.

    The pressure units may be in inches of HG, mm of HG, psi, lb/ft^2,
    hpa and mb.  The units are specified as: 'in HG', 'mm HG', 'psi',
    'lb/in**2', 'psf', 'lb/ft**2 'hpa', 'mb' or 'pa'.

    The altitude may be in feet ('ft'), metres ('m'), kilometres ('km'),
    statute miles, ('sm') or nautical miles ('nm').

    The temperature may be in deg C, F, K or R.
```

```python
def tas2dp(
tas,
altitude,
temp,
speed_units=default_speed_units,
alt_units=default_alt_units,
temp_units=default_temp_units,
press_units=default_press_units,
):
    """
    If the units are not specified, the units in default_units.py are used.

    This first version only works for CAS < 661.48 kt.
    """
    ...
    return dp
```

## CAS to EAS

`Return the EAS for a given CAS, pressure altitude and temperature.`

```The speed units may be 'kt', 'mph', 'km/h', 'm/s' and 'ft/s'.

    The altitude may be in feet ('ft'), metres ('m'), kilometres ('km'),
    statute miles, ('sm') or nautical miles ('nm').
```

```python
def cas2eas(
cas, altitude, speed_units=default_speed_units, alt_units=default_alt_units,
):
    """
    If the units are not specified, the units in default_units.py are used.
    """
    ...
    return eas
```

## interactive CAS to EAS

`Return the EAS for a given CAS, pressure altitude and temp, with interactive input from the user.`

```python
def i_cas2eas(data_items):
    # version that goes interactive, if required
    ...
    print(return_string)
```

## CAS to TAS

`Return the TAS for a given CAS, pressure altitude and temperature.`

```
The speed units may be 'kt', 'mph', 'km/h', 'm/s' and 'ft/s'.

    The altitude may be in feet ('ft'), metres ('m'), kilometres ('km'),
    statute miles, ('sm') or nautical miles ('nm').

    The temperature may be in deg C, F, K or R. The temperature defaults to std
    temperature if it is not input.
```

```python
def cas2tas(
cas,
altitude,
temp="std",
speed_units=default_speed_units,
alt_units=default_alt_units,
temp_units=default_temp_units,
):
    """
    If the units are not specified, the units in default_units.py are used.
    """
    ...
    return tas
```

## interactive CAS to TAS

`Return the TAS for a given CAS, pressure altitude and temp, with interactive input from the user.`

```python
def i_cas2tas(data_items):
    # version that goes interactive, if required
    ...
    print(return_string)
```

## EAS to TAS

`Return the TAS for a given EAS, pressure altitude and temperature.`

```
The speed units may be 'kt', 'mph', 'km/h', 'm/s' and 'ft/s'.

    The altitude may be in feet ('ft'), metres ('m'), kilometres ('km'),
    statute miles, ('sm') or nautical miles ('nm').

    The temperature may be in deg C, F, K or R. The temperature defaults to std
    temperature if it is not input.
```

```python
def eas2tas(
eas,
altitude,
temp="std",
speed_units=default_speed_units,
alt_units=default_alt_units,
temp_units=default_temp_units,
):
    """
    If the units are not specified, the units in default_units.py are used.
    """
    ...
    return tas
```

## interactive EAS to TAS

`Return the TAS for a given EAS, pressure altitude and temp, with interactive input from the user.`

```python
def i_eas2tas(data_items):
    # version that goes interactive, if required
    ...
    print(return_string)
```

## EAS to CAS

```python
def eas2cas(
eas, altitude, speed_units=default_speed_units, alt_units=default_alt_units,
):
"""
Return the CAS for a given EAS, pressure altitude and temperature.

    The speed units may be 'kt', 'mph', 'km/h', 'm/s' and 'ft/s'.

    The altitude may be in feet ('ft'), metres ('m'), kilometres ('km'),
    statute miles, ('sm') or nautical miles ('nm').

    If the units are not specified, the default units in default_units.py are used.

    Examples:

    Determine equivalent Air Speed for 250 kt CAS at 10,000 ft:
    >>> cas2eas(250, 10000)
    248.09577137102258

    Determine equivalent Air Speed for 250 mph CAS at 10,000 ft:
    >>> cas2eas(250, 10000, speed_units = 'mph')
    248.54048288757579
    """

    dp = eas2dp(eas, altitude, speed_units, alt_units)
    cas = dp2cas(dp, speed_units=speed_units)

    return cas
```

## interactive EAS to CAS

```python
def i_eas2cas(data_items):
"""
Return the CAS for a given EAS, pressure altitude, with
interactive input from the user.

    The speed units may be 'kt', 'mph', 'km/h', 'm/s' and 'ft/s'.

    The altitude may be in feet ('ft'), metres ('m'), kilometres ('km'),
    statute miles, ('sm') or nautical miles ('nm').

    If the units are not specified, the units in default_units.py are used.

    """

    data_items["eas"] = _get_EAS(data_items)
    eas = data_items["eas"]

    data_items["speed_units"] = _get_speed_units(data_items)
    speed_units = data_items["speed_units"]

    data_items["altitude"] = _get_alt(data_items)
    altitude = data_items["altitude"]

    data_items["alt_units"] = _get_alt_units(data_items)
    alt_units = data_items["alt_units"]

    print()
    print("EAS = ", eas, speed_units)
    print("Altitude = ", altitude, alt_units)
    print()

    cas = eas2cas(eas, altitude, speed_units, alt_units)
    data_items["cas"] = cas
    return_string = "CAS = " + str(cas) + " " + speed_units
    print(return_string)
```

## TAS to CAS

```python
def tas2cas(
tas,
altitude,
temp="std",
speed_units=default_speed_units,
alt_units=default_alt_units,
temp_units=default_temp_units,
):
"""
Return the CAS for a given TAS, pressure altitude and temperature.

    The speed units may be 'kt', 'mph', 'km/h', 'm/s' and 'ft/s'.

    The altitude may be in feet ('ft'), metres ('m'), kilometres ('km'),
    statute miles, ('sm') or nautical miles ('nm').

    The temperature may be in deg C, F, K or R. The temperature defaults to std
    temperature if it is not input.

    If the units are not specified, the units in default_units.py are used.

    Examples:

    Determine the true Air Speed for 250 kt CAS at 10,000 ft with standard
    temperature:
    >>> cas2tas(250, 10000)
    288.70227231079861

    Determine the true Air Speed for 250 mph CAS at 10,000 ft with standard
    temperature:
    >>> cas2tas(250, 10000, speed_units = 'mph')
    289.21977095514148

    Determine the true Air Speed for 250 mph CAS at 10,000 ft with
    temperature of 0 deg C:
    >>> cas2tas(250, 10000, 0, speed_units = 'mph')
    291.80148048806217

    Determine the true Air Speed for 250 mph CAS at 10,000 ft with
    temperature of 0 deg F:
    >>> cas2tas(250, 10000, 0, speed_units = 'mph', temp_units = 'F')
    282.14588227473797
    """

    if temp == "std":
        temp = SA.alt2temp(altitude, temp_units=temp_units, alt_units=alt_units)

    dp = tas2dp(
        tas, altitude, temp, speed_units, alt_units=alt_units, temp_units=temp_units,
    )
    cas = dp2cas(dp, speed_units=speed_units)

    return cas
```

## interactive TAS to CAS

```python
def i_tas2cas(data_items):
"""
Return the CAS for a given TAS, pressure altitude and temp, with
interactive input from the user.

    The speed units may be 'kt', 'mph', 'km/h', 'm/s' and 'ft/s'.

    The altitude may be in feet ('ft'), metres ('m'), kilometres ('km'),
    statute miles, ('sm') or nautical miles ('nm').

    The temperature may be in deg C, F, K or R. The temperature defaults to std
    temperature if it is not input.

    If the units are not specified, the units in default_units.py are used.

    """

    data_items["tas"] = _get_TAS(data_items)
    tas = data_items["tas"]

    data_items["speed_units"] = _get_speed_units(data_items)
    speed_units = data_items["speed_units"]

    data_items["altitude"] = _get_alt(data_items)
    altitude = data_items["altitude"]

    data_items["alt_units"] = _get_alt_units(data_items)
    alt_units = data_items["alt_units"]

    data_items["temp_units"] = _get_temp_units(data_items)
    temp_units = data_items["temp_units"]

    data_items["temp"] = _get_temp(data_items)
    temp = data_items["temp"]

    print()
    print("TAS = ", tas, speed_units)
    print("Altitude = ", altitude, alt_units)
    print("Temperature = ", temp, "deg", temp_units)
    print()

    cas = tas2cas(tas, altitude, temp, speed_units, alt_units, temp_units,)
    data_items["cas"] = cas
    return_string = "CAS = " + str(cas) + " " + speed_units
    print(return_string)
```

## TAS to EAS

```python
def tas2eas(
tas,
altitude,
temp="std",
speed_units=default_speed_units,
alt_units=default_alt_units,
temp_units=default_temp_units,
):
"""
Return the EAS for a given TAS, pressure altitude and temperature.

    The speed units may be 'kt', 'mph', 'km/h', 'm/s' and 'ft/s'.

    The altitude may be in feet ('ft'), metres ('m'), kilometres ('km'),
    statute miles, ('sm') or nautical miles ('nm').

    The temperature may be in deg C, F, K or R. The temperature defaults to std
    temperature if it is not input.

    If the units are not specified, the units in default_units.py are used.

    """

    if temp == "std":
        temp = SA.alt2temp(altitude, temp_units=temp_units, alt_units=alt_units)

    dp = tas2dp(
        tas, altitude, temp, speed_units, alt_units=alt_units, temp_units=temp_units,
    )
    eas = dp2eas(dp, altitude, alt_units=alt_units, speed_units=speed_units)

    return eas
```

## interactive TAS to EAS

```python
def i_tas2eas(data_items):
"""
Return the EAS for a given TAS, pressure altitude and temp, with
interactive input from the user.

    The speed units may be 'kt', 'mph', 'km/h', 'm/s' and 'ft/s'.

    The altitude may be in feet ('ft'), metres ('m'), kilometres ('km'),
    statute miles, ('sm') or nautical miles ('nm').

    The temperature may be in deg C, F, K or R. The temperature defaults to std
    temperature if it is not input.

    If the units are not specified, the units in default_units.py are used.

    """

    data_items["tas"] = _get_TAS(data_items)
    tas = data_items["tas"]

    data_items["speed_units"] = _get_speed_units(data_items)
    speed_units = data_items["speed_units"]

    data_items["altitude"] = _get_alt(data_items)
    altitude = data_items["altitude"]

    data_items["alt_units"] = _get_alt_units(data_items)
    alt_units = data_items["alt_units"]

    data_items["temp_units"] = _get_temp_units(data_items)
    temp_units = data_items["temp_units"]

    data_items["temp"] = _get_temp(data_items)
    temp = data_items["temp"]

    print()
    print("TAS = ", tas, speed_units)
    print("Altitude = ", altitude, alt_units)
    print("Temperature = ", temp, "deg", temp_units)
    print()

    eas = tas2eas(tas, altitude, temp, speed_units, alt_units, temp_units,)
    data_items["eas"] = eas
    return_string = "EAS = " + str(eas) + " " + speed_units
    print(return_string)
```

## delta p over p to Mach

```python
def dp_over_p2mach(dp_over_p):
"""
Return the mach number for a given delta p over p.

    Mach must be less than or equal to 10.
    """

    #   mach = (5*( (dp_over_p + 1)**(2/7.) -1) )**0.5

    mach = M.sqrt(5.0 * ((dp_over_p + 1.0) ** (2.0 / 7.0) - 1.0))

    if mach <= 1.0:
        return mach
    else:

        # supersonic case - need to iterate a solution.  Set upper and lower
        # guesses, and iterate until we zero in on a mach that produces the
        # desired result.

        dp_over_p_seek = dp_over_p

        low = 1.0  # initial lower guess for mach

        # This function works up to Mach 10  The upper limit can be
        # extended by increasing the value of the initial upper guess
        # ("high").

        high = 10  # initial upper guess for mach

        # confirm initial low and high are OK:

        dp_over_p_low = mach2dp_over_p(low)
        if dp_over_p_low > dp_over_p_seek:
            raise ValueError("Initial lower mach guess is too high.")

        dp_over_p_high = mach2dp_over_p(high)
        if dp_over_p_high < dp_over_p_seek:
            raise ValueError("Initial upper mach guess is too low.")

        guess = (low + high) / 2.0
        dp_over_p_guess = mach2dp_over_p(guess)

        # keep iterating until dp is within 0.001% of desired value

        while M.fabs(dp_over_p_guess - dp_over_p_seek) / dp_over_p_seek > 1e-5:
            if dp_over_p_guess > dp_over_p_seek:
                high = guess
            else:
                low = guess

            guess = (low + high) / 2.0
            dp_over_p_guess = mach2dp_over_p(guess)

    return guess
```

## Mach to delta p over p

```python
def mach2dp_over_p(M):
"""
Return the delta p over p for a given mach number.
The result is equal to:
(pitot pressure - static pressure) / static pressure

    Example - determine the delta p over p at mach 0.4:

    >>> mach2dp_over_p(.4)
    0.11655196580975336
    """

    if M <= 1.0:
        dp_over_p = (M ** 2.0 / 5.0 + 1.0) ** 3.5 - 1.0
    else:
        dp_over_p = (F * M ** 7.0) / (7.0 * M ** 2.0 - 1.0) ** 2.5 - 1.0

    return dp_over_p
```

# conversions between cas, mach and altitude

> `NB: pick any two values, and find the third`

```python
def cas_mach2alt(
cas, mach, speed_units=default_speed_units, alt_units=default_alt_units,
):
    """
    Return the altitude that corresponds to a given CAS and mach.

    The speed units may be 'kt', 'mph', 'km/h', 'm/s' and 'ft/s'.

    The altitude may be in feet ('ft'), metres ('m'), kilometres ('km'),
    statute miles, ('sm') or nautical miles ('nm').

    If the units are not specified, the units in default_units.py are used.

    """

    dp = cas2dp(cas, speed_units=speed_units, press_units="pa")
    dp_over_p = mach2dp_over_p(mach)
    p = dp / dp_over_p
    altitude = SA.press2alt(p, press_units="pa", alt_units=alt_units)

    return altitude
```

```python
def i_cas_mach2alt(data_items):
    """
    Return the altitude that corresponds to a given CAS and mach, with an
    interactive interface.
    """

    data_items["cas"] = _get_CAS(data_items)
    cas = data_items["cas"]

    data_items["speed_units"] = _get_speed_units(data_items)
    speed_units = data_items["speed_units"]

    data_items["mach"] = _get_mach(data_items)
    mach = data_items["mach"]

    data_items["alt_units"] = _get_alt_units(data_items)
    alt_units = data_items["alt_units"]

    print()
    print("CAS = ", cas, speed_units)
    print("Mach = ", mach)

    #   print 'Desired altitude units are: ', alt_units

    print()

    alt = cas_mach2alt(cas, mach, speed_units, alt_units)
    data_items["altitude"] = alt

    return_string = "Altitude = " + str(alt) + " " + alt_units
    print(return_string)
```

```python
def cas_alt2mach(
cas, altitude, speed_units=default_speed_units, alt_units=default_alt_units,
):
    """
    Return the mach that corresponds to a given CAS and altitude.

    The speed units may be 'kt', 'mph', 'km/h', 'm/s' and 'ft/s'.

    The altitude may be in feet ('ft'), metres ('m'), kilometres ('km'),
    statute miles, ('sm') or nautical miles ('nm').

    If the units are not specified, the units in default_units.py are used.

    """

    dp = cas2dp(cas, speed_units=speed_units, press_units="pa")
    p = SA.alt2press(altitude, alt_units=alt_units, press_units="pa")
    dp_over_p = dp / p
    mach = dp_over_p2mach(dp_over_p)

    return mach
```

```python
def i_cas_alt2mach(data_items):
    """
    Return the mach that corresponds to a given CAS and altitude, using an
    interactive interface.
    """

    data_items["cas"] = _get_CAS(data_items)
    cas = data_items["cas"]

    data_items["speed_units"] = _get_speed_units(data_items)
    speed_units = data_items["speed_units"]

    data_items["altitude"] = _get_alt(data_items)
    altitude = data_items["altitude"]

    data_items["alt_units"] = _get_alt_units(data_items)
    alt_units = data_items["alt_units"]

    print()
    print("CAS = ", cas, speed_units)
    print("Altitude = ", altitude, alt_units)
    print()

    mach = cas_alt2mach(cas, altitude, speed_units, alt_units)
    data_items["mach"] = mach
    print("Mach = ", mach)
```

```python
def \_cas_alt2mach2(
cas, altitude, speed_units=default_speed_units, alt_units=default_alt_units,
):
"""
Alternative, trial variant of cas_alt2mach, using the equations from
USAF TPS notes.

    The speed units may be 'kt', 'mph', 'km/h', 'm/s' and 'ft/s'.

    The altitude may be in feet ('ft'), metres ('m'), kilometres ('km'),
    statute miles, ('sm') or nautical miles ('nm').

    If the units are not specified, the units in default_units.py are used.

    """

    PR = SA.alt2press_ratio(altitude, alt_units)
    cas = U.speed_conv(cas, from_units=speed_units, to_units="m/s")

    if cas <= A0:

        # <= 661.48 kt

        mach = M.sqrt(
            5.0
            * (
                ((1.0 / PR) * ((1.0 + 0.2 * (cas / A0) ** 2.0) ** 3.5 - 1.0) + 1.0)
                ** (2.0 / 7.0)
                - 1.0
            )
        )
    else:
        raise ValueError("CAS too high.")

    return mach
```

```python
def mach_alt2cas(
mach, altitude, alt_units=default_alt_units, speed_units=default_speed_units,
):
"""
Return the calibrated Air Speed that corresponds to a given mach and
altitude.

    The speed units may be 'kt', 'mph', 'km/h', 'm/s' and 'ft/s'.

    The altitude may be in feet ('ft'), metres ('m'), kilometres ('km'),
    statute miles, ('sm') or nautical miles ('nm').

    If the units are not specified, the units in default_units.py are used.

    """

    p = SA.alt2press(altitude, alt_units=alt_units, press_units="pa")
    dp_over_p = mach2dp_over_p(mach)
    dp = dp_over_p * p
    cas = dp2cas(dp, press_units="pa", speed_units=speed_units)

    return cas
```

```python
def i_mach_alt2cas(data_items):
"""
Return the calibrated Air Speed that corresponds to a given mach and
altitude, using an interactive interface.
"""

    data_items["mach"] = _get_mach(data_items)
    mach = data_items["mach"]

    data_items["altitude"] = _get_alt(data_items)
    altitude = data_items["altitude"]

    data_items["alt_units"] = _get_alt_units(data_items)
    alt_units = data_items["alt_units"]

    data_items["speed_units"] = _get_speed_units(data_items)
    speed_units = data_items["speed_units"]

    print()
    print("Altitude = ", altitude, alt_units)
    print("Mach = ", mach)
    print()

    cas = mach_alt2cas(mach, altitude, alt_units, speed_units)
    data_items["cas"] = cas
    return_string = "CAS = " + str(cas) + " " + speed_units
    print(return_string)
```

#

## Mach and temperature to TAS

```python
def mach2tas(
mach,
temp="std",
altitude="blank",
temp_units=default_temp_units,
alt_units=default_alt_units,
speed_units=default_speed_units,
):
"""
Return the TAS for a given mach number. The temperature or altitude
must also be specified. If the altitude is specified, the temperature
is assumed to be standard. If both the altitude and temperature are
specified, the altitude input is ignored.

    The speed units may be 'kt', 'mph', 'km/h', 'm/s' and 'ft/s'.

    The altitude may be in feet ('ft'), metres ('m'), kilometres ('km'),
    statute miles, ('sm') or nautical miles ('nm').

    The temperature may be in deg C, F, K or R. The temperature defaults to std
    temperature if it is not input.

    If the units are not specified, the units in default_units.py are used.

    Examples:

    Determine the TAS in kt at 0.8 mach at a temperature of
    -15 deg C:
    >>> mach2tas(0.8, -15)
    500.87884108468597

    Determine the TAS in kt at 0.8 mach at 30,000 ft, assuming
    standard temperature:
    >>> mach2tas(0.8, altitude = 30000)
    471.45798523415107

    Determine the TAS in mph at 0.8 mach at 5000 m, assuming
    standard temperature:
    >>> mach2tas(0.8, altitude = 5000, alt_units = 'm', speed_units = 'mph')
    573.60326790383715

    Determine the TAS in km/h at 0.4 mach at a temperature of
    300 deg K:
    >>> mach2tas(0.4, 300, temp_units = 'K', speed_units = 'km/h')
    499.99796329569176
    """

    if temp == "std":
        if altitude != "blank":
            temp = SA.alt2temp(altitude, temp_units=temp_units, alt_units=alt_units)
        else:
            raise ValueError(
                "At least one of the temperature or altitude must be specified."
            )

    tas = mach * SA.temp2speed_of_sound(temp, temp_units, speed_units)

    return tas
```

## interactive Mach and temperature to TAS

```python
def i_mach2tas(data_items):
"""
Return the TAS that corresponds to a given Mach, altitude, and temperature
using an interactive interface.
"""

    data_items["mach"] = _get_mach(data_items)
    mach = data_items["mach"]

    data_items["altitude"] = _get_alt(data_items)
    altitude = data_items["altitude"]

    data_items["alt_units"] = _get_alt_units(data_items)
    alt_units = data_items["alt_units"]

    data_items["temp_units"] = _get_temp_units(data_items)
    temp_units = data_items["temp_units"]

    data_items["temp"] = _get_temp(data_items)
    temp = data_items["temp"]

    data_items["speed_units"] = _get_speed_units(data_items)
    speed_units = data_items["speed_units"]

    print()
    print("Mach = ", mach)
    print("Altitude = ", altitude, alt_units)
    print("Temperature =", temp, temp_units)
    print()

    tas = mach2tas(mach, temp, altitude, temp_units, alt_units, speed_units,)
    data_items["tas"] = tas
    print("TAS = ", tas, speed_units)
```

## TAS and temperature to Mach

```python
def tas2mach(
tas,
temp="std",
altitude="blank",
temp_units=default_temp_units,
alt_units=default_alt_units,
speed_units=default_speed_units,
):
"""
Return the mach number for a given TAS. The temperature or altitude
must also be specified. If the altitude is specified, the temperature
is assumed to be standard. If both the altitude and temperature are
specified, the altitude input is ignored.

    The speed units may be 'kt', 'mph', 'km/h', 'm/s' and 'ft/s'.

    The altitude may be in feet ('ft'), metres ('m'), kilometres ('km'),
    statute miles, ('sm') or nautical miles ('nm').

    The temperature may be in deg C, F, K or R. The temperature defaults to std
    temperature if it is not input.

    If the units are not specified, the units in default_units.py are used.

    Examples:

    Determine the mach number for a TAS of 500 kt at a temperature of
    -15 deg C:
    >>> tas2mach(500, -15)
    0.79859632148519943

    Determine the mach number for a TAS of 500 kt at a temperature of
    0 deg F:
    >>> tas2mach(500, 0, temp_units = 'F')
    0.80292788758764277

    Determine the mach number for a TAS of 500 kt at an altitude of
    10,000 ft, assuming standard temperature:
    >>> tas2mach(500, altitude = 10000)
    0.78328945665870209

    Determine the mach number for a TAS of 400 mph at an altitude of
    5000 m, assuming standard temperature:
    >>> tas2mach(400, altitude = 5000, speed_units = 'mph', alt_units = 'm')
    0.55787687746166581
    """

    if temp == "std":
        if altitude != "blank":
            temp = SA.alt2temp(altitude, temp_units=temp_units, alt_units=alt_units)
        else:
            raise ValueError(
                "At least one of the temperature or altitude must be specified."
            )

    mach = tas / SA.temp2speed_of_sound(temp, temp_units, speed_units)

    return mach
```

## interactive TAS and temperature to Mach

```python
def i_tas2mach(data_items):
"""
Return the mach that corresponds to a given TAS, altitude, and temperature
using an interactive interface.
"""

    data_items["tas"] = _get_TAS(data_items)
    tas = data_items["tas"]

    data_items["speed_units"] = _get_speed_units(data_items)
    speed_units = data_items["speed_units"]

    data_items["altitude"] = _get_alt(data_items)
    altitude = data_items["altitude"]

    data_items["alt_units"] = _get_alt_units(data_items)
    alt_units = data_items["alt_units"]

    data_items["temp_units"] = _get_temp_units(data_items)
    temp_units = data_items["temp_units"]

    data_items["temp"] = _get_temp(data_items)
    temp = data_items["temp"]

    print()
    print("TAS = ", tas, speed_units)
    print("Altitude = ", altitude, alt_units)
    print("Temperature =", temp, temp_units)
    print()

    mach = tas2mach(tas, temp, altitude, temp_units, alt_units, speed_units,)
    data_items["mach"] = mach
    print("Mach = ", mach)
```

# Ram temperature rise calculations

## Mach and indicated temperature to ambient temperature

```python
def mach2temp(
mach, indicated_temp, recovery_factor, temp_units=default_temp_units,
):
"""
Return the ambient temp, given the mach number, indicated
temperature and the temperature probe's recovery factor.

    The temperature may be in deg C, F, K or R.

    If the units are not specified, the units in default_units.py are used.


    Examples:

    Determine the ambient temperature with an indicated temperature of
    -20 deg C at mach 0.6 with a probe recovery factor of 0.8:

    >>> mach2temp(0.6, -20, 0.8)
    -33.787291981845698

    Determine the ambient temperature with an indicated temperature of
    75 deg F at mach 0.3 with a probe recovery factor of 0.9:

    >>> mach2temp(0.3, 75, 0.9, temp_units = 'F')
    66.476427868529839
    """

    indicated_temp = U.temp_conv(indicated_temp, from_units=temp_units, to_units="K")
    ambient_temp = indicated_temp / (1.0 + (0.2 * recovery_factor) * mach ** 2.0)

    ambient_temp = U.temp_conv(ambient_temp, from_units="K", to_units=temp_units)

    return ambient_temp
```

## TAS and indicated temperature to ambient temperature

```python
def tas2temp(
tas,
indicated_temp,
recovery_factor,
speed_units=default_speed_units,
temp_units=default_temp_units,
):
"""
Return the ambient temp, given the TAS, indicated temperature
and the temperature probe's recovery factor.

    The speed units may be 'kt', 'mph', 'km/h', 'm/s' and 'ft/s'.

    The temperature may be in deg C, F, K or R. The temperature defaults to std
    temperature if it is not input.

    If the units are not specified, the units in default_units.py are used.

    """

    indicated_temp = U.temp_conv(indicated_temp, from_units=temp_units, to_units="K")
    tas = U.speed_conv(tas, from_units=speed_units, to_units="kt")

    # value 7592.4732909142658 was adjusted to make the result equal that
    # obtained using mach2temp

    ambient_temp = indicated_temp - (recovery_factor * tas ** 2.0) / 7592.4732909142658

    ambient_temp = U.temp_conv(ambient_temp, from_units="K", to_units=temp_units)

    return ambient_temp
```
