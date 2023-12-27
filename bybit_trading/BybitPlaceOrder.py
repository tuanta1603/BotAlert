from pybit.unified_trading import HTTP


def place_order(botalert):
    session = HTTP(
        testnet=True,
        api_key="TC5XE7EFtKNiJmVpyY",
        api_secret="9Ge3Ls7BvoU4IX5Tw1yEuPkS8l3S0wwunCLC",
    )
    result = session.place_order(
        category="spot",
        symbol="BTCUSDT",
        side="Buy",
        orderType="Limit",
        qty="0.1",
        price="15600",
        timeInForce="PostOnly",
        orderLinkId="spot-test-postonly",
        isLeverage=0,
        orderFilter="Order",
    )
    print("1111111111", result)
    return result
