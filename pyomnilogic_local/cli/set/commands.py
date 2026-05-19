# Need to figure out how to resolve the 'Untyped decorator makes function "..." untyped' errors in mypy when using click decorators
# mypy: disable-error-code="misc"

from __future__ import annotations

import click

from pyomnilogic_local.cli.set.equipment import equipment_off, equipment_on
from pyomnilogic_local.cli.set.heater_temp import heater_temp, solar_temp
from pyomnilogic_local.cli.set.speed import speed


@click.group()
@click.pass_context
def set(ctx: click.Context) -> None:
    """Control pool equipment (turn on/off, set temperature, set speed).

    These commands send control signals to pool equipment. They require
    equipment system IDs which can be found using the 'get' commands.

    Use with caution — these commands directly control physical equipment.
    """
    ctx.ensure_object(dict)


# Register subcommands
set.add_command(equipment_on)
set.add_command(equipment_off)
set.add_command(heater_temp)
set.add_command(solar_temp)
set.add_command(speed)
