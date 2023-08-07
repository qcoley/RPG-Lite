import gameplay_functions
import drawing_functions
import combat_scenario
import random
import time


def marrow_district(pygame, screen, graphic_dict, player, marrow_bg, over_world_song_set, marrow_music,
                    interaction_popup, font, save_check_window, user_interface, bar_backdrop, hp_bar, en_bar, xp_bar,
                    button_highlighted, button_highlight, in_over_world, interacted, info_text_1, info_text_2,
                    info_text_3, info_text_4, npc_tic, movement_able, equipment_screen, staff, sword, bow, npc_garan,
                    offense_meter, defense_meter, weapon_select, pet_energy_window, artherian, player_battle_sprite,
                    current_npc_interacting, in_npc_interaction, hearth_stone, marrow_attuned, sfx_hearth,
                    marrow_ghouls, enemy_tic, barrier_active, sharp_sense_active, ghoul_battle_sprite, in_battle,
                    current_enemy_battling, Enemy, Item, UiElement, artherian_star, noren, boro, maydria, npcs,
                    maydria_star, sub_marrow, sfx_ladder, vanished, vanish_overlay):

    if not over_world_song_set:
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.fadeout(50)
            pygame.mixer.music.load(marrow_music)
            pygame.mixer.music.play(loops=-1)
            over_world_song_set = True

    screen.blit(marrow_bg, (0, 0))
    screen.blit(equipment_screen.surf, equipment_screen.rect)
    screen.blit(offense_meter.surf, offense_meter.rect)
    screen.blit(defense_meter.surf, defense_meter.rect)
    drawing_functions.weapon_draw(player, graphic_dict, staff, sword, bow, npc_garan, weapon_select)
    screen.blit(artherian.surf, artherian.rect)
    screen.blit(noren.surf, noren.rect)
    screen.blit(boro.surf, boro.rect)
    screen.blit(maydria.surf, maydria.rect)

    if not artherian.quest_complete:
        screen.blit(artherian_star.surf, artherian_star.rect)
    if not maydria.quest_complete:
        screen.blit(maydria_star.surf, maydria_star.rect)

    screen.blit(hearth_stone.surf, hearth_stone.rect)

    respawned_dict = gameplay_functions.enemy_respawn(player, marrow_ghouls, marrow_ghouls, marrow_ghouls,
                                                      marrow_ghouls, marrow_ghouls, marrow_ghouls, marrow_ghouls,
                                                      marrow_ghouls, marrow_ghouls, Enemy, Item, graphic_dict,
                                                      UiElement, marrow_ghouls, marrow_ghouls, marrow_ghouls,
                                                      marrow_ghouls, marrow_ghouls)
    marrow_ghouls = respawned_dict["marrow_ghouls"]

    for ghoul in marrow_ghouls:
        screen.blit(ghoul.surf, ghoul.rect)
    try:
        for pet in player.pet:
            if pet.active:
                screen.blit(pet.surf, pet.rect)
    except AttributeError:
        pass
    screen.blit(player.surf, player.rect)
    if vanished:
        vanish_overlay.update(player.x_coordinate, player.y_coordinate, graphic_dict["vanish_img"])
        screen.blit(vanish_overlay.surf, vanish_overlay.rect)
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

    if pygame.sprite.collide_rect(player, artherian):
        interaction_popup.update(artherian.x_coordinate, artherian.y_coordinate - 50,
                                 graphic_dict["popup_interaction_purple"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str(artherian.name), True, "black", (203, 195, 227))
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (artherian.x_coordinate, artherian.y_coordinate - 50)
        screen.blit(interaction_info_surf, interaction_info_rect)

        info_text_1 = "Press 'F' key to talk to NPC."
        info_text_2 = ""
        info_text_3 = ""
        info_text_4 = ""

        if interacted and in_over_world:
            interacted = False
            current_npc_interacting = artherian
            in_over_world = False
            in_npc_interaction = True
            movement_able = False
            drawing_functions.loot_popup_container.clear()
            drawing_functions.loot_text_container.clear()
            combat_scenario.battle_animation_player(player, player_battle_sprite, False,
                                                    False, graphic_dict)

    if pygame.sprite.collide_rect(player, noren):
        interaction_popup.update(noren.x_coordinate, noren.y_coordinate - 50,
                                 graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str(noren.name), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (noren.x_coordinate, noren.y_coordinate - 50)
        screen.blit(interaction_info_surf, interaction_info_rect)

        info_text_1 = ""
        info_text_2 = ""
        info_text_3 = ""
        info_text_4 = ""

        if interacted and in_over_world:
            interacted = False

    if pygame.sprite.collide_rect(player, boro):
        interaction_popup.update(boro.x_coordinate, boro.y_coordinate - 50,
                                 graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str(boro.name), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (boro.x_coordinate, boro.y_coordinate - 50)
        screen.blit(interaction_info_surf, interaction_info_rect)

        info_text_1 = ""
        info_text_2 = ""
        info_text_3 = ""
        info_text_4 = ""

        if interacted and in_over_world:
            interacted = False

    if pygame.sprite.collide_rect(player, maydria):
        interaction_popup.update(maydria.x_coordinate, maydria.y_coordinate - 50,
                                 graphic_dict["popup_interaction_purple"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str(maydria.name), True, "black", (203, 195, 227))
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (maydria.x_coordinate, maydria.y_coordinate - 50)
        screen.blit(interaction_info_surf, interaction_info_rect)

        info_text_1 = "Press 'F' key to talk to NPC."
        info_text_2 = ""
        info_text_3 = ""
        info_text_4 = ""

        if interacted and in_over_world:
            interacted = False
            current_npc_interacting = maydria
            in_over_world = False
            in_npc_interaction = True
            movement_able = False
            drawing_functions.loot_popup_container.clear()
            drawing_functions.loot_text_container.clear()
            combat_scenario.battle_animation_player(player, player_battle_sprite, False,
                                                    False, graphic_dict)

    if pygame.sprite.collide_rect(player, hearth_stone):
        interaction_popup.update(hearth_stone.x_coordinate, hearth_stone.y_coordinate - 25,
                                 graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str("hearth stone"), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (hearth_stone.x_coordinate, hearth_stone.y_coordinate - 25)
        screen.blit(interaction_info_surf, interaction_info_rect)

        if not marrow_attuned:
            info_text_1 = "Press 'F' key to attune to stone."
            info_text_2 = ""
            info_text_3 = ""
            info_text_4 = ""

            if interacted and in_over_world:
                pygame.mixer.find_channel(True).play(sfx_hearth)
                hearth_stone.update(hearth_stone.x_coordinate, hearth_stone.y_coordinate,
                                    graphic_dict["hearth_stone_lit"])
                marrow_attuned = True
                info_text_1 = "You have attuned to the stone."
                info_text_2 = "You may now fast travel here."
                interacted = False
    else:
        hearth_stone.update(hearth_stone.x_coordinate, hearth_stone.y_coordinate, graphic_dict["hearth_stone"])

    if pygame.Rect.colliderect(player.rect, sub_marrow):
        interaction_popup.update(365, 575, graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str("Subterranean"), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (365, 575)
        screen.blit(interaction_info_surf, interaction_info_rect)

        info_text_1 = "Press 'F' key to climb down ladder."
        info_text_2 = ""
        info_text_3 = ""
        info_text_4 = ""

        if interacted and in_over_world:
            pygame.mixer.find_channel(True).play(sfx_ladder)
            interacted = False
            player.current_zone = "sub marrow"
            player.x_coordinate = 425
            player.y_coordinate = 650
            player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))

    # --------------------------------------------------------------------------------------------------
    for save_window in save_check_window:
        screen.blit(save_window.surf, save_window.rect)
    for ui_elements in user_interface:
        if len(drawing_functions.item_info_window) != 0:
            if ui_elements.name != "star power":
                screen.blit(ui_elements.surf, ui_elements.rect)
        else:
            screen.blit(ui_elements.surf, ui_elements.rect)

    if len(drawing_functions.loot_popup_container) > 0:
        for popup in drawing_functions.loot_popup_container:
            screen.blit(popup.surf, popup.rect)
    if len(drawing_functions.loot_text_container) > 0:
        for loot_text in drawing_functions.loot_text_container:
            screen.blit(loot_text[0], loot_text[1])

    screen.blit(bar_backdrop.surf, bar_backdrop.rect)
    screen.blit(hp_bar.surf, hp_bar.rect)
    screen.blit(en_bar.surf, en_bar.rect)
    screen.blit(xp_bar.surf, xp_bar.rect)

    # draw texts to the screen, like message box, player rupees and level, inv and equ updates
    drawing_functions.text_info_draw(screen, player, font, info_text_1, info_text_2, info_text_3, info_text_4,
                                     in_over_world)
    drawing_functions.draw_it(screen)

    # if player collides with enemy sprite, doesn't have combat cooldown and chooses to interact with it
    enemy = pygame.sprite.spritecollideany(player, marrow_ghouls)
    if enemy:
        interaction_popup.update(enemy.x_coordinate, enemy.y_coordinate - 40, graphic_dict["popup_interaction_red"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str(enemy.name) + " lvl " + str(enemy.level), True, "black",
                                            (255, 204, 203))
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (enemy.x_coordinate, enemy.y_coordinate - 40)
        screen.blit(interaction_info_surf, interaction_info_rect)

        # lets player know if they are in range of enemy they can press f to attack it
        info_text_1 = "Press 'F' key to attack enemy."
        info_text_2 = ""
        info_text_3 = ""
        info_text_4 = ""

        if interacted and in_over_world:
            current_enemy_battling = enemy
            in_over_world = False
            in_battle = True

            drawing_functions.loot_popup_container.clear()
            drawing_functions.loot_text_container.clear()
            combat_scenario.battle_animation_player(player, player_battle_sprite, barrier_active,
                                                    sharp_sense_active, graphic_dict)
            combat_scenario.battle_animation_enemy(current_enemy_battling, ghoul_battle_sprite,
                                                   ghoul_battle_sprite, ghoul_battle_sprite, ghoul_battle_sprite,
                                                   ghoul_battle_sprite, ghoul_battle_sprite, ghoul_battle_sprite,
                                                   in_battle, in_npc_interaction, graphic_dict, ghoul_battle_sprite,
                                                   ghoul_battle_sprite, ghoul_battle_sprite, False, ghoul_battle_sprite,
                                                   0)

    # npc movement updates
    face_direction = random.choice(["front", "back", "left", "right"])
    face_this_npc = random.choice(npcs.sprites())
    if movement_able and in_over_world:
        npc_toc = time.perf_counter()
        if npc_toc - npc_tic > 5:
            npc_tic = time.perf_counter()
            if face_direction == "front":
                if face_this_npc.name == "adria":
                    face_this_npc.update(graphic_dict["adria_down"])
                if face_this_npc.name == "noren":
                    face_this_npc.update(graphic_dict["noren_down"])
                if face_this_npc.name == "boro":
                    face_this_npc.update(graphic_dict["boro_down"])
                if face_this_npc.name == "artherian":
                    face_this_npc.update(graphic_dict["artherian_down"])
            if face_direction == "back":
                if face_this_npc.name == "adria":
                    face_this_npc.update(graphic_dict["adria_up"])
                if face_this_npc.name == "noren":
                    face_this_npc.update(graphic_dict["noren_up"])
                if face_this_npc.name == "boro":
                    face_this_npc.update(graphic_dict["boro_up"])
                if face_this_npc.name == "artherian":
                    face_this_npc.update(graphic_dict["artherian_up"])
            if face_direction == "left":
                if face_this_npc.name == "adria":
                    face_this_npc.update(graphic_dict["adria_left"])
                if face_this_npc.name == "noren":
                    face_this_npc.update(graphic_dict["noren_left"])
                if face_this_npc.name == "boro":
                    face_this_npc.update(graphic_dict["boro_left"])
                if face_this_npc.name == "artherian":
                    face_this_npc.update(graphic_dict["artherian_left"])
            if face_direction == "right":
                if face_this_npc.name == "adria":
                    face_this_npc.update(graphic_dict["adria_right"])
                if face_this_npc.name == "noren":
                    face_this_npc.update(graphic_dict["noren_right"])
                if face_this_npc.name == "boro":
                    face_this_npc.update(graphic_dict["boro_right"])
                if face_this_npc.name == "artherian":
                    face_this_npc.update(graphic_dict["artherian_right"])

    # enemy movement updates
    direction_horizontal = random.choice(["left", "right"])
    direction_vertical = random.choice(["up", "down"])
    move_mon = random.choice(marrow_ghouls.sprites())
    if movement_able and in_over_world:
        enemy_toc = time.perf_counter()
        if enemy_toc - enemy_tic > 2:
            enemy_tic = time.perf_counter()
            move_mon.update_position([125, 600], [100, 300], direction_horizontal, direction_vertical)

    if player.y_coordinate <= 50:
        player.current_zone = "marrow entrance"
        over_world_song_set = False
        in_over_world = True
        player.x_coordinate = 465
        player.y_coordinate = 675
        player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))

    marrow_district_return = {"over_world_song_set": over_world_song_set, "npc_tic": npc_tic,
                              "info_text_1": info_text_1, "info_text_2": info_text_2, "info_text_3": info_text_3,
                              "info_text_4": info_text_4, "interacted": interacted, "in_over_world": in_over_world,
                              "movement_able": movement_able, "current_npc_interacting": current_npc_interacting,
                              "in_npc_interaction": in_npc_interaction, "marrow_attuned": marrow_attuned,
                              "enemy_tic": enemy_tic, "in_battle": in_battle, "current_enemy": current_enemy_battling,
                              "marrow_ghouls": marrow_ghouls}

    return marrow_district_return


def marrow_entrance(pygame, screen, graphic_dict, player, marrow_entrance_bg, over_world_song_set, interaction_popup,
                    font, save_check_window, user_interface, bar_backdrop,
                    hp_bar, en_bar, xp_bar, button_highlighted, button_highlight, in_over_world, interacted,
                    info_text_1, info_text_2, info_text_3, info_text_4, npc_tic, movement_able, equipment_screen,
                    staff, sword, bow, npc_garan, offense_meter, defense_meter, weapon_select, pet_energy_window,
                    overlay_marrow_west, overlay_marrow_east, overlay_switch, switch_shadow, switch_phase, switch_box,
                    marrow_entrance_bg_open, entrance_music, entrance_npc, entrance_1, entrance_2, entrance_3,
                    entrance_popup, sfx_switch, hearth_stone, mini_map):

    if not over_world_song_set:
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.fadeout(50)
            pygame.mixer.music.load(entrance_music)
            pygame.mixer.music.play(loops=-1)
            over_world_song_set = True

    if switch_phase == "complete":
        screen.blit(marrow_entrance_bg_open, (0, 0))
    else:
        screen.blit(marrow_entrance_bg, (0, 0))
    screen.blit(equipment_screen.surf, equipment_screen.rect)
    screen.blit(offense_meter.surf, offense_meter.rect)
    screen.blit(defense_meter.surf, defense_meter.rect)
    drawing_functions.weapon_draw(player, graphic_dict, staff, sword, bow, npc_garan, weapon_select)

    screen.blit(entrance_npc.surf, entrance_npc.rect)

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

    screen.blit(overlay_switch.surf, overlay_switch.rect)

    if pygame.Rect.colliderect(player.rect, overlay_marrow_west):
        interaction_popup.update(125, 220, graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str("West Ramparts"), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (125, 220)
        screen.blit(interaction_info_surf, interaction_info_rect)

        info_text_1 = "Press 'F' key to enter Ramparts."
        info_text_2 = ""
        info_text_3 = ""
        info_text_4 = ""

        if interacted and in_over_world:
            interacted = False
            mini_map.update(915, 596, graphic_dict["marrow_mini_map_tower_left"])
            player.current_zone = "marrow tower west"
            player.x_coordinate = 500
            player.y_coordinate = 675
            player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))

    if pygame.Rect.colliderect(player.rect, overlay_marrow_east):
        interaction_popup.update(905, 220, graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str("East Ramparts"), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (905, 220)
        screen.blit(interaction_info_surf, interaction_info_rect)

        info_text_1 = "Press 'F' key to enter Ramparts."
        info_text_2 = ""
        info_text_3 = ""
        info_text_4 = ""

        if interacted and in_over_world:
            interacted = False
            mini_map.update(915, 596, graphic_dict["marrow_mini_map_tower_right"])
            player.current_zone = "marrow tower east"
            player.x_coordinate = 500
            player.y_coordinate = 675
            player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))

    if pygame.Rect.colliderect(player.rect, switch_box):
        interaction_popup.update(515, 225, graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str("Barrier Switch"), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (515, 225)
        screen.blit(interaction_info_surf, interaction_info_rect)

        if interacted and in_over_world:
            interacted = False
            if switch_phase == "purple":
                pygame.mixer.find_channel(True).play(sfx_switch)
                switch_phase = "complete"
                overlay_switch.update(640, 360, graphic_dict["marrow_switch_complete"])
            else:
                info_text_1 = "Requires activation sequence."
                info_text_2 = ""
                info_text_3 = ""
                info_text_4 = ""

    # --------------------------------------------------------------------------------------------------
    for save_window in save_check_window:
        screen.blit(save_window.surf, save_window.rect)
    for ui_elements in user_interface:
        if len(drawing_functions.item_info_window) != 0:
            if ui_elements.name != "star power":
                screen.blit(ui_elements.surf, ui_elements.rect)
        else:
            screen.blit(ui_elements.surf, ui_elements.rect)

    if len(drawing_functions.loot_popup_container) > 0:
        for popup in drawing_functions.loot_popup_container:
            screen.blit(popup.surf, popup.rect)
    if len(drawing_functions.loot_text_container) > 0:
        for loot_text in drawing_functions.loot_text_container:
            screen.blit(loot_text[0], loot_text[1])

    screen.blit(bar_backdrop.surf, bar_backdrop.rect)
    screen.blit(hp_bar.surf, hp_bar.rect)
    screen.blit(en_bar.surf, en_bar.rect)
    screen.blit(xp_bar.surf, xp_bar.rect)

    screen.blit(mini_map.surf, mini_map.rect)

    # draw texts to the screen, like message box, player rupees and level, inv and equ updates
    drawing_functions.text_info_draw(screen, player, font, info_text_1, info_text_2, info_text_3, info_text_4,
                                     in_over_world)
    drawing_functions.draw_it(screen)

    if switch_phase != "complete":
        face_direction = random.choice(["left", "right", "front", "back"])
        if movement_able and in_over_world:
            npc_toc = time.perf_counter()
            if npc_toc - npc_tic > 7:
                npc_tic = time.perf_counter()
                if entrance_2:
                    entrance_3 = True
                if entrance_1:
                    entrance_1 = False
                    entrance_2 = True
                if face_direction == "left":
                    entrance_npc.update(graphic_dict["entrance_npc_left"])
                if face_direction == "right":
                    entrance_npc.update(graphic_dict["entrance_npc_right"])
                if face_direction == "front":
                    entrance_npc.update(graphic_dict["entrance_npc_down"])
                if face_direction == "back":
                    entrance_npc.update(graphic_dict["entrance_npc_up"])
        if entrance_1:
            entrance_text_surf = font.render("Please, you must help.", True, "black", "light yellow")
        if entrance_2:
            entrance_text_surf = font.render("The barrier is locked.", True, "black", "light yellow")
        if entrance_3:
            entrance_text_surf = font.render("The vanguard is trapped.", True, "black", "light yellow")

    else:
        face_direction = random.choice(["left", "right", "front", "back"])
        if movement_able and in_over_world:
            npc_toc = time.perf_counter()
            if npc_toc - npc_tic > 7:
                npc_tic = time.perf_counter()
                if face_direction == "left":
                    entrance_npc.update(graphic_dict["entrance_npc_left"])
                if face_direction == "right":
                    entrance_npc.update(graphic_dict["entrance_npc_right"])
                if face_direction == "front":
                    entrance_npc.update(graphic_dict["entrance_npc_down"])
                if face_direction == "back":
                    entrance_npc.update(graphic_dict["entrance_npc_up"])
            entrance_text_surf = font.render("Thank you.", True, "black", "light yellow")

    screen.blit(entrance_popup.surf, entrance_popup.rect)
    entrance_text_rect = entrance_text_surf.get_rect()
    entrance_text_rect.center = (entrance_popup.x_coordinate, entrance_popup.y_coordinate)
    screen.blit(entrance_text_surf, entrance_text_rect)

    if 450 < player.x_coordinate < 550 and player.y_coordinate < 40:
        hearth_stone.update(968, 595, graphic_dict["hearth_stone"])
        player.current_zone = "eldream"
        in_over_world = True
        over_world_song_set = False
        player.x_coordinate = 545
        player.y_coordinate = 690
        player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))
    if player.y_coordinate > 690:
        player.current_zone = "marrow"
        in_over_world = True
        over_world_song_set = False
        player.x_coordinate = 685
        player.y_coordinate = 170
        player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))

    marrow_entrance_return = {"over_world_song_set": over_world_song_set, "npc_tic": npc_tic,
                              "info_text_1": info_text_1, "info_text_2": info_text_2, "info_text_3": info_text_3,
                              "info_text_4": info_text_4, "interacted": interacted, "in_over_world": in_over_world,
                              "movement_able": movement_able, "switch_phase": switch_phase, "entrance_1": entrance_1,
                              "entrance_2": entrance_2, "entrance_3": entrance_3}

    return marrow_entrance_return


def marrow_tower_west(pygame, screen, graphic_dict, player, marrow_tower_w_bg, over_world_song_set, marrow_music,
                      interaction_popup, font, save_check_window, user_interface, bar_backdrop,
                      hp_bar, en_bar, xp_bar, button_highlighted, button_highlight, in_over_world, interacted,
                      info_text_1, info_text_2, info_text_3, info_text_4, npc_tic, movement_able, equipment_screen,
                      staff, sword, bow, npc_garan, offense_meter, defense_meter, weapon_select, pet_energy_window,
                      overlay_marrow_west, overlay_marrow_east, crate_1, crate_2, ramps_crate_1_got,
                      ramps_crate_2_got, sfx_item_potion, Item, necrola_1, necrola_2, necrola_rect_1, necrola_rect_2,
                      player_battle_sprite, barrier_active, sharp_sense_active, necrola_battle_sprite, in_battle,
                      current_enemy_battling, sfx_surprise, mini_map, vanished, vanish_overlay):

    if not over_world_song_set:
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.fadeout(50)
            pygame.mixer.music.load(marrow_music)
            pygame.mixer.music.play(loops=-1)
            over_world_song_set = True

    screen.blit(marrow_tower_w_bg, (0, 0))
    screen.blit(equipment_screen.surf, equipment_screen.rect)
    screen.blit(offense_meter.surf, offense_meter.rect)
    screen.blit(defense_meter.surf, defense_meter.rect)
    drawing_functions.weapon_draw(player, graphic_dict, staff, sword, bow, npc_garan, weapon_select)

    if not ramps_crate_1_got:
        screen.blit(crate_1.surf, crate_1.rect)
    if not ramps_crate_2_got:
        screen.blit(crate_2.surf, crate_2.rect)

    if necrola_1.alive_status:
        screen.blit(necrola_1.surf, necrola_1.rect)
    if necrola_2.alive_status:
        screen.blit(necrola_2.surf, necrola_2.rect)

    try:
        for pet in player.pet:
            if pet.active:
                screen.blit(pet.surf, pet.rect)
    except AttributeError:
        pass
    screen.blit(player.surf, player.rect)
    if vanished:
        vanish_overlay.update(player.x_coordinate, player.y_coordinate, graphic_dict["vanish_img"])
        screen.blit(vanish_overlay.surf, vanish_overlay.rect)
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

    # --------------------------------------------------------------------------------------------------
    for save_window in save_check_window:
        screen.blit(save_window.surf, save_window.rect)
    for ui_elements in user_interface:
        if len(drawing_functions.item_info_window) != 0:
            if ui_elements.name != "star power":
                screen.blit(ui_elements.surf, ui_elements.rect)
        else:
            screen.blit(ui_elements.surf, ui_elements.rect)

    if len(drawing_functions.loot_popup_container) > 0:
        for popup in drawing_functions.loot_popup_container:
            screen.blit(popup.surf, popup.rect)
    if len(drawing_functions.loot_text_container) > 0:
        for loot_text in drawing_functions.loot_text_container:
            screen.blit(loot_text[0], loot_text[1])

    screen.blit(bar_backdrop.surf, bar_backdrop.rect)
    screen.blit(hp_bar.surf, hp_bar.rect)
    screen.blit(en_bar.surf, en_bar.rect)
    screen.blit(xp_bar.surf, xp_bar.rect)

    screen.blit(mini_map.surf, mini_map.rect)

    # draw texts to the screen, like message box, player rupees and level, inv and equ updates
    drawing_functions.text_info_draw(screen, player, font, info_text_1, info_text_2, info_text_3, info_text_4,
                                     in_over_world)
    drawing_functions.draw_it(screen)

    if pygame.sprite.collide_rect(player, crate_1):
        if not ramps_crate_1_got:
            interaction_popup.update(crate_1.x_coordinate, crate_1.y_coordinate - 50,
                                     graphic_dict["popup_interaction"])
            screen.blit(interaction_popup.surf, interaction_popup.rect)
            interaction_info_surf = font.render(str("crate"), True, "black", "light yellow")
            interaction_info_rect = interaction_info_surf.get_rect()
            interaction_info_rect.center = (crate_1.x_coordinate, crate_1.y_coordinate - 50)
            screen.blit(interaction_info_surf, interaction_info_rect)

            if interacted:
                if not ramps_crate_1_got:
                    if len(player.items) < 16:
                        ramps_crate_1_got = True
                        pygame.mixer.find_channel(True).play(sfx_item_potion)
                        info_text_1 = "You found a health potion!"
                        info_text_2 = ""
                        player.items.append(Item("small health potion", "potion", 200, 200,
                                                 graphic_dict["health_pot_img"], 0))
                    else:
                        info_text_1 = "Your inventory is full."
                        info_text_2 = ""
                else:
                    info_text_1 = "This crate is empty."
                    info_text_2 = ""

            interacted = False

    if pygame.sprite.collide_rect(player, crate_2):
        if not ramps_crate_2_got:
            interaction_popup.update(crate_2.x_coordinate, crate_2.y_coordinate - 50,
                                     graphic_dict["popup_interaction"])
            screen.blit(interaction_popup.surf, interaction_popup.rect)
            interaction_info_surf = font.render(str("crate"), True, "black", "light yellow")
            interaction_info_rect = interaction_info_surf.get_rect()
            interaction_info_rect.center = (crate_2.x_coordinate, crate_2.y_coordinate - 50)
            screen.blit(interaction_info_surf, interaction_info_rect)

            if interacted:
                if not ramps_crate_2_got:
                    if len(player.items) < 16:
                        ramps_crate_2_got = True
                        pygame.mixer.find_channel(True).play(sfx_item_potion)
                        info_text_1 = "You found an energy potion!"
                        info_text_2 = ""
                        player.items.append(Item("small energy potion", "potion", 200, 200,
                                                 graphic_dict["energy_pot_img"], 0))
                    else:
                        info_text_1 = "Your inventory is full."
                        info_text_2 = ""
                else:
                    info_text_1 = "This crate is empty."
                    info_text_2 = ""

            interacted = False

    if necrola_1.alive_status:
        if pygame.Rect.colliderect(player.rect, necrola_rect_1):
            if necrola_1.x_coordinate >= player.x_coordinate:
                movement_able = False
                necrola_1.x_coordinate -= 5
                necrola_1.surf = graphic_dict["necrola"]
                necrola_1.rect = necrola_1.surf.get_rect(center=(necrola_1.x_coordinate, necrola_1.y_coordinate))
            else:
                pygame.mixer.find_channel(True).play(sfx_surprise)
                current_enemy_battling = necrola_1
                in_over_world = False
                movement_able = False
                in_battle = True
                drawing_functions.loot_popup_container.clear()
                drawing_functions.loot_text_container.clear()
                combat_scenario.battle_animation_player(player, player_battle_sprite, barrier_active,
                                                        sharp_sense_active, graphic_dict)
                combat_scenario.battle_animation_enemy(current_enemy_battling, necrola_battle_sprite,
                                                       necrola_battle_sprite,
                                                       necrola_battle_sprite, necrola_battle_sprite,
                                                       necrola_battle_sprite, necrola_battle_sprite,
                                                       necrola_battle_sprite, in_battle, necrola_battle_sprite,
                                                       graphic_dict, necrola_battle_sprite,
                                                       necrola_battle_sprite, necrola_battle_sprite,
                                                       False, necrola_battle_sprite, 0)
    if necrola_2.alive_status:
        if pygame.Rect.colliderect(player.rect, necrola_rect_2):
            if necrola_2.x_coordinate <= player.x_coordinate:
                movement_able = False
                necrola_2.x_coordinate += 5
                necrola_2.surf = graphic_dict["necrola"]
                necrola_2.rect = necrola_2.surf.get_rect(center=(necrola_2.x_coordinate, necrola_2.y_coordinate))
            else:
                pygame.mixer.find_channel(True).play(sfx_surprise)
                current_enemy_battling = necrola_2
                in_over_world = False
                movement_able = False
                in_battle = True
                drawing_functions.loot_popup_container.clear()
                drawing_functions.loot_text_container.clear()
                combat_scenario.battle_animation_player(player, player_battle_sprite, barrier_active,
                                                        sharp_sense_active, graphic_dict)
                combat_scenario.battle_animation_enemy(current_enemy_battling, necrola_battle_sprite,
                                                       necrola_battle_sprite,
                                                       necrola_battle_sprite, necrola_battle_sprite,
                                                       necrola_battle_sprite, necrola_battle_sprite,
                                                       necrola_battle_sprite, in_battle, necrola_battle_sprite,
                                                       graphic_dict, necrola_battle_sprite,
                                                       necrola_battle_sprite, necrola_battle_sprite,
                                                       False, necrola_battle_sprite, 0)

    if 425 < player.x_coordinate < 600 and player.y_coordinate >= 710:
        overlay_marrow_west.update(110, 250, graphic_dict["overlay_marrow_ramps_west"])
        overlay_marrow_east.update(925, 250, graphic_dict["overlay_marrow_ramps_east"])
        mini_map.update(915, 596, graphic_dict["marrow_mini_map"])
        player.current_zone = "marrow entrance"
        in_over_world = True
        player.x_coordinate = 120
        player.y_coordinate = 385
        player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))

    if 315 < player.x_coordinate < 350 and player.y_coordinate >= 575:
        overlay_marrow_west.update(570, 55, graphic_dict["overlay_marrow_ramps_west"])
        mini_map.update(915, 596, graphic_dict["marrow_mini_map_ramps_left"])
        player.current_zone = "marrow ramps west"
        in_over_world = True
        player.x_coordinate = 515
        player.y_coordinate = 200
        player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))

    marrow_tower_west_return = {"over_world_song_set": over_world_song_set, "npc_tic": npc_tic,
                                "info_text_1": info_text_1, "info_text_2": info_text_2, "info_text_3": info_text_3,
                                "info_text_4": info_text_4, "interacted": interacted, "in_over_world": in_over_world,
                                "movement_able": movement_able, "ramps_crate_1_got": ramps_crate_1_got,
                                "ramps_crate_2_got": ramps_crate_2_got, "in_battle": in_battle,
                                "current_enemy": current_enemy_battling}

    return marrow_tower_west_return


def marrow_tower_east(pygame, screen, graphic_dict, player, marrow_tower_e_bg, over_world_song_set, marrow_music,
                      interaction_popup, font, save_check_window, user_interface, bar_backdrop,
                      hp_bar, en_bar, xp_bar, button_highlighted, button_highlight, in_over_world, interacted,
                      info_text_1, info_text_2, info_text_3, info_text_4, npc_tic, movement_able, equipment_screen,
                      staff, sword, bow, npc_garan, offense_meter, defense_meter, weapon_select, pet_energy_window,
                      overlay_marrow_west, overlay_marrow_east, crate_3, crate_4, ramps_crate_3_got, ramps_crate_4_got,
                      sfx_item_potion, Item, necrola_3, in_battle, necrola_rect_3, player_battle_sprite,
                      barrier_active, sharp_sense_active, necrola_battle_sprite, current_enemy_battling,
                      sfx_surprise, mini_map, vanished, vanish_overlay):

    if not over_world_song_set:
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.fadeout(50)
            pygame.mixer.music.load(marrow_music)
            pygame.mixer.music.play(loops=-1)
            over_world_song_set = True

    screen.blit(marrow_tower_e_bg, (0, 0))
    screen.blit(equipment_screen.surf, equipment_screen.rect)
    screen.blit(offense_meter.surf, offense_meter.rect)
    screen.blit(defense_meter.surf, defense_meter.rect)
    drawing_functions.weapon_draw(player, graphic_dict, staff, sword, bow, npc_garan, weapon_select)

    if not ramps_crate_3_got:
        screen.blit(crate_3.surf, crate_3.rect)
    if not ramps_crate_4_got:
        screen.blit(crate_4.surf, crate_4.rect)

    if necrola_3.alive_status:
        screen.blit(necrola_3.surf, necrola_3.rect)

    try:
        for pet in player.pet:
            if pet.active:
                screen.blit(pet.surf, pet.rect)
    except AttributeError:
        pass
    screen.blit(player.surf, player.rect)
    if vanished:
        vanish_overlay.update(player.x_coordinate, player.y_coordinate, graphic_dict["vanish_img"])
        screen.blit(vanish_overlay.surf, vanish_overlay.rect)
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

    # --------------------------------------------------------------------------------------------------
    for save_window in save_check_window:
        screen.blit(save_window.surf, save_window.rect)
    for ui_elements in user_interface:
        if len(drawing_functions.item_info_window) != 0:
            if ui_elements.name != "star power":
                screen.blit(ui_elements.surf, ui_elements.rect)
        else:
            screen.blit(ui_elements.surf, ui_elements.rect)

    if len(drawing_functions.loot_popup_container) > 0:
        for popup in drawing_functions.loot_popup_container:
            screen.blit(popup.surf, popup.rect)
    if len(drawing_functions.loot_text_container) > 0:
        for loot_text in drawing_functions.loot_text_container:
            screen.blit(loot_text[0], loot_text[1])

    screen.blit(bar_backdrop.surf, bar_backdrop.rect)
    screen.blit(hp_bar.surf, hp_bar.rect)
    screen.blit(en_bar.surf, en_bar.rect)
    screen.blit(xp_bar.surf, xp_bar.rect)

    screen.blit(mini_map.surf, mini_map.rect)

    # draw texts to the screen, like message box, player rupees and level, inv and equ updates
    drawing_functions.text_info_draw(screen, player, font, info_text_1, info_text_2, info_text_3, info_text_4,
                                     in_over_world)
    drawing_functions.draw_it(screen)

    if pygame.sprite.collide_rect(player, crate_3):
        if not ramps_crate_3_got:
            interaction_popup.update(crate_3.x_coordinate, crate_3.y_coordinate - 50,
                                     graphic_dict["popup_interaction"])
            screen.blit(interaction_popup.surf, interaction_popup.rect)
            interaction_info_surf = font.render(str("crate"), True, "black", "light yellow")
            interaction_info_rect = interaction_info_surf.get_rect()
            interaction_info_rect.center = (crate_3.x_coordinate, crate_3.y_coordinate - 50)
            screen.blit(interaction_info_surf, interaction_info_rect)

            if interacted:
                if not ramps_crate_3_got:
                    if len(player.items) < 16:
                        ramps_crate_3_got = True
                        pygame.mixer.find_channel(True).play(sfx_item_potion)
                        info_text_1 = "You found a health potion!"
                        info_text_2 = ""
                        player.items.append(Item("small health potion", "potion", 200, 200,
                                                 graphic_dict["health_pot_img"], 0))
                    else:
                        info_text_1 = "Your inventory is full."
                        info_text_2 = ""
                else:
                    info_text_1 = "This crate is empty."
                    info_text_2 = ""

            interacted = False

    if pygame.sprite.collide_rect(player, crate_4):
        if not ramps_crate_4_got:
            interaction_popup.update(crate_4.x_coordinate, crate_4.y_coordinate - 50,
                                     graphic_dict["popup_interaction"])
            screen.blit(interaction_popup.surf, interaction_popup.rect)
            interaction_info_surf = font.render(str("crate"), True, "black", "light yellow")
            interaction_info_rect = interaction_info_surf.get_rect()
            interaction_info_rect.center = (crate_4.x_coordinate, crate_4.y_coordinate - 50)
            screen.blit(interaction_info_surf, interaction_info_rect)

            if interacted:
                if not ramps_crate_4_got:
                    if len(player.items) < 16:
                        ramps_crate_4_got = True
                        pygame.mixer.find_channel(True).play(sfx_item_potion)
                        info_text_1 = "You found an energy potion!"
                        info_text_2 = ""
                        player.items.append(Item("small energy potion", "potion", 200, 200,
                                                 graphic_dict["energy_pot_img"], 0))
                    else:
                        info_text_1 = "Your inventory is full."
                        info_text_2 = ""
                else:
                    info_text_1 = "This crate is empty."
                    info_text_2 = ""

            interacted = False

    if necrola_3.alive_status:
        if pygame.Rect.colliderect(player.rect, necrola_rect_3):
            if necrola_3.y_coordinate >= player.y_coordinate:
                necrola_3.y_coordinate -= 5
                necrola_3.surf = graphic_dict["necrola"]
                necrola_3.rect = necrola_3.surf.get_rect(center=(necrola_3.x_coordinate, necrola_3.y_coordinate))
            else:
                pygame.mixer.find_channel(True).play(sfx_surprise)
                current_enemy_battling = necrola_3
                in_over_world = False
                movement_able = False
                in_battle = True

                drawing_functions.loot_popup_container.clear()
                drawing_functions.loot_text_container.clear()
                combat_scenario.battle_animation_player(player, player_battle_sprite, barrier_active,
                                                        sharp_sense_active, graphic_dict)
                combat_scenario.battle_animation_enemy(current_enemy_battling, necrola_battle_sprite,
                                                       necrola_battle_sprite,
                                                       necrola_battle_sprite, necrola_battle_sprite,
                                                       necrola_battle_sprite, necrola_battle_sprite,
                                                       necrola_battle_sprite, in_battle, necrola_battle_sprite,
                                                       graphic_dict, necrola_battle_sprite,
                                                       necrola_battle_sprite, necrola_battle_sprite,
                                                       False, necrola_battle_sprite, 0)

    if 425 < player.x_coordinate < 600 and player.y_coordinate >= 710:
        overlay_marrow_west.update(110, 250, graphic_dict["overlay_marrow_ramps_west"])
        overlay_marrow_east.update(925, 250, graphic_dict["overlay_marrow_ramps_east"])
        mini_map.update(915, 596, graphic_dict["marrow_mini_map"])
        player.current_zone = "marrow entrance"
        in_over_world = True
        player.x_coordinate = 900
        player.y_coordinate = 385
        player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))

    if 700 < player.x_coordinate < 725 and player.y_coordinate >= 575:
        overlay_marrow_east.update(570, 55, graphic_dict["overlay_marrow_ramps_east"])
        mini_map.update(915, 596, graphic_dict["marrow_mini_map_ramps_right"])
        player.current_zone = "marrow ramps east"
        in_over_world = True
        over_world_song_set = False
        player.x_coordinate = 515
        player.y_coordinate = 200
        player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))

    marrow_tower_east_return = {"over_world_song_set": over_world_song_set, "npc_tic": npc_tic,
                                "info_text_1": info_text_1, "info_text_2": info_text_2, "info_text_3": info_text_3,
                                "info_text_4": info_text_4, "interacted": interacted, "in_over_world": in_over_world,
                                "movement_able": movement_able, "ramps_crate_3_got": ramps_crate_3_got,
                                "ramps_crate_4_got": ramps_crate_4_got, "in_battle": in_battle,
                                "current_enemy": current_enemy_battling}

    return marrow_tower_east_return


def marrow_ramps_west(pygame, screen, graphic_dict, player, marrow_ramps_w_bg, over_world_song_set, marrow_music,
                      interaction_popup, font, save_check_window, user_interface, bar_backdrop,
                      hp_bar, en_bar, xp_bar, button_highlighted, button_highlight, in_over_world, interacted,
                      info_text_1, info_text_2, info_text_3, info_text_4, npc_tic, movement_able, equipment_screen,
                      staff, sword, bow, npc_garan, offense_meter, defense_meter, weapon_select, pet_energy_window,
                      overlay_marrow_west, chroma_bridge, ghoul, ghoul_2, enemy_tic, mini_map):

    if not over_world_song_set:
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.fadeout(50)
            pygame.mixer.music.load(marrow_music)
            pygame.mixer.music.play(loops=-1)
            over_world_song_set = True

    screen.blit(marrow_ramps_w_bg, (0, 0))
    screen.blit(equipment_screen.surf, equipment_screen.rect)
    screen.blit(offense_meter.surf, offense_meter.rect)
    screen.blit(defense_meter.surf, defense_meter.rect)
    drawing_functions.weapon_draw(player, graphic_dict, staff, sword, bow, npc_garan, weapon_select)

    screen.blit(chroma_bridge.surf, chroma_bridge.rect)
    screen.blit(ghoul.surf, ghoul.rect)
    screen.blit(ghoul_2.surf, ghoul_2.rect)

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

    # --------------------------------------------------------------------------------------------------
    for save_window in save_check_window:
        screen.blit(save_window.surf, save_window.rect)
    for ui_elements in user_interface:
        if len(drawing_functions.item_info_window) != 0:
            if ui_elements.name != "star power":
                screen.blit(ui_elements.surf, ui_elements.rect)
        else:
            screen.blit(ui_elements.surf, ui_elements.rect)

    if len(drawing_functions.loot_popup_container) > 0:
        for popup in drawing_functions.loot_popup_container:
            screen.blit(popup.surf, popup.rect)
    if len(drawing_functions.loot_text_container) > 0:
        for loot_text in drawing_functions.loot_text_container:
            screen.blit(loot_text[0], loot_text[1])

    screen.blit(bar_backdrop.surf, bar_backdrop.rect)
    screen.blit(hp_bar.surf, hp_bar.rect)
    screen.blit(en_bar.surf, en_bar.rect)
    screen.blit(xp_bar.surf, xp_bar.rect)

    screen.blit(mini_map.surf, mini_map.rect)

    # draw texts to the screen, like message box, player rupees and level, inv and equ updates
    drawing_functions.text_info_draw(screen, player, font, info_text_1, info_text_2, info_text_3, info_text_4,
                                     in_over_world)
    drawing_functions.draw_it(screen)

    if pygame.Rect.colliderect(player.rect, overlay_marrow_west):
        interaction_popup.update(570, 55, graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str("West Tower"), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (570, 55)
        screen.blit(interaction_info_surf, interaction_info_rect)

        info_text_1 = "Press 'F' key to enter Tower."
        info_text_2 = ""
        info_text_3 = ""
        info_text_4 = ""

        if interacted and in_over_world:
            interacted = False
            mini_map.update(915, 596, graphic_dict["marrow_mini_map_tower_left"])
            player.current_zone = "marrow tower west"
            player.x_coordinate = 100
            player.y_coordinate = 550
            player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))

    ghouls = [ghoul, ghoul_2]
    ghoul_choice = random.choice(ghouls)
    # enemy movement updates
    direction_horizontal = random.choice(["left", "right"])
    direction_vertical = random.choice(["up", "down"])
    if movement_able and in_over_world:
        enemy_toc = time.perf_counter()
        if enemy_toc - enemy_tic > 2:
            enemy_tic = time.perf_counter()
            if ghoul_choice.name == "ramps ghoul":
                ghoul.update_position([100, 300], [200, 300], direction_horizontal, direction_vertical)
            if ghoul_choice.name == "ramps ghoul 2":
                ghoul_2.update_position([700, 900], [200, 300], direction_horizontal, direction_vertical)

    if player.y_coordinate >= 675:
        mini_map.update(915, 596, graphic_dict["marrow_mini_map_ramps_left_end"])
        player.current_zone = "marrow ramps west end"
        in_over_world = True
        player.x_coordinate = 515
        player.y_coordinate = 150
        player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))

    marrow_tower_west_return = {"over_world_song_set": over_world_song_set, "npc_tic": npc_tic,
                                "info_text_1": info_text_1, "info_text_2": info_text_2, "info_text_3": info_text_3,
                                "info_text_4": info_text_4, "interacted": interacted, "in_over_world": in_over_world,
                                "movement_able": movement_able, "enemy_tic": enemy_tic}

    return marrow_tower_west_return


def marrow_ramps_east(pygame, screen, graphic_dict, player, marrow_ramps_e_bg, over_world_song_set, marrow_music,
                      interaction_popup, font, save_check_window, user_interface, bar_backdrop,
                      hp_bar, en_bar, xp_bar, button_highlighted, button_highlight, in_over_world, interacted,
                      info_text_1, info_text_2, info_text_3, info_text_4, npc_tic, movement_able, equipment_screen,
                      staff, sword, bow, npc_garan, offense_meter, defense_meter, weapon_select, pet_energy_window,
                      overlay_marrow_east, mini_map):

    if not over_world_song_set:
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.fadeout(50)
            pygame.mixer.music.load(marrow_music)
            pygame.mixer.music.play(loops=-1)
            over_world_song_set = True

    screen.blit(marrow_ramps_e_bg, (0, 0))
    screen.blit(equipment_screen.surf, equipment_screen.rect)
    screen.blit(offense_meter.surf, offense_meter.rect)
    screen.blit(defense_meter.surf, defense_meter.rect)
    drawing_functions.weapon_draw(player, graphic_dict, staff, sword, bow, npc_garan, weapon_select)

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

    # --------------------------------------------------------------------------------------------------
    for save_window in save_check_window:
        screen.blit(save_window.surf, save_window.rect)
    for ui_elements in user_interface:
        if len(drawing_functions.item_info_window) != 0:
            if ui_elements.name != "star power":
                screen.blit(ui_elements.surf, ui_elements.rect)
        else:
            screen.blit(ui_elements.surf, ui_elements.rect)

    if len(drawing_functions.loot_popup_container) > 0:
        for popup in drawing_functions.loot_popup_container:
            screen.blit(popup.surf, popup.rect)
    if len(drawing_functions.loot_text_container) > 0:
        for loot_text in drawing_functions.loot_text_container:
            screen.blit(loot_text[0], loot_text[1])

    screen.blit(bar_backdrop.surf, bar_backdrop.rect)
    screen.blit(hp_bar.surf, hp_bar.rect)
    screen.blit(en_bar.surf, en_bar.rect)
    screen.blit(xp_bar.surf, xp_bar.rect)

    screen.blit(mini_map.surf, mini_map.rect)

    # draw texts to the screen, like message box, player rupees and level, inv and equ updates
    drawing_functions.text_info_draw(screen, player, font, info_text_1, info_text_2, info_text_3, info_text_4,
                                     in_over_world)
    drawing_functions.draw_it(screen)

    if pygame.Rect.colliderect(player.rect, overlay_marrow_east):
        interaction_popup.update(570, 55, graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str("East Tower"), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (570, 55)
        screen.blit(interaction_info_surf, interaction_info_rect)

        info_text_1 = "Press 'F' key to enter Tower."
        info_text_2 = ""
        info_text_3 = ""
        info_text_4 = ""

        if interacted and in_over_world:
            interacted = False
            over_world_song_set = False
            mini_map.update(915, 596, graphic_dict["marrow_mini_map_tower_right"])
            player.current_zone = "marrow tower east"
            player.x_coordinate = 930
            player.y_coordinate = 550
            player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))

    if player.y_coordinate >= 675:
        mini_map.update(915, 596, graphic_dict["marrow_mini_map_ramps_right_end"])
        player.current_zone = "marrow ramps east end"
        in_over_world = True
        player.x_coordinate = 515
        player.y_coordinate = 150
        player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))

    marrow_ramps_east_return = {"over_world_song_set": over_world_song_set, "npc_tic": npc_tic,
                                "info_text_1": info_text_1, "info_text_2": info_text_2, "info_text_3": info_text_3,
                                "info_text_4": info_text_4, "interacted": interacted, "in_over_world": in_over_world,
                                "movement_able": movement_able}

    return marrow_ramps_east_return


def marrow_ramps_east_end(pygame, screen, graphic_dict, player, marrow_ramps_e_end_bg, over_world_song_set,
                          interaction_popup, font, save_check_window, user_interface, bar_backdrop,
                          hp_bar, en_bar, xp_bar, button_highlighted, button_highlight, in_over_world, interacted,
                          info_text_1, info_text_2, info_text_3, info_text_4, npc_tic, movement_able, equipment_screen,
                          staff, sword, bow, npc_garan, offense_meter, defense_meter, weapon_select, pet_energy_window,
                          dungeon_chest, boots_obtained, chroma_boots, sfx_chest, switch_2, marrow_switch_phase,
                          main_switch, sfx_switch, erebyth_defeated, marrow_ramps_e_end_bg_block, erebyth,
                          player_battle_sprite, barrier_active, sharp_sense_active, snake_battle_sprite,
                          ghoul_battle_sprite, chorizon_battle_sprite, muchador_battle_sprite,
                          magmon_battle_sprite, bandile_battle_sprite, chinzilla_battle_sprite, in_npc_interaction,
                          necrola_battle_sprite, osodark_battle_sprite, stelli_battle_sprite, in_battle, boss_music,
                          erebyth_battle_sprite, apothis_push, apothis, apothis_popup, apothis_1, apothis_2,
                          enemy_vanish, mini_map, vanished, vanish_overlay):

    if not over_world_song_set:
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.fadeout(50)
            pygame.mixer.music.load(boss_music)
            pygame.mixer.music.play(loops=-1)
            over_world_song_set = True

    if erebyth_defeated:
        screen.blit(marrow_ramps_e_end_bg, (0, 0))
    else:
        screen.blit(marrow_ramps_e_end_bg_block, (0, 0))
        screen.blit(erebyth.surf, erebyth.rect)
    screen.blit(equipment_screen.surf, equipment_screen.rect)
    screen.blit(offense_meter.surf, offense_meter.rect)
    screen.blit(defense_meter.surf, defense_meter.rect)
    drawing_functions.weapon_draw(player, graphic_dict, staff, sword, bow, npc_garan, weapon_select)

    if erebyth_defeated and not apothis_push:
        npc_toc = time.perf_counter()
        if npc_toc - npc_tic < 3 and erebyth_defeated:
            screen.blit(apothis.surf, apothis.rect)
            entrance_text_surf = font.render("Harm him no more.", True, "black", "light yellow")
            screen.blit(apothis_popup.surf, apothis_popup.rect)
            entrance_text_rect = entrance_text_surf.get_rect()
            entrance_text_rect.center = (apothis_popup.x_coordinate, apothis_popup.y_coordinate)
            screen.blit(entrance_text_surf, entrance_text_rect)
        else:
            npc_tic = time.perf_counter()

    if erebyth_defeated and not apothis_push:
        screen.blit(apothis.surf, apothis.rect)
        if player.y_coordinate > 220:
            player.y_coordinate -= 2
            player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))
        else:
            apothis_2 = True

        if apothis_2:
            for alpha in range(255, 0):
                apothis.surf.set_alpha(alpha)
            apothis_2 = False
            apothis_push = True

    if erebyth_defeated and apothis_push:
        npc_toc = time.perf_counter()
        if npc_toc - npc_tic < 3:
            screen.blit(enemy_vanish.surf, enemy_vanish.rect)
        screen.blit(dungeon_chest.surf, dungeon_chest.rect)
        movement_able = True

    screen.blit(switch_2.surf, switch_2.rect)

    try:
        for pet in player.pet:
            if pet.active:
                screen.blit(pet.surf, pet.rect)
    except AttributeError:
        pass
    screen.blit(player.surf, player.rect)
    if vanished:
        vanish_overlay.update(player.x_coordinate, player.y_coordinate, graphic_dict["vanish_img"])
        screen.blit(vanish_overlay.surf, vanish_overlay.rect)
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

    if erebyth_defeated:
        if pygame.sprite.collide_rect(player, dungeon_chest):
            interaction_popup.update(dungeon_chest.x_coordinate, dungeon_chest.y_coordinate - 50,
                                     graphic_dict["popup_interaction"])
            screen.blit(interaction_popup.surf, interaction_popup.rect)
            interaction_info_surf = font.render(str("chest"), True, "black", "light yellow")
            interaction_info_rect = interaction_info_surf.get_rect()
            interaction_info_rect.center = (dungeon_chest.x_coordinate, dungeon_chest.y_coordinate - 50)
            screen.blit(interaction_info_surf, interaction_info_rect)

            if interacted and in_over_world:
                if not boots_obtained:
                    if len(player.items) < 16:
                        dungeon_chest.update(dungeon_chest.x_coordinate, dungeon_chest.y_coordinate,
                                             graphic_dict["dungeon_chest_open"])
                        pygame.mixer.find_channel(True).play(sfx_chest)
                        info_text_1 = "You've obtained the chroma boots!"
                        info_text_2 = ""
                        player.items.append(chroma_boots)
                        boots_obtained = True
                    else:
                        info_text_1 = "You're inventory is full."
                        info_text_2 = ""
                else:
                    info_text_1 = "You've already obtained this item."
                    info_text_2 = ""
                interacted = False

    if not erebyth_defeated:
        if pygame.sprite.collide_rect(player, erebyth):
            interaction_popup.update(erebyth.x_coordinate, erebyth.y_coordinate - 50,
                                     graphic_dict["popup_interaction_red"])
            screen.blit(interaction_popup.surf, interaction_popup.rect)
            interaction_info_surf = font.render(str("erebyth"), True, "black", (255, 204, 203))
            interaction_info_rect = interaction_info_surf.get_rect()
            interaction_info_rect.center = (erebyth.x_coordinate, erebyth.y_coordinate - 50)
            screen.blit(interaction_info_surf, interaction_info_rect)

            # lets player know if they are in range of enemy they can press f to attack it
            info_text_1 = "Press 'F' key to attack enemy."
            info_text_2 = ""
            info_text_3 = ""
            info_text_4 = ""

            if interacted:
                current_enemy_battling = erebyth
                in_over_world = False
                in_battle = True

                drawing_functions.loot_popup_container.clear()
                drawing_functions.loot_text_container.clear()
                combat_scenario.battle_animation_player(player, player_battle_sprite, barrier_active,
                                                        sharp_sense_active, graphic_dict)
                combat_scenario.battle_animation_enemy(current_enemy_battling, snake_battle_sprite, ghoul_battle_sprite,
                                                       chorizon_battle_sprite, muchador_battle_sprite,
                                                       magmon_battle_sprite, bandile_battle_sprite,
                                                       chinzilla_battle_sprite, in_battle, in_npc_interaction,
                                                       graphic_dict, necrola_battle_sprite,
                                                       osodark_battle_sprite, stelli_battle_sprite,
                                                       False, erebyth_battle_sprite, 0)

    # --------------------------------------------------------------------------------------------------
    for save_window in save_check_window:
        screen.blit(save_window.surf, save_window.rect)
    for ui_elements in user_interface:
        if len(drawing_functions.item_info_window) != 0:
            if ui_elements.name != "star power":
                screen.blit(ui_elements.surf, ui_elements.rect)
        else:
            screen.blit(ui_elements.surf, ui_elements.rect)

    if len(drawing_functions.loot_popup_container) > 0:
        for popup in drawing_functions.loot_popup_container:
            screen.blit(popup.surf, popup.rect)
    if len(drawing_functions.loot_text_container) > 0:
        for loot_text in drawing_functions.loot_text_container:
            screen.blit(loot_text[0], loot_text[1])

    screen.blit(bar_backdrop.surf, bar_backdrop.rect)
    screen.blit(hp_bar.surf, hp_bar.rect)
    screen.blit(en_bar.surf, en_bar.rect)
    screen.blit(xp_bar.surf, xp_bar.rect)

    screen.blit(mini_map.surf, mini_map.rect)

    # draw texts to the screen, like message box, player rupees and level, inv and equ updates
    drawing_functions.text_info_draw(screen, player, font, info_text_1, info_text_2, info_text_3, info_text_4,
                                     in_over_world)
    drawing_functions.draw_it(screen)

    if player.y_coordinate <= 75:
        mini_map.update(915, 596, graphic_dict["marrow_mini_map_ramps_right"])
        player.current_zone = "marrow ramps east"
        in_over_world = True
        player.x_coordinate = 515
        player.y_coordinate = 650
        player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))

    if pygame.Rect.colliderect(player.rect, switch_2):
        interaction_popup.update(195, 135, graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str("Gate Switch"), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (195, 135)
        screen.blit(interaction_info_surf, interaction_info_rect)

        info_text_1 = "Press 'F' key to activate switch."
        info_text_2 = ""
        info_text_3 = ""
        info_text_4 = ""

        if interacted and in_over_world:
            pygame.mixer.find_channel(True).play(sfx_switch)
            interacted = False
            switch_2.update(147, 74, graphic_dict["ramp_switch_east"])

            if marrow_switch_phase == 'none':
                main_switch.update(640, 360, graphic_dict["marrow_switch_red"])
                marrow_switch_phase = 'red'
            if marrow_switch_phase == 'blue':
                main_switch.update(640, 360, graphic_dict["marrow_switch_purple"])
                marrow_switch_phase = 'purple'

    marrow_ramps_east_end_return = {"over_world_song_set": over_world_song_set, "npc_tic": npc_tic,
                                    "info_text_1": info_text_1, "info_text_2": info_text_2, "info_text_3": info_text_3,
                                    "info_text_4": info_text_4, "interacted": interacted,
                                    "in_over_world": in_over_world, "movement_able": movement_able, "boots obtained":
                                        boots_obtained, "marrow_switch_phase": marrow_switch_phase,
                                    "erebyth_defeated": erebyth_defeated, "in_battle": in_battle,
                                    "apothis_push": apothis_push, "apothis_1": apothis_1, "apothis_2": apothis_2}
    if in_battle:
        marrow_ramps_east_end_return["current_enemy_battling"] = erebyth

    return marrow_ramps_east_end_return


def marrow_ramps_west_end(pygame, screen, graphic_dict, player, marrow_ramps_w_end_bg, over_world_song_set,
                          marrow_music, interaction_popup, font, save_check_window, user_interface, bar_backdrop,
                          hp_bar, en_bar, xp_bar, button_highlighted, button_highlight, in_over_world, interacted,
                          info_text_1, info_text_2, info_text_3, info_text_4, npc_tic, movement_able, equipment_screen,
                          staff, sword, bow, npc_garan, offense_meter, defense_meter, weapon_select, pet_energy_window,
                          switch_1, marrow_switch_phase, main_switch, sfx_switch, flower, crate, crate_got, Item,
                          sfx_item_key, mini_map):

    if not over_world_song_set:
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.fadeout(50)
            pygame.mixer.music.load(marrow_music)
            pygame.mixer.music.play(loops=-1)
            over_world_song_set = True

    screen.blit(marrow_ramps_w_end_bg, (0, 0))
    screen.blit(equipment_screen.surf, equipment_screen.rect)
    screen.blit(offense_meter.surf, offense_meter.rect)
    screen.blit(defense_meter.surf, defense_meter.rect)
    drawing_functions.weapon_draw(player, graphic_dict, staff, sword, bow, npc_garan, weapon_select)

    screen.blit(switch_1.surf, switch_1.rect)
    screen.blit(flower.surf, flower.rect)

    if not crate_got:
        screen.blit(crate.surf, crate.rect)

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

    # --------------------------------------------------------------------------------------------------
    for save_window in save_check_window:
        screen.blit(save_window.surf, save_window.rect)
    for ui_elements in user_interface:
        if len(drawing_functions.item_info_window) != 0:
            if ui_elements.name != "star power":
                screen.blit(ui_elements.surf, ui_elements.rect)
        else:
            screen.blit(ui_elements.surf, ui_elements.rect)

    if len(drawing_functions.loot_popup_container) > 0:
        for popup in drawing_functions.loot_popup_container:
            screen.blit(popup.surf, popup.rect)
    if len(drawing_functions.loot_text_container) > 0:
        for loot_text in drawing_functions.loot_text_container:
            screen.blit(loot_text[0], loot_text[1])

    screen.blit(bar_backdrop.surf, bar_backdrop.rect)
    screen.blit(hp_bar.surf, hp_bar.rect)
    screen.blit(en_bar.surf, en_bar.rect)
    screen.blit(xp_bar.surf, xp_bar.rect)

    screen.blit(mini_map.surf, mini_map.rect)

    # draw texts to the screen, like message box, player rupees and level, inv and equ updates
    drawing_functions.text_info_draw(screen, player, font, info_text_1, info_text_2, info_text_3, info_text_4,
                                     in_over_world)
    drawing_functions.draw_it(screen)

    if player.y_coordinate <= 75:
        mini_map.update(915, 596, graphic_dict["marrow_mini_map_ramps_left"])
        player.current_zone = "marrow ramps west"
        in_over_world = True
        player.x_coordinate = 515
        player.y_coordinate = 650
        player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))

    if pygame.Rect.colliderect(player.rect, switch_1):
        interaction_popup.update(945, 135, graphic_dict["popup_interaction"])
        screen.blit(interaction_popup.surf, interaction_popup.rect)
        interaction_info_surf = font.render(str("Gate Switch"), True, "black", "light yellow")
        interaction_info_rect = interaction_info_surf.get_rect()
        interaction_info_rect.center = (945, 135)
        screen.blit(interaction_info_surf, interaction_info_rect)

        info_text_1 = "Press 'F' key to activate switch."
        info_text_2 = ""
        info_text_3 = ""
        info_text_4 = ""

        if interacted and in_over_world:
            pygame.mixer.find_channel(True).play(sfx_switch)
            interacted = False
            switch_1.update(995, 90, graphic_dict["ramp_switch_west"])

            if marrow_switch_phase == 'none':
                main_switch.update(640, 360, graphic_dict["marrow_switch_blue"])
                marrow_switch_phase = 'blue'
            if marrow_switch_phase == 'red':
                main_switch.update(640, 360, graphic_dict["marrow_switch_purple"])
                marrow_switch_phase = 'purple'

    if pygame.Rect.colliderect(player.rect, crate):
        if not crate_got:
            interaction_popup.update(crate.x_coordinate, crate.y_coordinate - 50,
                                     graphic_dict["popup_interaction"])
            screen.blit(interaction_popup.surf, interaction_popup.rect)
            interaction_info_surf = font.render(str("crate"), True, "black", "light yellow")
            interaction_info_rect = interaction_info_surf.get_rect()
            interaction_info_rect.center = (crate.x_coordinate, crate.y_coordinate - 50)
            screen.blit(interaction_info_surf, interaction_info_rect)

        if interacted and in_over_world:
            if not crate_got:
                if len(player.items) < 16:
                    pygame.mixer.find_channel(True).play(sfx_item_key)
                    info_text_1 = "You found a golden key!"
                    info_text_2 = ""
                    player.items.append(Item("ramps key", "key", 200, 200, graphic_dict["key_img"], 0))
                    crate_got = True
                    crate.kill()
                else:
                    info_text_1 = "Your inventory is full."
                    info_text_2 = ""
            else:
                info_text_1 = "This crate is empty."
                info_text_2 = ""
            interacted = False

    marrow_ramps_west_end_return = {"over_world_song_set": over_world_song_set, "npc_tic": npc_tic,
                                    "info_text_1": info_text_1, "info_text_2": info_text_2, "info_text_3": info_text_3,
                                    "info_text_4": info_text_4, "interacted": interacted,
                                    "in_over_world": in_over_world, "movement_able": movement_able,
                                    "marrow_switch_phase": marrow_switch_phase, "ramps_crate_5_got": crate_got}

    return marrow_ramps_west_end_return


def sub_marrow(pygame, screen, graphic_dict, player, marrow_ramps_w_end_bg, over_world_song_set,
               marrow_music, interaction_popup, font, save_check_window, user_interface, bar_backdrop,
               hp_bar, en_bar, xp_bar, button_highlighted, button_highlight, in_over_world, interacted,
               info_text_1, info_text_2, info_text_3, info_text_4, npc_tic, movement_able, equipment_screen,
               staff, sword, bow, npc_garan, offense_meter, defense_meter, weapon_select, pet_energy_window,
               Item, in_battle, vanished, vanish_overlay):

    if not over_world_song_set:
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.fadeout(50)
            pygame.mixer.music.load(marrow_music)
            pygame.mixer.music.play(loops=-1)
            over_world_song_set = True

    screen.blit(marrow_ramps_w_end_bg, (0, 0))
    screen.blit(equipment_screen.surf, equipment_screen.rect)
    screen.blit(offense_meter.surf, offense_meter.rect)
    screen.blit(defense_meter.surf, defense_meter.rect)
    drawing_functions.weapon_draw(player, graphic_dict, staff, sword, bow, npc_garan, weapon_select)

    try:
        for pet in player.pet:
            if pet.active:
                screen.blit(pet.surf, pet.rect)
    except AttributeError:
        pass
    screen.blit(player.surf, player.rect)
    if vanished:
        vanish_overlay.update(player.x_coordinate, player.y_coordinate, graphic_dict["vanish_img"])
        screen.blit(vanish_overlay.surf, vanish_overlay.rect)
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

    # --------------------------------------------------------------------------------------------------
    for save_window in save_check_window:
        screen.blit(save_window.surf, save_window.rect)
    for ui_elements in user_interface:
        if len(drawing_functions.item_info_window) != 0:
            if ui_elements.name != "star power":
                screen.blit(ui_elements.surf, ui_elements.rect)
        else:
            screen.blit(ui_elements.surf, ui_elements.rect)

    if len(drawing_functions.loot_popup_container) > 0:
        for popup in drawing_functions.loot_popup_container:
            screen.blit(popup.surf, popup.rect)
    if len(drawing_functions.loot_text_container) > 0:
        for loot_text in drawing_functions.loot_text_container:
            screen.blit(loot_text[0], loot_text[1])

    screen.blit(bar_backdrop.surf, bar_backdrop.rect)
    screen.blit(hp_bar.surf, hp_bar.rect)
    screen.blit(en_bar.surf, en_bar.rect)
    screen.blit(xp_bar.surf, xp_bar.rect)

    # draw texts to the screen, like message box, player rupees and level, inv and equ updates
    drawing_functions.text_info_draw(screen, player, font, info_text_1, info_text_2, info_text_3, info_text_4,
                                     in_over_world)
    drawing_functions.draw_it(screen)

    if player.y_coordinate <= 75:
        player.current_zone = "marrow ramps west"
        in_over_world = True
        player.x_coordinate = 515
        player.y_coordinate = 650
        player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))

    sub_marrow_return = {"over_world_song_set": over_world_song_set, "npc_tic": npc_tic, "in_battle": in_battle,
                         "info_text_1": info_text_1, "info_text_2": info_text_2, "info_text_3": info_text_3,
                         "info_text_4": info_text_4, "interacted": interacted, "in_over_world": in_over_world,
                         "movement_able": movement_able}

    return sub_marrow_return
