# mypy: disable-error-code="misc"

from __future__ import annotations

import asyncio
from typing import TYPE_CHECKING

import click

from pyomnilogic_local.filter import Filter
from pyomnilogic_local.pump import Pump

if TYPE_CHECKING:
    from pyomnilogic_local import OmniLogic


@click.command("speed")
@click.argument("system_id", type=int)
@click.argument("percent", type=int)
@click.pass_context
def speed(ctx: click.Context, system_id: int, percent: int) -> None:
    """Set pump or filter speed (0-100 percent).

    SYSTEM_ID is the pump or filter's system ID (use 'get pumps' or 'get filters' to find it).
    PERCENT is the speed percentage (0 will turn the pump off).

    Example:
        omnilogic set speed 3 75
    """
    omnilogic: OmniLogic = ctx.obj["OMNILOGIC"]

    equipment = omnilogic.all_pumps.get_by_id(system_id)
    if equipment is None:
        equipment = omnilogic.all_filters.get_by_id(system_id)

    if equipment is None:
        raise click.ClickException(
            f"No pump or filter found with system_id {system_id}. "
            "Use 'omnilogic get pumps' or 'omnilogic get filters' to list available equipment."
        )

    if not isinstance(equipment, (Pump, Filter)):
        raise click.ClickException(f"Equipment with system_id {system_id} is not a pump or filter.")

    asyncio.run(equipment.set_speed(percent))
    click.echo(f"Set '{equipment.name}' (system_id={system_id}) to {percent}%")
