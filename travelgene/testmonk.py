__author__ = 'lubron'
import monkapi


def add_sample_label():
    monkapi.init_monk()
    monkapi.init_database()



    monkapi.add_label(monkapi.get_entity_id("Seattle","Seattle_00000001"), "likeTravel", "Y")
    monkapi.add_label(monkapi.get_entity_id("Seattle","Seattle_00000002"), "likeTravel", "Y")
    monkapi.add_label(monkapi.get_entity_id("Seattle","Seattle_00000003"), "likeTravel", "Y")





