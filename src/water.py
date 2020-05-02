import argparse
import contextlib
import os
import sys

from http.cookiejar import CookieJar
from typing import NoReturn
from urllib.parse import urlencode
from urllib.request import build_opener
from urllib.request import HTTPCookieProcessor
from urllib.request import Request


BOTTLE_19L = "1661"


def R(url, data=None, method=None):
    if data is not None:
        data = urlencode(data).encode()
    return Request(url, data=data, method=method)


def main(argv=None) -> NoReturn:
    parser = argparse.ArgumentParser()
    parser.add_argument("date")
    args = parser.parse_args(argv)

    cookie_jar = CookieJar()
    with contextlib.closing(
        build_opener(HTTPCookieProcessor(cookie_jar))
    ) as opener:
        opener.open(R(
            "https://nsk.mywatershop.ru/account/login?ReturnUrl=%2F",
            data={
                "UserName": os.getenv("WATER_LOGIN"),
                "Password": os.getenv("WATER_PASSWORD"),
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
                "DeliveryDate": args.date,
                "DeliveryStartHour": "13",
                "DeliveryEndHour": "15",
                "range": "13;15",
                "PayType": "1",
                "Email": os.getenv("WATER_EMAIL"),
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


if __name__ == "__main__":
    sys.exit(main())
