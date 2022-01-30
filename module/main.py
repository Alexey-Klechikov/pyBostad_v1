import requests
from bs4 import BeautifulSoup
from datetime import datetime
from dateutil.relativedelta import relativedelta
from pprint import pprint
from .log import Log


class Walk_Bostad():

    def __init__(self):
        self.log = []

        self._heimstaden()
        self._akelius()
        self._wallenstram()
        self._rikshem()
        self._deromeFastighet()
        self._bostaden_umea()
        self._vasbyhem()
        self._upplands_brohus()
        self._hebaFast()
        self._hasselbyHem()
        self._ekeroBostader()
        self._forvaltaren()
        self._einarMattsson()
        self._haningeBostader()
        self._sollentunaHem()
        self._tyresoBostader()
        self._lkf()
        self._aranas()

    def _heimstaden(self):
        # Global
        ## HeimStaden.se + +
        message, ACCOUNTS = "Global, HeimStaden: ", [["8904041236", "C804BBa0", "Alexey Klechikov"],
                                                     ["8903057985", "Malvina123!", "Elena Belan"]]
        try:
            for account in ACCOUNTS:
                URL = "https://mitt.heimstaden.com/mina-sidor/logga-in"
                with requests.session() as s:
                    info = {"ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$txtUserID": account[0],
                            "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$txtPassword": account[1],
                            "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$btnLogin": "Logga in"}

                    r_get = s.get(URL)
                    soup = BeautifulSoup(r_get.text, 'html.parser')

                    info["__VIEWSTATE"] = soup.find("input", attrs={"name": "__VIEWSTATE"})["value"]
                    info["__VIEWSTATEGENERATOR"] = soup.find("input", attrs={"name": "__VIEWSTATEGENERATOR"})["value"]
                    info["__EVENTVALIDATION"] = soup.find("input", attrs={"name": "__EVENTVALIDATION"})["value"]
                    info["ctl00$ctl01$hdnRequestVerificationToken"] = \
                        soup.find("input", attrs={"name": "ctl00$ctl01$hdnRequestVerificationToken"})["value"]

                    response_post = s.post(URL, data=info)
                    soup = BeautifulSoup(response_post.text, 'html.parser')

                    success = True if str(soup).find(account[2]) > 0 else False
                    message += ("(OK - " if success else "(Error - ") + account[2] + ") "
                    message = ("" if success else "---") + message
        except:
            message = "---" + message
        self.log.append(message)

    def _akelius(self):
        # Global
        ## Akelius.se +
        message, ACCOUNTS = "Global, Akelius: ", [["198904041236", "C804BBa0", "Alexey Klechikov"]]
        try:
            for account in ACCOUNTS:
                URL = "https://xpdapi.akelius.se/IncitXpandWeb07038_1/Internet/Cm/Logon.aspx"
                with requests.session() as s:
                    info = {"ctl00$cphRightFrame$LogonBox1$txtUserName": account[0],
                            "ctl00$cphRightFrame$LogonBox1$ctl00_cphRightFrame_LogonBox1_ctl06": account[1],
                            "ctl00$cphRightFrame$LogonBox1$btnLogon": "Logga in",
                            "ctl00$cphRightFrame$ContentManagementControl1$ImageExplorerUC$fuUploadImage": "(binary)"}

                    r_get = s.get(URL)
                    soup = BeautifulSoup(r_get.text, 'html.parser')

                    info["ctl00_ToolkitScriptManager1_HiddenField"] = \
                        soup.find("input", attrs={"name": "ctl00_ToolkitScriptManager1_HiddenField"})["value"]
                    info["__VIEWSTATE"] = soup.find("input", attrs={"name": "__VIEWSTATE"})["value"]
                    info["__VIEWSTATEGENERATOR"] = soup.find("input", attrs={"name": "__VIEWSTATEGENERATOR"})["value"]
                    info["__EVENTVALIDATION"] = soup.find("input", attrs={"name": "__EVENTVALIDATION"})["value"]

                    response_post = s.post(URL, data=info)
                    soup = BeautifulSoup(response_post.text, 'html.parser')

                    success = not soup.find("div", attrs={"id": 'ctl00_Header1_pnlPage'}) == None
                    message += ("(OK - " if success else "(Error - ") + account[2] + ") "
                    message = ("" if success else "---") + message
        except:
            message = "---" + message
        self.log.append(message)

    def _wallenstram(self):
        # Global
        ## Wallenstam.se + +
        message, ACCOUNTS = "Global, Wallenstam: ", [["alexey.klechikov@gmail.com", "=Munk6V7", "Alexey Klechikov"],
                                                     ["elena.belan@hotmail.com", "GForward!5", "Elena Belan"]]
        try:
            for account in ACCOUNTS:
                URL = "https://www.wallenstam.se/sv/mina-sidor/logga-in/Login/"
                with requests.session() as s:
                    # 1 - Login
                    info = {"Username": account[0],
                            "Password": account[1]}
                    response_post = s.post(URL, data=info)  # Login

                    # 2 - Kö
                    URL = "https://www.wallenstam.se/sv/mina-sidor/bostadsko/koinstallningar/"
                    response_get = s.get(URL)  # Queue
                    soup = BeautifulSoup(response_get.text, 'html.parser')

                    # 3 - Update kö
                    info = {
                        "ViewModel.FormView.UserId": soup.find("input", attrs={"id": "ViewModel_FormView_UserId"})["value"],
                        "renewButton": "Förnya köplats"}
                    URL = "https://www.wallenstam.se/sv/mina-sidor/bostadsko/koinstallningar/UpdateQueue/"
                    response_post = s.post(URL, data=info)  # Update queue

                    # 4 - Check
                    URL = "https://www.wallenstam.se/sv/mina-sidor/bostadsko/koinstallningar/"
                    response_get = s.get(URL)  # Queue
                    soup = BeautifulSoup(response_get.text, 'html.parser')

                    success = True if str(soup).find(str(datetime.today() + relativedelta(years=1))[:10]) > 0 else False
                    message += ("(OK - " if success else "(Error - ") + account[2] + ") "
                    message = ("" if success else "---") + message
        except:
            message = "---" + message
        self.log.append(message)

    def _ikanoBostad__depricated(self):
        # Global
        ## IkanoBostad.se + + --> Merged with HomeQ
        message, ACCOUNTS = "Global, IkanoBostad: ", [["8904041236", "C804BBa0!", "Alexey Klechikov"], ["8903057985", "Malvina123!", "Elena Belan"]]
        try:
            for account in ACCOUNTS:
                URL = "https://hyresratt.ikanobostad.se/mina-sidor/logga-in"
                with requests.session() as s:
                    info = {"ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$txtUserID": account[0],
                            "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$txtPassword": account[1],
                            "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$btnLogin": "Logga in"}

                    r_get = s.get(URL)
                    soup = BeautifulSoup(r_get.text, 'html.parser')

                    info["__VIEWSTATE"] = soup.find("input", attrs={"name": "__VIEWSTATE"})["value"]
                    info["__VIEWSTATEGENERATOR"] = soup.find("input", attrs={"name": "__VIEWSTATEGENERATOR"})["value"]
                    info["__EVENTVALIDATION"] = soup.find("input", attrs={"name": "__EVENTVALIDATION"})["value"]
                    info["ctl00$ctl01$hdnRequestVerificationToken"] = soup.find("input", attrs={"name": "ctl00$ctl01$hdnRequestVerificationToken"})["value"]

                    response_post = s.post(URL, data=info)
                    soup = BeautifulSoup(response_post.text, 'html.parser')

                    success = True if str(soup).find(str(datetime.today() + relativedelta(months=6))[:7]) > 0 else False
                    message += ("(OK - " if success else "(Error - ") + account[2] + ") "
                    message = ("" if success else "---") + message
        except:
            message = "---" + message
        self.log.append(message)

    def _rikshem(self):
        # Global
        ## RiksHem.se + +
        message, ACCOUNTS = "Global, RiksHem: ", [["198904041236", "C804BBa0", "Alexey Klechikov"],
                                                  ["198903057985", "Malvina123!", "Elena Belan"]]
        try:
            for account in ACCOUNTS:
                URL = 'https://minasidor.rikshem.se/mina-sidor/logga-in/Default.aspx'
                with requests.session() as s:
                    info = {"ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col1$LoginControl1$txtUserID": account[0],
                            "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col1$LoginControl1$txtPassword": account[1],
                            "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col1$LoginControl1$btnLogin": "Logga in"}

                    r_get = s.get(URL)
                    soup = BeautifulSoup(r_get.text, 'html.parser')
                    
                    info["__VIEWSTATE"] = soup.find("input", attrs={"name": "__VIEWSTATE"})["value"]
                    info["__VIEWSTATEGENERATOR"] = soup.find("input", attrs={"name": "__VIEWSTATEGENERATOR"})["value"]
                    info["__EVENTVALIDATION"] = soup.find("input", attrs={"name": "__EVENTVALIDATION"})["value"]

                    response_post = s.post(URL, data=info)
                    soup = BeautifulSoup(response_post.text, 'html.parser')
                    
                    success = True if account[2] in str(soup) else False
                    message += ("(OK - " if success else "(Error - ") + account[2] + ") "
                    message = ("" if success else "---") + message
        except:
            message = "---" + message
        self.log.append(message)

    def _deromeFastighet(self):
        # Global
        ## DeromeFastighet.se + +
        message, ACCOUNTS = "Global, DeromeFastighet: ", [["8904041236", "C804BBa0", "Alexey Klechikov"],
                                                          ["8903057985", "Malvina123!", "Elena Belan"]]
        try:
            for account in ACCOUNTS:
                URL = "https://www.deromefastighet.se/mina-sidor/logga-in"
                with requests.session() as s:
                    info = {"ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$txtUserID": account[0],
                            "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$txtPassword": account[1],
                            "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$btnLogin": "Logga in"}

                    r_get = s.get(URL)
                    soup = BeautifulSoup(r_get.text, 'html.parser')

                    info["__VIEWSTATE"] = soup.find("input", attrs={"name": "__VIEWSTATE"})["value"]
                    info["__VIEWSTATEGENERATOR"] = soup.find("input", attrs={"name": "__VIEWSTATEGENERATOR"})["value"]
                    info["__EVENTVALIDATION"] = soup.find("input", attrs={"name": "__EVENTVALIDATION"})["value"]

                    response_post = s.post(URL, data=info)
                    soup = BeautifulSoup(response_post.text, 'html.parser')

                    success = True if str(soup).find(str(datetime.today() + relativedelta(years=1))[:10]) > 0 else False
                    message += ("(OK - " if success else "(Error - ") + account[2] + ") "
                    message = ("" if success else "---") + message
        except:
            message = "---" + message
        self.log.append(message)

    def _bostaden_umea(self):
        # Umea
        ## Bostaden.Umea.se +
        message, ACCOUNTS = "Umea, Bostaden: ", [["Alexey", "C804BBa0", "Alexey Klechikov"]]
        try:
            for account in ACCOUNTS:
                URL = 'https://www.bostaden.umea.se'
                with requests.session() as s:
                    info = {"ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col1$LoginControl$txtUserID": account[0],
                            "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col1$LoginControl$txtPassword": account[1],
                            "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col1$LoginControl$btnLogin": "Logga in"}

                    r_get = s.get(URL)
                    soup = BeautifulSoup(r_get.text, 'html.parser')

                    info["ctl00$ctl01$hdnRequestVerificationToken"] = \
                        soup.find("input", attrs={"name": "ctl00$ctl01$hdnRequestVerificationToken"})["value"]
                    info["__VIEWSTATE"] = soup.find("input", attrs={"name": "__VIEWSTATE"})["value"]
                    info["__VIEWSTATEGENERATOR"] = soup.find("input", attrs={"name": "__VIEWSTATEGENERATOR"})["value"]
                    info["__EVENTVALIDATION"] = soup.find("input", attrs={"name": "__EVENTVALIDATION"})["value"]

                    response_post = s.post(URL, data=info)
                    soup = BeautifulSoup(response_post.text, 'html.parser')

                    searchDate = datetime.today() + relativedelta(years=1)
                    success = True if str(soup).find(
                        f"{searchDate.month}/{searchDate.day}/{searchDate.year}") > 0 else False
                    message += ("(OK - " if success else "(Error - ") + account[2] + ") "
                    message = ("" if success else "---") + message
        except:
            message = "---" + message
        self.log.append(message)

    def _vasbyhem(self):
        # Stockholm
        ## Vasbyhem.se + +
        message, ACCOUNTS = "Stockholm, Vasbyhem: ", [["8904041236", "C804BBa0", "Alexey Klechikov"],
                                                      ["8903057985", "Malvina123!", "Elena Belan"]]
        try:
            for account in ACCOUNTS:
                URL = "https://www.vasbyhem.se/mina-sidor/logga-in"
                with requests.session() as s:
                    info = {"ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$txtUserID": account[0],
                            "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$txtPassword": account[1],
                            "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$btnLogin": "Logga in"}

                    r_get = s.get(URL)
                    soup = BeautifulSoup(r_get.text, 'html.parser')

                    info["ctl00$ctl01$hdnRequestVerificationToken"] = \
                        soup.find("input", attrs={"name": "ctl00$ctl01$hdnRequestVerificationToken"})["value"]
                    info["__VIEWSTATE"] = soup.find("input", attrs={"name": "__VIEWSTATE"})["value"]
                    info["__VIEWSTATEGENERATOR"] = soup.find("input", attrs={"name": "__VIEWSTATEGENERATOR"})["value"]
                    info["__EVENTVALIDATION"] = soup.find("input", attrs={"name": "__EVENTVALIDATION"})["value"]

                    response_post = s.post(URL, data=info)
                    soup = BeautifulSoup(response_post.text, 'html.parser')

                    success = True if str(soup).find(str(datetime.today() + relativedelta(years=1))[:10]) > 0 else False
                    message += ("(OK - " if success else "(Error - ") + account[2] + ") "
                    message = ("" if success else "---") + message
        except:
            message = "---" + message
        self.log.append(message)

    def _upplands_brohus(self):
        # Stockholm
        ## Upplands-Brohus.se +
        message, ACCOUNTS = "Stockholm, Upplands-Brohus: ", [["198904041236", "C804BBa0", "Alexey Klechikov"],
                                                             ["elbl0001", "Malvina123!", "Elena Belan"]]
        try:
            for account in ACCOUNTS:
                URL = "https://marknad.upplands-brohus.se/pgLogin.aspx"
                with requests.session() as s:
                    info = {}

                    r_get = s.get(URL)
                    soup = BeautifulSoup(r_get.text, 'html.parser')
                    info["__EVENTTARGET"] = "DoLogin"
                    info["__EVENTARGUMENT"] = '{"method":"LOGIN","username":"' + account[0] + '","password":"' + account[
                        1] + '"}'
                    info["__VIEWSTATE"] = soup.find("input", attrs={"name": "__VIEWSTATE"})["value"]
                    info["__VIEWSTATEGENERATOR"] = soup.find("input", attrs={"name": "__VIEWSTATEGENERATOR"})["value"]

                    response_post = s.post(URL, data=info)
                    soup = BeautifulSoup(response_post.text, 'html.parser')

                    success = not soup.find("span", attrs={
                        "id": '_ctl0__ctl0_HolderForNestedPage_placeAction_ucClientInfoWidget1_lbl_InfoWidgetName'}) == None
                    message += ("(OK - " if success else "(Error - ") + account[2] + ") "
                    message = ("" if success else "---") + message
        except:
            message = "---" + message
        self.log.append(message)

    def _hebaFast(self):
        # Stockholm
        ## HebaFast.se + +
        message, ACCOUNTS = "Stockholm, HebaFast: ", [["8904041236", "C804BBa0", "Alexey Klechikov"],
                                                      ["8903057985", "Malvina123!", "Elena Belan"]]
        try:
            for account in ACCOUNTS:
                URL = "https://www.hebafast.se/mina-sidor/logga-in"
                with requests.session() as s:
                    info = {"ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$txtUserID": account[0],
                            "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$txtPassword": account[1],
                            "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$btnLogin": "Logga in"}

                    r_get = s.get(URL)
                    soup = BeautifulSoup(r_get.text, 'html.parser')

                    info["__VIEWSTATE"] = soup.find("input", attrs={"name": "__VIEWSTATE"})["value"]
                    info["__VIEWSTATEGENERATOR"] = soup.find("input", attrs={"name": "__VIEWSTATEGENERATOR"})["value"]
                    info["__EVENTVALIDATION"] = soup.find("input", attrs={"name": "__EVENTVALIDATION"})["value"]
                    info["ctl00$ctl01$hdnRequestVerificationToken"] = \
                        soup.find("input", attrs={"name": "ctl00$ctl01$hdnRequestVerificationToken"})["value"]

                    response_post = s.post(URL, data=info)
                    soup = BeautifulSoup(response_post.text, 'html.parser')

                    success = True if str(soup).find(str(datetime.today() + relativedelta(years=1))[:10]) > 0 else False
                    message += ("(OK - " if success else "(Error - ") + account[2] + ") "
                    message = ("" if success else "---") + message
        except:
            message = "---" + message
        self.log.append(message)

    def _hasselbyHem(self):
        # Stockholm
        ## HasselbyHem.se + +
        message, ACCOUNTS = "Stockholm, HasselbyHem: ", [["8904041236", "C804BBa0", "Alexey Klechikov"],
                                                         ["8903057985", "Malvina123!", "Elena Belan"]]
        try:
            for account in ACCOUNTS:
                URL = "https://bostad.hasselbyhem.se/User/MyPagesLogin.aspx"
                with requests.session() as s:
                    info = {"ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$txtUserID": account[0],
                            "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$txtPassword": account[1],
                            "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$btnLogin": "Logga in"}

                    r_get = s.get(URL)
                    soup = BeautifulSoup(r_get.text, 'html.parser')

                    info["__VIEWSTATE"] = soup.find("input", attrs={"name": "__VIEWSTATE"})["value"]
                    info["__VIEWSTATEGENERATOR"] = soup.find("input", attrs={"name": "__VIEWSTATEGENERATOR"})["value"]
                    info["__EVENTVALIDATION"] = soup.find("input", attrs={"name": "__EVENTVALIDATION"})["value"]

                    response_post = s.post(URL, data=info)
                    soup = BeautifulSoup(response_post.text, 'html.parser')

                    success = True if str(soup).find(str(datetime.today() + relativedelta(years=1))[:10]) > 0 else False
                    message += ("(OK - " if success else "(Error - ") + account[2] + ") "
                    message = ("" if success else "---") + message
        except:
            message = "---" + message
        self.log.append(message)

    def _ekeroBostader(self):
        # Stockholm
        ## EkeroBostader.se + +
        message, ACCOUNTS = "Stockholm, EkeroBostader: ", [["8904041236", "C804BBa0", "Alexey Klechikov"],
                                                           ["8903057985", "Malvina123!", "Elena Belan"]]
        try:
            for account in ACCOUNTS:
                URL = "https://minasidor.ekerobostader.se/mina-sidor/logga-in"
                with requests.session() as s:
                    info = {"ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$txtUserID": account[0],
                            "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$txtPassword": account[1],
                            "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$btnLogin": "Logga in"}

                    r_get = s.get(URL)
                    soup = BeautifulSoup(r_get.text, 'html.parser')

                    info["__VIEWSTATE"] = soup.find("input", attrs={"name": "__VIEWSTATE"})["value"]
                    info["__VIEWSTATEGENERATOR"] = soup.find("input", attrs={"name": "__VIEWSTATEGENERATOR"})["value"]
                    info["__EVENTVALIDATION"] = soup.find("input", attrs={"name": "__EVENTVALIDATION"})["value"]

                    response_post = s.post(URL, data=info)
                    soup = BeautifulSoup(response_post.text, 'html.parser')

                    success = True if str(soup).find(" poäng)") > 0 else False
                    message += ("(OK - " if success else "(Error - ") + account[2] + ") "
                    message = ("" if success else "---") + message
        except:
            message = "---" + message
        self.log.append(message)

    def _forvaltaren(self):
        # Stockholm
        ## Forvaltaren.se + +
        message, ACCOUNTS = "Stockholm, Forvaltaren: ", [["8904041236", "C804BBa0", "Alexey Klechikov"],
                                                         ["8903057985", "Malvina123!", "Elena Belan"]]
        try:
            for account in ACCOUNTS:
                URL = "https://www.forvaltaren.se/mina-sidor/logga-in"
                with requests.session() as s:
                    info = {"ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$txtUserID": account[0],
                            "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$txtPassword": account[1],
                            "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$btnLogin": "Logga in"}

                    r_get = s.get(URL)
                    soup = BeautifulSoup(r_get.text, 'html.parser')

                    info["__VIEWSTATE"] = soup.find("input", attrs={"name": "__VIEWSTATE"})["value"]
                    info["__VIEWSTATEGENERATOR"] = soup.find("input", attrs={"name": "__VIEWSTATEGENERATOR"})["value"]
                    info["__EVENTVALIDATION"] = soup.find("input", attrs={"name": "__EVENTVALIDATION"})["value"]

                    response_post = s.post(URL, data=info)
                    soup = BeautifulSoup(response_post.text, 'html.parser')

                    success = True if str(soup).find(account[2]) > 0 else False
                    message += ("(OK - " if success else "(Error - ") + account[2] + ") "
                    message = ("" if success else "---") + message
        except:
            message = "---" + message
        self.log.append(message)

    def _einarMattsson(self):
        # Stockholm
        ## EinarMattsson.se + +
        message, ACCOUNTS = "Stockholm, EinarMattsson: ", [["8904041236", "C804BBa0", "Alexey Klechikov"],
                                                           ["8903057985", "Malvina123!", "Elena Belan"]]
        try:
            for account in ACCOUNTS:
                URL = "https://minasidor.einarmattsson.se/User/MyPagesLogin.aspx"
                with requests.session() as s:
                    info = {"ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$txtUserID": account[0],
                            "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$txtPassword": account[1],
                            "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$btnLogin": "Logga in"}

                    r_get = s.get(URL)
                    soup = BeautifulSoup(r_get.text, 'html.parser')

                    info["__VIEWSTATE"] = soup.find("input", attrs={"name": "__VIEWSTATE"})["value"]
                    info["__VIEWSTATEGENERATOR"] = soup.find("input", attrs={"name": "__VIEWSTATEGENERATOR"})["value"]
                    info["__EVENTVALIDATION"] = soup.find("input", attrs={"name": "__EVENTVALIDATION"})["value"]
                    info["ctl00$ctl01$hdnRequestVerificationToken"] = \
                        soup.find("input", attrs={"name": "ctl00$ctl01$hdnRequestVerificationToken"})["value"]

                    response_post = s.post(URL, data=info)
                    soup = BeautifulSoup(response_post.text, 'html.parser')

                    success = True if str(soup).find(str(datetime.today() + relativedelta(years=1))[:10]) > 0 else False
                    message += ("(OK - " if success else "(Error - ") + account[2] + ") "
                    message = ("" if success else "---") + message
        except:
            message = "---" + message
        self.log.append(message)

    def _haningeBostader(self):
        # Stockholm
        ## HaningeBostader.se + +
        message, ACCOUNTS = "Stockholm, HaningeBostader: ", [["8904041236", "C804BBa0", "Alexey Klechikov", "2020-09-09"],
                                                             ["8903057985", "Malvina123!", "Elena Belan", "2020-09-22"]]
        try:
            for account in ACCOUNTS:
                URL = "https://minasidor.haningebostader.se/mina-sidor/logga-in"
                with requests.session() as s:
                    info = {"ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$txtUserID": account[0],
                            "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$txtPassword": account[1],
                            "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$btnLogin": "Logga in"}

                    r_get = s.get(URL)
                    soup = BeautifulSoup(r_get.text, 'html.parser')

                    info["__VIEWSTATE"] = soup.find("input", attrs={"name": "__VIEWSTATE"})["value"]
                    info["__VIEWSTATEGENERATOR"] = soup.find("input", attrs={"name": "__VIEWSTATEGENERATOR"})["value"]
                    info["__EVENTVALIDATION"] = soup.find("input", attrs={"name": "__EVENTVALIDATION"})["value"]
                    info["ctl00$ctl01$hdnRequestVerificationToken"] = \
                        soup.find("input", attrs={"name": "ctl00$ctl01$hdnRequestVerificationToken"})["value"]

                    response_post = s.post(URL, data=info)
                    soup = BeautifulSoup(response_post.text, 'html.parser')

                    success = True if str(soup).find(account[3]) > 0 else False
                    message += ("(OK - " if success else "(Error - ") + account[2] + ") "
                    message = ("" if success else "---") + message
        except:
            message = "---" + message
        self.log.append(message)

    def _sollentunaHem(self):
        # Stockholm
        ## SollentunaHem.se + +
        message, ACCOUNTS = "Stockholm, SollentunaHem: ", [["8904041236", "C804BBa0", "Alexey Klechikov", "2020-09-09"],
                                                           ["8903057985", "Malvina123!", "Elena Belan", "2020-09-22"]]
        try:
            for account in ACCOUNTS:
                URL = "https://minasidor.sollentunahem.se/mina-sidor/logga-in"
                with requests.session() as s:
                    info = {"ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$txtUserID": account[0],
                            "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$txtPassword": account[1],
                            "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$btnLogin": "Logga in"}

                    r_get = s.get(URL)
                    soup = BeautifulSoup(r_get.text, 'html.parser')

                    info["__VIEWSTATE"] = soup.find("input", attrs={"name": "__VIEWSTATE"})["value"]
                    info["__VIEWSTATEGENERATOR"] = soup.find("input", attrs={"name": "__VIEWSTATEGENERATOR"})["value"]
                    info["__EVENTVALIDATION"] = soup.find("input", attrs={"name": "__EVENTVALIDATION"})["value"]

                    response_post = s.post(URL, data=info)
                    soup = BeautifulSoup(response_post.text, 'html.parser')

                    success = True if str(soup).find(account[3]) > 0 else False
                    message += ("(OK - " if success else "(Error - ") + account[2] + ") "
                    message = ("" if success else "---") + message
        except:
            message = "---" + message
        self.log.append(message)

    def _tyresoBostader(self):
        # Stockholm
        ## TyresoBostader.se + +
        message, ACCOUNTS = "Stockholm, TyresoBostader: ", [["8904041236", "C804BBa0", "Alexey Klechikov"],
                                                            ["8903057985", "Malvina123!", "Elena Belan"]]
        try:
            for account in ACCOUNTS:
                URL = "https://www.tyresobostader.se/mina-sidor/logga-in"
                with requests.session() as s:
                    # Login
                    info = {"ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$txtUserID": account[0],
                            "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$txtPassword": account[1],
                            "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$btnLogin": "Logga in"}

                    r_get = s.get(URL)
                    soup = BeautifulSoup(r_get.text, 'html.parser')

                    info["__VIEWSTATE"] = soup.find("input", attrs={"name": "__VIEWSTATE"})["value"]
                    info["__VIEWSTATEGENERATOR"] = soup.find("input", attrs={"name": "__VIEWSTATEGENERATOR"})["value"]
                    info["__EVENTVALIDATION"] = soup.find("input", attrs={"name": "__EVENTVALIDATION"})["value"]

                    response_post = s.post(URL, data=info)

                    # Update
                    info = {"ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col1$txtNoOfAdults": "2",
                            "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col1$txtNoOfChildren": "1",
                            "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col1$chkAreas$0": "AREA_213",
                            "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col1$chkAreas$8": "AREA_212",
                            "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col1$chkAreas$16": "AREA_229",
                            "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col1$chkAreas$1": "AREA_211",
                            "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col1$chkAreas$9": "AREA_194",
                            "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col1$chkAreas$17": "AREA_208",
                            "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col1$chkAreas$2": "AREA_198",
                            "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col1$chkAreas$10": "AREA_533",
                            "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col1$chkAreas$18": "AREA_195",
                            "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col1$chkAreas$3": "AREA_207",
                            "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col1$chkAreas$11": "AREA_205",
                            "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col1$chkAreas$19": "AREA_209",
                            "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col1$chkAreas$4": "AREA_227",
                            "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col1$chkAreas$12": "AREA_222",
                            "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col1$chkAreas$20": "AREA_496",
                            "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col1$chkAreas$5": "AREA_223",
                            "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col1$chkAreas$13": "AREA_210",
                            "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col1$chkAreas$21": "AREA_206",
                            "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col1$chkAreas$6": "AREA_203",
                            "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col1$chkAreas$14": "AREA_199",
                            "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col1$chkAreas$22": "AREA_202",
                            "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col1$chkAreas$7": "AREA_196",
                            "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col1$chkAreas$15": "AREA_197",
                            "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col1$chkAreas$23": "AREA_201",
                            "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col1$txtMaxCost": "10000",
                            "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col1$drpMinRooms": "2",
                            "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col1$drpMaxRooms": "3",
                            "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col1$rblConsent": "1",
                            "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col1$rblSubscribe": "0",
                            "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col1$btnSave": "Spara"}
                    URL = "https://www.tyresobostader.se/mina-sidor/intresseanmalan/lagenhet"

                    r_get = s.get(URL)
                    soup = BeautifulSoup(r_get.text, 'html.parser')

                    info["__VIEWSTATE"] = soup.find("input", attrs={"name": "__VIEWSTATE"})["value"]
                    info["__VIEWSTATEGENERATOR"] = soup.find("input", attrs={"name": "__VIEWSTATEGENERATOR"})["value"]
                    info["__EVENTVALIDATION"] = soup.find("input", attrs={"name": "__EVENTVALIDATION"})["value"]

                    response_post = s.post(URL, data=info)
                    soup = BeautifulSoup(response_post.text, 'html.parser')

                    success = True if str(soup).find(str(datetime.today() + relativedelta(years=1))[:10]) > 0 else False
                    message += ("(OK - " if success else "(Error - ") + account[2] + ") "
                    message = ("" if success else "---") + message
        except:
            message = "---" + message
        self.log.append(message)

    def _lkf(self):
        # Lund
        ## lkf.se + +
        message, ACCOUNTS = "Lund, lkf: ", [["8904041236", "C804BBa0", "Alexey Klechikov"],
                                            ["8903057985", "Malvina123!", "Elena Belan"]]
        try:
            for account in ACCOUNTS:
                URL = "https://minasidor.lkf.se/User/MyPagesLogin.aspx"
                with requests.session() as s:
                    info = {"ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$txtUserID": account[0],
                            "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$txtPassword": account[1],
                            "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$btnLogin": "Logga in"}

                    r_get = s.get(URL)
                    soup = BeautifulSoup(r_get.text, 'html.parser')

                    info["ctl00$ctl01$hdnRequestVerificationToken"] = \
                        soup.find("input", attrs={"name": "ctl00$ctl01$hdnRequestVerificationToken"})["value"]
                    info["__VIEWSTATE"] = soup.find("input", attrs={"name": "__VIEWSTATE"})["value"]
                    info["__VIEWSTATEGENERATOR"] = soup.find("input", attrs={"name": "__VIEWSTATEGENERATOR"})["value"]
                    info["__EVENTVALIDATION"] = soup.find("input", attrs={"name": "__EVENTVALIDATION"})["value"]

                    response_post = s.post(URL, data=info)
                    soup = BeautifulSoup(response_post.text, 'html.parser')

                    try:
                        r_get = s.get(soup.find("a", attrs={"id": "ctl00_ctl01_ucTopLinks_hlMyPages"})["href"])
                        soup = BeautifulSoup(r_get.text, 'html.parser')
                    except:
                        pass

                    success = True if str(soup).find(account[2]) > 0 else False
                    message += ("(OK - " if success else "(Error - ") + account[2] + ") "
                    message = ("" if success else "---") + message
        except:
            message = "---" + message
        self.log.append(message)

    def _aranas(self):
        # Göteborg
        ## Aranas.se + +
        message, ACCOUNTS = "Goteborg, Aranas: ", [["8904041236", "C804BBa0", "Alexey Klechikov", "2020-09-09"],
                                                   ["8903057985", "Malvina123!", "Elena Belan", "2020-09-22"]]
        try:
            for account in ACCOUNTS:
                URL = "https://marknad.aranas.se/User/MyPagesLogin.aspx"
                with requests.session() as s:
                    info = {"ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$txtUserID": account[0],
                            "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$txtPassword": account[1],
                            "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$btnLogin": "Logga in"}

                    r_get = s.get(URL)
                    soup = BeautifulSoup(r_get.text, 'html.parser')

                    info["__VIEWSTATE"] = soup.find("input", attrs={"name": "__VIEWSTATE"})["value"]
                    info["__VIEWSTATEGENERATOR"] = soup.find("input", attrs={"name": "__VIEWSTATEGENERATOR"})["value"]
                    info["__EVENTVALIDATION"] = soup.find("input", attrs={"name": "__EVENTVALIDATION"})["value"]

                    response_post = s.post(URL, data=info)
                    soup = BeautifulSoup(response_post.text, 'html.parser')

                    success = True if str(soup).find(account[3]) > 0 else False
                    message += ("(OK - " if success else "(Error - ") + account[2] + ") "
                    message = ("" if success else "---") + message
        except:
            message = "---" + message
        self.log.append(message)

def run():
    walk_obj = Walk_Bostad()
    Log(walk_obj.log)
    
if __name__ == "__main__":
    run()