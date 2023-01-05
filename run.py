import asyncio
from inspect import getmembers, isfunction
import itertools

from module import generic_sites, non_generic_sites, utils


async def run():
    SCRIPTS = (
        i[1]
        for i in (
            itertools.chain.from_iterable(
                [
                    getmembers(file, isfunction)
                    for file in (generic_sites, non_generic_sites)
                ]
            )
        )
        if i[0] not in ("_get", "_post", "dataclass", "ping_generic_schema")
    )

    tasks = tuple(map(lambda s: asyncio.create_task(s()), SCRIPTS))
    responses = await asyncio.gather(*tasks)

    utils.Log(responses)


asyncio.run(run())
