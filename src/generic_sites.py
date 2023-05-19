from .secrets import CREDENTIALS
from .utils import Account, Site

SITES = (
    Site(
        "Global, HeimStaden: ",
        "https://mitt.heimstaden.com/mina-sidor/logga-in",
        "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$",
        [
            Account(**CREDENTIALS["alex_1"]),
            Account(**CREDENTIALS["elena_1"]),
        ],
        {
            "{base}txtUserID": "{login}",
            "{base}txtPassword": "{password}",
            "{base}btnLogin": "Logga in",
        },
        [
            "__VIEWSTATE",
            "__VIEWSTATEGENERATOR",
            "__EVENTVALIDATION",
            "ctl00$ctl01$hdnRequestVerificationToken",
        ],
    ),
    Site(
        "Global, RiksHem: ",
        "https://minasidor.rikshem.se/mina-sidor/logga-in/Default.aspx",
        "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col1$LoginControl1$",
        [
            Account(**CREDENTIALS["alex_1"]),
            Account(**CREDENTIALS["elena_1"]),
        ],
        {
            "{base}txtUserID": "{login}",
            "{base}txtPassword": "{password}",
            "{base}btnLogin": "Logga in",
        },
        [
            "__VIEWSTATE",
            "__VIEWSTATEGENERATOR",
            "__EVENTVALIDATION",
        ],
    ),
    Site(
        "Goteborg, Aranas: ",
        "https://marknad.aranas.se/mina-sidor/logga-in",
        "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$",
        [
            Account(**CREDENTIALS["alex_1"]),
            Account(**CREDENTIALS["elena_1"]),
        ],
        {
            "UserID": "{login}",
            "Password": "{password}",
        },
        [
            "__RequestVerificationToken",
        ],
    ),
    Site(
        "Lund, lkf: ",
        "https://minasidor.lkf.se/User/MyPagesLogin.aspx",
        "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$",
        [
            Account(**CREDENTIALS["alex_1"]),
            Account(**CREDENTIALS["elena_1"]),
        ],
        {
            "{base}txtUserID": "{login}",
            "{base}txtPassword": "{password}",
            "{base}btnLogin": "Logga in",
        },
        [
            "__VIEWSTATE",
            "__VIEWSTATEGENERATOR",
            "__EVENTVALIDATION",
            "ctl00$ctl01$hdnRequestVerificationToken",
        ],
    ),
    Site(
        "Stockholm, EinarMattsson: ",
        "https://minasidor.einarmattsson.se/User/MyPagesLogin.aspx",
        "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$",
        [
            Account(**CREDENTIALS["alex_1"]),
            Account(**CREDENTIALS["elena_1"]),
        ],
        {
            "{base}txtUserID": "{login}",
            "{base}txtPassword": "{password}",
            "{base}btnLogin": "Logga in",
        },
        [
            "__VIEWSTATE",
            "__VIEWSTATEGENERATOR",
            "__EVENTVALIDATION",
            "ctl00$ctl01$hdnRequestVerificationToken",
        ],
    ),
    Site(
        "Global, DeromeFastighet: ",
        "https://minasidor.deromefastighet.se/Account/Login?returnUrl=",
        "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$",
        [
            Account(**CREDENTIALS["alex_1"]),
            Account(**CREDENTIALS["elena_1"]),
        ],
        {
            "UserId": "{login}",
            "Password": "{password}",
            "RememberMe": "true",
        },
        ["__RequestVerificationToken"],
    ),
    Site(
        "Stockholm, HaningeBostader: ",
        "https://www.vasbyhem.se/Account/Login",
        "",
        [
            Account(**CREDENTIALS["alex_1"]),
            Account(**CREDENTIALS["elena_1"]),
        ],
        {
            "UserID": "{login}",
            "Password": "{password}",
            "RememberMe": "true",
        },
        ["__RequestVerificationToken"],
    ),
    Site(
        "Stockholm, HebaFast: ",
        "https://www.hebafast.se/mina-sidor/logga-in",
        "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$",
        [
            Account(**CREDENTIALS["alex_1"]),
            Account(**CREDENTIALS["elena_1"]),
        ],
        {
            "{base}txtUserID": "{login}",
            "{base}txtPassword": "{password}",
            "{base}btnLogin": "Logga in",
        },
        [
            "__VIEWSTATE",
            "__VIEWSTATEGENERATOR",
            "__EVENTVALIDATION",
            "ctl00$ctl01$hdnRequestVerificationToken",
        ],
    ),
    Site(
        "Stockholm, HasselbyHem: ",
        "https://bostad.hasselbyhem.se/User/MyPagesLogin.aspx",
        "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$",
        [
            Account(**CREDENTIALS["alex_1"]),
            Account(**CREDENTIALS["elena_1"]),
        ],
        {
            "{base}txtUserID": "{login}",
            "{base}txtPassword": "{password}",
            "{base}btnLogin": "Logga in",
        },
        [
            "__VIEWSTATE",
            "__VIEWSTATEGENERATOR",
            "__EVENTVALIDATION",
        ],
    ),
    Site(
        "Stockholm, EkeroBostader: ",
        "https://minasidor.ekerobostader.se/mina-sidor/logga-in",
        "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$",
        [Account(**CREDENTIALS["alex_1"])],
        {
            "{base}txtUserID": "{login}",
            "{base}txtPassword": "{password}",
            "{base}btnLogin": "Logga in",
        },
        [
            "__VIEWSTATE",
            "__VIEWSTATEGENERATOR",
            "__EVENTVALIDATION",
        ],
    ),
    Site(
        "Stockholm, HaningeBostader: ",
        "https://minasidor.haningebostader.se/",
        "",
        [
            Account(**CREDENTIALS["alex_1"]),
            Account(**CREDENTIALS["elena_1"]),
        ],
        {
            "UserId": "{login}",
            "Password": "{password}",
            "RememberMe": "true",
        },
        ["__RequestVerificationToken"],
    ),
    Site(
        "Stockholm, SollentunaHem: ",
        "https://minasidor.sollentunahem.se/mina-sidor/logga-in",
        "",
        [
            Account(**CREDENTIALS["alex_1"]),
            Account(**CREDENTIALS["elena_1"]),
        ],
        {
            "UserId": "{login}",
            "Password": "{password}",
            "RememberMe": "true",
        },
        ["__RequestVerificationToken"],
    ),
    Site(
        "Helsinborg, Bjuv: ",
        "https://bostad.bjuvsbostader.se/mina-sidor/logga-in",
        "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$",
        [
            Account(**CREDENTIALS["alex_1"]),
            Account(**CREDENTIALS["elena_1"]),
        ],
        {
            "{base}txtUserID": "{login}",
            "{base}txtPassword": "{password}",
            "{base}btnLogin": "Logga in",
        },
        ["__VIEWSTATE", "__VIEWSTATEGENERATOR", "__EVENTVALIDATION"],
    ),
    Site(
        "Eda, Eda Bostad: ",
        "https://marknad-bostadsbolaget.eda.se//User/MyPagesLogin.aspx",
        "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$",
        [
            Account(**CREDENTIALS["alex_1"]),
            Account(**CREDENTIALS["elena_1"]),
        ],
        {
            "{base}txtUserID": "{login}",
            "{base}txtPassword": "{password}",
            "{base}btnLogin": "Logga in",
            "{base}hdnSelectedTab": "p",
        },
        [
            "__VIEWSTATE",
            "__VIEWSTATEGENERATOR",
            "__EVENTVALIDATION",
            "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$hdnSession",
            "ctl00$ctl01$hdnRequestVerificationToken",
        ],
    ),
    Site(
        "Malmo, MalmoCityFastigheter: ",
        "https://minasidor.malmocityfastigheter.se//CK/User/MyPagesLogin.aspx",
        "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col1$LoginControl1$",
        [
            Account(**CREDENTIALS["alex_2"]),
            Account(**CREDENTIALS["elena_2"]),
        ],
        {
            "{base}txtUserID": "{login}",
            "{base}txtPassword": "{password}",
            "{base}btnLogin": "Logga in",
            "{base}hdnSelectedTab": "p",
        },
        [
            "__VIEWSTATE",
            "__VIEWSTATEGENERATOR",
            "__EVENTVALIDATION",
            "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col1$LoginControl1$hdnSession",
            "ctl00$ctl01$hdnRequestVerificationToken",
        ],
    ),
    Site(
        "Tyreso, TyresoBostader: ",
        "https://www.tyresobostader.se/mina-sidor/logga-in",
        "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$",
        [
            Account(**CREDENTIALS["alex_1"]),
            Account(**CREDENTIALS["elena_1"]),
        ],
        {
            "{base}txtUserID": "{login}",
            "{base}txtPassword": "{password}",
            "{base}btnLogin": "Logga in",
        },
        [
            "__VIEWSTATE",
            "__VIEWSTATEGENERATOR",
            "__EVENTVALIDATION",
        ],
    ),
    Site(
        "Umea, Bostaden: ",
        "https://www.bostaden.umea.se/mina-sidor/logga-in",
        "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$",
        [
            Account(**CREDENTIALS["alex_3"]),
        ],
        {
            "{base}txtUserID": "{login}",
            "{base}txtPassword": "{password}",
            "{base}btnLogin": "Logga in",
            "{base}hdnSelectedTab": "p",
        },
        [
            "__VIEWSTATE",
            "__VIEWSTATEGENERATOR",
            "__EVENTVALIDATION",
            "ctl00$ctl01$hdnRequestVerificationToken",
            "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$hdnSession",
        ],
    ),
)
