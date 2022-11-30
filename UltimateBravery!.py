import random
import pygame
import time
import sys
import os
import pickle

pygame.init()
pygame.mixer.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height), pygame.RESIZABLE)
pygame.display.set_caption("Ultimate Bravery")


white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (34, 177, 76)
yellow = (200, 200, 0)
blue = (100, 100, 255)
dark_green = (20, 100, 50)
dark_red = (155, 0, 0)
dark_yellow = (100, 100, 0)
dark_blue = (0, 0, 155)

sys.setrecursionlimit(1500)

clock = pygame.time.Clock()

smallfont = pygame.font.SysFont("Calibri", 25)
medfont = pygame.font.SysFont("Elephant", 50)
largefont = pygame.font.SysFont("Stencil", 75)

icon = pygame.image.load(os.path.join('images/icon.png'))
pygame.display.set_icon(icon)
void = pygame.image.load(os.path.join("images/void.png"))
img_background_start = pygame.image.load(os.path.join("images/background.png"))
img_quit_active = pygame.image.load(os.path.join("images/quit_active.png"))
letsgo_active = pygame.image.load(os.path.join("images/button_letsgo_active.png"))
letsgo_inactive = pygame.image.load(os.path.join("images/button_letsgo_inactive.png"))
img_quit_inactive = pygame.image.load(os.path.join("images/quit_inactive.png"))
img_playnow_active = pygame.image.load(os.path.join("images/start_active.png"))
img_playnow_inactive = pygame.image.load(os.path.join("images/start_inactive.png"))
img_howling_abyss_active = pygame.image.load(os.path.join("images/howling_abyss_button_active.png"))
img_howling_abyss_inactive = pygame.image.load(os.path.join("images/howling_abyss_button_inactive.png"))
img_background_howling = pygame.image.load(os.path.join("images/background_howling abyss.png"))
img_background_summoner = pygame.image.load(os.path.join("images/background_summoner's rift.png"))
img_summoner_active = pygame.image.load(os.path.join("images/summoner_button_active.png"))
img_summoner_inactive = pygame.image.load(os.path.join("images/summoner_button_inactive.png"))
img_background_twisted = pygame.image.load(os.path.join("images/background_twisted treeline.png"))
img_twisted_active = pygame.image.load(os.path.join("images/twisted_treeline_button_active.png"))
img_twisted_inactive = pygame.image.load(os.path.join("images/twisted_treeline_button_inactive.png"))
button_reroll_active = pygame.image.load(os.path.join("images/button_reroll_active.png"))
button_reroll_inactive = pygame.image.load(os.path.join("images/button_reroll_inactive.png"))
settings_active = pygame.image.load(os.path.join("images/settings_active.png"))
settings_inactive = pygame.image.load(os.path.join("images/settings_inactive.png"))
image_1 = pygame.image.load(os.path.join("images/1.png"))
image_2 = pygame.image.load(os.path.join("images/2.png"))
image_3 = pygame.image.load(os.path.join("images/3.png"))
image_4 = pygame.image.load(os.path.join("images/4.png"))
image_5 = pygame.image.load(os.path.join("images/5.png"))
img_rules_inactive = pygame.image.load(os.path.join("images/rules_inactive.png"))
img_rules_active = pygame.image.load(os.path.join("images/rules_active.png"))
back_inactive = pygame.image.load(os.path.join("images/back_inactive.png"))
back_active = pygame.image.load(os.path.join("images/back_active.png"))
img_title = pygame.image.load(os.path.join("images/Title.png"))
rules_text = pygame.image.load(os.path.join("images/rules.png"))
#item_set_active = pygame.image.load(os.path.join("images/button_create_item_set_active.png"))
#item_set_inactive = pygame.image.load(os.path.join("images/button_create_item_set_inactive.png"))

def message_to_screen(msg, color, y_displace=0,x_displace=0, size="small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (int(display_width / 2) + x_displace, int(display_height / 2) + y_displace)
    gameDisplay.blit(textSurf, textRect)


def text_objects(text, color, size="small"):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)

    return textSurface, textSurface.get_rect()

#Loading...
message_to_screen("Loading...", white, size="large")
pygame.display.update()
#Load les images
for i in range(1):
    m_Aatrox_i = pygame.image.load("images/mini_champs_inactive_Aatrox.png")
    m_Aatrox_a = pygame.image.load("images/mini_champs_active_Aatrox.png")
    b_Aatrox = pygame.image.load("images/big_champs_Aatrox.png")
    m_Ahri_i = pygame.image.load("images/mini_champs_inactive_Ahri.png")
    m_Ahri_a = pygame.image.load("images/mini_champs_active_Ahri.png")
    b_Ahri = pygame.image.load("images/big_champs_Ahri.png")
    m_Akali_i = pygame.image.load("images/mini_champs_inactive_Akali.png")
    m_Akali_a = pygame.image.load("images/mini_champs_active_Akali.png")
    b_Akali = pygame.image.load("images/big_champs_Akali.png")
    m_Alistar_i = pygame.image.load("images/mini_champs_inactive_Alistar.png")
    m_Alistar_a = pygame.image.load("images/mini_champs_active_Alistar.png")
    b_Alistar = pygame.image.load("images/big_champs_Alistar.png")
    m_Amumu_i = pygame.image.load("images/mini_champs_inactive_Amumu.png")
    m_Amumu_a = pygame.image.load("images/mini_champs_active_Amumu.png")
    b_Amumu = pygame.image.load("images/big_champs_Amumu.png")
    m_Anivia_i = pygame.image.load("images/mini_champs_inactive_Anivia.png")
    m_Anivia_a = pygame.image.load("images/mini_champs_active_Anivia.png")
    b_Anivia = pygame.image.load("images/big_champs_Anivia.png")
    m_Annie_i = pygame.image.load("images/mini_champs_inactive_Annie.png")
    m_Annie_a = pygame.image.load("images/mini_champs_active_Annie.png")
    b_Annie = pygame.image.load("images/big_champs_Annie.png")
    m_Ashe_i = pygame.image.load("images/mini_champs_inactive_Ashe.png")
    m_Ashe_a = pygame.image.load("images/mini_champs_active_Ashe.png")
    b_Ashe = pygame.image.load("images/big_champs_Ashe.png")
    m_AurelionSol_i = pygame.image.load("images/mini_champs_inactive_AurelionSol.png")
    m_AurelionSol_a = pygame.image.load("images/mini_champs_active_AurelionSol.png")
    b_AurelionSol = pygame.image.load("images/big_champs_AurelionSol.png")
    m_Azir_i = pygame.image.load("images/mini_champs_inactive_Azir.png")
    m_Azir_a = pygame.image.load("images/mini_champs_active_Azir.png")
    b_Azir = pygame.image.load("images/big_champs_Azir.png")
    m_Bard_i = pygame.image.load("images/mini_champs_inactive_Bard.png")
    m_Bard_a = pygame.image.load("images/mini_champs_active_Bard.png")
    b_Bard = pygame.image.load("images/big_champs_Bard.png")
    m_Blitzcrank_i = pygame.image.load("images/mini_champs_inactive_Blitzcrank.png")
    m_Blitzcrank_a = pygame.image.load("images/mini_champs_active_Blitzcrank.png")
    b_Blitzcrank = pygame.image.load("images/big_champs_Blitzcrank.png")
    m_Brand_i = pygame.image.load("images/mini_champs_inactive_Brand.png")
    m_Brand_a = pygame.image.load("images/mini_champs_active_Brand.png")
    b_Brand = pygame.image.load("images/big_champs_Brand.png")
    m_Braum_i = pygame.image.load("images/mini_champs_inactive_Braum.png")
    m_Braum_a = pygame.image.load("images/mini_champs_active_Braum.png")
    b_Braum = pygame.image.load("images/big_champs_Braum.png")
    m_Caitlyn_i = pygame.image.load("images/mini_champs_inactive_Caitlyn.png")
    m_Caitlyn_a = pygame.image.load("images/mini_champs_active_Caitlyn.png")
    b_Caitlyn = pygame.image.load("images/big_champs_Caitlyn.png")
    m_Cassiopeia_i = pygame.image.load("images/mini_champs_inactive_Cassiopeia.png")
    m_Cassiopeia_a = pygame.image.load("images/mini_champs_active_Cassiopeia.png")
    b_Cassiopeia = pygame.image.load("images/big_champs_Cassiopeia.png")
    m_Chogath_i = pygame.image.load("images/mini_champs_inactive_Chogath.png")
    m_Chogath_a = pygame.image.load("images/mini_champs_active_Chogath.png")
    b_Chogath = pygame.image.load("images/big_champs_Chogath.png")
    m_Corki_i = pygame.image.load("images/mini_champs_inactive_Corki.png")
    m_Corki_a = pygame.image.load("images/mini_champs_active_Corki.png")
    b_Corki = pygame.image.load("images/big_champs_Corki.png")
    m_Darius_i = pygame.image.load("images/mini_champs_inactive_Darius.png")
    m_Darius_a = pygame.image.load("images/mini_champs_active_Darius.png")
    b_Darius = pygame.image.load("images/big_champs_Darius.png")
    m_Diana_i = pygame.image.load("images/mini_champs_inactive_Diana.png")
    m_Diana_a = pygame.image.load("images/mini_champs_active_Diana.png")
    b_Diana = pygame.image.load("images/big_champs_Diana.png")
    m_DrMundo_i = pygame.image.load("images/mini_champs_inactive_DrMundo.png")
    m_DrMundo_a = pygame.image.load("images/mini_champs_active_DrMundo.png")
    b_DrMundo = pygame.image.load("images/big_champs_DrMundo.png")
    m_Draven_i = pygame.image.load("images/mini_champs_inactive_Draven.png")
    m_Draven_a = pygame.image.load("images/mini_champs_active_Draven.png")
    b_Draven = pygame.image.load("images/big_champs_Draven.png")
    m_Ekko_i = pygame.image.load("images/mini_champs_inactive_Ekko.png")
    m_Ekko_a = pygame.image.load("images/mini_champs_active_Ekko.png")
    b_Ekko = pygame.image.load("images/big_champs_Ekko.png")
    m_Elise_i = pygame.image.load("images/mini_champs_inactive_Elise.png")
    m_Elise_a = pygame.image.load("images/mini_champs_active_Elise.png")
    b_Elise = pygame.image.load("images/big_champs_Elise.png")
    m_Evelynn_i = pygame.image.load("images/mini_champs_inactive_Evelynn.png")
    m_Evelynn_a = pygame.image.load("images/mini_champs_active_Evelynn.png")
    b_Evelynn = pygame.image.load("images/big_champs_Evelynn.png")
    m_Ezreal_i = pygame.image.load("images/mini_champs_inactive_Ezreal.png")
    m_Ezreal_a = pygame.image.load("images/mini_champs_active_Ezreal.png")
    b_Ezreal = pygame.image.load("images/big_champs_Ezreal.png")
    m_FiddleSticks_i = pygame.image.load("images/mini_champs_inactive_FiddleSticks.png")
    m_FiddleSticks_a = pygame.image.load("images/mini_champs_active_FiddleSticks.png")
    b_FiddleSticks = pygame.image.load("images/big_champs_FiddleSticks.png")
    m_Fiora_i = pygame.image.load("images/mini_champs_inactive_Fiora.png")
    m_Fiora_a = pygame.image.load("images/mini_champs_active_Fiora.png")
    b_Fiora = pygame.image.load("images/big_champs_Fiora.png")
    m_Fizz_i = pygame.image.load("images/mini_champs_inactive_Fizz.png")
    m_Fizz_a = pygame.image.load("images/mini_champs_active_Fizz.png")
    b_Fizz = pygame.image.load("images/big_champs_Fizz.png")
    m_Galio_i = pygame.image.load("images/mini_champs_inactive_Galio.png")
    m_Galio_a = pygame.image.load("images/mini_champs_active_Galio.png")
    b_Galio = pygame.image.load("images/big_champs_Galio.png")
    m_Gangplank_i = pygame.image.load("images/mini_champs_inactive_Gangplank.png")
    m_Gangplank_a = pygame.image.load("images/mini_champs_active_Gangplank.png")
    b_Gangplank = pygame.image.load("images/big_champs_Gangplank.png")
    m_Garen_i = pygame.image.load("images/mini_champs_inactive_Garen.png")
    m_Garen_a = pygame.image.load("images/mini_champs_active_Garen.png")
    b_Garen = pygame.image.load("images/big_champs_Garen.png")
    m_Gnar_i = pygame.image.load("images/mini_champs_inactive_Gnar.png")
    m_Gnar_a = pygame.image.load("images/mini_champs_active_Gnar.png")
    b_Gnar = pygame.image.load("images/big_champs_Gnar.png")
    m_Gragas_i = pygame.image.load("images/mini_champs_inactive_Gragas.png")
    m_Gragas_a = pygame.image.load("images/mini_champs_active_Gragas.png")
    b_Gragas = pygame.image.load("images/big_champs_Gragas.png")
    m_Graves_i = pygame.image.load("images/mini_champs_inactive_Graves.png")
    m_Graves_a = pygame.image.load("images/mini_champs_active_Graves.png")
    b_Graves = pygame.image.load("images/big_champs_Graves.png")
    m_Hecarim_i = pygame.image.load("images/mini_champs_inactive_Hecarim.png")
    m_Hecarim_a = pygame.image.load("images/mini_champs_active_Hecarim.png")
    b_Hecarim = pygame.image.load("images/big_champs_Hecarim.png")
    m_Heimerdinger_i = pygame.image.load("images/mini_champs_inactive_Heimerdinger.png")
    m_Heimerdinger_a = pygame.image.load("images/mini_champs_active_Heimerdinger.png")
    b_Heimerdinger = pygame.image.load("images/big_champs_Heimerdinger.png")
    m_Illaoi_i = pygame.image.load("images/mini_champs_inactive_Illaoi.png")
    m_Illaoi_a = pygame.image.load("images/mini_champs_active_Illaoi.png")
    b_Illaoi = pygame.image.load("images/big_champs_Illaoi.png")
    m_Irelia_i = pygame.image.load("images/mini_champs_inactive_Irelia.png")
    m_Irelia_a = pygame.image.load("images/mini_champs_active_Irelia.png")
    b_Irelia = pygame.image.load("images/big_champs_Irelia.png")
    m_Janna_i = pygame.image.load("images/mini_champs_inactive_Janna.png")
    m_Janna_a = pygame.image.load("images/mini_champs_active_Janna.png")
    b_Janna = pygame.image.load("images/big_champs_Janna.png")
    m_JarvanIV_i = pygame.image.load("images/mini_champs_inactive_JarvanIV.png")
    m_JarvanIV_a = pygame.image.load("images/mini_champs_active_JarvanIV.png")
    b_JarvanIV = pygame.image.load("images/big_champs_JarvanIV.png")
    m_Jax_i = pygame.image.load("images/mini_champs_inactive_Jax.png")
    m_Jax_a = pygame.image.load("images/mini_champs_active_Jax.png")
    b_Jax = pygame.image.load("images/big_champs_Jax.png")
    m_Jayce_i = pygame.image.load("images/mini_champs_inactive_Jayce.png")
    m_Jayce_a = pygame.image.load("images/mini_champs_active_Jayce.png")
    b_Jayce = pygame.image.load("images/big_champs_Jayce.png")
    m_Jhin_i = pygame.image.load("images/mini_champs_inactive_Jhin.png")
    m_Jhin_a = pygame.image.load("images/mini_champs_active_Jhin.png")
    b_Jhin = pygame.image.load("images/big_champs_Jhin.png")
    m_Jinx_i = pygame.image.load("images/mini_champs_inactive_Jinx.png")
    m_Jinx_a = pygame.image.load("images/mini_champs_active_Jinx.png")
    b_Jinx = pygame.image.load("images/big_champs_Jinx.png")
    m_Kalista_i = pygame.image.load("images/mini_champs_inactive_Kalista.png")
    m_Kalista_a = pygame.image.load("images/mini_champs_active_Kalista.png")
    b_Kalista = pygame.image.load("images/big_champs_Kalista.png")
    m_Karma_i = pygame.image.load("images/mini_champs_inactive_Karma.png")
    m_Karma_a = pygame.image.load("images/mini_champs_active_Karma.png")
    b_Karma = pygame.image.load("images/big_champs_Karma.png")
    m_Karthus_i = pygame.image.load("images/mini_champs_inactive_Karthus.png")
    m_Karthus_a = pygame.image.load("images/mini_champs_active_Karthus.png")
    b_Karthus = pygame.image.load("images/big_champs_Karthus.png")
    m_Kassadin_i = pygame.image.load("images/mini_champs_inactive_Kassadin.png")
    m_Kassadin_a = pygame.image.load("images/mini_champs_active_Kassadin.png")
    b_Kassadin = pygame.image.load("images/big_champs_Kassadin.png")
    m_Katarina_i = pygame.image.load("images/mini_champs_inactive_Katarina.png")
    m_Katarina_a = pygame.image.load("images/mini_champs_active_Katarina.png")
    b_Katarina = pygame.image.load("images/big_champs_Katarina.png")
    m_Kayle_i = pygame.image.load("images/mini_champs_inactive_Kayle.png")
    m_Kayle_a = pygame.image.load("images/mini_champs_active_Kayle.png")
    b_Kayle = pygame.image.load("images/big_champs_Kayle.png")
    m_Kennen_i = pygame.image.load("images/mini_champs_inactive_Kennen.png")
    m_Kennen_a = pygame.image.load("images/mini_champs_active_Kennen.png")
    b_Kennen = pygame.image.load("images/big_champs_Kennen.png")
    m_Khazix_i = pygame.image.load("images/mini_champs_inactive_Khazix.png")
    m_Khazix_a = pygame.image.load("images/mini_champs_active_Khazix.png")
    b_Khazix = pygame.image.load("images/big_champs_Khazix.png")
    m_Kindred_i = pygame.image.load("images/mini_champs_inactive_Kindred.png")
    m_Kindred_a = pygame.image.load("images/mini_champs_active_Kindred.png")
    b_Kindred = pygame.image.load("images/big_champs_Kindred.png")
    m_Kled_i = pygame.image.load("images/mini_champs_inactive_Kled.png")
    m_Kled_a = pygame.image.load("images/mini_champs_active_Kled.png")
    b_Kled = pygame.image.load("images/big_champs_Kled.png")
    m_KogMaw_i = pygame.image.load("images/mini_champs_inactive_KogMaw.png")
    m_KogMaw_a = pygame.image.load("images/mini_champs_active_KogMaw.png")
    b_KogMaw = pygame.image.load("images/big_champs_KogMaw.png")
    m_Leblanc_i = pygame.image.load("images/mini_champs_inactive_Leblanc.png")
    m_Leblanc_a = pygame.image.load("images/mini_champs_active_Leblanc.png")
    b_Leblanc = pygame.image.load("images/big_champs_Leblanc.png")
    m_LeeSin_i = pygame.image.load("images/mini_champs_inactive_LeeSin.png")
    m_LeeSin_a = pygame.image.load("images/mini_champs_active_LeeSin.png")
    b_LeeSin = pygame.image.load("images/big_champs_LeeSin.png")
    m_Leona_i = pygame.image.load("images/mini_champs_inactive_Leona.png")
    m_Leona_a = pygame.image.load("images/mini_champs_active_Leona.png")
    b_Leona = pygame.image.load("images/big_champs_Leona.png")
    m_Lissandra_i = pygame.image.load("images/mini_champs_inactive_Lissandra.png")
    m_Lissandra_a = pygame.image.load("images/mini_champs_active_Lissandra.png")
    b_Lissandra = pygame.image.load("images/big_champs_Lissandra.png")
    m_Lucian_i = pygame.image.load("images/mini_champs_inactive_Lucian.png")
    m_Lucian_a = pygame.image.load("images/mini_champs_active_Lucian.png")
    b_Lucian = pygame.image.load("images/big_champs_Lucian.png")
    m_Lulu_i = pygame.image.load("images/mini_champs_inactive_Lulu.png")
    m_Lulu_a = pygame.image.load("images/mini_champs_active_Lulu.png")
    b_Lulu = pygame.image.load("images/big_champs_Lulu.png")
    m_Lux_i = pygame.image.load("images/mini_champs_inactive_Lux.png")
    m_Lux_a = pygame.image.load("images/mini_champs_active_Lux.png")
    b_Lux = pygame.image.load("images/big_champs_Lux.png")
    m_Malphite_i = pygame.image.load("images/mini_champs_inactive_Malphite.png")
    m_Malphite_a = pygame.image.load("images/mini_champs_active_Malphite.png")
    b_Malphite = pygame.image.load("images/big_champs_Malphite.png")
    m_Malzahar_i = pygame.image.load("images/mini_champs_inactive_Malzahar.png")
    m_Malzahar_a = pygame.image.load("images/mini_champs_active_Malzahar.png")
    b_Malzahar = pygame.image.load("images/big_champs_Malzahar.png")
    m_Maokai_i = pygame.image.load("images/mini_champs_inactive_Maokai.png")
    m_Maokai_a = pygame.image.load("images/mini_champs_active_Maokai.png")
    b_Maokai = pygame.image.load("images/big_champs_Maokai.png")
    m_MasterYi_i = pygame.image.load("images/mini_champs_inactive_MasterYi.png")
    m_MasterYi_a = pygame.image.load("images/mini_champs_active_MasterYi.png")
    b_MasterYi = pygame.image.load("images/big_champs_MasterYi.png")
    m_MissFortune_i = pygame.image.load("images/mini_champs_inactive_MissFortune.png")
    m_MissFortune_a = pygame.image.load("images/mini_champs_active_MissFortune.png")
    b_MissFortune = pygame.image.load("images/big_champs_MissFortune.png")
    m_Mordekaiser_i = pygame.image.load("images/mini_champs_inactive_Mordekaiser.png")
    m_Mordekaiser_a = pygame.image.load("images/mini_champs_active_Mordekaiser.png")
    b_Mordekaiser = pygame.image.load("images/big_champs_Mordekaiser.png")
    m_Morgana_i = pygame.image.load("images/mini_champs_inactive_Morgana.png")
    m_Morgana_a = pygame.image.load("images/mini_champs_active_Morgana.png")
    b_Morgana = pygame.image.load("images/big_champs_Morgana.png")
    m_Nami_i = pygame.image.load("images/mini_champs_inactive_Nami.png")
    m_Nami_a = pygame.image.load("images/mini_champs_active_Nami.png")
    b_Nami = pygame.image.load("images/big_champs_Nami.png")
    m_Nasus_i = pygame.image.load("images/mini_champs_inactive_Nasus.png")
    m_Nasus_a = pygame.image.load("images/mini_champs_active_Nasus.png")
    b_Nasus = pygame.image.load("images/big_champs_Nasus.png")
    m_Nautilus_i = pygame.image.load("images/mini_champs_inactive_Nautilus.png")
    m_Nautilus_a = pygame.image.load("images/mini_champs_active_Nautilus.png")
    b_Nautilus = pygame.image.load("images/big_champs_Nautilus.png")
    m_Nidalee_i = pygame.image.load("images/mini_champs_inactive_Nidalee.png")
    m_Nidalee_a = pygame.image.load("images/mini_champs_active_Nidalee.png")
    b_Nidalee = pygame.image.load("images/big_champs_Nidalee.png")
    m_Nocturne_i = pygame.image.load("images/mini_champs_inactive_Nocturne.png")
    m_Nocturne_a = pygame.image.load("images/mini_champs_active_Nocturne.png")
    b_Nocturne = pygame.image.load("images/big_champs_Nocturne.png")
    m_Nunu_i = pygame.image.load("images/mini_champs_inactive_Nunu.png")
    m_Nunu_a = pygame.image.load("images/mini_champs_active_Nunu.png")
    b_Nunu = pygame.image.load("images/big_champs_Nunu.png")
    m_Olaf_i = pygame.image.load("images/mini_champs_inactive_Olaf.png")
    m_Olaf_a = pygame.image.load("images/mini_champs_active_Olaf.png")
    b_Olaf = pygame.image.load("images/big_champs_Olaf.png")
    m_Orianna_i = pygame.image.load("images/mini_champs_inactive_Orianna.png")
    m_Orianna_a = pygame.image.load("images/mini_champs_active_Orianna.png")
    b_Orianna = pygame.image.load("images/big_champs_Orianna.png")
    m_Pantheon_i = pygame.image.load("images/mini_champs_inactive_Pantheon.png")
    m_Pantheon_a = pygame.image.load("images/mini_champs_active_Pantheon.png")
    b_Pantheon = pygame.image.load("images/big_champs_Pantheon.png")
    m_Poppy_i = pygame.image.load("images/mini_champs_inactive_Poppy.png")
    m_Poppy_a = pygame.image.load("images/mini_champs_active_Poppy.png")
    b_Poppy = pygame.image.load("images/big_champs_Poppy.png")
    m_Quinn_i = pygame.image.load("images/mini_champs_inactive_Quinn.png")
    m_Quinn_a = pygame.image.load("images/mini_champs_active_Quinn.png")
    b_Quinn = pygame.image.load("images/big_champs_Quinn.png")
    m_Rammus_i = pygame.image.load("images/mini_champs_inactive_Rammus.png")
    m_Rammus_a = pygame.image.load("images/mini_champs_active_Rammus.png")
    b_Rammus = pygame.image.load("images/big_champs_Rammus.png")
    m_RekSai_i = pygame.image.load("images/mini_champs_inactive_RekSai.png")
    m_RekSai_a = pygame.image.load("images/mini_champs_active_RekSai.png")
    b_RekSai = pygame.image.load("images/big_champs_RekSai.png")
    m_Renekton_i = pygame.image.load("images/mini_champs_inactive_Renekton.png")
    m_Renekton_a = pygame.image.load("images/mini_champs_active_Renekton.png")
    b_Renekton = pygame.image.load("images/big_champs_Renekton.png")
    m_Rengar_i = pygame.image.load("images/mini_champs_inactive_Rengar.png")
    m_Rengar_a = pygame.image.load("images/mini_champs_active_Rengar.png")
    b_Rengar = pygame.image.load("images/big_champs_Rengar.png")
    m_Riven_i = pygame.image.load("images/mini_champs_inactive_Riven.png")
    m_Riven_a = pygame.image.load("images/mini_champs_active_Riven.png")
    b_Riven = pygame.image.load("images/big_champs_Riven.png")
    m_Rumble_i = pygame.image.load("images/mini_champs_inactive_Rumble.png")
    m_Rumble_a = pygame.image.load("images/mini_champs_active_Rumble.png")
    b_Rumble = pygame.image.load("images/big_champs_Rumble.png")
    m_Ryze_i = pygame.image.load("images/mini_champs_inactive_Ryze.png")
    m_Ryze_a = pygame.image.load("images/mini_champs_active_Ryze.png")
    b_Ryze = pygame.image.load("images/big_champs_Ryze.png")
    m_Sejuani_i = pygame.image.load("images/mini_champs_inactive_Sejuani.png")
    m_Sejuani_a = pygame.image.load("images/mini_champs_active_Sejuani.png")
    b_Sejuani = pygame.image.load("images/big_champs_Sejuani.png")
    m_Shaco_i = pygame.image.load("images/mini_champs_inactive_Shaco.png")
    m_Shaco_a = pygame.image.load("images/mini_champs_active_Shaco.png")
    b_Shaco = pygame.image.load("images/big_champs_Shaco.png")
    m_Shen_i = pygame.image.load("images/mini_champs_inactive_Shen.png")
    m_Shen_a = pygame.image.load("images/mini_champs_active_Shen.png")
    b_Shen = pygame.image.load("images/big_champs_Shen.png")
    m_Shyvana_i = pygame.image.load("images/mini_champs_inactive_Shyvana.png")
    m_Shyvana_a = pygame.image.load("images/mini_champs_active_Shyvana.png")
    b_Shyvana = pygame.image.load("images/big_champs_Shyvana.png")
    m_Singed_i = pygame.image.load("images/mini_champs_inactive_Singed.png")
    m_Singed_a = pygame.image.load("images/mini_champs_active_Singed.png")
    b_Singed = pygame.image.load("images/big_champs_Singed.png")
    m_Sion_i = pygame.image.load("images/mini_champs_inactive_Sion.png")
    m_Sion_a = pygame.image.load("images/mini_champs_active_Sion.png")
    b_Sion = pygame.image.load("images/big_champs_Sion.png")
    m_Sivir_i = pygame.image.load("images/mini_champs_inactive_Sivir.png")
    m_Sivir_a = pygame.image.load("images/mini_champs_active_Sivir.png")
    b_Sivir = pygame.image.load("images/big_champs_Sivir.png")
    m_Skarner_i = pygame.image.load("images/mini_champs_inactive_Skarner.png")
    m_Skarner_a = pygame.image.load("images/mini_champs_active_Skarner.png")
    b_Skarner = pygame.image.load("images/big_champs_Skarner.png")
    m_Sona_i = pygame.image.load("images/mini_champs_inactive_Sona.png")
    m_Sona_a = pygame.image.load("images/mini_champs_active_Sona.png")
    b_Sona = pygame.image.load("images/big_champs_Sona.png")
    m_Soraka_i = pygame.image.load("images/mini_champs_inactive_Soraka.png")
    m_Soraka_a = pygame.image.load("images/mini_champs_active_Soraka.png")
    b_Soraka = pygame.image.load("images/big_champs_Soraka.png")
    m_Swain_i = pygame.image.load("images/mini_champs_inactive_Swain.png")
    m_Swain_a = pygame.image.load("images/mini_champs_active_Swain.png")
    b_Swain = pygame.image.load("images/big_champs_Swain.png")
    m_Syndra_i = pygame.image.load("images/mini_champs_inactive_Syndra.png")
    m_Syndra_a = pygame.image.load("images/mini_champs_active_Syndra.png")
    b_Syndra = pygame.image.load("images/big_champs_Syndra.png")
    m_TahmKench_i = pygame.image.load("images/mini_champs_inactive_TahmKench.png")
    m_TahmKench_a = pygame.image.load("images/mini_champs_active_TahmKench.png")
    b_TahmKench = pygame.image.load("images/big_champs_TahmKench.png")
    m_Taliyah_i = pygame.image.load("images/mini_champs_inactive_Taliyah.png")
    m_Taliyah_a = pygame.image.load("images/mini_champs_active_Taliyah.png")
    b_Taliyah = pygame.image.load("images/big_champs_Taliyah.png")
    m_Talon_i = pygame.image.load("images/mini_champs_inactive_Talon.png")
    m_Talon_a = pygame.image.load("images/mini_champs_active_Talon.png")
    b_Talon = pygame.image.load("images/big_champs_Talon.png")
    m_Taric_i = pygame.image.load("images/mini_champs_inactive_Taric.png")
    m_Taric_a = pygame.image.load("images/mini_champs_active_Taric.png")
    b_Taric = pygame.image.load("images/big_champs_Taric.png")
    m_Teemo_i = pygame.image.load("images/mini_champs_inactive_Teemo.png")
    m_Teemo_a = pygame.image.load("images/mini_champs_active_Teemo.png")
    b_Teemo = pygame.image.load("images/big_champs_Teemo.png")
    m_Thresh_i = pygame.image.load("images/mini_champs_inactive_Thresh.png")
    m_Thresh_a = pygame.image.load("images/mini_champs_active_Thresh.png")
    b_Thresh = pygame.image.load("images/big_champs_Thresh.png")
    m_Tristana_i = pygame.image.load("images/mini_champs_inactive_Tristana.png")
    m_Tristana_a = pygame.image.load("images/mini_champs_active_Tristana.png")
    b_Tristana = pygame.image.load("images/big_champs_Tristana.png")
    m_Trundle_i = pygame.image.load("images/mini_champs_inactive_Trundle.png")
    m_Trundle_a = pygame.image.load("images/mini_champs_active_Trundle.png")
    b_Trundle = pygame.image.load("images/big_champs_Trundle.png")
    m_Tryndamere_i = pygame.image.load("images/mini_champs_inactive_Tryndamere.png")
    m_Tryndamere_a = pygame.image.load("images/mini_champs_active_Tryndamere.png")
    b_Tryndamere = pygame.image.load("images/big_champs_Tryndamere.png")
    m_TwistedFate_i = pygame.image.load("images/mini_champs_inactive_TwistedFate.png")
    m_TwistedFate_a = pygame.image.load("images/mini_champs_active_TwistedFate.png")
    b_TwistedFate = pygame.image.load("images/big_champs_TwistedFate.png")
    m_Twitch_i = pygame.image.load("images/mini_champs_inactive_Twitch.png")
    m_Twitch_a = pygame.image.load("images/mini_champs_active_Twitch.png")
    b_Twitch = pygame.image.load("images/big_champs_Twitch.png")
    m_Udyr_i = pygame.image.load("images/mini_champs_inactive_Udyr.png")
    m_Udyr_a = pygame.image.load("images/mini_champs_active_Udyr.png")
    b_Udyr = pygame.image.load("images/big_champs_Udyr.png")
    m_Urgot_i = pygame.image.load("images/mini_champs_inactive_Urgot.png")
    m_Urgot_a = pygame.image.load("images/mini_champs_active_Urgot.png")
    b_Urgot = pygame.image.load("images/big_champs_Urgot.png")
    m_Varus_i = pygame.image.load("images/mini_champs_inactive_Varus.png")
    m_Varus_a = pygame.image.load("images/mini_champs_active_Varus.png")
    b_Varus = pygame.image.load("images/big_champs_Varus.png")
    m_Vayne_i = pygame.image.load("images/mini_champs_inactive_Vayne.png")
    m_Vayne_a = pygame.image.load("images/mini_champs_active_Vayne.png")
    b_Vayne = pygame.image.load("images/big_champs_Vayne.png")
    m_Veigar_i = pygame.image.load("images/mini_champs_inactive_Veigar.png")
    m_Veigar_a = pygame.image.load("images/mini_champs_active_Veigar.png")
    b_Veigar = pygame.image.load("images/big_champs_Veigar.png")
    m_Velkoz_i = pygame.image.load("images/mini_champs_inactive_Velkoz.png")
    m_Velkoz_a = pygame.image.load("images/mini_champs_active_Velkoz.png")
    b_Velkoz = pygame.image.load("images/big_champs_Velkoz.png")
    m_Vi_i = pygame.image.load("images/mini_champs_inactive_Vi.png")
    m_Vi_a = pygame.image.load("images/mini_champs_active_Vi.png")
    b_Vi = pygame.image.load("images/big_champs_Vi.png")
    m_Viktor_i = pygame.image.load("images/mini_champs_inactive_Viktor.png")
    m_Viktor_a = pygame.image.load("images/mini_champs_active_Viktor.png")
    b_Viktor = pygame.image.load("images/big_champs_Viktor.png")
    m_Vladimir_i = pygame.image.load("images/mini_champs_inactive_Vladimir.png")
    m_Vladimir_a = pygame.image.load("images/mini_champs_active_Vladimir.png")
    b_Vladimir = pygame.image.load("images/big_champs_Vladimir.png")
    m_Volibear_i = pygame.image.load("images/mini_champs_inactive_Volibear.png")
    m_Volibear_a = pygame.image.load("images/mini_champs_active_Volibear.png")
    b_Volibear = pygame.image.load("images/big_champs_Volibear.png")
    m_Warwick_i = pygame.image.load("images/mini_champs_inactive_Warwick.png")
    m_Warwick_a = pygame.image.load("images/mini_champs_active_Warwick.png")
    b_Warwick = pygame.image.load("images/big_champs_Warwick.png")
    m_Wukong_i = pygame.image.load("images/mini_champs_inactive_Wukong.png")
    m_Wukong_a = pygame.image.load("images/mini_champs_active_Wukong.png")
    b_Wukong = pygame.image.load("images/big_champs_Wukong.png")
    m_Xerath_i = pygame.image.load("images/mini_champs_inactive_Xerath.png")
    m_Xerath_a = pygame.image.load("images/mini_champs_active_Xerath.png")
    b_Xerath = pygame.image.load("images/big_champs_Xerath.png")
    m_XinZhao_i = pygame.image.load("images/mini_champs_inactive_XinZhao.png")
    m_XinZhao_a = pygame.image.load("images/mini_champs_active_XinZhao.png")
    b_XinZhao = pygame.image.load("images/big_champs_XinZhao.png")
    m_Yasuo_i = pygame.image.load("images/mini_champs_inactive_Yasuo.png")
    m_Yasuo_a = pygame.image.load("images/mini_champs_active_Yasuo.png")
    b_Yasuo = pygame.image.load("images/big_champs_Yasuo.png")
    m_Yorick_i = pygame.image.load("images/mini_champs_inactive_Yorick.png")
    m_Yorick_a = pygame.image.load("images/mini_champs_active_Yorick.png")
    b_Yorick = pygame.image.load("images/big_champs_Yorick.png")
    m_Zac_i = pygame.image.load("images/mini_champs_inactive_Zac.png")
    m_Zac_a = pygame.image.load("images/mini_champs_active_Zac.png")
    b_Zac = pygame.image.load("images/big_champs_Zac.png")
    m_Zed_i = pygame.image.load("images/mini_champs_inactive_Zed.png")
    m_Zed_a = pygame.image.load("images/mini_champs_active_Zed.png")
    b_Zed = pygame.image.load("images/big_champs_Zed.png")
    m_Ziggs_i = pygame.image.load("images/mini_champs_inactive_Ziggs.png")
    m_Ziggs_a = pygame.image.load("images/mini_champs_active_Ziggs.png")
    b_Ziggs = pygame.image.load("images/big_champs_Ziggs.png")
    m_Zilean_i = pygame.image.load("images/mini_champs_inactive_Zilean.png")
    m_Zilean_a = pygame.image.load("images/mini_champs_active_Zilean.png")
    b_Zilean = pygame.image.load("images/big_champs_Zilean.png")
    m_Zyra_i = pygame.image.load("images/mini_champs_inactive_Zyra.png")
    m_Zyra_a = pygame.image.load("images/mini_champs_active_Zyra.png")
    b_Zyra = pygame.image.load("images/big_champs_Zyra.png")
    m_Camille_i = pygame.image.load("images/mini_champs_inactive_Camille.png")
    m_Camille_a = pygame.image.load("images/mini_champs_active_Camille.png")
    b_Camille = pygame.image.load("images/big_champs_Camille.png")
    m_Ivern_i = pygame.image.load("images/mini_champs_inactive_Ivern.png")
    m_Ivern_a = pygame.image.load("images/mini_champs_active_Ivern.png")
    b_Ivern = pygame.image.load("images/big_champs_Ivern.png")
    b_Random = pygame.image.load("images/big_champs_Random.png")
    m_Random_a = pygame.image.load("images/mini_champs_active_Random.png")
    m_Random_i = pygame.image.load("images/mini_champs_inactive_Random.png")



big_champ = b_Random
img_background = img_background_summoner
champion = "Random"


def text_to_button(msg, color, buttonx, buttony, buttonwidth, buttonheight, size = "medium"):
    textSurf,textRect = text_objects(msg,color,size)
    textRect.center = ((buttonx+(buttonwidth/2)), buttony+(buttonheight/2))
    gameDisplay.blit(textSurf,textRect)


def button(text, x, y, width, height, inactive_color, active_color, text_color = black, action = None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(gameDisplay, active_color, (x,y,width,height))
        if click[0] == 1 and action != None:
            if action == "quit":
                pygame.quit()
                pygame.mixer.quit()
                quit()
    else:
        pygame.draw.rect(gameDisplay, inactive_color, (x, y, width, height))

    text_to_button(text,text_color,x,y,width,height)

# Do not use this function
def find(name):
    findNum = True
    for root in os.walk("C:/"):
        print("Searching ...", root)
        print("Looking for "+ name)
        if name in root:
            print(root)
            findNum = False
    if findNum:
        for root, dirs, files in os.walk("D:/"):
            print("Searching ...", root)
            print("Looking for" + name)
            if name in root:
                print(root)
                findNum = False
        if findNum:
            for root, dirs, files in os.walk("E:/"):
                print("Searching ...", root)
                print("Looking for" + name)
                if name in root:
                    print(root)



def img_button(text, x, y, width, height, img_active, img_inactive, img_choice = None, action = None, text_color = black):
    global big_champ
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + width > cur[0] > x and y + height > cur[1] > y:
        img = img_active
        gameDisplay.blit(img, (x, y))
        if click[0] == 1 and action != None:
            pygame.mixer.stop()
            if action == "quit":
                pygame.quit()
                pygame.mixer.quit()
                quit()
            if action == "start":
                main()
            if action == "champ_choice":
                big_champ = img_choice
            if action == "roll":
                rolled()
            if action == "rules":
                rules()
            if action == "back":
                menu()
            if action == "create_item_set":
                find("Riot Games\\League of Legends\\Config\\Champions\\"+champion)



    else:
        img = img_inactive
        gameDisplay.blit(img, (x,y))

    if text != None:
        text_to_button(text,text_color,x,y,width,height)


def img_button_champ_map(x, y, width, height, mini_i, mini_a, big, champ = None, type = "champ",):
    global img_background
    global big_champ
    global champion

    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + width > cur[0] > x and y + height > cur[1] > y:
        img = mini_a
        gameDisplay.blit(img, (x, y))
        if click[0] == 1:
            if type == "champ":
                big_champ = big
                champion = champ
            if type == "map":
                img_background = big
    else:
        img = mini_i
        gameDisplay.blit(img, (x,y))


def rules():
    global gameDisplay
    global display_height,display_width
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.VIDEORESIZE:
                gameDisplay = pygame.display.set_mode(event.dict['size'], pygame.RESIZABLE)
                size = event.dict['size']
                display_width = size[0]
                display_height = size[1]

        wp_rules = pygame.image.load("images/rules_wp.png")

        gameDisplay.blit(pygame.transform.scale(wp_rules,(display_width,display_height)), (0, 0))

        # message_to_screen("1. Pick a champion", white, -250, -230, "medium")
        # message_to_screen("2. Pick a map", white, -100, -295, "medium")
        # message_to_screen("3. Roll!", white, 50, -370, "medium")
        # message_to_screen("4. Build your items in the given order", white, 200, 0, "medium")

        gameDisplay.blit(pygame.transform.scale(rules_text, (int(display_width/2),display_height)),(display_width/6,0))

        img_button(None, display_width/160, display_height/1.11888111888, display_width/8, display_height/10.666667, pygame.transform.scale(back_active, (int(display_width/8),int(display_height/10.666667))), pygame.transform.scale(back_inactive, (int(display_width/8),int(display_height/10.666667))), action="back")


        pygame.display.update()


def display_build(champion):
    global x_max_spell, y_max_spell, sumSpell1, sumSpell2, keystone, max_spell, buildArr
    wp = pygame.image.load("images/wp_champs_" + champion + ".png")
    #global gameDisplay
    #global display_height
    #global display_width

    gameDisplay.blit(pygame.transform.scale(image_3,(int(display_width/32),int(display_height/16))), (display_width/2.06451612903, display_height/2.13333333333))
    pygame.display.update()
    time.sleep(1)
    gameDisplay.blit(pygame.transform.scale(wp,(display_width,display_height)), (0, 0))

    gameDisplay.blit(pygame.transform.scale(image_2, (int(display_width / 32), int(display_height / 16))),(display_width / 2.06451612903, display_height / 2.13333333333))
    pygame.display.update()
    time.sleep(1)
    gameDisplay.blit(pygame.transform.scale(wp, (display_width, display_height)), (0, 0))

    gameDisplay.blit(pygame.transform.scale(image_1, (int(display_width / 32), int(display_height / 16))),(display_width / 2.06451612903, display_height / 2.13333333333))
    pygame.display.update()
    time.sleep(1)
    gameDisplay.blit(pygame.transform.scale(wp, (display_width, display_height)), (0, 0))




    champ_select_sound = pygame.mixer.Sound("sounds/sounds_champions_" + champion + ".wav")
    champ_select_sound.play()

    if img_background == img_background_summoner:
        map = "Summoner's Rift"
    elif img_background == img_background_howling:
        map = "Howling Abyss"
    elif img_background == img_background_twisted:
        map = "Twisted Treeline"

    #Summoner Spells
    sumSpellArr = ["Flash", "Ignite", "Teleport", "Ghost", "Barrier", "Cleanse", "Heal", "Smite", "Exhaust", "Mark", "Clarity"]

    if map == "Summoner's Rift":
        sumSpellArr.remove("Mark")
        sumSpellArr.remove("Clarity")

    elif map == "Twisted Treeline":
        sumSpellArr.remove("Mark")
        sumSpellArr.remove("Clarity")

    elif map == "Howling Abyss":
        sumSpellArr.remove("Teleport")
        sumSpellArr.remove("Smite")

    randnum = random.randint(0,len(sumSpellArr)-1)
    sumSpell1 = sumSpellArr[randnum]
    sumSpellArr.remove(sumSpell1)
    randnum = random.randint(0, len(sumSpellArr)-1)
    sumSpell2 = sumSpellArr[randnum]

    #Max ability
    if champion == "Udyr":
        maxArr = ["Q", "W", "E", "R"]
    else:
        maxArr = ["Q", "W", "E"]

    randnum = random.randint(0, len(maxArr)-1)
    max_spell = maxArr[randnum]


    #Keystone
    keystoneArr = ["Warlord's Bloodlust", "Fervor of Battle", "Deathfire Touch", "Stormraider's Surge",
                   "Thunderlord's Decree", "Windspeaker's Blessing", "Grasp of the Undying", "Courage of the Colossus",
                   "Bond of Stone"]

    randnum = random.randint(0, len(keystoneArr)-1)

    keystone = keystoneArr[randnum]

    itemsArr = ["Rabadon's_Deathcap","Trinity_Force","Mercurial_Scimitar","The_Bloodthirster","Essence_Reaver",
                "Infinity_Edge","Death's_Dance","Titanic_Hydra","Ravenous_Hydra","Zhonya's_Hourglass","The_Black_Cleaver",
                "Blade_Of_The_Ruined_King","Hextech_Gunblade","Maw_Of_Malmortius","Duskblade_Of_Draktharr","Luden's_Echo",
                "Liandry's_Torment","Youmuu's_Ghostblade","Rylai's_Crystal_Scepter","Lich_Bane","Frozen_Mallet","Seraph's_Embrace",
                "Nashor's_Tooth","Rod_Of_Ages","Dead_Man's_Plate","Randuin's_Omen","Banshee's_Veil","Banner_Of_Command",
                "Warmog's_Armor","Guinsoo's_Rageblade","Frozen_Heart","Wit's_End","Spirit_Visage","Athene's_Unholy_Grail",
                "Sunfire_Cape","Sterak's_Gage","Lord_Dominik's_Regards","Mortal_Reminder","Iceborn_Gauntlet","Void_Staff",
                "Righteous_Glory","Rapid_Firecannon","Statikk_Shiv","Runaan's_Hurricane","Phantom_Dancer",
                "Locket_Of_The_Iron_Solari","Morellonomicon","Muramana","Thornmail","Abyssal_Scepter","Zeke's_Harbinger",
                "Mikael's_Crucible","Hextech_Protobelt-01","Hextech_GLP-800","Ardent_Censer","Guardian_Angel",
                "Mejai's_Soulstealer","Zz'Rot_Portal","Ohmwrecker","Edge_of_Night",
                "Knight's_Vow","Lord_Van_Damm's_Pillager","Moonflair_Spellblade","Redemption","Wooglet's_Witchcap"]
    global buildArr

    machetesArr = ["Skirmisher's_Sabre", "Stalker's_Blade", "Tracker's_Knife"]
    enchantsArr = ["Cinderhulk", "Bloodrazor", "Runic_Echoes", "Warrior"]

    bootsArr = ["Sorcerer's_Shoes", "Berserker's_Greaves", "Boots_of_Mobility", "Ionian_Boots_of_Lucidity", "Mercury's_Treads",
                "Ninja_Tabi"]

    itemSupArr = ["Eye_of_the_Equinox","Eye_of_the_Oasis",
                  "Eye_of_the_Watchers","Frost_Queen's_Claim","Face_of_the_Mountain","Talisman_of_Ascension"]

    global aram
    aram = False
    global supItemTest
    supItemTest = False

    if map == "Summoner's Rift":
        itemsArr.remove("Lord_Van_Damm's_Pillager")
        itemsArr.remove("Moonflair_Spellblade")
        itemsArr.remove("Wooglet's_Witchcap")

        randSup = random.randint(1,len(itemsArr))
        if randSup < 7:
            supItemTest = True

    elif map == "Twisted Treeline":
        itemSupArr.remove("Eye_of_the_Equinox")
        itemSupArr.remove("Eye_of_the_Oasis")
        itemSupArr.remove("Eye_of_the_Watchers")
        itemsArr.remove("Ohmwrecker")
        itemsArr.remove("Zz'Rot_Portal")
        itemsArr.remove("Mejai's_Soulstealer")
        machetesArr.remove("Tracker's_Knife")

        randSup = random.randint(1, len(itemsArr))
        if randSup < 4:
            supItemTest = True

    elif map == "Howling Abyss":
        itemSupArr.remove("Eye_of_the_Equinox")
        itemSupArr.remove("Eye_of_the_Oasis")
        itemSupArr.remove("Eye_of_the_Watchers")
        itemsArr.remove("Ohmwrecker")
        itemsArr.remove("Zz'Rot_Portal")
        itemsArr.remove("Guardian_Angel")
        itemsArr.remove("Lord_Van_Damm's_Pillager")
        itemsArr.remove("Moonflair_Spellblade")
        itemsArr.remove("Wooglet's_Witchcap")
        itemsArr.remove("Mejai's_Soulstealer")

        randSup = random.randint(1, len(itemsArr))
        if randSup < 4:
            supItemTest = True

        aram = True

    if champion in {"Aatrox" ,"Akali" ,"Alistar" ,"Amumu" ,"Blitzcrank" ,"Braum" ,"Camille" ,"Chogath" ,"Darius" ,"Diana" ,"DrMundo" ,"Ekko" ,"Evelynn" ,"Fiora" ,"Fizz" ,"Galio" ,"Gangplank" ,"Garen" ,"Gragas" ,"Hecarim" ,"Illaoi" ,"Irelia" ,"JarvanIV" ,"Jax" ,"Kassadin" ,"Katarina" ,"Khazix" ,"Kled" ,"LeeSin" ,"Leona" ,"Malphite" ,"Maokai" ,"MasterYi" ,"Mordekaiser" ,"Nasus" ,"Nautilus" ,"Nocturne" ,"Nunu" ,"Olaf" ,"Pantheon" ,"Poppy" ,"Rammus" ,"RekSai" ,"Renekton" ,"Rengar" ,"Riven" ,"Rumble" ,"Sejuani" ,"Shaco" ,"Shen" ,"Shyvana" ,"Singed" ,"Sion" ,"Skarner" ,"TahmKench" ,"Talon" ,"Taric" ,"Trundle" ,"Tryndamere" ,"Udyr" ,"Vi" ,"Volibear" ,"Warwick" ,"Wukong" ,"XinZhao" ,"Yasuo" ,"Yorick" ,"Zac" ,"Zed"}:
        itemsArr.remove("Runaan's_Hurricane")
    elif champion in {"Ahri" ,"Anivia" ,"Annie" ,"Ashe" ,"AurelionSol" ,"Azir" ,"Bard" ,"Brand" ,"Caitlyn" ,"Corki" ,"Draven" ,"Ezreal" ,"FiddleSticks" ,"Graves" ,"Heimerdinger" ,"Janna" ,"Jhin" ,"Jinx" ,"Kalista" ,"Karma" ,"Karthus" ,"Kennen" ,"Kindred" ,"KogMaw" ,"Leblanc" ,"Lissandra" ,"Lucian" ,"Lulu" ,"Lux" ,"Malzahar" ,"MissFortune" ,"Morgana" ,"Nami" ,"Orianna" ,"Quinn" ,"Ryze" ,"Sivir" ,"Sona" ,"Soraka" ,"Swain" ,"Syndra" ,"Taliyah" ,"Teemo" ,"Thresh" ,"Tristana" ,"TwistedFate" ,"Twitch" ,"Urgot" ,"Varus" ,"Vayne" ,"Veigar" ,"VelKoz" ,"Vladimir" ,"Xerath" ,"Ziggs" ,"Zilean" ,"Zyra"}:
        itemsArr.remove("Ravenous_Hydra")
        itemsArr.remove("Titanic_Hydra")

    buildArr = []


    for i in range(6):
        randnum = random.randint(0, len(itemsArr)-1)
        appendItem = itemsArr[randnum]


        buildArr.append(appendItem)

    randnum = random.randint(0, len(enchantsArr) - 1)
    enchant = enchantsArr[randnum]
    randnum = random.randint(0, len(machetesArr)-1)
    mach = machetesArr[randnum]

    machete = mach + "_(" + enchant + ")"

    randnum = random.randint(0, len(bootsArr)-1)
    boots = bootsArr[randnum]

    randnum = random.randint(0, len(itemSupArr)-1)
    supItem = itemSupArr[randnum]

    if champion == "Cassiopeia":
        if sumSpell1 == "Smite" or sumSpell2 == "Smite":
            buildArr[0] = machete
            if supItemTest:
                randNumSup = random.randint(1, 5)
                buildArr[randNumSup] = supItem

                supItemTest = False
        if supItemTest:
            randNumSup = random.randint(0, 5)
            buildArr[randNumSup] = supItem
    elif champion == "Viktor":
        buildArr[0] = boots
        buildArr[1] = "Perfect_Hex_Core"
        if sumSpell1 == "Smite" or sumSpell2 == "Smite":
            buildArr[2] = machete
            if supItemTest:
                randNumSup = random.randint(3, 5)
                buildArr[randNumSup] = supItem
                supItemTest = False
        if supItemTest:
            randNumSup = random.randint(2, 5)
            buildArr[randNumSup] = supItem
    else:
        buildArr[0] = boots
        if sumSpell1 == "Smite" or sumSpell2 == "Smite":
            buildArr[1] = machete
            if supItemTest:
                randNumSup = random.randint(2,5)
                buildArr[randNumSup] = supItem
                supItemTest = False
        if supItemTest:
            randNumSup = random.randint(1, 5)
            buildArr[randNumSup] = supItem

    #ITEMS
    x_max_spell = display_width/1.07382550336
    y_max_spell = display_height/1.15942028986

    gameDisplay.blit(pygame.transform.scale(wp, (display_width, display_height)), (0, 0))
    gameDisplay.blit(pygame.transform.scale(pygame.image.load("images/abilities_" + max_spell + "_" + champion + ".png"),
                                            (int(display_width / 16), int(display_height / 8))),
                     (display_width / 1.07382550336, display_height / 1.15942028986))

    gameDisplay.blit(pygame.transform.scale(pygame.image.load("images/" + max_spell + ".png"),
                                            (int(display_width / 72.7272727273), int(display_height / 36.3636363636))),
                     (display_width / 1.07382550336, display_height / 1.15942028986))

    gameDisplay.blit(pygame.transform.scale(pygame.image.load("images/" + sumSpell1 + ".png"),
                                            (int(display_width / 16), int(display_height / 8))),
                     (display_width / 160, display_height / 1.37931034483))
    gameDisplay.blit(pygame.transform.scale(pygame.image.load("images/" + sumSpell2 + ".png"),
                                            (int(display_width / 16), int(display_height / 8))),
                     (display_width / 160, display_height / 1.15942028986))

    gameDisplay.blit(pygame.transform.scale(pygame.image.load("images/" + buildArr[0] + ".png"),
                                            (int(display_width / 7.61904762), int(display_height / 3.80952380952))),
                     (display_width / 13.3333333333, display_height / 1.37931034483))
    gameDisplay.blit(
        pygame.transform.scale(pygame.image.load("images/1.png"), (int(display_width / 32), int(display_height / 16))),
        (display_width / 14.5454545455, display_height / 1.37931034483))
    gameDisplay.blit(pygame.transform.scale(pygame.image.load("images/" + buildArr[1] + ".png"),
                                            (int(display_width / 7.61904762), int(display_height / 3.80952380952))),
                     (display_width / 4.57142857143, display_height / 1.37931034483))
    gameDisplay.blit(
        pygame.transform.scale(pygame.image.load("images/2.png"), (int(display_width / 32), int(display_height / 16))),
        (display_width / 4.70588235294, display_height / 1.37931034483))
    gameDisplay.blit(pygame.transform.scale(pygame.image.load("images/" + buildArr[2] + ".png"),
                                            (int(display_width / 7.61904762), int(display_height / 3.80952380952))),
                     (display_width / 2.75862068966, display_height / 1.37931034483))
    gameDisplay.blit(
        pygame.transform.scale(pygame.image.load("images/3.png"), (int(display_width / 32), int(display_height / 16))),
        (display_width / 2.80701754386, display_height / 1.37931034483))
    gameDisplay.blit(pygame.transform.scale(pygame.image.load("images/" + buildArr[3] + ".png"),
                                            (int(display_width / 7.61904762), int(display_height / 3.80952380952))),
                     (display_width / 1.97530864198, display_height / 1.37931034483))
    gameDisplay.blit(
        pygame.transform.scale(pygame.image.load("images/4.png"), (int(display_width / 32), int(display_height / 16))),
        (display_width / 1.98757763975, display_height / 1.37931034483))
    gameDisplay.blit(pygame.transform.scale(pygame.image.load("images/" + buildArr[4] + ".png"),
                                            (int(display_width / 7.61904762), int(display_height / 3.80952380952))),
                     (display_width / 1.53846153846, display_height / 1.37931034483))
    gameDisplay.blit(
        pygame.transform.scale(pygame.image.load("images/5.png"), (int(display_width / 32), int(display_height / 16))),
        (display_width / 1.55339805825, display_height / 1.37931034483))
    gameDisplay.blit(pygame.transform.scale(pygame.image.load("images/" + buildArr[5] + ".png"),
                                            (int(display_width / 7.61904762), int(display_height / 3.80952380952))),
                     (display_width / 1.25984251969, display_height / 1.37931034483))
    gameDisplay.blit(
        pygame.transform.scale(pygame.image.load("images/6.png"), (int(display_width / 32), int(display_height / 16))),
        (display_width / 1.26984126984, display_height / 1.37931034483))

    gameDisplay.blit(pygame.transform.scale(pygame.image.load("images/" + keystone + ".png"),
                                            (int(display_width / 16), int(display_height / 8))),
                     (display_width / 1.07382550336, display_height / 1.37931034483))


    pygame.display.update()



def menu():
    global gameDisplay
    global display_width
    global display_height

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.VIDEORESIZE:
                gameDisplay = pygame.display.set_mode(event.dict['size'], pygame.RESIZABLE)
                size = event.dict['size']
                display_width = size[0]
                display_height = size[1]

        gameDisplay.blit(pygame.transform.scale(img_background_start, (display_width,display_height)), (0, 0))
        gameDisplay.blit(pygame.transform.scale(img_title,(int(display_width),int(display_height/4))), (0, 0))


        img_button (None,
                    display_width/1.39130434783,
                    display_height/1.14285714286,
                    display_width / 8,
                    display_height/10.6666666667,
                    pygame.transform.scale(img_rules_active,(int(display_width/8),int(display_height / 10.66666666678))),
                    pygame.transform.scale(img_rules_inactive,(int(display_width / 8), int(display_height / 10.66666666678))),
                    action = "rules")
        img_button(None,
                   display_width/1.16363636364,
                   display_height/1.14285714286,
                   display_width / 8,
                   display_height/10.6666666667,
                   pygame.transform.scale(img_quit_active,(int(display_width / 8), int(display_height / 10.66666666678))),
                   pygame.transform.scale(img_quit_inactive,(int(display_width / 8), int(display_height / 10.66666666678))),
                   action="quit")
        img_button(None,
                   display_width/2.66666666667,
                   display_height/2.46153846154,
                   display_width / 4,
                   display_height/5.33333333333,
                   pygame.transform.scale(img_playnow_active,(int(display_width / 4), int(display_height / 5.33333333333))),
                   pygame.transform.scale(img_playnow_inactive,(int(display_width / 4), int(display_height / 5.33333333333))),
                   None,
                   action="start")

        pygame.display.update()
        clock.tick(30)

def main():
    global champion
    global gameDisplay
    global display_width
    global display_height
    global championArr
    champion = "Random"


    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.VIDEORESIZE:
                gameDisplay = pygame.display.set_mode(event.dict['size'], pygame.RESIZABLE)
                size = event.dict['size']
                display_width = size[0]
                display_height = size[1]

        gameDisplay.blit(pygame.transform.scale(img_background,(display_width,display_height)), (0, 0))
        size_b_w = int(display_width / 6.4)
        size_b_h = int(display_height / 3.2)
        if champion == "Random":
            gameDisplay.blit(pygame.transform.scale(b_Random, (size_b_w, size_b_h)), (display_width/1.68421052632, display_height/1.52380952381))
        else:
            gameDisplay.blit(pygame.transform.scale(big_champ, (size_b_w, size_b_h)), (display_width/1.68421052632, display_height/1.52380952381))

        for i in range(1):

            img_button_champ_map(display_width/1.18518518519, display_height/2.66666666667, display_width/8, display_height/4, pygame.transform.scale(img_howling_abyss_inactive,(int(display_width/8), int(display_height/4))), pygame.transform.scale(img_howling_abyss_active,(int(display_width/8), int(display_height/4))),
                                 img_background_howling, type="map")
            img_button_champ_map(display_width/1.18518518519, display_height/16, display_width/8, display_height/4, pygame.transform.scale(img_summoner_inactive,(int(display_width/8), int(display_height/4))),pygame.transform.scale(img_summoner_active,(int(display_width/8), int(display_height/4))),
                                 img_background_summoner, type="map")
            img_button_champ_map(display_width/1.18518518519, display_height/1.45454545455, display_width/8, display_height/4, pygame.transform.scale(img_twisted_inactive,(int(display_width/8), int(display_height/4))), pygame.transform.scale(img_twisted_active,(int(display_width/8),int(display_height/4))),
                                 img_background_twisted, type="map")
            champArr = ["Aatrox", "Ahri", "Akali", "Alistar", "Amumu", "Anivia", "Annie", "Ashe", "AurelionSol",
                        "Azir", "Bard", "Blitzcrank", "Brand", "Braum", "Caitlyn", "Cassiopeia", "Chogath",
                        "Corki", "Darius", "Diana", "DrMundo", "Draven", "Ekko",
                        "Elise", "Evelynn", "Ezreal", "FiddleSticks", "Fiora", "Fizz", "Galio", "Gangplank",
                        "Garen", "Gnar", "Gragas", "Graves", "Hecarim", "Heimerdinger", "Illaoi", "Irelia",
                        "Janna", "JarvanIV", "Jax", "Jayce", "Jhin",
                        "Jinx", "Kalista", "Karma", "Karthus", "Kassadin", "Katarina", "Kayle", "Kennen",
                        "Khazix", "Kindred", "Kled", "KogMaw", "Leblanc", "LeeSin", "Leona", "Lissandra",
                        "Lucian", "Lulu", "Lux", "Malphite", "Malzahar", "Maokai",
                        "MasterYi", "MissFortune", "Mordekaiser", "Morgana", "Nami", "Nasus", "Nautilus",
                        "Nidalee", "Nocturne", "Nunu", "Olaf", "Orianna", "Pantheon", "Poppy", "Quinn",
                        "Rammus", "RekSai", "Renekton", "Rengar", "Riven",
                        "Rumble", "Ryze", "Sejuani", "Shaco", "Shen", "Shyvana", "Singed", "Sion", "Sivir",
                        "Skarner", "Sona", "Soraka", "Swain", "Syndra", "TahmKench", "Taliyah", "Talon",
                        "Taric", "Teemo", "Thresh", "Tristana", "Trundle", "Tryndamere",
                        "TwistedFate", "Twitch", "Udyr", "Urgot", "Varus", "Vayne", "Veigar", "Velkoz", "Vi",
                        "Viktor", "Vladimir", "Volibear", "Warwick", "Wukong", "Xerath", "XinZhao",
                        "Yasuo", "Yorick", "Zac", "Zed", "Ziggs", "Zilean", "Zyra", "Camille", "Ivern"]
            size_mini_w = int(display_width/32)
            size_mini_h = int(display_height/16)


            #for champ in champArr:


            # pygame.transform.scale(pygame.Surface("m_" + champ + "_i"), (size_mini,10))
            img_button_champ_map(display_width / 160, display_height / 80, size_mini_w, size_mini_h,
                                 pygame.transform.scale(m_Aatrox_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Aatrox_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Aatrox, (size_b_w, size_b_h)), 'Aatrox')
            img_button_champ_map(display_width / 22.8571428571, display_height / 80, size_mini_w, size_mini_h,
                                 pygame.transform.scale(m_Ahri_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Ahri_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Ahri, (size_b_w, size_b_h)), 'Ahri')
            img_button_champ_map(display_width / 12.3076923077, display_height / 80, size_mini_w, size_mini_h,
                                 pygame.transform.scale(m_Akali_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Akali_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Akali, (size_b_w, size_b_h)), 'Akali')
            img_button_champ_map(display_width / 8.42105263158, display_height / 80, size_mini_w, size_mini_h,
                                 pygame.transform.scale(m_Alistar_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Alistar_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Alistar, (size_b_w, size_b_h)), 'Alistar')
            img_button_champ_map(display_width / 6.4, display_height / 80, size_mini_w, size_mini_h,
                                 pygame.transform.scale(m_Amumu_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Amumu_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Amumu, (size_b_w, size_b_h)), 'Amumu')
            img_button_champ_map(display_width / 5.16129032258, display_height / 80, size_mini_w, size_mini_h,
                                 pygame.transform.scale(m_Anivia_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Anivia_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Anivia, (size_b_w, size_b_h)), 'Anivia')
            img_button_champ_map(display_width / 4.32432432432, display_height / 80, size_mini_w, size_mini_h,
                                 pygame.transform.scale(m_Annie_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Annie_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Annie, (size_b_w, size_b_h)), 'Annie')
            img_button_champ_map(display_width / 3.72093023256, display_height / 80, size_mini_w, size_mini_h,
                                 pygame.transform.scale(m_Ashe_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Ashe_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Ashe, (size_b_w, size_b_h)), 'Ashe')
            img_button_champ_map(display_width / 3.26530612245, display_height / 80, size_mini_w, size_mini_h,
                                 pygame.transform.scale(m_AurelionSol_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_AurelionSol_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_AurelionSol, (size_b_w, size_b_h)), 'AurelionSol')
            img_button_champ_map(display_width / 2.90909090909, display_height / 80, size_mini_w, size_mini_h,
                                 pygame.transform.scale(m_Azir_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Azir_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Azir, (size_b_w, size_b_h)), 'Azir')
            img_button_champ_map(display_width / 2.62295081967, display_height / 80, size_mini_w, size_mini_h,
                                 pygame.transform.scale(m_Bard_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Bard_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Bard, (size_b_w, size_b_h)), 'Bard')
            img_button_champ_map(display_width / 2.38805970149, display_height / 80, size_mini_w, size_mini_h,
                                 pygame.transform.scale(m_Blitzcrank_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Blitzcrank_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Blitzcrank, (size_b_w, size_b_h)), 'Blitzcrank')
            img_button_champ_map(display_width / 2.19178082192, display_height / 80, size_mini_w, size_mini_h,
                                 pygame.transform.scale(m_Brand_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Brand_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Brand, (size_b_w, size_b_h)), 'Brand')
            img_button_champ_map(display_width / 160, display_height / 11.4285714286, size_mini_w, size_mini_h,
                                 pygame.transform.scale(m_Braum_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Braum_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Braum, (size_b_w, size_b_h)), 'Braum')
            img_button_champ_map(display_width / 22.8571428571, display_height / 11.4285714286, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Caitlyn_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Caitlyn_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Caitlyn, (size_b_w, size_b_h)), 'Caitlyn')
            img_button_champ_map(display_width / 12.3076923077, display_height / 11.4285714286, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Cassiopeia_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Cassiopeia_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Cassiopeia, (size_b_w, size_b_h)), 'Cassiopeia')
            img_button_champ_map(display_width / 8.42105263158, display_height / 11.4285714286, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Chogath_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Chogath_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Chogath, (size_b_w, size_b_h)), 'Chogath')
            img_button_champ_map(display_width / 6.4, display_height / 11.4285714286, size_mini_w, size_mini_h,
                                 pygame.transform.scale(m_Corki_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Corki_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Corki, (size_b_w, size_b_h)), 'Corki')
            img_button_champ_map(display_width / 5.16129032258, display_height / 11.4285714286, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Darius_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Darius_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Darius, (size_b_w, size_b_h)), 'Darius')
            img_button_champ_map(display_width / 4.32432432432, display_height / 11.4285714286, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Diana_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Diana_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Diana, (size_b_w, size_b_h)), 'Diana')
            img_button_champ_map(display_width / 3.72093023256, display_height / 11.4285714286, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_DrMundo_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_DrMundo_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_DrMundo, (size_b_w, size_b_h)), 'DrMundo')
            img_button_champ_map(display_width / 3.26530612245, display_height / 11.4285714286, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Draven_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Draven_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Draven, (size_b_w, size_b_h)), 'Draven')
            img_button_champ_map(display_width / 2.90909090909, display_height / 11.4285714286, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Ekko_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Ekko_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Ekko, (size_b_w, size_b_h)), 'Ekko')
            img_button_champ_map(display_width / 2.62295081967, display_height / 11.4285714286, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Elise_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Elise_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Elise, (size_b_w, size_b_h)), 'Elise')
            img_button_champ_map(display_width / 2.38805970149, display_height / 11.4285714286, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Evelynn_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Evelynn_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Evelynn, (size_b_w, size_b_h)), 'Evelynn')
            img_button_champ_map(display_width / 2.19178082192, display_height / 11.4285714286, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Ezreal_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Ezreal_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Ezreal, (size_b_w, size_b_h)), 'Ezreal')
            img_button_champ_map(display_width / 160, display_height / 6.15384615385, size_mini_w, size_mini_h,
                                 pygame.transform.scale(m_FiddleSticks_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_FiddleSticks_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_FiddleSticks, (size_b_w, size_b_h)), 'FiddleSticks')
            img_button_champ_map(display_width / 22.8571428571, display_height / 6.15384615385, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Fiora_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Fiora_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Fiora, (size_b_w, size_b_h)), 'Fiora')
            img_button_champ_map(display_width / 12.3076923077, display_height / 6.15384615385, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Fizz_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Fizz_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Fizz, (size_b_w, size_b_h)), 'Fizz')
            img_button_champ_map(display_width / 8.42105263158, display_height / 6.15384615385, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Galio_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Galio_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Galio, (size_b_w, size_b_h)), 'Galio')
            img_button_champ_map(display_width / 6.4, display_height / 6.15384615385, size_mini_w, size_mini_h,
                                 pygame.transform.scale(m_Gangplank_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Gangplank_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Gangplank, (size_b_w, size_b_h)), 'Gangplank')
            img_button_champ_map(display_width / 5.16129032258, display_height / 6.15384615385, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Garen_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Garen_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Garen, (size_b_w, size_b_h)), 'Garen')
            img_button_champ_map(display_width / 4.32432432432, display_height / 6.15384615385, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Gnar_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Gnar_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Gnar, (size_b_w, size_b_h)), 'Gnar')
            img_button_champ_map(display_width / 3.72093023256, display_height / 6.15384615385, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Gragas_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Gragas_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Gragas, (size_b_w, size_b_h)), 'Gragas')
            img_button_champ_map(display_width / 3.26530612245, display_height / 6.15384615385, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Graves_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Graves_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Graves, (size_b_w, size_b_h)), 'Graves')
            img_button_champ_map(display_width / 2.90909090909, display_height / 6.15384615385, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Hecarim_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Hecarim_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Hecarim, (size_b_w, size_b_h)), 'Hecarim')
            img_button_champ_map(display_width / 2.62295081967, display_height / 6.15384615385, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Heimerdinger_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Heimerdinger_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Heimerdinger, (size_b_w, size_b_h)), 'Heimerdinger')
            img_button_champ_map(display_width / 2.38805970149, display_height / 6.15384615385, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Illaoi_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Illaoi_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Illaoi, (size_b_w, size_b_h)), 'Illaoi')
            img_button_champ_map(display_width / 2.19178082192, display_height / 6.15384615385, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Irelia_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Irelia_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Irelia, (size_b_w, size_b_h)), 'Irelia')
            img_button_champ_map(display_width / 160, display_height / 4.21052631579, size_mini_w, size_mini_h,
                                 pygame.transform.scale(m_Janna_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Janna_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Janna, (size_b_w, size_b_h)), 'Janna')
            img_button_champ_map(display_width / 22.8571428571, display_height / 4.21052631579, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_JarvanIV_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_JarvanIV_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_JarvanIV, (size_b_w, size_b_h)), 'JarvanIV')
            img_button_champ_map(display_width / 12.3076923077, display_height / 4.21052631579, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Jax_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Jax_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Jax, (size_b_w, size_b_h)), 'Jax')
            img_button_champ_map(display_width / 8.42105263158, display_height / 4.21052631579, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Jayce_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Jayce_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Jayce, (size_b_w, size_b_h)), 'Jayce')
            img_button_champ_map(display_width / 6.4, display_height / 4.21052631579, size_mini_w, size_mini_h,
                                 pygame.transform.scale(m_Jhin_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Jhin_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Jhin, (size_b_w, size_b_h)), 'Jhin')
            img_button_champ_map(display_width / 5.16129032258, display_height / 4.21052631579, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Jinx_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Jinx_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Jinx, (size_b_w, size_b_h)), 'Jinx')
            img_button_champ_map(display_width / 4.32432432432, display_height / 4.21052631579, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Kalista_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Kalista_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Kalista, (size_b_w, size_b_h)), 'Kalista')
            img_button_champ_map(display_width / 3.72093023256, display_height / 4.21052631579, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Karma_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Karma_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Karma, (size_b_w, size_b_h)), 'Karma')
            img_button_champ_map(display_width / 3.26530612245, display_height / 4.21052631579, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Karthus_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Karthus_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Karthus, (size_b_w, size_b_h)), 'Karthus')
            img_button_champ_map(display_width / 2.90909090909, display_height / 4.21052631579, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Kassadin_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Kassadin_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Kassadin, (size_b_w, size_b_h)), 'Kassadin')
            img_button_champ_map(display_width / 2.62295081967, display_height / 4.21052631579, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Katarina_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Katarina_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Katarina, (size_b_w, size_b_h)), 'Katarina')
            img_button_champ_map(display_width / 2.38805970149, display_height / 4.21052631579, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Kayle_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Kayle_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Kayle, (size_b_w, size_b_h)), 'Kayle')
            img_button_champ_map(display_width / 2.19178082192, display_height / 4.21052631579, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Kennen_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Kennen_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Kennen, (size_b_w, size_b_h)), 'Kennen')
            img_button_champ_map(display_width / 160, display_height / 3.2, size_mini_w, size_mini_h,
                                 pygame.transform.scale(m_Khazix_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Khazix_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Khazix, (size_b_w, size_b_h)), 'Khazix')
            img_button_champ_map(display_width / 22.8571428571, display_height / 3.2, size_mini_w, size_mini_h,
                                 pygame.transform.scale(m_Kindred_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Kindred_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Kindred, (size_b_w, size_b_h)), 'Kindred')
            img_button_champ_map(display_width / 12.3076923077, display_height / 3.2, size_mini_w, size_mini_h,
                                 pygame.transform.scale(m_Kled_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Kled_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Kled, (size_b_w, size_b_h)), 'Kled')
            img_button_champ_map(display_width / 8.42105263158, display_height / 3.2, size_mini_w, size_mini_h,
                                 pygame.transform.scale(m_KogMaw_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_KogMaw_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_KogMaw, (size_b_w, size_b_h)), 'KogMaw')
            img_button_champ_map(display_width / 6.4, display_height / 3.2, size_mini_w, size_mini_h,
                                 pygame.transform.scale(m_Leblanc_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Leblanc_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Leblanc, (size_b_w, size_b_h)), 'Leblanc')
            img_button_champ_map(display_width / 5.16129032258, display_height / 3.2, size_mini_w, size_mini_h,
                                 pygame.transform.scale(m_LeeSin_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_LeeSin_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_LeeSin, (size_b_w, size_b_h)), 'LeeSin')
            img_button_champ_map(display_width / 4.32432432432, display_height / 3.2, size_mini_w, size_mini_h,
                                 pygame.transform.scale(m_Leona_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Leona_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Leona, (size_b_w, size_b_h)), 'Leona')
            img_button_champ_map(display_width / 3.72093023256, display_height / 3.2, size_mini_w, size_mini_h,
                                 pygame.transform.scale(m_Lissandra_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Lissandra_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Lissandra, (size_b_w, size_b_h)), 'Lissandra')
            img_button_champ_map(display_width / 3.26530612245, display_height / 3.2, size_mini_w, size_mini_h,
                                 pygame.transform.scale(m_Lucian_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Lucian_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Lucian, (size_b_w, size_b_h)), 'Lucian')
            img_button_champ_map(display_width / 2.90909090909, display_height / 3.2, size_mini_w, size_mini_h,
                                 pygame.transform.scale(m_Lulu_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Lulu_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Lulu, (size_b_w, size_b_h)), 'Lulu')
            img_button_champ_map(display_width / 2.62295081967, display_height / 3.2, size_mini_w, size_mini_h,
                                 pygame.transform.scale(m_Lux_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Lux_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Lux, (size_b_w, size_b_h)), 'Lux')
            img_button_champ_map(display_width / 2.38805970149, display_height / 3.2, size_mini_w, size_mini_h,
                                 pygame.transform.scale(m_Malphite_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Malphite_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Malphite, (size_b_w, size_b_h)), 'Malphite')
            img_button_champ_map(display_width / 2.19178082192, display_height / 3.2, size_mini_w, size_mini_h,
                                 pygame.transform.scale(m_Malzahar_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Malzahar_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Malzahar, (size_b_w, size_b_h)), 'Malzahar')
            img_button_champ_map(display_width / 160, display_height / 2.58064516129, size_mini_w, size_mini_h,
                                 pygame.transform.scale(m_Maokai_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Maokai_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Maokai, (size_b_w, size_b_h)), 'Maokai')
            img_button_champ_map(display_width / 22.8571428571, display_height / 2.58064516129, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_MasterYi_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_MasterYi_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_MasterYi, (size_b_w, size_b_h)), 'MasterYi')
            img_button_champ_map(display_width / 12.3076923077, display_height / 2.58064516129, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_MissFortune_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_MissFortune_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_MissFortune, (size_b_w, size_b_h)), 'MissFortune')
            img_button_champ_map(display_width / 8.42105263158, display_height / 2.58064516129, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Mordekaiser_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Mordekaiser_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Mordekaiser, (size_b_w, size_b_h)), 'Mordekaiser')
            img_button_champ_map(display_width / 6.4, display_height / 2.58064516129, size_mini_w, size_mini_h,
                                 pygame.transform.scale(m_Morgana_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Morgana_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Morgana, (size_b_w, size_b_h)), 'Morgana')
            img_button_champ_map(display_width / 5.16129032258, display_height / 2.58064516129, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Nami_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Nami_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Nami, (size_b_w, size_b_h)), 'Nami')
            img_button_champ_map(display_width / 4.32432432432, display_height / 2.58064516129, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Nasus_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Nasus_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Nasus, (size_b_w, size_b_h)), 'Nasus')
            img_button_champ_map(display_width / 3.72093023256, display_height / 2.58064516129, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Nautilus_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Nautilus_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Nautilus, (size_b_w, size_b_h)), 'Nautilus')
            img_button_champ_map(display_width / 3.26530612245, display_height / 2.58064516129, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Nidalee_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Nidalee_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Nidalee, (size_b_w, size_b_h)), 'Nidalee')
            img_button_champ_map(display_width / 2.90909090909, display_height / 2.58064516129, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Nocturne_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Nocturne_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Nocturne, (size_b_w, size_b_h)), 'Nocturne')
            img_button_champ_map(display_width / 2.62295081967, display_height / 2.58064516129, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Nunu_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Nunu_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Nunu, (size_b_w, size_b_h)), 'Nunu')
            img_button_champ_map(display_width / 2.38805970149, display_height / 2.58064516129, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Olaf_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Olaf_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Olaf, (size_b_w, size_b_h)), 'Olaf')
            img_button_champ_map(display_width / 2.19178082192, display_height / 2.58064516129, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Orianna_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Orianna_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Orianna, (size_b_w, size_b_h)), 'Orianna')
            img_button_champ_map(display_width / 160, display_height / 2.16216216216, size_mini_w, size_mini_h,
                                 pygame.transform.scale(m_Pantheon_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Pantheon_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Pantheon, (size_b_w, size_b_h)), 'Pantheon')
            img_button_champ_map(display_width / 22.8571428571, display_height / 2.16216216216, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Poppy_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Poppy_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Poppy, (size_b_w, size_b_h)), 'Poppy')
            img_button_champ_map(display_width / 12.3076923077, display_height / 2.16216216216, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Quinn_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Quinn_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Quinn, (size_b_w, size_b_h)), 'Quinn')
            img_button_champ_map(display_width / 8.42105263158, display_height / 2.16216216216, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Rammus_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Rammus_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Rammus, (size_b_w, size_b_h)), 'Rammus')
            img_button_champ_map(display_width / 6.4, display_height / 2.16216216216, size_mini_w, size_mini_h,
                                 pygame.transform.scale(m_RekSai_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_RekSai_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_RekSai, (size_b_w, size_b_h)), 'RekSai')
            img_button_champ_map(display_width / 5.16129032258, display_height / 2.16216216216, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Renekton_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Renekton_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Renekton, (size_b_w, size_b_h)), 'Renekton')
            img_button_champ_map(display_width / 4.32432432432, display_height / 2.16216216216, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Rengar_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Rengar_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Rengar, (size_b_w, size_b_h)), 'Rengar')
            img_button_champ_map(display_width / 3.72093023256, display_height / 2.16216216216, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Riven_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Riven_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Riven, (size_b_w, size_b_h)), 'Riven')
            img_button_champ_map(display_width / 3.26530612245, display_height / 2.16216216216, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Rumble_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Rumble_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Rumble, (size_b_w, size_b_h)), 'Rumble')
            img_button_champ_map(display_width / 2.90909090909, display_height / 2.16216216216, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Ryze_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Ryze_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Ryze, (size_b_w, size_b_h)), 'Ryze')
            img_button_champ_map(display_width / 2.62295081967, display_height / 2.16216216216, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Sejuani_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Sejuani_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Sejuani, (size_b_w, size_b_h)), 'Sejuani')
            img_button_champ_map(display_width / 2.38805970149, display_height / 2.16216216216, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Shaco_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Shaco_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Shaco, (size_b_w, size_b_h)), 'Shaco')
            img_button_champ_map(display_width / 2.19178082192, display_height / 2.16216216216, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Shen_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Shen_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Shen, (size_b_w, size_b_h)), 'Shen')
            img_button_champ_map(display_width / 160, display_height / 1.86046511628, size_mini_w, size_mini_h,
                                 pygame.transform.scale(m_Shyvana_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Shyvana_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Shyvana, (size_b_w, size_b_h)), 'Shyvana')
            img_button_champ_map(display_width / 22.8571428571, display_height / 1.86046511628, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Singed_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Singed_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Singed, (size_b_w, size_b_h)), 'Singed')
            img_button_champ_map(display_width / 12.3076923077, display_height / 1.86046511628, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Sion_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Sion_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Sion, (size_b_w, size_b_h)), 'Sion')
            img_button_champ_map(display_width / 8.42105263158, display_height / 1.86046511628, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Sivir_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Sivir_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Sivir, (size_b_w, size_b_h)), 'Sivir')
            img_button_champ_map(display_width / 6.4, display_height / 1.86046511628, size_mini_w, size_mini_h,
                                 pygame.transform.scale(m_Skarner_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Skarner_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Skarner, (size_b_w, size_b_h)), 'Skarner')
            img_button_champ_map(display_width / 5.16129032258, display_height / 1.86046511628, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Sona_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Sona_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Sona, (size_b_w, size_b_h)), 'Sona')
            img_button_champ_map(display_width / 4.32432432432, display_height / 1.86046511628, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Soraka_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Soraka_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Soraka, (size_b_w, size_b_h)), 'Soraka')
            img_button_champ_map(display_width / 3.72093023256, display_height / 1.86046511628, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Swain_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Swain_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Swain, (size_b_w, size_b_h)), 'Swain')
            img_button_champ_map(display_width / 3.26530612245, display_height / 1.86046511628, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Syndra_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Syndra_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Syndra, (size_b_w, size_b_h)), 'Syndra')
            img_button_champ_map(display_width / 2.90909090909, display_height / 1.86046511628, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_TahmKench_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_TahmKench_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_TahmKench, (size_b_w, size_b_h)), 'TahmKench')
            img_button_champ_map(display_width / 2.62295081967, display_height / 1.86046511628, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Taliyah_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Taliyah_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Taliyah, (size_b_w, size_b_h)), 'Taliyah')
            img_button_champ_map(display_width / 2.38805970149, display_height / 1.86046511628, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Talon_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Talon_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Talon, (size_b_w, size_b_h)), 'Talon')
            img_button_champ_map(display_width / 2.19178082192, display_height / 1.86046511628, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Taric_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Taric_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Taric, (size_b_w, size_b_h)), 'Taric')
            img_button_champ_map(display_width / 160, display_height / 1.63265306122, size_mini_w, size_mini_h,
                                 pygame.transform.scale(m_Teemo_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Teemo_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Teemo, (size_b_w, size_b_h)), 'Teemo')
            img_button_champ_map(display_width / 22.8571428571, display_height / 1.63265306122, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Thresh_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Thresh_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Thresh, (size_b_w, size_b_h)), 'Thresh')
            img_button_champ_map(display_width / 12.3076923077, display_height / 1.63265306122, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Tristana_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Tristana_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Tristana, (size_b_w, size_b_h)), 'Tristana')
            img_button_champ_map(display_width / 8.42105263158, display_height / 1.63265306122, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Trundle_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Trundle_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Trundle, (size_b_w, size_b_h)), 'Trundle')
            img_button_champ_map(display_width / 6.4, display_height / 1.63265306122, size_mini_w, size_mini_h,
                                 pygame.transform.scale(m_Tryndamere_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Tryndamere_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Tryndamere, (size_b_w, size_b_h)), 'Tryndamere')
            img_button_champ_map(display_width / 5.16129032258, display_height / 1.63265306122, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_TwistedFate_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_TwistedFate_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_TwistedFate, (size_b_w, size_b_h)), 'TwistedFate')
            img_button_champ_map(display_width / 4.32432432432, display_height / 1.63265306122, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Twitch_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Twitch_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Twitch, (size_b_w, size_b_h)), 'Twitch')
            img_button_champ_map(display_width / 3.72093023256, display_height / 1.63265306122, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Udyr_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Udyr_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Udyr, (size_b_w, size_b_h)), 'Udyr')
            img_button_champ_map(display_width / 3.26530612245, display_height / 1.63265306122, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Urgot_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Urgot_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Urgot, (size_b_w, size_b_h)), 'Urgot')
            img_button_champ_map(display_width / 2.90909090909, display_height / 1.63265306122, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Varus_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Varus_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Varus, (size_b_w, size_b_h)), 'Varus')
            img_button_champ_map(display_width / 2.62295081967, display_height / 1.63265306122, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Vayne_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Vayne_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Vayne, (size_b_w, size_b_h)), 'Vayne')
            img_button_champ_map(display_width / 2.38805970149, display_height / 1.63265306122, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Veigar_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Veigar_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Veigar, (size_b_w, size_b_h)), 'Veigar')
            img_button_champ_map(display_width / 2.19178082192, display_height / 1.63265306122, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Velkoz_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Velkoz_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Velkoz, (size_b_w, size_b_h)), 'Velkoz')
            img_button_champ_map(display_width / 160, display_height / 1.45454545455, size_mini_w, size_mini_h,
                                 pygame.transform.scale(m_Vi_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Vi_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Vi, (size_b_w, size_b_h)), 'Vi')
            img_button_champ_map(display_width / 22.8571428571, display_height / 1.45454545455, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Viktor_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Viktor_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Viktor, (size_b_w, size_b_h)), 'Viktor')
            img_button_champ_map(display_width / 12.3076923077, display_height / 1.45454545455, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Vladimir_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Vladimir_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Vladimir, (size_b_w, size_b_h)), 'Vladimir')
            img_button_champ_map(display_width / 8.42105263158, display_height / 1.45454545455, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Volibear_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Volibear_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Volibear, (size_b_w, size_b_h)), 'Volibear')
            img_button_champ_map(display_width / 6.4, display_height / 1.45454545455, size_mini_w, size_mini_h,
                                 pygame.transform.scale(m_Warwick_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Warwick_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Warwick, (size_b_w, size_b_h)), 'Warwick')
            img_button_champ_map(display_width / 5.16129032258, display_height / 1.45454545455, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Wukong_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Wukong_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Wukong, (size_b_w, size_b_h)), 'Wukong')
            img_button_champ_map(display_width / 4.32432432432, display_height / 1.45454545455, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Xerath_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Xerath_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Xerath, (size_b_w, size_b_h)), 'Xerath')
            img_button_champ_map(display_width / 3.72093023256, display_height / 1.45454545455, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_XinZhao_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_XinZhao_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_XinZhao, (size_b_w, size_b_h)), 'XinZhao')
            img_button_champ_map(display_width / 3.26530612245, display_height / 1.45454545455, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Yasuo_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Yasuo_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Yasuo, (size_b_w, size_b_h)), 'Yasuo')
            img_button_champ_map(display_width / 2.90909090909, display_height / 1.45454545455, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Yorick_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Yorick_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Yorick, (size_b_w, size_b_h)), 'Yorick')
            img_button_champ_map(display_width / 2.62295081967, display_height / 1.45454545455, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Zac_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Zac_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Zac, (size_b_w, size_b_h)), 'Zac')
            img_button_champ_map(display_width / 2.38805970149, display_height / 1.45454545455, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Zed_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Zed_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Zed, (size_b_w, size_b_h)), 'Zed')
            img_button_champ_map(display_width / 2.19178082192, display_height / 1.45454545455, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Ziggs_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Ziggs_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Ziggs, (size_b_w, size_b_h)), 'Ziggs')
            img_button_champ_map(display_width / 160, display_height / 1.31147540984, size_mini_w, size_mini_h,
                                 pygame.transform.scale(m_Zilean_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Zilean_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Zilean, (size_b_w, size_b_h)), 'Zilean')
            img_button_champ_map(display_width / 22.8571428571, display_height / 1.31147540984, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Zyra_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Zyra_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Zyra, (size_b_w, size_b_h)), 'Zyra')
            img_button_champ_map(display_width / 12.3076923077, display_height / 1.31147540984, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Camille_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Camille_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Camille, (size_b_w, size_b_h)), 'Camille')
            img_button_champ_map(display_width / 8.42105263158, display_height / 1.31147540984, size_mini_w,
                                 size_mini_h, pygame.transform.scale(m_Ivern_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Ivern_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Ivern, (size_b_w, size_b_h)), 'Ivern')
            img_button_champ_map(display_width / 6.4, display_height / 1.31147540984, size_mini_w, size_mini_h,
                                 pygame.transform.scale(m_Random_i, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(m_Random_a, (size_mini_w, size_mini_h)),
                                 pygame.transform.scale(b_Random, (size_b_w, size_b_h)), 'Random')

        img_button(None, display_width/4, display_height/1.23076923077, display_width/4.57142857143, display_height/8, pygame.transform.scale(letsgo_active,(int(display_width/4.57142857143),int(display_height/8))), pygame.transform.scale(letsgo_inactive,(int(display_width/4.57142857143),int(display_height/8))), action="roll")
        img_button(None, display_width/160, display_height/1.11888111888, display_width/8, display_height/10.6666666667, pygame.transform.scale(back_active,(int(display_width/8),int(display_height/10.6666666667))), pygame.transform.scale(back_inactive,(int(display_width/8),int(display_height/10.6666666667))), action="back")

        pygame.display.update()

        clock.tick(30)

def rolled():
    global champion
    global gameDisplay
    global display_width
    global display_height
    time.sleep(0.5)

    if champion == "Random":
        champArr = ["Aatrox", "Ahri", "Akali", "Alistar", "Amumu", "Anivia", "Annie", "Ashe", "AurelionSol",
                    "Azir", "Bard", "Blitzcrank", "Brand", "Braum", "Caitlyn", "Cassiopeia", "Chogath",
                    "Corki", "Darius", "Diana", "DrMundo", "Draven", "Ekko",
                    "Elise", "Evelynn", "Ezreal", "FiddleSticks", "Fiora", "Fizz", "Galio", "Gangplank",
                    "Garen", "Gnar", "Gragas", "Graves", "Hecarim", "Heimerdinger", "Illaoi", "Irelia",
                    "Janna", "JarvanIV", "Jax", "Jayce", "Jhin",
                    "Jinx", "Kalista", "Karma", "Karthus", "Kassadin", "Katarina", "Kayle", "Kennen",
                    "Khazix", "Kindred", "Kled", "KogMaw", "Leblanc", "LeeSin", "Leona", "Lissandra",
                    "Lucian", "Lulu", "Lux", "Malphite", "Malzahar", "Maokai",
                    "MasterYi", "MissFortune", "Mordekaiser", "Morgana", "Nami", "Nasus", "Nautilus",
                    "Nidalee", "Nocturne", "Nunu", "Olaf", "Orianna", "Pantheon", "Poppy", "Quinn",
                    "Rammus", "RekSai", "Renekton", "Rengar", "Riven",
                    "Rumble", "Ryze", "Sejuani", "Shaco", "Shen", "Shyvana", "Singed", "Sion", "Sivir",
                    "Skarner", "Sona", "Soraka", "Swain", "Syndra", "TahmKench", "Taliyah", "Talon",
                    "Taric", "Teemo", "Thresh", "Tristana", "Trundle", "Tryndamere",
                    "TwistedFate", "Twitch", "Udyr", "Urgot", "Varus", "Vayne", "Veigar", "Velkoz", "Vi",
                    "Viktor", "Vladimir", "Volibear", "Warwick", "Wukong", "Xerath", "XinZhao",
                    "Yasuo", "Yorick", "Zac", "Zed", "Ziggs", "Zilean", "Zyra", "Camille", "Ivern"]
        randnum = random.randint(0, len(champArr)-1)
        champion = champArr[randnum]

    wp = pygame.image.load("images/wp_champs_" + champion + ".png")

    loop = True

    gameDisplay.blit(pygame.transform.scale(wp,(display_width,display_height)), (0, 0))


    display_build(champion)

    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.VIDEORESIZE:
                gameDisplay = pygame.display.set_mode(event.dict['size'], pygame.RESIZABLE)
                size = event.dict['size']
                display_width = size[0]
                display_height = size[1]
                gameDisplay.blit(pygame.transform.scale(wp,(display_width,display_height)), (0, 0))
                gameDisplay.blit(pygame.transform.scale(pygame.image.load("images/abilities_" + max_spell + "_" + champion + ".png"),(int(display_width/16),int(display_height/8))),
                                 (display_width / 1.07382550336, display_height / 1.15942028986))

                gameDisplay.blit(pygame.transform.scale(pygame.image.load("images/" + max_spell + ".png"),(int(display_width/72.7272727273),int(display_height/36.3636363636))), (display_width / 1.07382550336, display_height / 1.15942028986))

                gameDisplay.blit(pygame.transform.scale(pygame.image.load("images/" + sumSpell1 + ".png"),(int(display_width/16),int(display_height/8))),
                                 (display_width / 160, display_height / 1.37931034483))
                gameDisplay.blit(pygame.transform.scale(pygame.image.load("images/" + sumSpell2 + ".png"),(int(display_width/16),int(display_height/8))),
                                 (display_width / 160, display_height / 1.15942028986))

                gameDisplay.blit(pygame.transform.scale(pygame.image.load("images/" + buildArr[0] + ".png"),(int(display_width/7.61904762),int(display_height/3.80952380952))), (display_width/13.3333333333, display_height/1.37931034483))
                gameDisplay.blit(pygame.transform.scale(pygame.image.load("images/1.png"),(int(display_width/32),int(display_height/16))), (display_width/14.5454545455, display_height/1.37931034483))
                gameDisplay.blit(pygame.transform.scale(pygame.image.load("images/" + buildArr[1] + ".png"),(int(display_width/7.61904762),int(display_height/3.80952380952))), (display_width/4.57142857143, display_height/1.37931034483))
                gameDisplay.blit(pygame.transform.scale(pygame.image.load("images/2.png"),(int(display_width/32),int(display_height/16))), (display_width/4.70588235294, display_height/1.37931034483))
                gameDisplay.blit(pygame.transform.scale(pygame.image.load("images/" + buildArr[2] + ".png"),(int(display_width/7.61904762),int(display_height/3.80952380952))), (display_width/2.75862068966, display_height/1.37931034483))
                gameDisplay.blit(pygame.transform.scale(pygame.image.load("images/3.png"),(int(display_width/32),int(display_height/16))), (display_width/2.80701754386, display_height/1.37931034483))
                gameDisplay.blit(pygame.transform.scale(pygame.image.load("images/" + buildArr[3] + ".png"),(int(display_width/7.61904762),int(display_height/3.80952380952))), (display_width/1.97530864198, display_height/1.37931034483))
                gameDisplay.blit(pygame.transform.scale(pygame.image.load("images/4.png"),(int(display_width/32),int(display_height/16))), (display_width/1.98757763975, display_height/1.37931034483))
                gameDisplay.blit(pygame.transform.scale(pygame.image.load("images/" + buildArr[4] + ".png"),(int(display_width/7.61904762),int(display_height/3.80952380952))), (display_width/1.53846153846, display_height/1.37931034483))
                gameDisplay.blit(pygame.transform.scale(pygame.image.load("images/5.png"),(int(display_width/32),int(display_height/16))), (display_width/1.55339805825, display_height/1.37931034483))
                gameDisplay.blit(pygame.transform.scale(pygame.image.load("images/" + buildArr[5] + ".png"),(int(display_width/7.61904762),int(display_height/3.80952380952))), (display_width/1.25984251969, display_height/1.37931034483))
                gameDisplay.blit(pygame.transform.scale(pygame.image.load("images/6.png"),(int(display_width/32),int(display_height/16))), (display_width/1.26984126984, display_height/1.37931034483))

                gameDisplay.blit(pygame.transform.scale(pygame.image.load("images/" + keystone + ".png"),(int(display_width/16),int(display_height/8))), (display_width/1.07382550336, display_height/1.37931034483))

        img_button(None, display_width/1.13798008535, display_height/80, display_width/20.7792207792, display_height/19.0476190476, pygame.transform.scale(button_reroll_active,(int(display_width/20.7792207792),int(display_height/19.0476190476))), pygame.transform.scale(button_reroll_inactive,(int(display_width/20.7792207792),int(display_height/19.0476190476))), action="roll")
        img_button(None, display_width/1.07166778299, display_height/80, display_width/16.4948453608, display_height/19.0476190476, pygame.transform.scale(settings_active,(int(display_width/16.4948453608),int(display_height/19.0476190476))), pygame.transform.scale(settings_inactive,(int(display_width/16.4948453608),int(display_height/19.0476190476))), action="start")
        #img_button(None, 0, 0, display_width/4.06091370558,display_height/13.6363636364, pygame.transform.scale(item_set_active,(int(display_width/4.06091370558),int(display_height/13.6363636364))),pygame.transform.scale(item_set_inactive,(int(display_width/4.06091370558),int(display_height/13.6363636364))), action="create_item_set")


        pygame.display.update()
        clock.tick(15)


menu()
