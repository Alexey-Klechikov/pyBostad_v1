import logging
from dataclasses import dataclass
from typing import List

import aiohttp  # type: ignore
import telegram_send  # type: ignore
from bs4 import BeautifulSoup  # type: ignore


@dataclass
class Account:
    login: str
    password: str
    username: str


class Log:
    def __init__(self, log):
        telegram_send.send(messages=[self.parse_log(log)])

    def parse_log(self, log):

        message = ""

        for row in log:
            site = row.split(": ")[0]
            message += f"{site}\n"

            statuses = row.split("(")[1:]
            for s in statuses:
                message += f'> {s.split(")")[0]}\n'

            message += "\n"

        return message


async def _get(session: aiohttp.ClientSession, url: str):
    async with session.get(url) as response:
        return await response.text()


async def _post(session: aiohttp.ClientSession, url: str, data: dict, headers: dict):
    async with session.post(url, data=data, headers=headers) as response:
        return await response.text()


async def ping_generic_schema(
    message: str,
    url: str,
    base: str,
    accounts: List[Account],
    static_fields: dict = {},
    dynamic_fields: List[str] = [],
) -> str:
    try:
        for account in accounts:
            async with aiohttp.ClientSession() as session:
                headers = {
                    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
                }

                info = {}
                for k, v in static_fields.items():
                    info[k.format(base=base)] = v.format(
                        login=account.login, password=account.password
                    )

                response_get = await _get(session, url)
                soup = BeautifulSoup(response_get, "html.parser")

                for field in dynamic_fields:
                    info[field] = soup.find("input", attrs={"name": field}).get("value", "")  # type: ignore

                response_post = await _post(session, url, data=info, headers=headers)
                soup = BeautifulSoup(response_post, "html.parser")

                success = True if str(soup).find(account.username) > 0 else False
                message += (
                    ("(OK - " if success else "(Error - ") + account.username + ") "
                )
                message = ("" if success else "---") + message

    except Exception as e:
        logging.error(e)

        message = "---" + message

    return message
