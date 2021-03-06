import pygame

WIDTH = 480
HEIGHT = 320

# OUTPUT_WIDTH = 480
# OUTPUT_HEIGHT = 320

#MAP_FOCUS = (-88.1443375, 41.9268148)
MAP_FOCUS = (41.9611336,-87.6767838)

EVENTS = {
	'SONG_END': pygame.USEREVENT + 1
}

ACTIONS = {
	pygame.K_F1: "module_stats",
	pygame.K_F2: "module_items",
	pygame.K_F3: "module_data",
	pygame.K_1: "knob_1",
	pygame.K_2: "knob_2",
	pygame.K_3: "knob_3",
	pygame.K_4: "knob_4",
	pygame.K_5: "knob_5",
	pygame.K_UP: "dial_up",
	pygame.K_DOWN: "dial_down"
}

# Using GPIO.BCM as mode
GPIO_ACTIONS = {
  	14: "switch_mod", #GPIO 4
	4: "knob_1", #GPIO 17
	17: "knob_2", #GPIO 18
	27: "knob_3", #GPIO 7
	22: "knob_4", #GPIO 22
	23: "knob_5", #GPIO 27
}


MAP_ICONS = {
	"camp": 		pygame.image.load('images/map_icons/camp.png'),
	"factory": 		pygame.image.load('images/map_icons/factory.png'),
	"metro": 		pygame.image.load('images/map_icons/metro.png'),
	"misc": 		pygame.image.load('images/map_icons/misc.png'),
	"monument": 	pygame.image.load('images/map_icons/monument.png'),
	"vault": 		pygame.image.load('images/map_icons/vault.png'),
	"settlement": 	pygame.image.load('images/map_icons/settlement.png'),
	"ruin": 		pygame.image.load('images/map_icons/ruin.png'),
	"cave": 		pygame.image.load('images/map_icons/cave.png'),
	"landmark": 	pygame.image.load('images/map_icons/landmark.png'),
	"city": 		pygame.image.load('images/map_icons/city.png'),
	"office": 		pygame.image.load('images/map_icons/office.png'),
	"sewer": 		pygame.image.load('images/map_icons/sewer.png'),
}

AMENITIES = {
	'pub': 				MAP_ICONS['vault'],
	'nightclub': 		MAP_ICONS['vault'],
	'bar': 				MAP_ICONS['vault'],
	'fast_food': 		MAP_ICONS['sewer'],
	'cafe': 			MAP_ICONS['sewer'],
	'drinking_water': 	MAP_ICONS['sewer'],
	'restaurant': 		MAP_ICONS['settlement'],
	'cinema': 			MAP_ICONS['office'],
	'pharmacy': 		MAP_ICONS['office'],
	'school': 			MAP_ICONS['office'],
	'bank': 			MAP_ICONS['monument'],
	'townhall': 		MAP_ICONS['monument'],
	'bicycle_parking': 	MAP_ICONS['misc'],
	'place_of_worship': MAP_ICONS['misc'],
	'theatre': 			MAP_ICONS['misc'],
	'bus_station': 		MAP_ICONS['misc'],
	'parking': 			MAP_ICONS['misc'],
	'fountain': 		MAP_ICONS['misc'],
	'marketplace': 		MAP_ICONS['misc'],
	'atm': 				MAP_ICONS['misc'],
    'childcare':        MAP_ICONS['misc'],
    'doctors':        MAP_ICONS['vault'],
    'kindergarten':        MAP_ICONS['misc'],
    'animal_boarding':        MAP_ICONS['settlement'],
    'bicycle_rental':        MAP_ICONS['settlement'],
    'charging_station':        MAP_ICONS['settlement'],
    'clinic':        MAP_ICONS['misc'],
    'community_centre':        MAP_ICONS['city'],
    'dancing_school':        MAP_ICONS['misc'],
    'dentist':        MAP_ICONS['misc'],
    'doctors':        MAP_ICONS['misc'],
    'dojo':        MAP_ICONS['misc'],
    'driving_school':        MAP_ICONS['misc'],
    'fortune_teller':        MAP_ICONS['misc'],
    'gambling':        MAP_ICONS['factory'],
    'ice_cream':        MAP_ICONS['misc'],
    'kindergarten':        MAP_ICONS['misc'],
    'language_school':        MAP_ICONS['misc'],
    'library':        MAP_ICONS['city'],
    'music_school':        MAP_ICONS['misc'],
    'post_office':        MAP_ICONS['city'],
    'prep_school':        MAP_ICONS['factory'],
    'public_bookcase':        MAP_ICONS['city'],
    'social_facility':        MAP_ICONS['camp'],
    'studio':        MAP_ICONS['misc'],
    'taxi':        MAP_ICONS['camp'],
    'training':        MAP_ICONS['factory'],
    'vending_machine':        MAP_ICONS['camp'],
    'veterinary':        MAP_ICONS['misc'],
    'arts_centre':        MAP_ICONS['camp'],
    'car_rental':        MAP_ICONS['camp'],
    }

pygame.font.init()
FONTS = {}
for x in range(10, 28):
	FONTS[x] = pygame.font.Font('monofonto.ttf', x)
