from dataclasses import dataclass

from .utils import Account, Site

SITES = (
    Site(
        "Global, HeimStaden: ",
        "https://mitt.heimstaden.com/mina-sidor/logga-in",
        "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$",
        [
            Account("8904041236", "C804BBa0", "Alexey Klechikov"),
            Account("8903057985", "Malvina123!", "Elena Belan"),
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
            Account("198904041236", "C804BBa0", "Alexey Klechikov"),
            Account("198903057985", "Malvina123!", "Elena Belan"),
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
            Account("Alexey", "C804BBa0", "Alexey Klechikov"),
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
    Site(
        "Goteborg, Aranas: ",
        "https://marknad.aranas.se/User/MyPagesLogin.aspx",
        "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$",
        [
            Account("8904041236", "C804BBa0", "Alexey Klechikov"),
            Account("8903057985", "Malvina123!", "Elena Belan"),
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
        "Lund, lkf: ",
        "https://minasidor.lkf.se/User/MyPagesLogin.aspx",
        "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$",
        [
            Account("8904041236", "C804BBa0", "Alexey Klechikov"),
            Account("8903057985", "Malvina123!", "Elena Belan"),
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
            Account("8904041236", "C804BBa0", "Alexey Klechikov"),
            Account("8903057985", "Malvina123!", "Elena Belan"),
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
        "Stockholm, Forvaltaren: ",
        "https://www.forvaltaren.se/mina-sidor/logga-in",
        "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$",
        [
            Account("8904041236", "C804BBa0", "Alexey Klechikov"),
            Account("8903057985", "Malvina123!", "Elena Belan"),
        ],
        {
            "{base}txtUserID": "{login}",
            "{base}txtPassword": "{password}",
            "{base}btnLogin": "Logga in",
        },
        ["__VIEWSTATE", "__VIEWSTATEGENERATOR", "__EVENTVALIDATION"],
    ),
    Site(
        "Global, DeromeFastighet: ",
        "https://minasidor.deromefastighet.se/Account/Login?returnUrl=",
        "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$",
        [
            Account("8904041236", "C804BBa0", "Alexey Klechikov"),
            Account("8903057985", "Malvina123!", "Elena Belan"),
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
            Account("8904041236", "C804BBa0", "Alexey Klechikov"),
            Account("8903057985", "Malvina123!", "Elena Belan"),
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
            Account("8904041236", "C804BBa0", "Alexey Klechikov"),
            Account("8903057985", "Malvina123!", "Elena Belan"),
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
            Account("8904041236", "C804BBa0", "Alexey Klechikov"),
            Account("8903057985", "Malvina123!", "Elena Belan"),
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
        [
            Account("8904041236", "C804BBa0", "Alexey Klechikov"),
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
        "Stockholm, HaningeBostader: ",
        "https://minasidor.haningebostader.se/",
        "",
        [
            Account("8904041236", "C804BBa0", "Alexey Klechikov"),
            Account("8903057985", "Malvina123!", "Elena Belan"),
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
            Account("8904041236", "C804BBa0", "Alexey Klechikov"),
            Account("8903057985", "Malvina123!", "Elena Belan"),
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
            Account("8904041236", "C804BBa0", "Alexey Klechikov"),
            Account("8903057985", "Malvina123!", "Elena Belan"),
        ],
        {
            "{base}txtUserID": "{login}",
            "{base}txtPassword": "{password}",
            "{base}btnLogin": "Logga in",
        },
        ["__VIEWSTATE", "__VIEWSTATEGENERATOR", "__EVENTVALIDATION"],
    ),
    Site(
        "Lindkoping, Stangastaden: ",
        "https://www.stangastaden.se/loggain",
        "",
        [Account("8904041236", "C804BBa0", "Alexey Klechikov")],
        {
            "username": "{login}",
            "password": "{password}",
        },
        [],
    ),
    Site(
        "Malmo, MalmoCityFastigheter: ",
        "https://minasidor.malmocityfastigheter.se//CK/User/MyPagesLogin.aspx",
        "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col1$LoginControl1$",
        [
            Account("alexey.klechikov@gmail.com", "C804BBa0", "Alexey Klechikov"),
            Account("belan.elena89@gmail.com", "Malvina123!", "Elena Belan"),
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
        "Eda, Eda Bostad: ",
        "https://marknad-bostadsbolaget.eda.se//User/MyPagesLogin.aspx",
        "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$",
        [
            Account("198904041236", "C804BBa0", "Alexey Klechikov"),
            Account("198903057985", "Malvina123!", "Elena Belan"),
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
)
