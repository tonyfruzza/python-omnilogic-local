# mypy: disable-error-code="misc"

from __future__ import annotations

import asyncio
from typing import TYPE_CHECKING

import click

if TYPE_CHECKING:
    from pyomnilogic_local import OmniLogic


@click.command("on")
@click.argument("system_id", type=int)
@click.pass_context
def equipment_on(ctx: click.Context, system_id: int) -> None:
    """Turn equipment on.

    SYSTEM_ID is the equipment's system ID. Works with heaters, pumps, filters,
    lights, and relays. Use the appropriate 'get' command to find system IDs.

    Example:
        omnilogic set on 5
    """
    omnilogic: OmniLogic = ctx.obj["OMNILOGIC"]

    equipment = omnilogic.get_equipment_by_id(system_id)
    if equipment is None:
        raise click.ClickException(f"No equipment found with system_id {system_id}.")

    if not hasattr(equipment, "turn_on"):
        raise click.ClickException(f"Equipment '{equipment.name}' (system_id={system_id}) does not support turn_on.")

    asyncio.run(equipment.turn_on())
    click.echo(f"Turned on '{equipment.name}' (system_id={system_id})")


@click.command("off")
@click.argument("system_id", type=int)
@click.pass_context
def equipment_off(ctx: click.Context, system_id: int) -> None:
    """Turn equipment off.

    SYSTEM_ID is the equipment's system ID. Works with heaters, pumps, filters,
    lights, and relays. Use the appropriate 'get' command to find system IDs.

    Example:
        omnilogic set off 5
    """
    omnilogic: OmniLogic = ctx.obj["OMNILOGIC"]

    equipment = omnilogic.get_equipment_by_id(system_id)
    if equipment is None:
        raise click.ClickException(f"No equipment found with system_id {system_id}.")

    if not hasattr(equipment, "turn_off"):
        raise click.ClickException(f"Equipment '{equipment.name}' (system_id={system_id}) does not support turn_off.")

    asyncio.run(equipment.turn_off())
    click.echo(f"Turned off '{equipment.name}' (system_id={system_id})")
