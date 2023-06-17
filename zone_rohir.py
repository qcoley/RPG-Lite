import drawing_functions


def rohir_river(pygame, screen, player, over_world_song_set, rohir_river_bg, dungeon_entrance, water_1, water_2,
                water_3, water_4, water_5, water_player, graphic_dict, save_check_window, user_interface,
                bar_backdrop, hp_bar, en_bar, xp_bar, font, info_text_1, info_text_2, info_text_3, info_text_4,
                in_over_world, button_highlighted, button_highlight, rohir_river_music, interaction_popup, interacted,
                equipment_screen, staff, sword, bow, npc_garan, offense_meter, defense_meter, weapon_select,
                beyond_seldon, pet_energy_window):

    if not over_world_song_set:
        pygame.mixer.music.fadeout(100)

    screen.blit(rohir_river_bg, (0, 0))
    screen.blit(equipment_screen.surf, equipment_screen.rect)
    screen.blit(offense_meter.surf, offense_meter.rect)
    screen.blit(defense_meter.surf, defense_meter.rect)
    drawing_functions.weapon_draw(player, graphic_dict, staff, sword, bow, npc_garan, weapon_select)

    screen.blit(dungeon_entrance.surf, dungeon_entrance.rect)
    screen.blit(water_1.surf, water_1.rect)
    screen.blit(water_2.surf, water_2.rect)
    screen.blit(water_3.surf, water_3.rect)
    screen.blit(water_4.surf, water_4.rect)
    screen.blit(water_5.surf, water_5.rect)
    try:
        for pet in player.pet:
            if pet.active:
                screen.blit(pet.surf, pet.rect)
    except AttributeError:
        pass
    screen.blit(player.surf, player.rect)
    drawing_functions.draw_level_up(screen, in_over_world)
    try:
        for pet in player.pet:
            if pet.active:
                pet_energy_surf = font.render(str(pet.energy) + " /100", True, "dark green", "light yellow")
                pet_energy_rect = pet_energy_surf.get_rect()
                pet_energy_rect.midleft = (345, 57)
                screen.blit(pet_energy_window.surf, pet_energy_window.rect)
                screen.blit(pet_energy_surf, pet_energy_rect)
    except AttributeError:
        pass

    if 1000 > player.x_coordinate > 270:
        player.x_coordinate -= 0.5
        player.rect.midbottom = (player.x_coordinate, player.y_coordinate)
        water_player.update(player.x_coordinate, player.y_coordinate - 5, graphic_dict["water_player"])
        screen.blit(water_player.surf, water_player.rect)

    for save_window in save_check_window:
        screen.blit(save_window.surf, save_window.rect)
    for ui_elements in user_interface:
        if len(drawing_functions.item_info_window) != 0:
            if ui_elements.name != "star power":
                screen.blit(ui_elements.surf, ui_elements.rect)
        else:
            screen.blit(ui_elements.surf, ui_elements.rect)

    screen.blit(bar_backdrop.surf, bar_backdrop.rect)
    screen.blit(hp_bar.surf, hp_bar.rect)
    screen.blit(en_bar.surf, en_bar.rect)
    screen.blit(xp_bar.surf, xp_bar.rect)

    # draw texts to the screen, like message box, player rupees and level, inv and equ updates
    drawing_functions.text_info_draw(screen, player, font, info_text_1, info_text_2, info_text_3,
                                     info_text_4, in_over_world)
    drawing_functions.draw_it(screen)

    if button_highlighted:
        screen.blit(button_highlight.surf, button_highlight.rect)

    # water movement animation -------------------------------------------------------------------------
    if 1000 > water_1.x_coordinate > 270:
        water_1.x_coordinate -= 1
        water_1.rect.midbottom = (water_1.x_coordinate, water_1.y_coordinate)
    else:
        water_1.update(900, water_1.y_coordinate, graphic_dict["water"])
    if 1000 > water_2.x_coordinate > 270:
        water_2.x_coordinate -= 1
        water_2.rect.midbottom = (water_2.x_coordinate, water_2.y_coordinate)
    else:
        water_2.update(900, water_2.y_coordinate, graphic_dict["water"])
    if 1000 > water_3.x_coordinate > 270:
        water_3.x_coordinate -= 1
        water_3.rect.midbottom = (water_3.x_coordinate, water_3.y_coordinate)
    else:
        water_3.update(900, water_3.y_coordinate, graphic_dict["water"])
    if 1000 > water_4.x_coordinate > 270:
        water_4.x_coordinate -= 1
        water_4.rect.midbottom = (water_4.x_coordinate, water_4.y_coordinate)
    else:
        water_4.update(900, water_4.y_coordinate, graphic_dict["water"])
    if 1000 > water_5.x_coordinate > 270:
        water_5.x_coordinate -= 1
        water_5.rect.midbottom = (water_5.x_coordinate, water_5.y_coordinate)
    else:
        water_5.update(900, water_5.y_coordinate, graphic_dict["water"])
    # --------------------------------------------------------------------------------------------------

    if not over_world_song_set:
        pygame.mixer.music.load(rohir_river_music)
        pygame.mixer.music.play(loops=-1)
        over_world_song_set = True

    if pygame.sprite.collide_rect(player, dungeon_entrance):
        interaction_popup.update(dungeon_entrance.x_coordinate + 40,
                                 dungeon_entrance.y_coordinate - 50,
                                 graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str(dungeon_entrance.name), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (dungeon_entrance.x_coordinate + 50,
                                        dungeon_entrance.y_coordinate - 50)
        screen.blit(interaction_info_surf, interaction_info_rect)

        # lets player know if they are in range of building they can press f to enter it
        info_text_1 = "Press 'F' key to enter dungeon.."
        info_text_2 = ""
        info_text_3 = ""
        info_text_4 = ""

        if interacted and in_over_world:
            player.current_zone = "reservoir a"
            in_over_world = True
            over_world_song_set = False
            player.x_coordinate = 525
            player.y_coordinate = 650
            player.rect = player.surf.get_rect(midbottom=(player.x_coordinate,
                                                          player.y_coordinate))
            interacted = False
            beyond_seldon = True

    rohir_return = {"over_world_song_set": over_world_song_set, "info_text_1": info_text_1, "info_text_2": info_text_2,
                    "info_text_3": info_text_3, "info_text_4": info_text_4, "in_over_world": in_over_world,
                    "interacted": interacted, "beyond seldon": beyond_seldon}

    return rohir_return
