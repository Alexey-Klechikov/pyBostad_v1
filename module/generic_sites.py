from .utils import Account, ping_generic_schema


async def heimstaden() -> str:
    url = "https://mitt.heimstaden.com/mina-sidor/logga-in"
    base = "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$"
    accounts = [
        Account("8904041236", "C804BBa0", "Alexey Klechikov"),
        Account("8903057985", "Malvina123!", "Elena Belan"),
    ]
    static_fields = {
        "{base}txtUserID": "{login}",
        "{base}txtPassword": "{password}",
        "{base}btnLogin": "Logga in",
    }
    dynamic_fields = [
        "__VIEWSTATE",
        "__VIEWSTATEGENERATOR",
        "__EVENTVALIDATION",
        "ctl00$ctl01$hdnRequestVerificationToken",
    ]

    message = await ping_generic_schema(
        "Global, HeimStaden: ",
        url,
        base,
        accounts,
        static_fields,
        dynamic_fields,
    )

    return message


async def rikshem() -> str:
    url = "https://minasidor.rikshem.se/mina-sidor/logga-in/Default.aspx"
    base = "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col1$LoginControl1$"
    accounts = [
        Account("198904041236", "C804BBa0", "Alexey Klechikov"),
        Account("198903057985", "Malvina123!", "Elena Belan"),
    ]
    static_fields = {
        "{base}txtUserID": "{login}",
        "{base}txtPassword": "{password}",
        "{base}btnLogin": "Logga in",
    }
    dynamic_fields = [
        "__VIEWSTATE",
        "__VIEWSTATEGENERATOR",
        "__EVENTVALIDATION",
    ]

    message = await ping_generic_schema(
        "Global, RiksHem: ", url, base, accounts, static_fields, dynamic_fields
    )

    return message


async def bostaden_umea() -> str:
    url = "https://www.bostaden.umea.se/mina-sidor/logga-in"
    base = "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$"
    accounts = [
        Account("Alexey", "C804BBa0", "Alexey Klechikov"),
    ]
    static_fields = {
        "{base}txtUserID": "{login}",
        "{base}txtPassword": "{password}",
        "{base}btnLogin": "Logga in",
        "{base}hdnSelectedTab": "p",
    }
    dynamic_fields = [
        "__VIEWSTATE",
        "__VIEWSTATEGENERATOR",
        "__EVENTVALIDATION",
        "ctl00$ctl01$hdnRequestVerificationToken",
        "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$hdnSession",
    ]

    message = await ping_generic_schema(
        "Umea, Bostaden: ",
        url,
        base,
        accounts,
        static_fields,
        dynamic_fields,
    )

    return message


async def aranas() -> str:
    url = "https://marknad.aranas.se/User/MyPagesLogin.aspx"
    base = "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$"
    accounts = [
        Account("8904041236", "C804BBa0", "Alexey Klechikov"),
        Account("8903057985", "Malvina123!", "Elena Belan"),
    ]
    static_fields = {
        "{base}txtUserID": "{login}",
        "{base}txtPassword": "{password}",
        "{base}btnLogin": "Logga in",
    }
    dynamic_fields = [
        "__VIEWSTATE",
        "__VIEWSTATEGENERATOR",
        "__EVENTVALIDATION",
    ]

    message = await ping_generic_schema(
        "Goteborg, Aranas: ",
        url,
        base,
        accounts,
        static_fields,
        dynamic_fields,
    )

    return message


async def lkf() -> str:
    url = "https://minasidor.lkf.se/User/MyPagesLogin.aspx"
    base = "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$"
    accounts = [
        Account("8904041236", "C804BBa0", "Alexey Klechikov"),
        Account("8903057985", "Malvina123!", "Elena Belan"),
    ]
    static_fields = {
        "{base}txtUserID": "{login}",
        "{base}txtPassword": "{password}",
        "{base}btnLogin": "Logga in",
    }
    dynamic_fields = [
        "__VIEWSTATE",
        "__VIEWSTATEGENERATOR",
        "__EVENTVALIDATION",
        "ctl00$ctl01$hdnRequestVerificationToken",
    ]

    message = await ping_generic_schema(
        "Lund, lkf: ",
        url,
        base,
        accounts,
        static_fields,
        dynamic_fields,
    )

    return message


async def einar_mattsson() -> str:
    url = "https://minasidor.einarmattsson.se/User/MyPagesLogin.aspx"
    base = "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$"
    accounts = [
        Account("8904041236", "C804BBa0", "Alexey Klechikov"),
        Account("8903057985", "Malvina123!", "Elena Belan"),
    ]
    static_fields = {
        "{base}txtUserID": "{login}",
        "{base}txtPassword": "{password}",
        "{base}btnLogin": "Logga in",
    }
    dynamic_fields = [
        "__VIEWSTATE",
        "__VIEWSTATEGENERATOR",
        "__EVENTVALIDATION",
        "ctl00$ctl01$hdnRequestVerificationToken",
    ]

    message = await ping_generic_schema(
        "Stockholm, EinarMattsson: ",
        url,
        base,
        accounts,
        static_fields,
        dynamic_fields,
    )

    return message


async def forvaltaren() -> str:
    url = "https://www.forvaltaren.se/mina-sidor/logga-in"
    base = "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$"
    accounts = [
        Account("8904041236", "C804BBa0", "Alexey Klechikov"),
        Account("8903057985", "Malvina123!", "Elena Belan"),
    ]
    static_fields = {
        "{base}txtUserID": "{login}",
        "{base}txtPassword": "{password}",
        "{base}btnLogin": "Logga in",
    }
    dynamic_fields = ["__VIEWSTATE", "__VIEWSTATEGENERATOR", "__EVENTVALIDATION"]

    message = await ping_generic_schema(
        "Stockholm, Forvaltaren: ",
        url,
        base,
        accounts,
        static_fields,
        dynamic_fields,
    )

    return message


async def derome_fastighet() -> str:
    url = "https://minasidor.deromefastighet.se/Account/Login?returnUrl="
    base = "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$"
    accounts = [
        Account("8904041236", "C804BBa0", "Alexey Klechikov"),
        Account("8903057985", "Malvina123!", "Elena Belan"),
    ]
    static_fields = {
        "UserId": "{login}",
        "Password": "{password}",
        "RememberMe": "true",
    }
    dynamic_fields = ["__RequestVerificationToken"]

    message = await ping_generic_schema(
        "Global, DeromeFastighet: ",
        url,
        base,
        accounts,
        static_fields,
        dynamic_fields,
    )

    return message


async def vasby_hem() -> str:
    url = "https://www.vasbyhem.se/Account/Login"
    base = ""
    accounts = [
        Account("8904041236", "C804BBa0", "Alexey Klechikov"),
        Account("8903057985", "Malvina123!", "Elena Belan"),
    ]
    static_fields = {
        "UserID": "{login}",
        "Password": "{password}",
        "RememberMe": "true",
    }
    dynamic_fields = ["__RequestVerificationToken"]

    message = await ping_generic_schema(
        "Stockholm, HaningeBostader: ",
        url,
        base,
        accounts,
        static_fields,
        dynamic_fields,
    )

    return message


async def heba_fast() -> str:
    url = "https://www.hebafast.se/mina-sidor/logga-in"
    base = "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$"
    accounts = [
        Account("8904041236", "C804BBa0", "Alexey Klechikov"),
        Account("8903057985", "Malvina123!", "Elena Belan"),
    ]
    static_fields = {
        "{base}txtUserID": "{login}",
        "{base}txtPassword": "{password}",
        "{base}btnLogin": "Logga in",
    }
    dynamic_fields = [
        "__VIEWSTATE",
        "__VIEWSTATEGENERATOR",
        "__EVENTVALIDATION",
        "ctl00$ctl01$hdnRequestVerificationToken",
    ]

    message = await ping_generic_schema(
        "Stockholm, HebaFast: ",
        url,
        base,
        accounts,
        static_fields,
        dynamic_fields,
    )

    return message


async def hasselby_hem() -> str:
    url = "https://bostad.hasselbyhem.se/User/MyPagesLogin.aspx"
    base = "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$"
    accounts = [
        Account("8904041236", "C804BBa0", "Alexey Klechikov"),
        Account("8903057985", "Malvina123!", "Elena Belan"),
    ]
    static_fields = {
        "{base}txtUserID": "{login}",
        "{base}txtPassword": "{password}",
        "{base}btnLogin": "Logga in",
    }
    dynamic_fields = [
        "__VIEWSTATE",
        "__VIEWSTATEGENERATOR",
        "__EVENTVALIDATION",
    ]

    message = await ping_generic_schema(
        "Stockholm, HasselbyHem: ",
        url,
        base,
        accounts,
        static_fields,
        dynamic_fields,
    )

    return message


async def ekero_bostader() -> str:
    url = "https://minasidor.ekerobostader.se/mina-sidor/logga-in"
    base = "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$"
    accounts = [
        Account("8904041236", "C804BBa0", "Alexey Klechikov"),
    ]
    static_fields = {
        "{base}txtUserID": "{login}",
        "{base}txtPassword": "{password}",
        "{base}btnLogin": "Logga in",
    }
    dynamic_fields = [
        "__VIEWSTATE",
        "__VIEWSTATEGENERATOR",
        "__EVENTVALIDATION",
    ]

    message = await ping_generic_schema(
        "Stockholm, EkeroBostader: ",
        url,
        base,
        accounts,
        static_fields,
        dynamic_fields,
    )

    return message


async def haninge_bostader() -> str:
    url = "https://minasidor.haningebostader.se/"
    base = ""
    accounts = [
        Account("8904041236", "C804BBa0", "Alexey Klechikov"),
        Account("8903057985", "Malvina123!", "Elena Belan"),
    ]
    static_fields = {
        "UserId": "{login}",
        "Password": "{password}",
        "RememberMe": "true",
    }
    dynamic_fields = ["__RequestVerificationToken"]

    message = await ping_generic_schema(
        "Stockholm, HaningeBostader: ",
        url,
        base,
        accounts,
        static_fields,
        dynamic_fields,
    )

    return message


async def sollentuna_hem() -> str:
    url = "https://minasidor.sollentunahem.se/mina-sidor/logga-in"
    base = ""
    accounts = [
        Account("8904041236", "C804BBa0", "Alexey Klechikov"),
        Account("8903057985", "Malvina123!", "Elena Belan"),
    ]
    static_fields = {
        "UserId": "{login}",
        "Password": "{password}",
        "RememberMe": "true",
    }
    dynamic_fields = ["__RequestVerificationToken"]

    message = await ping_generic_schema(
        "Stockholm, SollentunaHem: ",
        url,
        base,
        accounts,
        static_fields,
        dynamic_fields,
    )

    return message


async def bjuvs_bostader() -> str:
    url = "https://bostad.bjuvsbostader.se/mina-sidor/logga-in"
    base = "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$"
    accounts = [
        Account("8904041236", "C804BBa0", "Alexey Klechikov"),
        Account("8903057985", "Malvina123!", "Elena Belan"),
    ]
    static_fields = {
        "{base}txtUserID": "{login}",
        "{base}txtPassword": "{password}",
        "{base}btnLogin": "Logga in",
    }
    dynamic_fields = ["__VIEWSTATE", "__VIEWSTATEGENERATOR", "__EVENTVALIDATION"]

    message = await ping_generic_schema(
        "Helsinborg, Bjuv: ",
        url,
        base,
        accounts,
        static_fields,
        dynamic_fields,
    )

    return message


async def stangastaden() -> str:
    url = "https://www.stangastaden.se/loggain"
    base = ""
    accounts = [Account("8904041236", "C804BBa0", "Alexey Klechikov")]
    static_fields = {
        "username": "{login}",
        "password": "{password}",
    }
    dynamic_fields: list = []

    message = await ping_generic_schema(
        "Lindkoping, Stangastaden: ",
        url,
        base,
        accounts,
        static_fields,
        dynamic_fields,
    )

    return message


async def malmocityfastigheter() -> str:
    url = "https://minasidor.malmocityfastigheter.se//CK/User/MyPagesLogin.aspx"
    base = "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col1$LoginControl1$"
    accounts = [
        Account("alexey.klechikov@gmail.com", "C804BBa0", "Alexey Klechikov"),
        Account("belan.elena89@gmail.com", "Malvina123!", "Elena Belan"),
    ]
    static_fields = {
        "{base}txtUserID": "{login}",
        "{base}txtPassword": "{password}",
        "{base}btnLogin": "Logga in",
        "{base}hdnSelectedTab": "p",
    }
    dynamic_fields = [
        "__VIEWSTATE",
        "__VIEWSTATEGENERATOR",
        "__EVENTVALIDATION",
        "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col1$LoginControl1$hdnSession",
        "ctl00$ctl01$hdnRequestVerificationToken",
    ]

    message = await ping_generic_schema(
        "Malmo, MalmoCityFastigheter: ",
        url,
        base,
        accounts,
        static_fields,
        dynamic_fields,
    )

    return message


async def eda_bostad() -> str:
    url = "https://marknad-bostadsbolaget.eda.se//User/MyPagesLogin.aspx"
    base = "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$"
    accounts = [
        Account("198904041236", "C804BBa0", "Alexey Klechikov"),
        Account("198903057985", "Malvina123!", "Elena Belan"),
    ]
    static_fields = {
        "{base}txtUserID": "{login}",
        "{base}txtPassword": "{password}",
        "{base}btnLogin": "Logga in",
        "{base}hdnSelectedTab": "p",
    }
    dynamic_fields = [
        "__VIEWSTATE",
        "__VIEWSTATEGENERATOR",
        "__EVENTVALIDATION",
        "ctl00$ctl01$DefaultSiteContentPlaceHolder1$Col2$LoginControl1$hdnSession",
        "ctl00$ctl01$hdnRequestVerificationToken",
    ]

    message = await ping_generic_schema(
        "Eda, Eda Bostad: ",
        url,
        base,
        accounts,
        static_fields,
        dynamic_fields,
    )

    return message
