# mypy: disable-error-code="misc"

from __future__ import annotations

import asyncio
from typing import TYPE_CHECKING

import click

if TYPE_CHECKING:
    from pyomnilogic_local import OmniLogic


@click.command("heater-temp")
@click.argument("system_id", type=int)
@click.argument("temperature", type=int)
@click.pass_context
def heater_temp(ctx: click.Context, system_id: int, temperature: int) -> None:
    """Set heater target temperature (Fahrenheit).

    SYSTEM_ID is the virtual heater's system ID (use 'get heaters' to find it).
    TEMPERATURE is the target temperature in Fahrenheit.

    Example:
        omnilogic set heater-temp 4 82
    """
    omnilogic: OmniLogic = ctx.obj["OMNILOGIC"]

    heater = omnilogic.all_heaters.get_by_id(system_id)
    if heater is None:
        raise click.ClickException(f"No heater found with system_id {system_id}. Use 'omnilogic get heaters' to list available heaters.")

    asyncio.run(heater.set_temperature(temperature))
    click.echo(f"Set heater '{heater.name}' (system_id={system_id}) to {temperature}°F")


@click.command("solar-temp")
@click.argument("system_id", type=int)
@click.argument("temperature", type=int)
@click.pass_context
def solar_temp(ctx: click.Context, system_id: int, temperature: int) -> None:
    """Set solar heater target temperature (Fahrenheit).

    SYSTEM_ID is the virtual heater's system ID (use 'get heaters' to find it).
    TEMPERATURE is the target solar temperature in Fahrenheit.

    Example:
        omnilogic set solar-temp 4 90
    """
    omnilogic: OmniLogic = ctx.obj["OMNILOGIC"]

    heater = omnilogic.all_heaters.get_by_id(system_id)
    if heater is None:
        raise click.ClickException(f"No heater found with system_id {system_id}. Use 'omnilogic get heaters' to list available heaters.")

    asyncio.run(heater.set_solar_temperature(temperature))
    click.echo(f"Set solar temperature for '{heater.name}' (system_id={system_id}) to {temperature}°F")
