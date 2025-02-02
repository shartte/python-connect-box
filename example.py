"""Get the data from an UPC Connect Box."""
import asyncio
from pprint import pprint

import aiohttp

from connect_box import ConnectBox


async def main():
    """Sample code to retrieve the data from an UPC Connect Box."""
    async with aiohttp.ClientSession() as session:
        client = ConnectBox(session, "password")

        # Print details about the downstream channel connectivity
        await client.async_get_downstream()
        pprint(client.ds_channels)

        # Print details about the upstream channel connectivity
        await client.async_get_upstream()
        pprint(client.us_channels)

        # Print details about the connected devices
        await client.async_get_devices()
        pprint(client.devices)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
