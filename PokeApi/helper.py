"""
"""

import datetime

from colorama import Fore

from POGOProtos.Inventory_pb2 import ItemId


def date_format(datetime):
    return datetime.strftime('%d.%m.%Y %H:%M:%S')


def print_items_awarded(logger, inventory, items_awarded):
    temp_items = {}
    for item in items_awarded:
        if str(item.item_id) not in temp_items.keys():
            temp_items[str(item.item_id)] = item.item_count
        else:
            temp_items[str(item.item_id)] += item.item_count

    for item in temp_items:      
        logger.info(Fore.CYAN + '%sx %s (Total: %s)',
                         temp_items[item],
                         ItemId.Name(int(item)),
                         inventory.get_items_count(int(item)) + temp_items[item])

def print_capture_award(logger, capture_award):
    total_xp = 0
    total_candy = 0
    total_stardust = 0

    for xp in capture_award.xp:
        total_xp += xp
    for candy in capture_award.candy:
        total_candy += candy
    for stardust in capture_award.stardust:
        total_stardust += stardust

    logger.info(Fore.CYAN + '%s xp', total_xp)
    logger.info(Fore.CYAN + '%sx candy', total_candy)
    logger.info(Fore.CYAN + '%s stardust', total_stardust)