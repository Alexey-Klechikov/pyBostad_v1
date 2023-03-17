import asyncio
from inspect import getmembers, isfunction

from src import generic_sites, non_generic_sites, utils


async def main():
    SCRIPTS = [
        i[1]
        for i in getmembers(non_generic_sites, isfunction)
        if i[0] not in ("_get", "_post", "dataclass", "ping_generic_schema")
    ] + [site.ping for site in generic_sites.SITES]

    tasks = tuple(map(lambda s: asyncio.create_task(s()), SCRIPTS))
    responses = await asyncio.gather(*tasks)

    utils.Log(responses)


asyncio.run(main())
