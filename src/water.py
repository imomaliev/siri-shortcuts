import contextlib

from http.cookiejar import CookieJar
from urllib.parse import urlencode
from urllib.request import build_opener
from urllib.request import HTTPCookieProcessor
from urllib.request import Request


BOTTLE_19L = "1661"


def R(url, data=None, method=None):
    if data is not None:
        data = urlencode(data).encode()
    return Request(url, data=data, method=method)


cookie_jar = CookieJar()

with contextlib.closing(
    build_opener(HTTPCookieProcessor(cookie_jar))
) as opener:
    opener.open(R(
        "https://nsk.mywatershop.ru/account/login?ReturnUrl=%2F",
        data={
            "UserName": input_data['login'],  # noqa: F821
            "Password": input_data['password'],  # noqa: F821
            "IsPersistent": "false",
        },
        method="POST"
    ))
    opener.open(R(
        "https://nsk.mywatershop.ru/cart/addposition",
        data={"uid": "0", "id": BOTTLE_19L, "count": "3"},
    ))
    opener.open(R(
        "https://nsk.mywatershop.ru/order",
        data={
            "DeliveryDate": input_data['date'],  # noqa: F821
            "DeliveryStartHour": "13",
            "DeliveryEndHour": "15",
            "range": "13;15",
            "PayType": "1",
            "Email": input_data['email'],  # noqa: F821
            "PayMasterMethod": "5",
            "CardId": "",
            "Comment": "",
            "AdvanceAmountAvailable": "0,0000",
            "AdvanceAmountToUse": "0",
            "AdvanceBonusAmountAvailable": "0",
            "AdvanceBonusAmountToUse": "0",
            "movingToOrder": "0",
        }),
        timeout=10,
    )

output = input_data  # noqa: F821
