import pygame

def get_rooms():
    rooms = [

    ]

    #room1 the hallway
    walls1 = [

        pygame.Rect(0, 0, 800, 20), #roof
        pygame.Rect(0, 580, 800, 20), #floor
        pygame.Rect(0, 0, 20, 600), #left wall
        pygame.Rect(780, 0, 20, 600), #right wall
        pygame.Rect(300, 300, 200, 20), #pillar in te middle of te screen                              

    ]
    rooms.append({
        "name": "The hallway",
        "background color" : (25, 12, 14),
        "wall_color" : (40, 52, 13),
        "atmosphere" : "this place feels familiar.",
    })

    #room2 the poolrooms
    walls2 = [
        pygame.Rect(0, 0, 800, 20),
        pygame.Rect(0, 570, 800, 20),
        pygame.Rect(0, 0, 20, 600),
        pygame.Rect(780, 0, 20, 600),
        pygame.Rect(150, 200, 150, 20),
        pygame.Rect(500, 400, 150, 20),
    ]
    rooms.append({
        "name" : "The poolrooms",
        "background_color" : (10, 20, 30),
        "wall_color" : (15, 40, 50),
        "atmosphere" : "the water feels warm",
    })

    #room3 the void
    walls3 = [
        pygame.Rect(0, 0, 800, 20),
        pygame.Rect(0, 580, 800, 20),
        pygame.Rect(0, 0, 20, 600),
        pygame.Rect(780, 0, 20, 600),
    ]
    rooms.append({
        "name" : "The void",
        "background_color" : (5, 5, 5),
        "wall_color" : (15, 15, 15),
        "atmosphere" : "only the relentless hum of my own thoughts.",
    })

    return rooms