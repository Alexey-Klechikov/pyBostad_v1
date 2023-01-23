from datetime import datetime

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
                message += ("(OK - " if success else "(Error - ") + account["username"] + ") "
                message = ("" if success else "---") + message
    except:
        message = "---" + message

    return message


async def tyreso_bostader() -> str:
    message = "Stockholm, TyresoBostader: "

    try:
        for account in [CREDENTIALS[acc] for acc in ["alex_1", "elena_1"]]:
            async with aiohttp.ClientSession() as session:
                url = "https://www.tyresobostader.se/mina-sidor/logga-in"
                # Login
                base = "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$"
                info = {
                    f"{base}txtUserID": account["login"],
                    f"{base}txtPassword": account["password"],
                    f"{base}btnLogin": "Logga in",
                }

                response_get = await _get(session, url)
                soup = BeautifulSoup(response_get, "html.parser")

                for field in [
                    "__VIEWSTATE",
                    "__VIEWSTATEGENERATOR",
                    "__EVENTVALIDATION",
                ]:
                    info[field] = soup.find("input", attrs={"name": field})["value"]  # type: ignore

                await _post(session, url, data=info, headers={})

                # Update
                base = "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col1$"

                info = {
                    f"{base}txtNoOfAdults": "2",
                    f"{base}txtNoOfChildren": "1",
                    f"{base}chkAreas$0": "AREA_213",
                    f"{base}chkAreas$8": "AREA_212",
                    f"{base}chkAreas$16": "AREA_229",
                    f"{base}chkAreas$1": "AREA_211",
                    f"{base}chkAreas$9": "AREA_194",
                    f"{base}chkAreas$17": "AREA_208",
                    f"{base}chkAreas$2": "AREA_198",
                    f"{base}chkAreas$10": "AREA_533",
                    f"{base}chkAreas$18": "AREA_195",
                    f"{base}chkAreas$3": "AREA_207",
                    f"{base}chkAreas$11": "AREA_205",
                    f"{base}chkAreas$19": "AREA_209",
                    f"{base}chkAreas$4": "AREA_227",
                    f"{base}chkAreas$12": "AREA_222",
                    f"{base}chkAreas$20": "AREA_496",
                    f"{base}chkAreas$5": "AREA_223",
                    f"{base}chkAreas$13": "AREA_210",
                    f"{base}chkAreas$21": "AREA_206",
                    f"{base}chkAreas$6": "AREA_203",
                    f"{base}chkAreas$14": "AREA_199",
                    f"{base}chkAreas$22": "AREA_202",
                    f"{base}chkAreas$7": "AREA_196",
                    f"{base}chkAreas$15": "AREA_197",
                    f"{base}chkAreas$23": "AREA_201",
                    f"{base}txtMaxCost": "10000",
                    f"{base}drpMinRooms": "2",
                    f"{base}drpMaxRooms": "3",
                    f"{base}rblConsent": "1",
                    f"{base}rblSubscribe": "0",
                    f"{base}btnSave": "Spara",
                }
                url = (
                    "https://www.tyresobostader.se/mina-sidor/intresseanmalan/lagenhet"
                )

                response_get = await _get(session, url)
                soup = BeautifulSoup(response_get, "html.parser")

                for field in [
                    "__VIEWSTATE",
                    "__VIEWSTATEGENERATOR",
                    "__EVENTVALIDATION",
                ]:
                    info[field] = soup.find("input", attrs={"name": field})["value"]  # type: ignore

                response_post = await _post(session, url, data=info, headers={})
                soup = BeautifulSoup(response_post, "html.parser")

                success = (
                    True
                    if str(soup).find(
                        str(datetime.today() + relativedelta(years=1))[:10]
                    )
                    > 0
                    else False
                )
                message += ("(OK - " if success else "(Error - ") + account["username"] + ") "
                message = ("" if success else "---") + message
    except:
        message = "---" + message

    return message


async def upplands_brohus() -> str:
    message = "Stockholm, Upplands-Brohus: "

    try:
        for account in [CREDENTIALS[acc] for acc in ["alex_4", "elena_4"]]:
            async with aiohttp.ClientSession() as session:
                url = "https://marknad.upplands-brohus.se/pgLogin.aspx"
                info = {
                    "__EVENTTARGET": "DoLogin",
                    "__EVENTARGUMENT": "{"
                    + f'"method":"LOGIN","username":"{account["login"]}","password":"{account["password"]}"'
                    + "}",
                }

                response_get = await _get(session, url)
                soup = BeautifulSoup(response_get, "html.parser")

                for field in [
                    "__VIEWSTATE",
                    "__VIEWSTATEGENERATOR",
                ]:
                    info[field] = soup.find("input", attrs={"name": field})["value"]  # type: ignore

                response_post = await _post(session, url, data=info, headers={})
                soup = BeautifulSoup(response_post, "html.parser")

                success = True if str(soup).find(account["username"]) > 0 else False
                message += ("(OK - " if success else "(Error - ") + account["username"] + ") "
                message = ("" if success else "---") + message
    except:
        message = "---" + message

    return message
