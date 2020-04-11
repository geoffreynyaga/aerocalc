from distutils.core import setup

setup(
    name="aerocalc3",
    version="0.10",
    description="Aeronautical and Atmospheric Engineering Calculations",
    long_description="""
                        Aero-calculator is a pure python package that performs various aeronautical
                        engineering calculations.  Currently it provides airspeed conversions,
                        standard atmosphere calculations, static source error correction calculations
                        and unit conversions.
                    """,
    author="Geoffrey Nyaga",
    author_email="geoffrey@geoffreynyaga.com",
    url="https://aerocalc3.netlify.com",
    download_url="https://github.com/geoffreynyaga/aerocalc/archive/v_01.tar.gz",
    packages=["aerocalc3"],
    license="BSD",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Scientific/Engineering :: Atmospheric Science",
        "Programming Language :: Python :: 3",
    ],
)
