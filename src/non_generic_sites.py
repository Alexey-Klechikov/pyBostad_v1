from datetime import datetime
import json

import aiohttp  # type: ignore
from bs4 import BeautifulSoup  # type: ignore
from dateutil.relativedelta import relativedelta  # type: ignore

from .secrets import CREDENTIALS
from .utils import _get, _post


async def wallenstram() -> str:
    message = "Global, Wallenstam: "

    try:
        for account in [CREDENTIALS[acc] for acc in ["alex_5", "elena_5"]]:
            async with aiohttp.ClientSession() as session:
                url = "https://www.wallenstam.se/sv/mina-sidor/logga-in/Login/"

                # 1 - Login
                info = {"Username": account["login"], "Password": account["password"]}
                await _post(session, url, data=info, headers={})  # Login

                # 2 - Kö
                url = (
                    "https://www.wallenstam.se/sv/mina-sidor/bostadsko/koinstallningar/"
                )
                response_get = await _get(session, url)  # Queue
                soup = BeautifulSoup(response_get, "html.parser")

                # 3 - Update kö
                info = {
                    "ViewModel.FormView.UserId": soup.find(
                        "input", attrs={"id": "ViewModel_FormView_UserId"}
                    )[  # type: ignore
                        "value"
                    ],  # type: ignore
                    "renewButton": "Förnya köplats",
                }
                url = "https://www.wallenstam.se/sv/mina-sidor/bostadsko/koinstallningar/UpdateQueue/"
                await _post(session, url, data=info, headers={})  # Update queue

                # 4 - Check
                url = (
                    "https://www.wallenstam.se/sv/mina-sidor/bostadsko/koinstallningar/"
                )
                response_get = await _get(session, url)  # Queue
                soup = BeautifulSoup(response_get, "html.parser")

                success = (
                    True
                    if str(soup).find(
                        str(datetime.today() + relativedelta(years=1))[:10]
                    )
                    > 0
                    else False
                )
                message += (
                    ("(OK - " if success else "(Error - ") + account["username"] + ") "
                )
                message = ("" if success else "---") + message
    except:
        message = "---" + message

    return message


async def stangastaden() -> str:
    message = "Lindkoping, Stangastaden: "

    try:
        for account in [CREDENTIALS[acc] for acc in ["alex_1"]]:
            async with aiohttp.ClientSession() as session:
                url = "https://www.stangastaden.se/wp-json/stud/v1/loginuser"

                # 1 - Login
                info = {"username": account["login"], "password": account["password"]}
                await _post(session, url, data=info, headers={})  # Login

                # 2 - Check
                url = "https://www.stangastaden.se/minasidor/"
                response_get = await _get(session, url)  # Queue
                soup = BeautifulSoup(response_get, "html.parser")

                success = True if str(soup).find(account["username"]) > 0 else False

                message += (
                    ("(OK - " if success else "(Error - ") + account["username"] + ") "
                )
                message = ("" if success else "---") + message
    except:
        message = "---" + message

    return message


async def homeq() -> str:
    message = "Stockholm, HomeQ: "

    try:
        for account in [CREDENTIALS[acc] for acc in ["alex_6", "elena_6"]]:
            async with aiohttp.ClientSession() as session:
                url = "https://api.homeq.se/api/v1/user/profile/login"

                # 1 - Login
                info = {"email": account["login"], "password": account["password"]}
                response_post = await _post(
                    session,
                    url,
                    json.dumps(info),  # type: ignore
                    headers={},
                )  # Queue

                # # 2 - Check
                response_post = json.loads(response_post).get("user_info", {})
                success = (
                    response_post.get("has_profile", False) is True
                    and response_post.get("queue_points", 0) > 0
                )

                message += (
                    ("(OK - " if success else "(Error - ") + account["username"] + ") "
                )
                message = ("" if success else "---") + message
    except:
        message = "---" + message

    return message
