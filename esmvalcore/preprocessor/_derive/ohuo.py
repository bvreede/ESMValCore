"""Derivation of variable `sispeed`."""

import logging
from iris import Constraint

from ._baseclass import DerivedVariableBase
from .._regrid import regrid

logger = logging.getLogger(__name__)


class DerivedVariable(DerivedVariableBase):
    """Derivation of variable `uhuo`."""

    # Required variables
    required = [
        {'short_name': 'uo', },
        {'short_name': 'thetao', }
    ]

    @staticmethod
    def calculate(cubes):
        """
        Compute horizontal ocean heat transport.

        From horizontal velocity and potential temperature.

        Arguments
        ----
            cubes: cubelist containing required variables.

        Returns
        -------
            Cube containing sea ice speed.

        """
        uo_cube = cubes.extract_strict(Constraint(name='sea_water_x_velocity'))
        thetao = cubes.extract_strict(
            Constraint(name='sea_water_potential_temperature')
        )
        rho = 1000.  # seawater density (1000 kg m^{-3})
        ohcp = 4000.  # specific ocean heat capacity (4000 J kg^{-1} K^{-1})
        try:
            return thetao * uo_cube * rho * ohcp
        except ValueError:
            uo_cube = regrid(uo_cube, thetao, 'linear')
        return thetao * uo_cube * rho * ohcp
