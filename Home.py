import pygame
from sys import exit
import importlib

pygame.init()
pygame.font.init()


class LoadingBar:
    def __init__(self, x, y, height, width, colour, border_colour, border_width):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.colour = colour
        self.border_colour = border_colour
        self.border_width = border_width
        self.progress = 0  # the first progress variable is to calculate how much should it be filled in
        # if remove that the loading bar won't work

    def draw_bar(self, screen):
        pygame.draw.rect(screen, self.border_colour, (
            self.x - self.border_width, self.y - self.border_width, self.width + 2 * self.border_width,
            self.height + 2 * self.border_width))
        pygame.draw.rect(screen, self.colour, (self.x, self.y, self.width * self.progress, self.height))


class GameHome:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1000, 600))
        pygame.display.set_caption('Home Page')
        self.loading_bar = LoadingBar(400, 500, 30, 200, (255, 255, 224), (0, 0, 0), 2)  # Fixed width initialization
        self.progress = 0  # this one is if I put 0.2 it will start the loading bar from 0.2

        self.image = pygame.image.load(
            "War of stick/Picture/utils/background_photo.jpg")  # Replace "home_image.jpg" with your image path
        self.image_rect = self.image.get_rect(center=(1000 // 2, 600 // 2))

        self.wood_plank_surface = pygame.image.load('Plant vs Stick/Picture/utils/wood.png').convert()
        self.wood_plank_surface = pygame.transform.scale(self.wood_plank_surface, (200, 60))
        self.pokemon_vs_naruto_rect = None
        self.stick_of_war_rect = None

        self.text_box_surface = pygame.image.load('Plant vs Stick/Picture/utils/wood.png').convert()
        self.text_box_surface = pygame.transform.scale(self.text_box_surface, (400, 60))

        self.loading = True
        self.finish_loading = False

        self.font = pygame.font.Font(None, 40)
        self.first_time = True
        self.choose_game_to_play = False
        self.choosing_login_method = True
        self.signing_in = False
        self.signing_up = False
        self.login_as_guest = False
        self.key_user = False
        self.key_pass = False


        #sign up
        self.user_text_box_rectangle = self.text_box_surface.get_rect(center=(500, 250))
        self.ask_username = self.font.render('Choose your username', True, (255, 255, 255))
        self.ask_username_rect = self.ask_username.get_rect(center=(500, 200))

        self.pass_text_box_rectangle = self.text_box_surface.get_rect(center=(500, 350))
        self.ask_password = self.font.render("Enter password", True, (255, 255, 255))
        self.ask_password_rect = self.ask_password.get_rect(center=(500, 300))

        self.enter_rectangle = self.wood_plank_surface.get_rect(center=(500, 450))
        self.enter_text = self.font.render("Enter", True, (255, 255, 255))
        self.enter_text_rect = self.enter_text.get_rect(center=self.enter_rectangle.center)

        self.back_rectangle = self.wood_plank_surface.get_rect(center=(100, 100))
        self.back_text = self.font.render("Back", True, (255, 255, 255))
        self.back_text_rect = self.back_text.get_rect(center=self.back_rectangle.center)

        self.sign_up_username = ""
        self.sign_up_password = ""
        self.signup_done = False



    def event_handling(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif self.choose_game_to_play and event.type == pygame.MOUSEBUTTONDOWN:
                if self.stick_of_war_rect.collidepoint(pygame.mouse.get_pos()):
                    self.go_level_py()
                elif self.pokemon_vs_naruto_rect.collidepoint(pygame.mouse.get_pos()):
                    self.go_pokemon_py()
            if self.choosing_login_method and event.type == pygame.MOUSEBUTTONDOWN:
                if self.sign_in_rect.collidepoint(pygame.mouse.get_pos()) and not self.signing_up and not self.login_as_guest:
                    self.signing_in = True
                    self.choosing_login_method = False
                elif self.sign_up_rect.collidepoint(pygame.mouse.get_pos()) and not self.signing_in and not self.login_as_guest:
                    self.signing_up = True
                    self.choosing_login_method = False
                elif self.login_as_guest_rect.collidepoint(pygame.mouse.get_pos()) and not self.signing_in and not self.signing_up:
                    self.login_as_guest = True
                    self.choosing_login_method = False

            if self.signing_up:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.user_text_box_rectangle.collidepoint(pygame.mouse.get_pos()):
                        self.key_user = True
                        self.key_pass = False
                    elif self.pass_text_box_rectangle.collidepoint(pygame.mouse.get_pos()):
                        self.key_user = False
                        self.key_pass = True
                    elif self.back_rectangle.collidepoint(pygame.mouse.get_pos()):
                        self.key_user = False
                        self.key_pass = False
                        self.signing_up = False
                        self.choosing_login_method = True
                    elif self.enter_rectangle.collidepoint(pygame.mouse.get_pos()):
                        self.key_user = False
                        self.key_pass = False
                        self.signing_up = False
                        self.choosing_login_method = True
                        self.signup_done = True
                if event.type == pygame.KEYDOWN:
                    if self.key_user:
                        if event.key == pygame.K_BACKSPACE:
                            self.sign_up_username = self.sign_up_username[:-1]
                        else:
                            self.sign_up_username += event.unicode
                    elif self.key_pass:
                        if event.key == pygame.K_BACKSPACE:
                            self.sign_up_password = self.sign_up_password[:-1]
                        else:
                            self.sign_up_password += event.unicode


    def go_pokemon_py(self):
        pygame.quit()  # Cleanup before switching
        importlib.invalidate_caches()  # Clear any cached importlib entries
        pokemon_module = importlib.import_module("Pokemon_vs_Stick")
        game_pokemon = pokemon_module.GamePokemonVsStick()
        game_pokemon.run()  # Call a method to start Stick_of_war game
        exit()

    def go_level_py(self):
        pygame.quit()  # Cleanup before switching
        importlib.invalidate_caches()  # Clear any cached importlib entries
        level_module = importlib.import_module('Level')
        game_level = level_module.GameLevel()
        game_level.run()
        exit()

    def game_start_bg(self):
        self.screen.blit(self.image, self.image_rect)

    def update_progress(self):
        # Simulating loading progress

        if self.progress <= 1:
            self.progress += 0.03
            self.finish_loading = False

        else:
            self.progress = 1
            self.finish_loading = True
            self.loading = False

        self.loading_bar.progress = self.progress
        self.loading_bar.draw_bar(self.screen)

    def choose_game(self):
        wood_plank_rectangle = self.wood_plank_surface.get_rect(center=(350, 430))
        self.screen.blit(self.wood_plank_surface, wood_plank_rectangle)
        pokemon_vs_naruto = self.font.render('Plant vs Zombie', True, (255, 255, 255))
        self.pokemon_vs_naruto_rect = pokemon_vs_naruto.get_rect(center=(350, 430))
        self.screen.blit(pokemon_vs_naruto, self.pokemon_vs_naruto_rect)

        wood_plank_rectangle = self.wood_plank_surface.get_rect(center=(650, 430))
        self.screen.blit(self.wood_plank_surface, wood_plank_rectangle)
        stick_of_war = self.font.render("Stick of War", True, (255, 255, 255))
        self.stick_of_war_rect = stick_of_war.get_rect(center=(650, 430))
        self.screen.blit(stick_of_war, self.stick_of_war_rect)

    def signing_user(self):
        wood_plank_rectangle = self.wood_plank_surface.get_rect(center=(350, 430))
        self.screen.blit(self.wood_plank_surface, wood_plank_rectangle)
        sign_up = self.font.render('Sign Up', True, (255, 255, 255))
        self.sign_up_rect = sign_up.get_rect(center=(350, 450))
        self.screen.blit(sign_up, self.sign_up_rect)

        wood_plank_rectangle = self.wood_plank_surface.get_rect(center=(650, 430))
        self.screen.blit(self.wood_plank_surface, wood_plank_rectangle)
        sign_in = self.font.render("Sign In", True, (255, 255, 255))
        self.sign_in_rect = sign_in.get_rect(center=(650, 450))
        self.screen.blit(sign_in, self.sign_in_rect)

        wood_plank_rectangle = self.wood_plank_surface.get_rect(center=(500, 300))
        self.screen.blit(self.wood_plank_surface, wood_plank_rectangle)
        guest = self.font.render("Login as Guest", True, (255, 255, 255))
        self.login_as_guest_rect = guest.get_rect(center=(500, 300))
        self.screen.blit(guest, self.login_as_guest_rect)

    def signing_in(self):
        pass

    def sign_up(self):
        # Draw username elements
        self.screen.blit(self.ask_username, self.ask_username_rect)
        self.screen.blit(self.text_box_surface, self.user_text_box_rectangle)
        self.username = self.font.render(self.sign_up_username, True, (255, 255, 255))
        username_rect = self.username.get_rect(center=self.user_text_box_rectangle.center)
        self.screen.blit(self.username, username_rect.move(0, 0))

        # Draw password elements
        self.screen.blit(self.ask_password, self.ask_password_rect)
        self.screen.blit(self.text_box_surface, self.pass_text_box_rectangle)
        self.password = self.font.render(self.sign_up_password, True, (255, 255, 255))
        password_rect = self.password.get_rect(center=self.pass_text_box_rectangle.center)
        self.screen.blit(self.password, password_rect.move(0, 0))

        # Draw enter button
        self.screen.blit(self.wood_plank_surface, self.enter_rectangle)
        self.screen.blit(self.enter_text, self.enter_text_rect)

        # Draw back button
        self.screen.blit(self.wood_plank_surface, self.back_rectangle)
        self.screen.blit(self.back_text, self.back_text_rect)

    def run(self):
        while True:
            self.screen.fill((255, 255, 255))

            self.event_handling()
            self.game_start_bg()
            if self.first_time:
                if self.loading:
                    self.update_progress()
                elif self.finish_loading:
                    if self.choosing_login_method:
                        self.signing_user()
                    elif self.signing_in:
                        pass
                    elif self.signing_up:
                        self.sign_up()
                    elif self.choose_game_to_play:
                        self.choose_game()
            else:
                self.choose_game()
            pygame.display.update()
            self.clock.tick(60)
    

if __name__ == '__main__':
    GameHome().run()
