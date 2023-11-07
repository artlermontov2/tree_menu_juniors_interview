import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tree.settings')

import django

django.setup()

from tree_menu.models import Menu, MenuItem


def load_data():
    # Удаляем существующее меню "main_menu"
    Menu.objects.filter(title="main_menu").delete()

    # Создаем меню "main_menu"
    main_menu = Menu.objects.create(title="main_menu", slug="main_menu")

    # Создаем корневой объект "Crypto"
    crypto = MenuItem.objects.create(title="Crypto", slug="crypto", menu=main_menu)

    # Создаем объекты 2-го уровня
    major = MenuItem.objects.create(title="Binance", slug="binance", menu=main_menu, parent=crypto)


    # Списки валютных пар
    major_pairs = ["BTCUSDT", "ETHUSDT", "BNBUSDT", "XRPUSDT", "ADAUSDT", "SOLUSDT", "TRXUSDT", "LINKUSDT", "MATICUSDT", "DOTUSDT"]


    # Создаем объекты 3-го уровня для основных пар
    for pair in major_pairs:
        MenuItem.objects.create(title=pair, slug=pair.lower(), parent=major, menu=main_menu)


    # Создаем объекты 4-го уровня и 5-го уровня для всех пар
    timeframes = [1, 5, 15, 30, 60]
    for pair in major_pairs:
        pair_item = MenuItem.objects.get(title=pair)

        for timeframe in timeframes:
            timeframe_item = MenuItem.objects.create(title=f"{pair}_{timeframe}", slug=f"{pair.lower()}_{timeframe}",
                                                     parent=pair_item, menu=main_menu)

            MenuItem.objects.create(title=f"{pair}_{timeframe}_ask", slug=f"{pair.lower()}_{timeframe}_ask",
                                    parent=timeframe_item, menu=main_menu)
            MenuItem.objects.create(title=f"{pair}_{timeframe}_bid", slug=f"{pair.lower()}_{timeframe}_bid",
                                    parent=timeframe_item, menu=main_menu)


if __name__ == "__main__":
    print("Loading data...")
    load_data()
    print("Binance menu successfully loaded")