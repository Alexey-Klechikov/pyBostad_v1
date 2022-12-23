import requests
from bs4 import BeautifulSoup
from datetime import datetime
from dateutil.relativedelta import relativedelta
from pprint import pprint
from .log import Log


class Walk_Bostad:
    def __init__(self):
        self.log = []

        self._haninge_bostader()
        self._sollentuna_hem()
        self._derome_fastighet()
        self._vasby_hem()
        self._heimstaden()
        self._wallenstram()
        self._rikshem()
        self._bostaden_umea()
        self._upplands_brohus()
        self._heba_fast()
        self._hasselby_hem()
        self._ekero_bostader()
        self._forvaltaren()
        self._einar_mattsson()
        self._tyreso_bostader()
        self._lkf()
        self._aranas()

    def _heimstaden(self):
        message, ACCOUNTS = "Global, HeimStaden: ", [
            ["8904041236", "C804BBa0", "Alexey Klechikov"],
            ["8903057985", "Malvina123!", "Elena Belan"],
        ]

        try:
            for account in ACCOUNTS:
                URL = "https://mitt.heimstaden.com/mina-sidor/logga-in"

                with requests.session() as s:
                    base = (
                        "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$"
                    )

                    info = {
                        f"{base}txtUserID": account[0],
                        f"{base}txtPassword": account[1],
                        f"{base}btnLogin": "Logga in",
                    }

                    r_get = s.get(URL)
                    soup = BeautifulSoup(r_get.text, "html.parser")

                    for field in [
                        "__VIEWSTATE",
                        "__VIEWSTATEGENERATOR",
                        "__EVENTVALIDATION",
                        "ctl00$ctl01$hdnRequestVerificationToken",
                    ]:
                        info[field] = soup.find("input", attrs={"name": field})["value"]  # type: ignore

                    response_post = s.post(URL, data=info)
                    soup = BeautifulSoup(response_post.text, "html.parser")

                    success = True if str(soup).find(account[2]) > 0 else False
                    message += (
                        ("(OK - " if success else "(Error - ") + account[2] + ") "
                    )
                    message = ("" if success else "---") + message
        except:
            message = "---" + message

        self.log.append(message)

    def _wallenstram(self):
        message, ACCOUNTS = "Global, Wallenstam: ", [
            ["alexey.klechikov@gmail.com", "=Munk6V7", "Alexey Klechikov"],
            ["elena.belan@hotmail.com", "GForward!5", "Elena Belan"],
        ]

        try:
            for account in ACCOUNTS:
                URL = "https://www.wallenstam.se/sv/mina-sidor/logga-in/Login/"

                with requests.session() as s:
                    # 1 - Login
                    info = {"Username": account[0], "Password": account[1]}
                    s.post(URL, data=info)  # Login

                    # 2 - Kö
                    URL = "https://www.wallenstam.se/sv/mina-sidor/bostadsko/koinstallningar/"
                    response_get = s.get(URL)  # Queue
                    soup = BeautifulSoup(response_get.text, "html.parser")

                    # 3 - Update kö
                    info = {
                        "ViewModel.FormView.UserId": soup.find(
                            "input", attrs={"id": "ViewModel_FormView_UserId"}
                        )[
                            "value"
                        ],  # type: ignore
                        "renewButton": "Förnya köplats",
                    }
                    URL = "https://www.wallenstam.se/sv/mina-sidor/bostadsko/koinstallningar/UpdateQueue/"
                    s.post(URL, data=info)  # Update queue

                    # 4 - Check
                    URL = "https://www.wallenstam.se/sv/mina-sidor/bostadsko/koinstallningar/"
                    response_get = s.get(URL)  # Queue
                    soup = BeautifulSoup(response_get.text, "html.parser")

                    success = (
                        True
                        if str(soup).find(
                            str(datetime.today() + relativedelta(years=1))[:10]
                        )
                        > 0
                        else False
                    )
                    message += (
                        ("(OK - " if success else "(Error - ") + account[2] + ") "
                    )
                    message = ("" if success else "---") + message
        except:
            message = "---" + message

        self.log.append(message)

    def _rikshem(self):
        message, ACCOUNTS = "Global, RiksHem: ", [
            ["198904041236", "C804BBa0", "Alexey Klechikov"],
            ["198903057985", "Malvina123!", "Elena Belan"],
        ]

        try:
            for account in ACCOUNTS:
                URL = "https://minasidor.rikshem.se/mina-sidor/logga-in/Default.aspx"

                with requests.session() as s:
                    base = (
                        "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col1$LoginControl1$"
                    )

                    info = {
                        f"{base}txtUserID": account[0],
                        f"{base}txtPassword": account[1],
                        f"{base}btnLogin": "Logga in",
                    }

                    r_get = s.get(URL)
                    soup = BeautifulSoup(r_get.text, "html.parser")

                    for field in [
                        "__VIEWSTATE",
                        "__VIEWSTATEGENERATOR",
                        "__EVENTVALIDATION",
                    ]:
                        info[field] = soup.find("input", attrs={"name": field})["value"]  # type: ignore

                    response_post = s.post(URL, data=info)
                    soup = BeautifulSoup(response_post.text, "html.parser")

                    success = True if account[2] in str(soup) else False
                    message += (
                        ("(OK - " if success else "(Error - ") + account[2] + ") "
                    )
                    message = ("" if success else "---") + message
        except:
            message = "---" + message

        self.log.append(message)

    def _derome_fastighet(self):
        message, ACCOUNTS = "Global, DeromeFastighet: ", [
            ["8904041236", "C804BBa0", "Alexey Klechikov"],
            ["8903057985", "Malvina123!", "Elena Belan"],
        ]

        try:
            for account in ACCOUNTS:
                URL = "https://minasidor.deromefastighet.se/Account/Login?returnUrl="

                with requests.session() as s:
                    info = {
                        "UserId": account[0],
                        "Password": account[1],
                        "RememberMe": "true",
                    }

                    r_get = s.get(URL.split("/Account")[0])
                    soup = BeautifulSoup(r_get.text, "html.parser")

                    info["__RequestVerificationToken"] = soup.find("input", attrs={"name": "__RequestVerificationToken"})["value"]  # type: ignore

                    response_post = s.post(URL, data=info)
                    soup = BeautifulSoup(response_post.text, "html.parser")

                    success = True if str(soup).find(account[2]) > 0 else False
                    message += (
                        ("(OK - " if success else "(Error - ") + account[2] + ") "
                    )
                    message = ("" if success else "---") + message
        except:
            message = "---" + message

        self.log.append(message)

    def _bostaden_umea(self):
        message, ACCOUNTS = "Umea, Bostaden: ", [
            ["Alexey", "C804BBa0", "Alexey Klechikov"]
        ]

        try:
            for account in ACCOUNTS:
                URL = "https://www.bostaden.umea.se/mina-sidor/logga-in"

                with requests.session() as s:
                    headers = {
                        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
                    }

                    base = (
                        "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$"
                    )

                    info = {
                        f"{base}txtUserID": account[0],
                        f"{base}txtPassword": account[1],
                        f"{base}btnLogin": "Logga in",
                        f"{base}hdnSelectedTab": "p",
                    }

                    r_get = s.get(URL)
                    soup = BeautifulSoup(r_get.text, "html.parser")

                    for field in [
                        "ctl00$ctl01$hdnRequestVerificationToken",
                        "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$hdnSession",
                        "__VIEWSTATE",
                        "__VIEWSTATEGENERATOR",
                        "__EVENTVALIDATION",
                    ]:
                        info[field] = soup.find("input", attrs={"name": field})["value"]  # type: ignore

                    response_post = s.post(URL, data=info, headers=headers)
                    soup = BeautifulSoup(response_post.text, "html.parser")

                    success = True if account[2] in str(soup) else False
                    message += (
                        ("(OK - " if success else "(Error - ") + account[2] + ") "
                    )
                    message = ("" if success else "---") + message
        except:
            message = "---" + message

        self.log.append(message)

    def _vasby_hem(self):
        message, ACCOUNTS = "Stockholm, Vasbyhem: ", [
            ["8904041236", "C804BBa0", "Alexey Klechikov"],
            ["8903057985", "Malvina123!", "Elena Belan"],
        ]

        try:
            for account in ACCOUNTS:
                URL = "https://www.vasbyhem.se/Account/Login"

                with requests.session() as s:
                    info = {
                        "UserID": account[0],
                        "Password": account[1],
                        "RememberMe": "true",
                    }

                    r_get = s.get(URL)
                    soup = BeautifulSoup(r_get.text, "html.parser")

                    info["__RequestVerificationToken"] = soup.find(
                        "input", attrs={"name": "__RequestVerificationToken"}
                    )[
                        "value"
                    ]  # type: ignore

                    response_post = s.post(URL, data=info)
                    soup = BeautifulSoup(response_post.text, "html.parser")

                    success = True if str(soup).find(account[2]) > 0 else False
                    message += (
                        ("(OK - " if success else "(Error - ") + account[2] + ") "
                    )
                    message = ("" if success else "---") + message
        except:
            message = "---" + message

        self.log.append(message)

    def _upplands_brohus(self):
        message, ACCOUNTS = "Stockholm, Upplands-Brohus: ", [
            ["198904041236", "C804BBa0", "Alexey Klechikov"],
            ["elbl0001", "Malvina123!", "Elena Belan"],
        ]

        try:
            for account in ACCOUNTS:
                URL = "https://marknad.upplands-brohus.se/pgLogin.aspx"

                with requests.session() as s:
                    info = {
                        "__EVENTTARGET": "DoLogin",
                        "__EVENTARGUMENT": "{"
                        + f'"method":"LOGIN","username":"{account[0]}","password":"{account[1]}"'
                        + "}",
                    }

                    r_get = s.get(URL)
                    soup = BeautifulSoup(r_get.text, "html.parser")

                    for field in [
                        "__VIEWSTATE",
                        "__VIEWSTATEGENERATOR",
                    ]:
                        info[field] = soup.find("input", attrs={"name": field})["value"]  # type: ignore

                    response_post = s.post(URL, data=info)
                    soup = BeautifulSoup(response_post.text, "html.parser")

                    success = (
                        not soup.find(
                            "span",
                            attrs={
                                "id": "_ctl0__ctl0_HolderForNestedPage_placeAction_ucClientInfoWidget1_lbl_InfoWidgetName"
                            },
                        )
                        == None
                    )
                    message += (
                        ("(OK - " if success else "(Error - ") + account[2] + ") "
                    )
                    message = ("" if success else "---") + message
        except:
            message = "---" + message
        self.log.append(message)

    def _heba_fast(self):
        message, ACCOUNTS = "Stockholm, HebaFast: ", [
            ["8904041236", "C804BBa0", "Alexey Klechikov"],
            ["8903057985", "Malvina123!", "Elena Belan"],
        ]

        try:
            for account in ACCOUNTS:
                URL = "https://www.hebafast.se/mina-sidor/logga-in"

                with requests.session() as s:
                    base = (
                        "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$"
                    )

                    info = {
                        f"{base}txtUserID": account[0],
                        f"{base}txtPassword": account[1],
                        f"{base}btnLogin": "Logga in",
                    }

                    r_get = s.get(URL)
                    soup = BeautifulSoup(r_get.text, "html.parser")

                    for field in [
                        "__VIEWSTATE",
                        "__VIEWSTATEGENERATOR",
                        "__EVENTVALIDATION",
                        "ctl00$ctl01$hdnRequestVerificationToken",
                    ]:
                        info[field] = soup.find("input", attrs={"name": field})["value"]  # type: ignore

                    response_post = s.post(URL, data=info)
                    soup = BeautifulSoup(response_post.text, "html.parser")

                    success = (
                        True
                        if str(soup).find(
                            str(datetime.today() + relativedelta(years=1))[:10]
                        )
                        > 0
                        else False
                    )
                    message += (
                        ("(OK - " if success else "(Error - ") + account[2] + ") "
                    )
                    message = ("" if success else "---") + message
        except:
            message = "---" + message
        self.log.append(message)

    def _hasselby_hem(self):
        message, ACCOUNTS = "Stockholm, HasselbyHem: ", [
            ["8904041236", "C804BBa0", "Alexey Klechikov"],
            ["8903057985", "Malvina123!", "Elena Belan"],
        ]

        try:
            for account in ACCOUNTS:
                URL = "https://bostad.hasselbyhem.se/User/MyPagesLogin.aspx"

                with requests.session() as s:
                    base = (
                        "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$"
                    )

                    info = {
                        f"{base}txtUserID": account[0],
                        f"{base}txtPassword": account[1],
                        f"{base}btnLogin": "Logga in",
                    }

                    r_get = s.get(URL)
                    soup = BeautifulSoup(r_get.text, "html.parser")

                    for field in [
                        "__VIEWSTATE",
                        "__VIEWSTATEGENERATOR",
                        "__EVENTVALIDATION",
                    ]:
                        info[field] = soup.find("input", attrs={"name": field})["value"]  # type: ignore

                    response_post = s.post(URL, data=info)
                    soup = BeautifulSoup(response_post.text, "html.parser")

                    success = (
                        True
                        if str(soup).find(
                            str(datetime.today() + relativedelta(years=1))[:10]
                        )
                        > 0
                        else False
                    )
                    message += (
                        ("(OK - " if success else "(Error - ") + account[2] + ") "
                    )
                    message = ("" if success else "---") + message
        except:
            message = "---" + message

        self.log.append(message)

    def _ekero_bostader(self):
        message, ACCOUNTS = "Stockholm, EkeroBostader: ", [
            ["8904041236", "C804BBa0", "Alexey Klechikov"],
            ["8903057985", "Malvina123!", "Elena Belan"],
        ]

        try:
            for account in ACCOUNTS:
                URL = "https://minasidor.ekerobostader.se/mina-sidor/logga-in"

                with requests.session() as s:
                    base = (
                        "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$"
                    )

                    info = {
                        f"{base}txtUserID": account[0],
                        f"{base}txtPassword": account[1],
                        f"{base}btnLogin": "Logga in",
                    }

                    r_get = s.get(URL)
                    soup = BeautifulSoup(r_get.text, "html.parser")

                    for field in [
                        "__VIEWSTATE",
                        "__VIEWSTATEGENERATOR",
                        "__EVENTVALIDATION",
                    ]:
                        info[field] = soup.find("input", attrs={"name": field})["value"]  # type: ignore

                    response_post = s.post(URL, data=info)
                    soup = BeautifulSoup(response_post.text, "html.parser")

                    success = True if str(soup).find(" poäng)") > 0 else False
                    message += (
                        ("(OK - " if success else "(Error - ") + account[2] + ") "
                    )
                    message = ("" if success else "---") + message
        except:
            message = "---" + message

        self.log.append(message)

    def _forvaltaren(self):
        message, ACCOUNTS = "Stockholm, Forvaltaren: ", [
            ["8904041236", "C804BBa0", "Alexey Klechikov"],
            ["8903057985", "Malvina123!", "Elena Belan"],
        ]

        try:
            for account in ACCOUNTS:
                URL = "https://www.forvaltaren.se/mina-sidor/logga-in"

                with requests.session() as s:
                    base = (
                        "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$"
                    )
                    info = {
                        f"{base}txtUserID": account[0],
                        f"{base}txtPassword": account[1],
                        f"{base}btnLogin": "Logga in",
                    }

                    r_get = s.get(URL)
                    soup = BeautifulSoup(r_get.text, "html.parser")

                    for field in [
                        "__VIEWSTATE",
                        "__VIEWSTATEGENERATOR",
                        "__EVENTVALIDATION",
                    ]:
                        info[field] = soup.find("input", attrs={"name": field})["value"]  # type: ignore

                    response_post = s.post(URL, data=info)
                    soup = BeautifulSoup(response_post.text, "html.parser")

                    success = True if str(soup).find(account[2]) > 0 else False
                    message += (
                        ("(OK - " if success else "(Error - ") + account[2] + ") "
                    )
                    message = ("" if success else "---") + message
        except:
            message = "---" + message

        self.log.append(message)

    def _einar_mattsson(self):
        message, ACCOUNTS = "Stockholm, EinarMattsson: ", [
            ["8904041236", "C804BBa0", "Alexey Klechikov"],
            ["8903057985", "Malvina123!", "Elena Belan"],
        ]
        try:
            for account in ACCOUNTS:
                URL = "https://minasidor.einarmattsson.se/User/MyPagesLogin.aspx"

                with requests.session() as s:
                    base = (
                        "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$"
                    )
                    info = {
                        f"{base}txtUserID": account[0],
                        f"{base}txtPassword": account[1],
                        f"{base}btnLogin": "Logga in",
                    }

                    r_get = s.get(URL)
                    soup = BeautifulSoup(r_get.text, "html.parser")

                    for field in [
                        "__VIEWSTATE",
                        "__VIEWSTATEGENERATOR",
                        "__EVENTVALIDATION",
                        "ctl00$ctl01$hdnRequestVerificationToken",
                    ]:
                        info[field] = soup.find("input", attrs={"name": field})["value"]  # type: ignore

                    response_post = s.post(URL, data=info)
                    soup = BeautifulSoup(response_post.text, "html.parser")

                    success = (
                        True
                        if str(soup).find(
                            str(datetime.today() + relativedelta(years=1))[:10]
                        )
                        > 0
                        else False
                    )
                    message += (
                        ("(OK - " if success else "(Error - ") + account[2] + ") "
                    )
                    message = ("" if success else "---") + message
        except:
            message = "---" + message

        self.log.append(message)

    def _haninge_bostader(self):
        message, ACCOUNTS = "Stockholm, HaningeBostader: ", [
            ["8904041236", "C804BBa0", "Alexey Klechikov"],
            ["8903057985", "Malvina123!", "Elena Belan"],
        ]

        try:
            for account in ACCOUNTS:
                URL = "https://minasidor.haningebostader.se/"

                with requests.session() as s:
                    info = {
                        "UserId": account[0],
                        "Password": account[1],
                        "RememberMe": "true",
                    }

                    r_get = s.get(URL)
                    soup = BeautifulSoup(r_get.text, "html.parser")

                    info["__RequestVerificationToken"] = soup.find("input", attrs={"name": "__RequestVerificationToken"})["value"]  # type: ignore

                    response_post = s.post(URL, data=info)
                    soup = BeautifulSoup(response_post.text, "html.parser")

                    success = True if str(soup).find(account[2]) > 0 else False
                    message += (
                        ("(OK - " if success else "(Error - ") + account[2] + ") "
                    )
                    message = ("" if success else "---") + message
        except:
            message = "---" + message

        self.log.append(message)

    def _sollentuna_hem(self):
        message, ACCOUNTS = "Stockholm, SollentunaHem: ", [
            ["8904041236", "C804BBa0", "Alexey Klechikov"],
            ["8903057985", "Malvina123!", "Elena Belan"],
        ]

        try:
            for account in ACCOUNTS:
                URL = "https://minasidor.sollentunahem.se/mina-sidor/logga-in"

                with requests.session() as s:
                    info = {
                        "UserId": account[0],
                        "Password": account[1],
                        "RememberMe": "true",
                    }

                    r_get = s.get(URL)
                    soup = BeautifulSoup(r_get.text, "html.parser")

                    info["__RequestVerificationToken"] = soup.find("input", attrs={"name": "__RequestVerificationToken"})["value"]  # type: ignore

                    response_post = s.post(URL, data=info)
                    soup = BeautifulSoup(response_post.text, "html.parser")

                    success = True if str(soup).find(account[2]) > 0 else False
                    message += (
                        ("(OK - " if success else "(Error - ") + account[2] + ") "
                    )
                    message = ("" if success else "---") + message
        except:
            message = "---" + message

        self.log.append(message)

    def _tyreso_bostader(self):
        message, ACCOUNTS = "Stockholm, TyresoBostader: ", [
            ["8904041236", "C804BBa0", "Alexey Klechikov"],
            ["8903057985", "Malvina123!", "Elena Belan"],
        ]

        try:
            for account in ACCOUNTS:
                URL = "https://www.tyresobostader.se/mina-sidor/logga-in"
                with requests.session() as s:
                    # Login
                    base = (
                        "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$"
                    )

                    info = {
                        f"{base}txtUserID": account[0],
                        f"{base}txtPassword": account[1],
                        f"{base}btnLogin": "Logga in",
                    }

                    r_get = s.get(URL)
                    soup = BeautifulSoup(r_get.text, "html.parser")

                    for field in [
                        "__VIEWSTATE",
                        "__VIEWSTATEGENERATOR",
                        "__EVENTVALIDATION",
                    ]:
                        info[field] = soup.find("input", attrs={"name": field})["value"]  # type: ignore

                    response_post = s.post(URL, data=info)

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
                    URL = "https://www.tyresobostader.se/mina-sidor/intresseanmalan/lagenhet"

                    r_get = s.get(URL)
                    soup = BeautifulSoup(r_get.text, "html.parser")

                    for field in [
                        "__VIEWSTATE",
                        "__VIEWSTATEGENERATOR",
                        "__EVENTVALIDATION",
                    ]:
                        info[field] = soup.find("input", attrs={"name": field})["value"]  # type: ignore

                    response_post = s.post(URL, data=info)
                    soup = BeautifulSoup(response_post.text, "html.parser")

                    success = (
                        True
                        if str(soup).find(
                            str(datetime.today() + relativedelta(years=1))[:10]
                        )
                        > 0
                        else False
                    )
                    message += (
                        ("(OK - " if success else "(Error - ") + account[2] + ") "
                    )
                    message = ("" if success else "---") + message
        except:
            message = "---" + message

        self.log.append(message)

    def _lkf(self):
        message, ACCOUNTS = "Lund, lkf: ", [
            ["8904041236", "C804BBa0", "Alexey Klechikov"],
            ["8903057985", "Malvina123!", "Elena Belan"],
        ]

        try:
            for account in ACCOUNTS:
                URL = "https://minasidor.lkf.se/User/MyPagesLogin.aspx"
                with requests.session() as s:
                    base = (
                        "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$"
                    )

                    info = {
                        f"{base}txtUserID": account[0],
                        f"{base}txtPassword": account[1],
                        f"{base}btnLogin": "Logga in",
                    }

                    r_get = s.get(URL)
                    soup = BeautifulSoup(r_get.text, "html.parser")

                    for field in [
                        "__VIEWSTATE",
                        "__VIEWSTATEGENERATOR",
                        "__EVENTVALIDATION",
                        "ctl00$ctl01$hdnRequestVerificationToken",
                    ]:
                        info[field] = soup.find("input", attrs={"name": field})["value"]  # type: ignore

                    response_post = s.post(URL, data=info)
                    soup = BeautifulSoup(response_post.text, "html.parser")

                    try:
                        r_get = s.get(
                            soup.find(
                                "a", attrs={"id": "ctl00_ctl01_ucTopLinks_hlMyPages"}
                            )[
                                "href"
                            ]  # type: ignore
                        )
                        soup = BeautifulSoup(r_get.text, "html.parser")
                    except:
                        pass

                    success = True if str(soup).find(account[2]) > 0 else False
                    message += (
                        ("(OK - " if success else "(Error - ") + account[2] + ") "
                    )
                    message = ("" if success else "---") + message
        except:
            message = "---" + message

        self.log.append(message)

    def _aranas(self):
        message, ACCOUNTS = "Goteborg, Aranas: ", [
            ["8904041236", "C804BBa0", "Alexey Klechikov", "2020-09-09"],
            ["8903057985", "Malvina123!", "Elena Belan", "2020-09-22"],
        ]

        try:
            for account in ACCOUNTS:
                URL = "https://marknad.aranas.se/User/MyPagesLogin.aspx"

                with requests.session() as s:
                    base = (
                        "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$"
                    )

                    info = {
                        f"{base}txtUserID": account[0],
                        f"{base}txtPassword": account[1],
                        f"{base}btnLogin": "Logga in",
                    }

                    r_get = s.get(URL)
                    soup = BeautifulSoup(r_get.text, "html.parser")

                    for field in [
                        "__VIEWSTATE",
                        "__VIEWSTATEGENERATOR",
                        "__EVENTVALIDATION",
                    ]:
                        info[field] = soup.find("input", attrs={"name": field})["value"]  # type: ignore

                    response_post = s.post(URL, data=info)
                    soup = BeautifulSoup(response_post.text, "html.parser")

                    success = True if str(soup).find(account[3]) > 0 else False
                    message += (
                        ("(OK - " if success else "(Error - ") + account[2] + ") "
                    )
                    message = ("" if success else "---") + message
        except:
            message = "---" + message

        self.log.append(message)


def run():
    walk_obj = Walk_Bostad()
    Log(walk_obj.log)
