import pygame
from sys import exit
import importlib
from Firebase import firebase
from Stick_of_War import stick_of_war

pygame.init()
pygame.font.init()


class GameLevel:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1000, 600))
        pygame.display.set_caption('Choose Level')

        self.wood_plank_surface = pygame.image.load('Plant vs Stick/Picture/utils/wood.png').convert()
        self.wood_plank_surface = pygame.transform.scale(self.wood_plank_surface, (100, 120))
        self.wood_plank_surface_back_and_store = pygame.transform.scale(self.wood_plank_surface, (90, 50))

        self.lock = pygame.image.load('War of stick/Picture/utils/lock.png')
        self.lock_surf = pygame.transform.scale(self.lock, (100, 100))

        self.one_star = pygame.image.load('War of stick/Picture/utils/one_star.png')
        self.one_star_surf = pygame.transform.scale(self.one_star, (90, 40))

        self.two_star = pygame.image.load('War of stick/Picture/utils/two_star.png')
        self.two_star_surf = pygame.transform.scale(self.two_star, (90, 40))

        self.three_star = pygame.image.load('War of stick/Picture/utils/three_star.png')
        self.three_star_surf = pygame.transform.scale(self.three_star, (90, 40))

        self.level_bg = pygame.image.load('War of stick/Picture/utils/choose level.png')

        # self.level_select_music = pygame.mixer.Sound('War of stick/Music/level.mp3')
        # self.level_select_music.set_volume(0.2)
        # self.level_select_music.play(loops=-1)

        # star rect for all level
        # level one
        self.star_one_rect = self.one_star_surf.get_rect(center=(180, 290))

        # level two
        self.star_two_rect = self.one_star_surf.get_rect(center=(335, 290))

        # level three
        self.star_three_rect = self.one_star_surf.get_rect(center=(495, 290))

        # level four
        self.star_four_rect = self.one_star_surf.get_rect(center=(650, 290))

        # level five
        self.star_five_rect = self.one_star_surf.get_rect(center=(805, 290))

        # level six
        self.star_six_rect = self.one_star_surf.get_rect(center=(180, 470))

        # level seven
        self.star_seven_rect = self.one_star_surf.get_rect(center=(335, 470))

        # level eight
        self.star_eight_rect = self.one_star_surf.get_rect(center=(495, 470))

        # level nine
        self.star_nine_rect = self.one_star_surf.get_rect(center=(650, 470))

        # level ten
<<<<<<< HEAD
        self.no_star_ten_rect = self.no_star_surf.get_rect(center=(805, 470))
        self.one_star_ten_rect = self.one_star_surf.get_rect(center=(805, 470))
        self.two_star_ten_rect = self.two_star_surf.get_rect(center=(805, 470))
        self.three_star_ten_rect = self.three_star_surf.get_rect(center=(805, 470))

<<<<<<< Updated upstream
        self.playing_lvl = [False,False,False,False,False,False,False,False,False,False]
        self.star_ten_rect = self.one_star_surf.get_rect(center=(805, 470))
=======
        # self.playing_lvl = [False,False,False,False,False,False,False,False,False,False]
        self.level_one = [(self.no_star_surf, self.no_star_one_rect)]
        self.level_two = [(self.no_star_surf, self.no_star_two_rect)]
        self.level_three = [(self.no_star_surf, self.no_star_three_rect)]
        self.level_four = [(self.no_star_surf, self.no_star_four_rect)]
        self.level_five = [(self.no_star_surf, self.no_star_five_rect)]
        self.level_six = [(self.no_star_surf, self.no_star_six_rect)]
        self.level_seven = [(self.no_star_surf, self.no_star_seven_rect)]
        self.level_eight = [(self.no_star_surf, self.no_star_eight_rect)]
        self.level_nine = [(self.no_star_surf, self.no_star_nine_rect)]
        self.level_ten = [(self.no_star_surf, self.no_star_ten_rect)]
=======
        self.star_ten_rect = self.one_star_surf.get_rect(center=(805, 470))
>>>>>>> e73e84320d2a3baf5a3f82f3d17532ab14d278ed
>>>>>>> Stashed changes

    def choose_level(self):
        self.wood_plank_rectangle_back = self.wood_plank_surface.get_rect(center=(115, 100))

        self.wood_plank_rectangle_store = self.wood_plank_surface.get_rect(center=(890, 100))

        self.wood_plank_rectangle_one = self.wood_plank_surface.get_rect(center=(180, 230))

        self.wood_plank_rectangle_two = self.wood_plank_surface.get_rect(center=(335, 230))
        self.lock_two_rect = self.lock_surf.get_rect(center=(335, 230))

        self.wood_plank_rectangle_three = self.wood_plank_surface.get_rect(center=(495, 230))
        self.lock_three_rect = self.lock_surf.get_rect(center=(495, 230))

        self.wood_plank_rectangle_four = self.wood_plank_surface.get_rect(center=(650, 230))
        self.lock_four_rect = self.lock_surf.get_rect(center=(650, 230))

        self.wood_plank_rectangle_five = self.wood_plank_surface.get_rect(center=(805, 230))
        self.lock_five_rect = self.lock_surf.get_rect(center=(805, 230))

        self.wood_plank_rectangle_six = self.wood_plank_surface.get_rect(center=(180, 410))
        self.lock_six_rect = self.lock_surf.get_rect(center=(180, 410))

        self.wood_plank_rectangle_seven = self.wood_plank_surface.get_rect(center=(335, 410))
        self.lock_seven_rect = self.lock_surf.get_rect(center=(335, 410))

        self.wood_plank_rectangle_eight = self.wood_plank_surface.get_rect(center=(495, 410))
        self.lock_eight_rect = self.lock_surf.get_rect(center=(495, 410))

        self.wood_plank_rectangle_nine = self.wood_plank_surface.get_rect(center=(650, 410))
        self.lock_nine_rect = self.lock_surf.get_rect(center=(650, 410))

        self.wood_plank_rectangle_ten = self.wood_plank_surface.get_rect(center=(805, 410))
        self.lock_ten_rect = self.lock_surf.get_rect(center=(805, 410))

        if firebase.stage_level == 1:
            self.screen.blit(self.wood_plank_surface_back_and_store, self.wood_plank_rectangle_back)
            self.screen.blit(self.wood_plank_surface_back_and_store, self.wood_plank_rectangle_store)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_one)
            self.screen.blit(self.level_bg, (0, 0))
            self.screen.blit(self.lock_surf, self.lock_two_rect)
            self.screen.blit(self.lock_surf, self.lock_three_rect)
            self.screen.blit(self.lock_surf, self.lock_four_rect)
            self.screen.blit(self.lock_surf, self.lock_five_rect)
            self.screen.blit(self.lock_surf, self.lock_six_rect)
            self.screen.blit(self.lock_surf, self.lock_seven_rect)
            self.screen.blit(self.lock_surf, self.lock_eight_rect)
            self.screen.blit(self.lock_surf, self.lock_nine_rect)
            self.screen.blit(self.lock_surf, self.lock_ten_rect)
            self.achievement()
            self.blit_star()
        elif firebase.stage_level == 2:
            self.screen.blit(self.wood_plank_surface_back_and_store, self.wood_plank_rectangle_back)
            self.screen.blit(self.wood_plank_surface_back_and_store, self.wood_plank_rectangle_store)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_one)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_two)
            self.screen.blit(self.level_bg, (0, 0))
            self.screen.blit(self.lock_surf, self.lock_three_rect)
            self.screen.blit(self.lock_surf, self.lock_four_rect)
            self.screen.blit(self.lock_surf, self.lock_five_rect)
            self.screen.blit(self.lock_surf, self.lock_six_rect)
            self.screen.blit(self.lock_surf, self.lock_seven_rect)
            self.screen.blit(self.lock_surf, self.lock_eight_rect)
            self.screen.blit(self.lock_surf, self.lock_nine_rect)
            self.screen.blit(self.lock_surf, self.lock_ten_rect)
            self.achievement()
            self.blit_star()
        elif firebase.stage_level == 3:
            self.screen.blit(self.wood_plank_surface_back_and_store, self.wood_plank_rectangle_back)
            self.screen.blit(self.wood_plank_surface_back_and_store, self.wood_plank_rectangle_store)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_one)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_two)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_three)
            self.screen.blit(self.level_bg, (0, 0))
            self.screen.blit(self.lock_surf, self.lock_four_rect)
            self.screen.blit(self.lock_surf, self.lock_five_rect)
            self.screen.blit(self.lock_surf, self.lock_six_rect)
            self.screen.blit(self.lock_surf, self.lock_seven_rect)
            self.screen.blit(self.lock_surf, self.lock_eight_rect)
            self.screen.blit(self.lock_surf, self.lock_nine_rect)
            self.screen.blit(self.lock_surf, self.lock_ten_rect)
            self.achievement()
            self.blit_star()
        elif firebase.stage_level == 4:
            self.screen.blit(self.wood_plank_surface_back_and_store, self.wood_plank_rectangle_back)
            self.screen.blit(self.wood_plank_surface_back_and_store, self.wood_plank_rectangle_store)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_one)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_two)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_three)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_four)
            self.screen.blit(self.level_bg, (0, 0))
            self.screen.blit(self.lock_surf, self.lock_five_rect)
            self.screen.blit(self.lock_surf, self.lock_six_rect)
            self.screen.blit(self.lock_surf, self.lock_seven_rect)
            self.screen.blit(self.lock_surf, self.lock_eight_rect)
            self.screen.blit(self.lock_surf, self.lock_nine_rect)
            self.screen.blit(self.lock_surf, self.lock_ten_rect)
            self.achievement()
            self.blit_star()
        elif firebase.stage_level == 5:
            self.screen.blit(self.wood_plank_surface_back_and_store, self.wood_plank_rectangle_back)
            self.screen.blit(self.wood_plank_surface_back_and_store, self.wood_plank_rectangle_store)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_one)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_two)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_three)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_four)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_five)
            self.screen.blit(self.level_bg, (0, 0))
            self.screen.blit(self.lock_surf, self.lock_six_rect)
            self.screen.blit(self.lock_surf, self.lock_seven_rect)
            self.screen.blit(self.lock_surf, self.lock_eight_rect)
            self.screen.blit(self.lock_surf, self.lock_nine_rect)
            self.screen.blit(self.lock_surf, self.lock_ten_rect)
            self.achievement()
            self.blit_star()
        elif firebase.stage_level == 6:
            self.screen.blit(self.wood_plank_surface_back_and_store, self.wood_plank_rectangle_back)
            self.screen.blit(self.wood_plank_surface_back_and_store, self.wood_plank_rectangle_store)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_one)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_two)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_three)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_four)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_five)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_six)
            self.screen.blit(self.level_bg, (0, 0))
            self.screen.blit(self.lock_surf, self.lock_seven_rect)
            self.screen.blit(self.lock_surf, self.lock_eight_rect)
            self.screen.blit(self.lock_surf, self.lock_nine_rect)
            self.screen.blit(self.lock_surf, self.lock_ten_rect)
            self.achievement()
            self.blit_star()
        elif firebase.stage_level == 7:
            self.screen.blit(self.wood_plank_surface_back_and_store, self.wood_plank_rectangle_back)
            self.screen.blit(self.wood_plank_surface_back_and_store, self.wood_plank_rectangle_store)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_one)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_two)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_three)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_four)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_five)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_six)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_seven)
            self.screen.blit(self.level_bg, (0, 0))
            self.screen.blit(self.lock_surf, self.lock_eight_rect)
            self.screen.blit(self.lock_surf, self.lock_nine_rect)
            self.screen.blit(self.lock_surf, self.lock_ten_rect)
            self.achievement()
            self.blit_star()
<<<<<<< Updated upstream

=======
>>>>>>> Stashed changes
        elif firebase.stage_level == 8:
            self.screen.blit(self.wood_plank_surface_back_and_store, self.wood_plank_rectangle_back)
            self.screen.blit(self.wood_plank_surface_back_and_store, self.wood_plank_rectangle_store)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_one)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_two)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_three)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_four)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_five)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_six)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_seven)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_eight)
            self.screen.blit(self.level_bg, (0, 0))
            self.screen.blit(self.lock_surf, self.lock_nine_rect)
            self.screen.blit(self.lock_surf, self.lock_ten_rect)
            self.achievement()
<<<<<<< Updated upstream
            self.blit_star()

=======
<<<<<<< HEAD
=======
            self.blit_star()
>>>>>>> e73e84320d2a3baf5a3f82f3d17532ab14d278ed
>>>>>>> Stashed changes
        elif firebase.stage_level == 9:
            self.screen.blit(self.wood_plank_surface_back_and_store, self.wood_plank_rectangle_back)
            self.screen.blit(self.wood_plank_surface_back_and_store, self.wood_plank_rectangle_store)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_one)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_two)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_three)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_four)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_five)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_six)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_seven)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_eight)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_nine)
            self.screen.blit(self.level_bg, (0, 0))
            self.screen.blit(self.lock_surf, self.lock_ten_rect)
            self.achievement()
<<<<<<< Updated upstream
            self.blit_star()

=======
<<<<<<< HEAD
=======
            self.blit_star()
>>>>>>> e73e84320d2a3baf5a3f82f3d17532ab14d278ed
>>>>>>> Stashed changes
        elif firebase.stage_level == 10:
            self.screen.blit(self.wood_plank_surface_back_and_store, self.wood_plank_rectangle_back)
            self.screen.blit(self.wood_plank_surface_back_and_store, self.wood_plank_rectangle_store)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_one)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_two)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_three)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_four)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_five)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_six)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_seven)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_eight)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_nine)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_ten)
            self.screen.blit(self.level_bg, (0, 0))
            self.achievement()
            self.blit_star()

    def event_handling(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.wood_plank_rectangle_store.collidepoint(pygame.mouse.get_pos()):
                    self.go_store_py()

                if self.wood_plank_rectangle_back.collidepoint(pygame.mouse.get_pos()):
                    self.go_home_py()

                if firebase.stage_level >= 1:
                    if self.wood_plank_rectangle_one.collidepoint(pygame.mouse.get_pos()):
<<<<<<< Updated upstream
                        firebase.lvl_choose = 1
                        stick_of_war.run()

                if firebase.stage_level >= 2:
                    if self.wood_plank_rectangle_two.collidepoint(pygame.mouse.get_pos()):
                        firebase.lvl_choose = 2
=======
<<<<<<< HEAD
                        stick_of_war.run()
                        self.achievement()
                        
                if firebase.stage_level >= 2:
                    if self.wood_plank_rectangle_two.collidepoint(pygame.mouse.get_pos()):
=======
                        firebase.lvl_choose = 1
>>>>>>> Stashed changes
                        stick_of_war.run()

                if firebase.stage_level >= 2:
                    if self.wood_plank_rectangle_two.collidepoint(pygame.mouse.get_pos()):
                        firebase.lvl_choose = 2
>>>>>>> e73e84320d2a3baf5a3f82f3d17532ab14d278ed
                        stick_of_war.run()
                        self.achievement()

                if firebase.stage_level >= 3:
                    if self.wood_plank_rectangle_three.collidepoint(pygame.mouse.get_pos()):
<<<<<<< Updated upstream
                        firebase.lvl_choose = 3
=======
<<<<<<< HEAD
=======
                        firebase.lvl_choose = 3
>>>>>>> e73e84320d2a3baf5a3f82f3d17532ab14d278ed
>>>>>>> Stashed changes
                        stick_of_war.run()
                        self.achievement()

                if firebase.stage_level >= 4:
                    if self.wood_plank_rectangle_four.collidepoint(pygame.mouse.get_pos()):
<<<<<<< Updated upstream
                        firebase.lvl_choose = 4
                        stick_of_war.run()

                if firebase.stage_level >= 5:
                    if self.wood_plank_rectangle_five.collidepoint(pygame.mouse.get_pos()):
                        firebase.lvl_choose = 5
=======
<<<<<<< HEAD
                        stick_of_war.run()
                        self.achievement()

                if firebase.stage_level >= 5:
                    if self.wood_plank_rectangle_five.collidepoint(pygame.mouse.get_pos()):
=======
                        firebase.lvl_choose = 4
>>>>>>> Stashed changes
                        stick_of_war.run()

                if firebase.stage_level >= 5:
                    if self.wood_plank_rectangle_five.collidepoint(pygame.mouse.get_pos()):
                        firebase.lvl_choose = 5
>>>>>>> e73e84320d2a3baf5a3f82f3d17532ab14d278ed
                        stick_of_war.run()
                        self.achievement()

                if firebase.stage_level >= 6:
                    if self.wood_plank_rectangle_six.collidepoint(pygame.mouse.get_pos()):
<<<<<<< Updated upstream
                        firebase.lvl_choose = 6
=======
<<<<<<< HEAD
=======
                        firebase.lvl_choose = 6
>>>>>>> e73e84320d2a3baf5a3f82f3d17532ab14d278ed
>>>>>>> Stashed changes
                        stick_of_war.run()
                        self.achievement()

                if firebase.stage_level >= 7:
                    if self.wood_plank_rectangle_seven.collidepoint(pygame.mouse.get_pos()):
<<<<<<< Updated upstream
                        firebase.lvl_choose = 7
=======
<<<<<<< HEAD
=======
                        firebase.lvl_choose = 7
>>>>>>> e73e84320d2a3baf5a3f82f3d17532ab14d278ed
>>>>>>> Stashed changes
                        stick_of_war.run()
                        self.achievement()

                if firebase.stage_level >= 8:
                    if self.wood_plank_rectangle_eight.collidepoint(pygame.mouse.get_pos()):
<<<<<<< Updated upstream
                        firebase.lvl_choose = 8
=======
<<<<<<< HEAD
=======
                        firebase.lvl_choose = 8
>>>>>>> e73e84320d2a3baf5a3f82f3d17532ab14d278ed
>>>>>>> Stashed changes
                        stick_of_war.run()
                        self.achievement()

                if firebase.stage_level >= 9:
                    if self.wood_plank_rectangle_nine.collidepoint(pygame.mouse.get_pos()):
<<<<<<< Updated upstream
                        firebase.lvl_choose = 9
=======
<<<<<<< HEAD
=======
                        firebase.lvl_choose = 9
>>>>>>> e73e84320d2a3baf5a3f82f3d17532ab14d278ed
>>>>>>> Stashed changes
                        stick_of_war.run()
                        self.achievement()

                if firebase.stage_level >= 10:
                    if self.wood_plank_rectangle_ten.collidepoint(pygame.mouse.get_pos()):
<<<<<<< Updated upstream
                        firebase.lvl_choose = 10
=======
<<<<<<< HEAD
=======
                        firebase.lvl_choose = 10
>>>>>>> e73e84320d2a3baf5a3f82f3d17532ab14d278ed
>>>>>>> Stashed changes
                        stick_of_war.run()
                        self.achievement()

    def go_store_py(self):
        # self.level_select_music.stop()
        store_module = importlib.import_module("Store")
        game_store = store_module.Game_Store()
        game_store.run()
        exit()

    def go_home_py(self):
        # self.level_select_music.stop()
<<<<<<< HEAD
        pygame.quit()  # Cleanup before switching
=======
>>>>>>> e73e84320d2a3baf5a3f82f3d17532ab14d278ed
        importlib.invalidate_caches()  # Clear any cached importlib entries
        home_module = importlib.import_module("Home")
        go_home = home_module.GameHome()
        go_home.run()
        exit()

    def blit_star(self):
        if firebase.stage_level >= 1:
            self.screen.blit(firebase.star_one_surf, self.star_one_rect)
        if firebase.stage_level >= 2:
            self.screen.blit(firebase.star_two_surf, self.star_two_rect)
        if firebase.stage_level >= 3:
            self.screen.blit(firebase.star_three_surf, self.star_three_rect)
        if firebase.stage_level >= 4:
            self.screen.blit(firebase.star_four_surf, self.star_four_rect)
        if firebase.stage_level >= 5:
            self.screen.blit(firebase.star_five_surf, self.star_five_rect)
        if firebase.stage_level >= 6:
            self.screen.blit(firebase.star_six_surf, self.star_six_rect)
        if firebase.stage_level >= 7:
            self.screen.blit(firebase.star_seven_surf, self.star_seven_rect)
        if firebase.stage_level >= 8:
            self.screen.blit(firebase.star_eight_surf, self.star_eight_rect)
        if firebase.stage_level >= 9:
            self.screen.blit(firebase.star_nine_surf, self.star_nine_rect)
        if firebase.stage_level >= 10:
            self.screen.blit(firebase.star_ten_surf, self.star_ten_rect)

    def achievement(self):
<<<<<<< HEAD
        stick_of_war.check_game_over()
        if stick_of_war.winner == "Enemy" or pygame.init:
            if firebase.stage_level >= 1:
                for star in self.level_one:
                    self.screen.blit(star[0], star[1])
            if firebase.stage_level >= 2:
                for star in self.level_two:
                    self.screen.blit(star[0], star[1])
            if firebase.stage_level >= 3:
                for star in self.level_three:
                    self.screen.blit(star[0], star[1])
            if firebase.stage_level >= 4:
                for star in self.level_four:
                    self.screen.blit(star[0], star[1])
            if firebase.stage_level >= 5:
                for star in self.level_five:
                    self.screen.blit(star[0], star[1])
            if firebase.stage_level >= 6:
                for star in self.level_six:
                    self.screen.blit(star[0], star[1])
            if firebase.stage_level >= 7:
                for star in self.level_seven:
                    self.screen.blit(star[0], star[1])
            if firebase.stage_level >= 8:
                for star in self.level_eight:
                    self.screen.blit(star[0], star[1])
            if firebase.stage_level >= 9:
                for star in self.level_nine:
                    self.screen.blit(star[0], star[1])
            if firebase.stage_level >= 10:
                for star in self.level_ten:
                    self.screen.blit(star[0], star[1])
            
        elif stick_of_war.winner == "User":
            if firebase.stage_level >= 1:
                self.level_one = []
                if 0 <= stick_of_war.current_time <= 120000:
                    self.level_one.append(self.three_star_surf, self.three_star_one_rect)
                    
                elif 120000 < stick_of_war.current_time <= 240000:
                    self.level_one.append(self.two_star_surf, self.two_star_one_rect)
                    
                elif stick_of_war.current_time > 240000:
                    self.level_one.append(self.one_star_surf, self.one_star_one_rect)

                self.screen.blit(self.level_one[0], self.level_one[1])

            elif firebase.stage_level >= 2:   
                self.level_two = [] 
                if 0 <= stick_of_war.current_time <= 120000:
                    self.level_two.append(self.three_star_surf, self.three_star_two_rect)
                    
                elif 120000 < stick_of_war.current_time <= 240000:
                    self.level_two.append(self.two_star_surf, self.two_star_two_rect)
                    
                elif stick_of_war.current_time > 240000:
                    self.level_two.append(self.one_star_surf, self.one_star_two_rect)
                
<<<<<<< Updated upstream
=======
                self.screen.blit(self.level_two[0], self.level_two[1])

            elif firebase.stage_level >= 3:
                self.level_three = []
                if 0 <= stick_of_war.current_time <= 120000:
                    self.level_three.append(self.three_star_surf, self.three_star_three_rect)
                    
                elif 120000 < stick_of_war.current_time <= 240000:
                    self.level_three.append(self.two_star_surf, self.two_star_three_rect)
                    
                elif stick_of_war.current_time > 240000:
                    self.level_three.append(self.one_star_surf, self.one_star_three_rect)

                self.screen.blit(self.level_three[0], self.level_three[1])

            elif firebase.stage_level >= 4:
                self.level_four = []
                if 0 <= stick_of_war.current_time <= 120000:
                    self.level_four.append(self.three_star_surf, self.three_star_four_rect)
                    
                elif 120000 < stick_of_war.current_time <= 240000:
                    self.level_four.append(self.two_star_surf, self.two_star_four_rect)
                    
                elif stick_of_war.current_time > 240000:
                    self.level_four.append(self.one_star_surf, self.one_star_four_rect)

                self.screen.blit(self.level_four[0], self.level_four[1])

            elif firebase.stage_level >= 5:
                self.level_five = []
                if 0 <= stick_of_war.current_time <= 120000:
                    self.level_five.append(self.three_star_surf, self.three_star_five_rect)
                    
                elif 120000 < stick_of_war.current_time <= 240000:
                    self.level_five.append(self.two_star_surf, self.two_star_five_rect)
                    
                elif stick_of_war.current_time > 240000:
                    self.level_five.append(self.one_star_surf, self.one_star_five_rect)

                self.screen.blit(self.level_five[0], self.level_five[1])

            elif firebase.stage_level >= 6:
                self.level_six = []
                if 0 <= stick_of_war.current_time <= 120000:
                    self.level_six.append(self.three_star_surf, self.three_star_six_rect)
                    
                elif 120000 < stick_of_war.current_time <= 240000:
                    self.level_six.append(self.two_star_surf, self.two_star_six_rect)
                    
                elif stick_of_war.current_time > 240000:
                    self.level_six.append(self.one_star_surf, self.one_star_six_rect)

                self.screen.blit(self.level_six[0], self.level_six[1])

            elif firebase.stage_level >= 7:
                self.level_seven = []
                if 0 <= stick_of_war.current_time <= 120000:
                    self.level_seven.append(self.three_star_surf, self.three_star_seven_rect)
                    
                elif 120000 < stick_of_war.current_time <= 240000:
                    self.level_seven.append(self.two_star_surf, self.two_star_seven_rect)
                    
                elif stick_of_war.current_time > 240000:
                    self.level_seven.append(self.one_star_surf, self.one_star_seven_rect)

                self.screen.blit(self.level_seven[0], self.level_seven[1])

            elif firebase.stage_level >= 8:
                self.level_eight = []
                if 0 <= stick_of_war.current_time <= 120000:
                    self.level_eight.append(self.three_star_surf, self.three_star_eight_rect)
                    
                elif 120000 < stick_of_war.current_time <= 240000:
                    self.level_eight.append(self.two_star_surf, self.two_star_eight_rect)
                    
                elif stick_of_war.current_time > 240000:
                    self.level_eight.append(self.one_star_surf, self.one_star_eight_rect)

                self.screen.blit(self.level_eight[0], self.level_eight[1])

            elif firebase.stage_level >= 9:
                self.level_nine = []
                if 0 <= stick_of_war.current_time <= 120000:
                    self.level_nine.append(self.three_star_surf, self.three_star_nine_rect)
                    
                elif 120000 < stick_of_war.current_time <= 240000:
                    self.level_nine.append(self.two_star_surf, self.two_star_nine_rect)
                    
                elif stick_of_war.current_time > 240000:
                    self.level_nine.append(self.one_star_surf, self.one_star_nine_rect)

                self.screen.blit(self.level_nine[0], self.level_nine[1])

            elif firebase.stage_level >= 10:
                self.level_ten = []
                if 0 <= stick_of_war.current_time <= 120000:
                    self.level_ten.append(self.three_star_surf, self.three_star_ten_rect)
                    
                elif 120000 < stick_of_war.current_time <= 240000:
                    self.level_ten.append(self.two_star_surf, self.two_star_ten_rect)
                    
                elif stick_of_war.current_time > 240000:
                    self.level_ten.append(self.one_star_surf, self.one_star_ten_rect)

                self.screen.blit(self.level_ten[0], self.level_ten[1])
                
=======
>>>>>>> Stashed changes
        if stick_of_war.winner == "User":
            if firebase.lvl_choose == 1:
                if 0 <= stick_of_war.current_time <= 120000:
                    firebase.star_one_surf = self.three_star_surf

                elif 120000 < stick_of_war.current_time <= 240000:
                    firebase.star_one_surf = self.two_star_surf

                elif stick_of_war.current_time > 240000:
                    firebase.star_one_surf = self.one_star_surf

                firebase.lvl_choose = None

            if firebase.lvl_choose == 2:
                if 0 <= stick_of_war.current_time <= 120000:
                    firebase.star_two_surf = self.three_star_surf

                elif 120000 < stick_of_war.current_time <= 240000:
                    firebase.star_two_surf = self.two_star_surf

                elif stick_of_war.current_time > 240000:
                    firebase.star_two_surf = self.one_star_surf

                firebase.lvl_choose = None

            if firebase.lvl_choose == 3:
                if 0 <= stick_of_war.current_time <= 120000:
                    firebase.star_three_surf = self.three_star_surf

                elif 120000 < stick_of_war.current_time <= 240000:
                    firebase.star_three_surf = self.two_star_surf

                elif stick_of_war.current_time > 240000:
                    firebase.star_three_surf = self.one_star_surf

                firebase.lvl_choose = None

            if firebase.lvl_choose == 4:
                if 0 <= stick_of_war.current_time <= 120000:
                    firebase.star_four_surf = self.three_star_surf

                elif 120000 < stick_of_war.current_time <= 240000:
                    firebase.star_four_surf = self.two_star_surf

                elif stick_of_war.current_time > 240000:
                    firebase.star_four_surf = self.one_star_surf

                firebase.lvl_choose = None

            if firebase.lvl_choose == 5:
                if 0 <= stick_of_war.current_time <= 120000:
                    firebase.star_five_surf = self.three_star_surf

                elif 120000 < stick_of_war.current_time <= 240000:
                    firebase.star_five_surf = self.two_star_surf

                elif stick_of_war.current_time > 240000:
                    firebase.star_five_surf = self.one_star_surf

                firebase.lvl_choose = None

            if firebase.lvl_choose == 6:
                if 0 <= stick_of_war.current_time <= 120000:
                    firebase.star_six_surf = self.three_star_surf

                elif 120000 < stick_of_war.current_time <= 240000:
                    firebase.star_six_surf = self.two_star_surf

                elif stick_of_war.current_time >= 240000:
                    firebase.star_six_surf = self.one_star_surf

                firebase.lvl_choose = None

            if firebase.lvl_choose == 7:
                if 0 <= stick_of_war.current_time <= 120000:
                    firebase.star_seven_surf = self.three_star_surf

                elif 120000 < stick_of_war.current_time <= 240000:
                    firebase.star_seven_surf = self.two_star_surf

                elif stick_of_war.current_time >= 240000:
                    firebase.star_seven_surf = self.one_star_surf

                firebase.lvl_choose = None

            if firebase.lvl_choose == 8:
                if 0 <= stick_of_war.current_time <= 120000:
                    firebase.star_eight_surf = self.three_star_surf

                elif 120000 < stick_of_war.current_time <= 240000:
                    firebase.star_eight_surf = self.two_star_surf

                elif stick_of_war.current_time >= 240000:
                    firebase.star_eight_surf = self.one_star_surf

                firebase.lvl_choose = None

            if firebase.lvl_choose == 9:
                if 0 <= stick_of_war.current_time <= 120000:
                    firebase.star_nine_surf = self.three_star_surf

                elif 120000 < stick_of_war.current_time <= 240000:
                    firebase.star_nine_surf = self.two_star_surf

                elif stick_of_war.current_time > 240000:
                    firebase.star_nine_surf = self.one_star_surf

                firebase.lvl_choose = None

            if firebase.lvl_choose == 10:
                if 0 <= stick_of_war.current_time <= 120000:
                    firebase.star_ten_surf = self.three_star_surf

                elif 120000 < stick_of_war.current_time <= 240000:
                    firebase.star_ten_surf = self.two_star_surf

                elif stick_of_war.current_time > 240000:
                    firebase.star_ten_surf = self.one_star_surf

                firebase.lvl_choose = None

            stick_of_war.winner = None

<<<<<<< Updated upstream
=======
>>>>>>> e73e84320d2a3baf5a3f82f3d17532ab14d278ed
>>>>>>> Stashed changes
    def run(self):
        while True:
            self.screen.fill((255, 255, 255))

            self.event_handling()

            self.choose_level()

            pygame.display.update()
            self.clock.tick(60)


if __name__ == '__main__':
    GameLevel().run()

<<<<<<< HEAD
level = GameLevel()

<<<<<<< Updated upstream
=======
=======
>>>>>>> e73e84320d2a3baf5a3f82f3d17532ab14d278ed
# import pygame
# from sys import exit
# import importlib
# from Firebase import firebase
# from Stick_of_War import stick_of_war
>>>>>>> Stashed changes


<<<<<<< Updated upstream
=======

# class GameLevel:
#     def __init__(self):
#         pygame.init()
#         pygame.font.init()
#         self.clock = pygame.time.Clock()
#         self.screen = pygame.display.set_mode((1000, 600))
#         pygame.display.set_caption('Choose Level')
<<<<<<< HEAD
        
=======

>>>>>>> e73e84320d2a3baf5a3f82f3d17532ab14d278ed
#         self.wood_plank_surface = pygame.image.load('Plant vs Stick/Picture/utils/wood.png').convert()
#         self.wood_plank_surface = pygame.transform.scale(self.wood_plank_surface, (100, 120))
#         self.wood_plank_surface_back_and_store = pygame.transform.scale(self.wood_plank_surface, (90,50))

#         self.lock = pygame.image.load('War of stick/Picture/utils/lock.png')
#         self.lock_surf = pygame.transform.scale(self.lock, ( 100, 100))

#         self.no_star = pygame.image.load('War of stick/Picture/utils/no_star.png')
#         self.no_star_surf = pygame.transform.scale(self.no_star, (90, 40))

#         self.one_star = pygame.image.load('War of stick/Picture/utils/one_star.png')
#         self.one_star_surf = pygame.transform.scale(self.one_star, (90, 40))

#         self.two_star = pygame.image.load('War of stick/Picture/utils/two_star.png')
#         self.two_star_surf = pygame.transform.scale(self.two_star, (90, 40))

#         self.three_star = pygame.image.load('War of stick/Picture/utils/three_star.png')
#         self.three_star_surf = pygame.transform.scale(self.three_star, (90, 40))

#         self.level_bg = pygame.image.load('War of stick/Picture/utils/choose level.png')

#         # self.level_select_music = pygame.mixer.Sound('War of stick/Music/level.mp3')
#         # self.level_select_music.set_volume(0.2)
#         # self.level_select_music.play(loops=-1)

#         # star rect for all level
#         # level one
#         self.no_star_one_rect = self.no_star_surf.get_rect(center=(180, 290))
#         self.one_star_one_rect = self.one_star_surf.get_rect(center=(180, 290))
#         self.two_star_one_rect = self.two_star_surf.get_rect(center=(180, 290)) #470
#         self.three_star_one_rect = self.three_star_surf.get_rect(center=(180, 290))

#         # level two
#         self.no_star_two_rect = self.no_star_surf.get_rect(center=(335, 290))
#         self.one_star_two_rect = self.one_star_surf.get_rect(center=(335, 290))
#         self.two_star_two_rect = self.two_star_surf.get_rect(center=(335, 290))
#         self.three_star_two_rect = self.three_star_surf.get_rect(center=(335, 290))

#         # level three
#         self.no_star_three_rect = self.no_star_surf.get_rect(center=(495, 290))
#         self.one_star_three_rect = self.one_star_surf.get_rect(center=(495, 290))
#         self.two_star_three_rect = self.two_star_surf.get_rect(center=(495, 290))
#         self.three_star_three_rect = self.three_star_surf.get_rect(center=(495, 290))

#         # level four
#         self.no_star_four_rect = self.no_star_surf.get_rect(center=(650, 290))
#         self.one_star_four_rect = self.one_star_surf.get_rect(center=(650, 290))
#         self.two_star_four_rect = self.two_star_surf.get_rect(center=(650, 290))
#         self.three_star_four_rect = self.three_star_surf.get_rect(center=(650, 290))

#         # level five
#         self.no_star_five_rect = self.no_star_surf.get_rect(center=(805, 290))
#         self.one_star_five_rect = self.one_star_surf.get_rect(center=(805, 290))
#         self.two_star_five_rect = self.two_star_surf.get_rect(center=(805, 290))
#         self.three_star_five_rect = self.three_star_surf.get_rect(center=(805, 290))

#         # level six
#         self.no_star_six_rect = self.no_star_surf.get_rect(center=(180, 470))
#         self.one_star_six_rect = self.one_star_surf.get_rect(center=(180, 470))
#         self.two_star_six_rect = self.two_star_surf.get_rect(center=(180, 470))
#         self.three_star_six_rect = self.three_star_surf.get_rect(center=(180, 470))

#         # level seven
#         self.no_star_seven_rect = self.no_star_surf.get_rect(center=(335, 470))
#         self.one_star_seven_rect = self.one_star_surf.get_rect(center=(335, 470))
#         self.two_star_seven_rect = self.two_star_surf.get_rect(center=(335, 470))
#         self.three_star_seven_rect = self.three_star_surf.get_rect(center=(335, 470))

#         # level eight
#         self.no_star_eight_rect = self.no_star_surf.get_rect(center=(495, 470))
#         self.one_star_eight_rect = self.one_star_surf.get_rect(center=(495, 470))
#         self.two_star_eight_rect = self.two_star_surf.get_rect(center=(495, 470))
#         self.three_star_eight_rect = self.three_star_surf.get_rect(center=(495, 470))

#         # level nine
#         self.no_star_nine_rect = self.no_star_surf.get_rect(center=(650, 470))
#         self.one_star_nine_rect = self.one_star_surf.get_rect(center=(650, 470))
#         self.two_star_nine_rect = self.two_star_surf.get_rect(center=(650, 470))
#         self.three_star_nine_rect = self.three_star_surf.get_rect(center=(650, 470))

#         # level ten
#         self.no_star_ten_rect = self.no_star_surf.get_rect(center=(805, 470))
#         self.one_star_ten_rect = self.one_star_surf.get_rect(center=(805, 470))
#         self.two_star_ten_rect = self.two_star_surf.get_rect(center=(805, 470))
#         self.three_star_ten_rect = self.three_star_surf.get_rect(center=(805, 470))

#         # self.playing_lvl = [False,False,False,False,False,False,False,False,False,False]

#     def choose_level(self):
#         self.wood_plank_rectangle_back = self.wood_plank_surface.get_rect(center=(115, 100))

#         self.wood_plank_rectangle_store = self.wood_plank_surface.get_rect(center=(890, 100))

#         self.wood_plank_rectangle_one = self.wood_plank_surface.get_rect(center=(180, 230))
<<<<<<< HEAD
        
=======

>>>>>>> e73e84320d2a3baf5a3f82f3d17532ab14d278ed
#         self.wood_plank_rectangle_two = self.wood_plank_surface.get_rect(center=(335, 230))
#         self.lock_two_rect = self.lock_surf.get_rect(center=(335, 230))

#         self.wood_plank_rectangle_three = self.wood_plank_surface.get_rect(center=(495, 230))
#         self.lock_three_rect = self.lock_surf.get_rect(center=(495, 230))
<<<<<<< HEAD
        
#         self.wood_plank_rectangle_four = self.wood_plank_surface.get_rect(center=(650, 230))
#         self.lock_four_rect = self.lock_surf.get_rect(center=(650, 230))
        
#         self.wood_plank_rectangle_five = self.wood_plank_surface.get_rect(center=(805, 230))
#         self.lock_five_rect = self.lock_surf.get_rect(center=(805, 230))
        
#         self.wood_plank_rectangle_six = self.wood_plank_surface.get_rect(center=(180, 410))
#         self.lock_six_rect = self.lock_surf.get_rect(center=(180, 410))
        
#         self.wood_plank_rectangle_seven = self.wood_plank_surface.get_rect(center=(335, 410))
#         self.lock_seven_rect = self.lock_surf.get_rect(center=(335, 410))
        
=======

#         self.wood_plank_rectangle_four = self.wood_plank_surface.get_rect(center=(650, 230))
#         self.lock_four_rect = self.lock_surf.get_rect(center=(650, 230))

#         self.wood_plank_rectangle_five = self.wood_plank_surface.get_rect(center=(805, 230))
#         self.lock_five_rect = self.lock_surf.get_rect(center=(805, 230))

#         self.wood_plank_rectangle_six = self.wood_plank_surface.get_rect(center=(180, 410))
#         self.lock_six_rect = self.lock_surf.get_rect(center=(180, 410))

#         self.wood_plank_rectangle_seven = self.wood_plank_surface.get_rect(center=(335, 410))
#         self.lock_seven_rect = self.lock_surf.get_rect(center=(335, 410))

>>>>>>> e73e84320d2a3baf5a3f82f3d17532ab14d278ed
#         self.wood_plank_rectangle_eight = self.wood_plank_surface.get_rect(center=(495, 410))
#         self.lock_eight_rect = self.lock_surf.get_rect(center=(495, 410))

#         self.wood_plank_rectangle_nine = self.wood_plank_surface.get_rect(center=(650, 410))
#         self.lock_nine_rect = self.lock_surf.get_rect(center=(650, 410))

#         self.wood_plank_rectangle_ten = self.wood_plank_surface.get_rect(center=(805, 410))
#         self.lock_ten_rect = self.lock_surf.get_rect(center=(805, 410))

#         if firebase.stage_level == 1:
#             self.screen.blit(self.wood_plank_surface_back_and_store, self.wood_plank_rectangle_back)
#             self.screen.blit(self.wood_plank_surface_back_and_store, self.wood_plank_rectangle_store)
#             self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_one)
#             self.screen.blit(self.level_bg, (0, 0))
#             self.screen.blit(self.lock_surf, self.lock_two_rect)
#             self.screen.blit(self.lock_surf, self.lock_three_rect)
#             self.screen.blit(self.lock_surf, self.lock_four_rect)
#             self.screen.blit(self.lock_surf, self.lock_five_rect)
#             self.screen.blit(self.lock_surf, self.lock_six_rect)
#             self.screen.blit(self.lock_surf, self.lock_seven_rect)
#             self.screen.blit(self.lock_surf, self.lock_eight_rect)
#             self.screen.blit(self.lock_surf, self.lock_nine_rect)
#             self.screen.blit(self.lock_surf, self.lock_ten_rect)
#             self.achievement()
#         elif firebase.stage_level == 2:
#             self.screen.blit(self.wood_plank_surface_back_and_store, self.wood_plank_rectangle_back)
#             self.screen.blit(self.wood_plank_surface_back_and_store, self.wood_plank_rectangle_store)
#             self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_one)
#             self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_two)
#             self.screen.blit(self.level_bg, (0, 0))
#             self.screen.blit(self.lock_surf, self.lock_three_rect)
#             self.screen.blit(self.lock_surf, self.lock_four_rect)
#             self.screen.blit(self.lock_surf, self.lock_five_rect)
#             self.screen.blit(self.lock_surf, self.lock_six_rect)
#             self.screen.blit(self.lock_surf, self.lock_seven_rect)
#             self.screen.blit(self.lock_surf, self.lock_eight_rect)
#             self.screen.blit(self.lock_surf, self.lock_nine_rect)
#             self.screen.blit(self.lock_surf, self.lock_ten_rect)
#             self.achievement()
#         elif firebase.stage_level == 3:
#             self.screen.blit(self.wood_plank_surface_back_and_store, self.wood_plank_rectangle_back)
#             self.screen.blit(self.wood_plank_surface_back_and_store, self.wood_plank_rectangle_store)
#             self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_one)
#             self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_two)
#             self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_three)
#             self.screen.blit(self.level_bg, (0, 0))
#             self.screen.blit(self.lock_surf, self.lock_four_rect)
#             self.screen.blit(self.lock_surf, self.lock_five_rect)
#             self.screen.blit(self.lock_surf, self.lock_six_rect)
#             self.screen.blit(self.lock_surf, self.lock_seven_rect)
#             self.screen.blit(self.lock_surf, self.lock_eight_rect)
#             self.screen.blit(self.lock_surf, self.lock_nine_rect)
#             self.screen.blit(self.lock_surf, self.lock_ten_rect)
#             self.achievement()
#         elif firebase.stage_level == 4:
#             self.screen.blit(self.wood_plank_surface_back_and_store, self.wood_plank_rectangle_back)
#             self.screen.blit(self.wood_plank_surface_back_and_store, self.wood_plank_rectangle_store)
#             self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_one)
#             self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_two)
#             self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_three)
#             self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_four)
#             self.screen.blit(self.level_bg, (0, 0))
#             self.screen.blit(self.lock_surf, self.lock_five_rect)
#             self.screen.blit(self.lock_surf, self.lock_six_rect)
#             self.screen.blit(self.lock_surf, self.lock_seven_rect)
#             self.screen.blit(self.lock_surf, self.lock_eight_rect)
#             self.screen.blit(self.lock_surf, self.lock_nine_rect)
#             self.screen.blit(self.lock_surf, self.lock_ten_rect)
#             self.achievement()
#         elif firebase.stage_level == 5:
#             self.screen.blit(self.wood_plank_surface_back_and_store, self.wood_plank_rectangle_back)
#             self.screen.blit(self.wood_plank_surface_back_and_store, self.wood_plank_rectangle_store)
#             self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_one)
#             self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_two)
#             self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_three)
#             self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_four)
#             self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_five)
#             self.screen.blit(self.level_bg, (0, 0))
#             self.screen.blit(self.lock_surf, self.lock_six_rect)
#             self.screen.blit(self.lock_surf, self.lock_seven_rect)
#             self.screen.blit(self.lock_surf, self.lock_eight_rect)
#             self.screen.blit(self.lock_surf, self.lock_nine_rect)
#             self.screen.blit(self.lock_surf, self.lock_ten_rect)
#             self.achievement()
#         elif firebase.stage_level == 6:
#             self.screen.blit(self.wood_plank_surface_back_and_store, self.wood_plank_rectangle_back)
#             self.screen.blit(self.wood_plank_surface_back_and_store, self.wood_plank_rectangle_store)
#             self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_one)
#             self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_two)
#             self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_three)
#             self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_four)
#             self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_five)
#             self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_six)
#             self.screen.blit(self.level_bg, (0, 0))
#             self.screen.blit(self.lock_surf, self.lock_seven_rect)
#             self.screen.blit(self.lock_surf, self.lock_eight_rect)
#             self.screen.blit(self.lock_surf, self.lock_nine_rect)
#             self.screen.blit(self.lock_surf, self.lock_ten_rect)
#             self.achievement()
#         elif firebase.stage_level == 7:
#             self.screen.blit(self.wood_plank_surface_back_and_store, self.wood_plank_rectangle_back)
#             self.screen.blit(self.wood_plank_surface_back_and_store, self.wood_plank_rectangle_store)
#             self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_one)
#             self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_two)
#             self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_three)
#             self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_four)
#             self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_five)
#             self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_six)
#             self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_seven)
#             self.screen.blit(self.level_bg, (0, 0))
#             self.screen.blit(self.lock_surf, self.lock_eight_rect)
#             self.screen.blit(self.lock_surf, self.lock_nine_rect)
#             self.screen.blit(self.lock_surf, self.lock_ten_rect)
#             self.achievement()
#         elif firebase.stage_level == 8:
#             self.screen.blit(self.wood_plank_surface_back_and_store, self.wood_plank_rectangle_back)
#             self.screen.blit(self.wood_plank_surface_back_and_store, self.wood_plank_rectangle_store)
#             self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_one)
#             self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_two)
#             self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_three)
#             self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_four)
#             self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_five)
#             self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_six)
#             self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_seven)
#             self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_eight)
#             self.screen.blit(self.level_bg, (0, 0))
#             self.screen.blit(self.lock_surf, self.lock_nine_rect)
#             self.screen.blit(self.lock_surf, self.lock_ten_rect)
#             self.achievement()
#         elif firebase.stage_level == 9:
#             self.screen.blit(self.wood_plank_surface_back_and_store, self.wood_plank_rectangle_back)
#             self.screen.blit(self.wood_plank_surface_back_and_store, self.wood_plank_rectangle_store)
#             self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_one)
#             self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_two)
#             self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_three)
#             self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_four)
#             self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_five)
#             self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_six)
#             self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_seven)
#             self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_eight)
#             self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_nine)
#             self.screen.blit(self.level_bg, (0, 0))
#             self.screen.blit(self.lock_surf, self.lock_ten_rect)
#             self.achievement()
#         elif firebase.stage_level == 10:
#             self.screen.blit(self.wood_plank_surface_back_and_store, self.wood_plank_rectangle_back)
#             self.screen.blit(self.wood_plank_surface_back_and_store, self.wood_plank_rectangle_store)
#             self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_one)
#             self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_two)
#             self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_three)
#             self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_four)
#             self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_five)
#             self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_six)
#             self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_seven)
#             self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_eight)
#             self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_nine)
#             self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_ten)
#             self.screen.blit(self.level_bg, (0, 0))
#             self.achievement()

#     def event_handling(self):
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 exit()
#             elif event.type == pygame.MOUSEBUTTONDOWN:
#                 if self.wood_plank_rectangle_store.collidepoint(pygame.mouse.get_pos()):
#                     self.go_store_py()

#                 if self.wood_plank_rectangle_back.collidepoint(pygame.mouse.get_pos()):
#                     self.go_home_py()

#                 if firebase.stage_level >= 1:
#                     if self.wood_plank_rectangle_one.collidepoint(pygame.mouse.get_pos()):
#                         # self.playing_lvl = [False,False,False,False,False,False,False,False,False,False]
#                         # self.playing_lvl[0] = True
#                         stick_of_war.run()
<<<<<<< HEAD
                        
                    
=======


>>>>>>> e73e84320d2a3baf5a3f82f3d17532ab14d278ed
#                 if firebase.stage_level >= 2:
#                     if self.wood_plank_rectangle_two.collidepoint(pygame.mouse.get_pos()):
#                         # self.playing_lvl = [False,False,False,False,False,False,False,False,False,False]
#                         # self.playing_lvl[1] = True
#                         stick_of_war.run()


#                 if firebase.stage_level >= 3:
#                     if self.wood_plank_rectangle_three.collidepoint(pygame.mouse.get_pos()):
#                         # self.playing_lvl = [False,False,False,False,False,False,False,False,False,False]
#                         # self.playing_lvl[2] = True
#                         stick_of_war.run()

#                 if firebase.stage_level >= 4:
#                     if self.wood_plank_rectangle_four.collidepoint(pygame.mouse.get_pos()):
#                         # self.playing_lvl = [False,False,False,False,False,False,False,False,False,False]
#                         # self.playing_lvl[3] = True
<<<<<<< HEAD
#                         stick_of_war.run()                    
=======
#                         stick_of_war.run()
>>>>>>> e73e84320d2a3baf5a3f82f3d17532ab14d278ed

#                 if firebase.stage_level >= 5:
#                     if self.wood_plank_rectangle_five.collidepoint(pygame.mouse.get_pos()):
#                         # self.playing_lvl = [False,False,False,False,False,False,False,False,False,False]
#                         # self.playing_lvl[4] = True
#                         stick_of_war.run()

#                 if firebase.stage_level >= 6:
#                     if self.wood_plank_rectangle_six.collidepoint(pygame.mouse.get_pos()):
#                         # self.playing_lvl = [False,False,False,False,False,False,False,False,False,False]
#                         # self.playing_lvl[5] = True
#                         stick_of_war.run()

#                 if firebase.stage_level >= 7:
#                     if self.wood_plank_rectangle_seven.collidepoint(pygame.mouse.get_pos()):
#                         # self.playing_lvl = [False,False,False,False,False,False,False,False,False,False]
#                         # self.playing_lvl[6] = True
#                         stick_of_war.run()

#                 if firebase.stage_level >= 8:
#                     if self.wood_plank_rectangle_eight.collidepoint(pygame.mouse.get_pos()):
#                         # self.playing_lvl = [False,False,False,False,False,False,False,False,False,False]
#                         # self.playing_lvl[7] = True
#                         stick_of_war.run()

#                 if firebase.stage_level >= 9:
#                     if self.wood_plank_rectangle_nine.collidepoint(pygame.mouse.get_pos()):
#                         # self.playing_lvl = [False,False,False,False,False,False,False,False,False,False]
#                         # self.playing_lvl[8] = True
#                         stick_of_war.run()

<<<<<<< HEAD
#                 if firebase.stage_level >= 10:     
=======
#                 if firebase.stage_level >= 10:
>>>>>>> e73e84320d2a3baf5a3f82f3d17532ab14d278ed
#                     if self.wood_plank_rectangle_ten.collidepoint(pygame.mouse.get_pos()):
#                         # self.playing_lvl = [False,False,False,False,False,False,False,False,False,False]
#                         # self.playing_lvl[9] = True
#                         stick_of_war.run()

#     def go_store_py(self):
#         # self.level_select_music.stop()
#         store_module = importlib.import_module("Store")
#         game_store = store_module.Game_Store()
#         game_store.run()
#         exit()

#     def go_home_py(self):
#         # self.level_select_music.stop()
#         pygame.quit()  # Cleanup before switching
#         importlib.invalidate_caches()  # Clear any cached importlib entries
#         home_module = importlib.import_module("Home")
#         go_home = home_module.GameHome()
#         go_home.run()
#         exit()

#     def achievement(self):
#         stick_of_war.check_game_over()
#         if stick_of_war.winner == "Enemy" or pygame.init:
#             if firebase.stage_level >= 1:
#                 self.screen.blit(self.no_star_surf, self.no_star_one_rect)
#             if firebase.stage_level >= 2:
#                 self.screen.blit(self.no_star_surf, self.no_star_two_rect)
#             if firebase.stage_level >= 3:
#                 self.screen.blit(self.no_star_surf, self.no_star_three_rect)
#             if firebase.stage_level >= 4:
#                 self.screen.blit(self.no_star_surf, self.no_star_four_rect)
#             if firebase.stage_level >= 5:
#                 self.screen.blit(self.no_star_surf, self.no_star_five_rect)
#             if firebase.stage_level >= 6:
#                 self.screen.blit(self.no_star_surf, self.no_star_six_rect)
#             if firebase.stage_level >= 7:
#                 self.screen.blit(self.no_star_surf, self.no_star_seven_rect)
#             if firebase.stage_level >= 8:
#                 self.screen.blit(self.no_star_surf, self.no_star_eight_rect)
#             if firebase.stage_level >= 9:
#                 self.screen.blit(self.no_star_surf, self.no_star_nine_rect)
#             if firebase.stage_level >= 10:
#                 self.screen.blit(self.no_star_surf, self.no_star_ten_rect)
<<<<<<< HEAD
            
=======

>>>>>>> e73e84320d2a3baf5a3f82f3d17532ab14d278ed
#         if stick_of_war.winner == "User":
#             if firebase.stage_level == 1:
#                 if 0 <= stick_of_war.time_string <= 120000:
#                     self.screen.blit(self.three_star_surf, self.three_star_one_rect)
<<<<<<< HEAD
                    
#                 elif 120000 < stick_of_war.time_string <= 240000:
#                     self.screen.blit(self.two_star_surf, self.two_star_one_rect)
                    
=======

#                 elif 120000 < stick_of_war.time_string <= 240000:
#                     self.screen.blit(self.two_star_surf, self.two_star_one_rect)

>>>>>>> e73e84320d2a3baf5a3f82f3d17532ab14d278ed
#                 elif stick_of_war.time_string > 240000:
#                     self.screen.blit(self.one_star_surf, self.one_star_one_rect)

#                 # self.playing_lvl[0] = False
<<<<<<< HEAD
                    
#             if firebase.stage_level == 2:                   
#                 if 0 <= stick_of_war.time_string <= 120000:
#                     self.screen.blit(self.three_star_surf, self.three_star_two_rect)
                    
=======

#             if firebase.stage_level == 2:                   
#                 if 0 <= stick_of_war.time_string <= 120000:
#                     self.screen.blit(self.three_star_surf, self.three_star_two_rect)

>>>>>>> e73e84320d2a3baf5a3f82f3d17532ab14d278ed
#                 elif 120000 < stick_of_war.time_string <= 240000:
#                     self.screen.blit(self.two_star_surf, self.two_star_two_rect)

#                 elif stick_of_war.time_string > 240000:
#                     self.screen.blit(self.one_star_surf, self.one_star_two_rect)

#                 # self.playing_lvl[1] = False

#             if firebase.stage_level == 3:
#                 if 0 <= stick_of_war.current_time <= 120000:
#                     self.screen.blit(self.three_star_surf, self.three_star_three_rect)

#                 elif 120000 < stick_of_war.current_time <= 240000:
#                     self.screen.blit(self.two_star_surf, self.two_star_three_rect)

#                 elif stick_of_war.current_time > 240000:
#                     self.screen.blit(self.one_star_surf, self.one_star_three_rect)

#                 # self.playing_lvl[2] = False

#             if firebase.stage_level == 4:
#                 if 0 <= stick_of_war.current_time <= 120000:
#                     self.screen.blit(self.three_star_surf, self.three_star_four_rect)

#                 elif 120000 < stick_of_war.current_time <= 240000:
#                     self.screen.blit(self.two_star_surf, self.two_star_four_rect)

#                 elif stick_of_war.current_time > 240000:
#                     self.screen.blit(self.one_star_surf, self.one_star_four_rect)

#                 # self.playing_lvl[3] = False

#             if firebase.stage_level == 5:
#                 if 0 <= stick_of_war.current_time <= 120000:
#                     self.screen.blit(self.three_star_surf, self.three_star_five_rect)

#                 elif 120000 < stick_of_war.current_time <= 240000:
#                     self.screen.blit(self.two_star_surf, self.two_star_five_rect)

#                 elif stick_of_war.current_time > 240000:
#                     self.screen.blit(self.one_star_surf, self.one_star_five_rect)

#                 # self.playing_lvl[4] = False

#             if firebase.stage_level == 6:
#                 if 0 <= stick_of_war.current_time <= 120000:
#                     self.screen.blit(self.three_star_surf, self.three_star_six_rect)

#                 elif 120000 < stick_of_war.current_time <= 240000:
#                     self.screen.blit(self.two_star_surf, self.two_star_six_rect)

#                 elif stick_of_war.current_time >= 240000:
#                     self.screen.blit(self.one_star_surf, self.one_star_six_rect)

#                 # self.playing_lvl[5] = False

#             if firebase.stage_level == 7:
#                 if 0 <= stick_of_war.current_time <= 120000:
#                     self.screen.blit(self.three_star_surf, self.three_star_seven_rect)

#                 elif 120000 < stick_of_war.current_time <= 240000:
#                     self.screen.blit(self.two_star_surf, self.two_star_seven_rect)

#                 elif stick_of_war.current_time >= 240000:
#                     self.screen.blit(self.one_star_surf, self.one_star_seven_rect)

#                 # self.playing_lvl[6] = False

#             if firebase.stage_level == 8:
#                 if 0 <= stick_of_war.current_time <= 120000:
#                     self.screen.blit(self.three_star_surf, self.three_star_eight_rect)

#                 elif 120000 < stick_of_war.current_time <= 240000:
#                     self.screen.blit(self.two_star_surf, self.two_star_eight_rect)

#                 elif stick_of_war.current_time >= 240000:
#                     self.screen.blit(self.one_star_surf, self.one_star_eight_rect)

#                 # self.playing_lvl[7] = False

#             if firebase.stage_level == 9:
#                 if 0 <= stick_of_war.current_time <= 120000:
#                     self.screen.blit(self.three_star_surf, self.three_star_nine_rect)

#                 elif 120000 < stick_of_war.current_time <= 240000:
#                     self.screen.blit(self.two_star_surf, self.two_star_nine_rect)

#                 elif stick_of_war.current_time > 240000:
#                     self.screen.blit(self.one_star_surf, self.one_star_nine_rect)

#                 # self.playing_lvl[8] = False

#             if firebase.stage_level == 10:
#                 if 0 <= stick_of_war.current_time <= 120000:
#                     self.screen.blit(self.three_star_surf, self.three_star_ten_rect)

#                 elif 120000 < stick_of_war.current_time <= 240000:
#                     self.screen.blit(self.two_star_surf, self.two_star_ten_rect)

#                 elif stick_of_war.current_time > 240000:  
#                     self.screen.blit(self.one_star_surf, self.one_star_ten_rect)

#                 # self.playing_lvl[9] = False
<<<<<<< HEAD
                
=======

>>>>>>> e73e84320d2a3baf5a3f82f3d17532ab14d278ed
#     def run(self):
#         while True:
#             self.screen.fill((255, 255, 255))

#             self.event_handling()

#             self.choose_level()

#             pygame.display.update()
#             self.clock.tick(60)

# if __name__ == '__main__':
#     GameLevel().run()

<<<<<<< HEAD
# level = GameLevel()
=======
# level = GameLevel()
>>>>>>> e73e84320d2a3baf5a3f82f3d17532ab14d278ed
>>>>>>> Stashed changes
