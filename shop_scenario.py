import drawing_functions


# go through shop items and assign inventory slots (coordinates) to them
def shop_keeper_inventory_draw(npc_amuna_shopkeeper, shopkeeper_items, basic_armor, forged_armor, mythical_armor,
                               cookie, candy, tart, small_health, small_energy, seldon_firework, korlok_firework,
                               eldream_firework, seldon_bait, korlok_bait, eldream_bait):

    # if shopkeeper has items in their inventory
    if len(npc_amuna_shopkeeper.items) > 0:
        buy_first_coord = 810
        buy_second_coord = 435

        buy_inventory_counter = 0
        for shop_item in npc_amuna_shopkeeper.items:
            if shop_item.name == "small health potion":
                shop_item.update(buy_first_coord, buy_second_coord, small_health)
                shopkeeper_items.append(shop_item)
                buy_inventory_counter += 1
            if shop_item.name == "small energy potion":
                shop_item.update(buy_first_coord, buy_second_coord, small_energy)
                shopkeeper_items.append(shop_item)
                buy_inventory_counter += 1
            if shop_item.name == "basic armor":
                shop_item.update(buy_first_coord, buy_second_coord, basic_armor)
                shopkeeper_items.append(shop_item)
                buy_inventory_counter += 1
            if shop_item.name == "forged armor":
                shop_item.update(buy_first_coord, buy_second_coord, forged_armor)
                shopkeeper_items.append(shop_item)
                buy_inventory_counter += 1
            if shop_item.name == "mythical armor":
                shop_item.update(buy_first_coord, buy_second_coord, mythical_armor)
                shopkeeper_items.append(shop_item)
                buy_inventory_counter += 1
            if shop_item.name == "pet cookie":
                shop_item.update(buy_first_coord, buy_second_coord, cookie)
                shopkeeper_items.append(shop_item)
                buy_inventory_counter += 1
            if shop_item.name == "pet candy":
                shop_item.update(buy_first_coord, buy_second_coord, candy)
                shopkeeper_items.append(shop_item)
                buy_inventory_counter += 1
            if shop_item.name == "pet tart":
                shop_item.update(buy_first_coord, buy_second_coord, tart)
                shopkeeper_items.append(shop_item)
                buy_inventory_counter += 1
            if shop_item.name == "seldon firework":
                shop_item.update(buy_first_coord, buy_second_coord, seldon_firework)
                shopkeeper_items.append(shop_item)
                buy_inventory_counter += 1
            if shop_item.name == "korlok firework":
                shop_item.update(buy_first_coord, buy_second_coord, korlok_firework)
                shopkeeper_items.append(shop_item)
                buy_inventory_counter += 1
            if shop_item.name == "eldream firework":
                shop_item.update(buy_first_coord, buy_second_coord, eldream_firework)
                shopkeeper_items.append(shop_item)
                buy_inventory_counter += 1
            if shop_item.name == "seldon bait":
                shop_item.update(buy_first_coord, buy_second_coord, seldon_bait)
                shopkeeper_items.append(shop_item)
                buy_inventory_counter += 1
            if shop_item.name == "korlok bait":
                shop_item.update(buy_first_coord, buy_second_coord, korlok_bait)
                shopkeeper_items.append(shop_item)
                buy_inventory_counter += 1
            if shop_item.name == "eldream bait":
                shop_item.update(buy_first_coord, buy_second_coord, eldream_bait)
                shopkeeper_items.append(shop_item)
                buy_inventory_counter += 1
            buy_first_coord += 58
            if buy_inventory_counter > 3:
                buy_second_coord += 58
                buy_first_coord = 810
                buy_inventory_counter = 0


def sell_items(pygame, player, sell_choice, current_sell_item, sfx_sell):
    sell_return = {"info 1": "", "info 2": "", "sold": False}
    if sell_choice == "yes":
        # ensures sell confirmation button can only be selected when confirmation window is drawn
        if len(drawing_functions.sell_info_window) > 0:
            try:
                if current_sell_item.name == "small health potion":
                    sell_return["info 1"] = "Sold Small Health Potion for 5 rupees."
                    sell_return["info 2"] = "Small Health Potion removed from inventory."
                    player.items.remove(current_sell_item)
                    drawing_functions.player_items.remove(current_sell_item)
                    pygame.mixer.find_channel(True).play(sfx_sell)
                    player.rupees = player.rupees + 5
                    sell_return["sold"] = True
                    drawing_functions.sell_info_window.clear()
                if current_sell_item.name == "small energy potion":
                    sell_return["info 1"] = "Sold Small Energy Potion for 5 rupees."
                    sell_return["info 2"] = "Small Energy Potion removed from inventory."
                    player.items.remove(current_sell_item)
                    drawing_functions.player_items.remove(current_sell_item)
                    pygame.mixer.find_channel(True).play(sfx_sell)
                    player.rupees = player.rupees + 5
                    sell_return["sold"] = True
                    drawing_functions.sell_info_window.clear()
                if current_sell_item.name == "shiny rock":
                    sell_return["info 1"] = "Sold Shiny Rock for 5 rupees."
                    sell_return["info 2"] = "Shiny Rock removed from inventory."
                    player.items.remove(current_sell_item)
                    drawing_functions.player_items.remove(current_sell_item)
                    pygame.mixer.find_channel(True).play(sfx_sell)
                    player.rupees = player.rupees + 5
                    sell_return["sold"] = True
                    drawing_functions.sell_info_window.clear()
                if current_sell_item.name == "bone dust":
                    sell_return["info 1"] = "Sold Bone Dust for 10 rupees."
                    sell_return["info 2"] = "Bone Dust removed from inventory."
                    player.items.remove(current_sell_item)
                    drawing_functions.player_items.remove(current_sell_item)
                    pygame.mixer.find_channel(True).play(sfx_sell)
                    player.rupees = player.rupees + 10
                    sell_return["sold"] = True
                    drawing_functions.sell_info_window.clear()
                if current_sell_item.name == "cracked ember":
                    sell_return["info 1"] = "Sold Cracked Ember for 25 rupees."
                    sell_return["info 2"] = "Cracked Ember removed from inventory."
                    player.items.remove(current_sell_item)
                    drawing_functions.player_items.remove(current_sell_item)
                    pygame.mixer.find_channel(True).play(sfx_sell)
                    player.rupees = player.rupees + 25
                    sell_return["sold"] = True
                    drawing_functions.sell_info_window.clear()
                if current_sell_item.name == "broken band":
                    sell_return["info 1"] = "Sold Broken Band for 20 rupees."
                    sell_return["info 2"] = "Broken Band removed from inventory."
                    player.items.remove(current_sell_item)
                    drawing_functions.player_items.remove(current_sell_item)
                    pygame.mixer.find_channel(True).play(sfx_sell)
                    player.rupees = player.rupees + 20
                    sell_return["sold"] = True
                    drawing_functions.sell_info_window.clear()
                if current_sell_item.name == "dried fins":
                    sell_return["info 1"] = "Sold Dried Fins for 40 rupees."
                    sell_return["info 2"] = "Dried Fins removed from inventory."
                    player.items.remove(current_sell_item)
                    drawing_functions.player_items.remove(current_sell_item)
                    pygame.mixer.find_channel(True).play(sfx_sell)
                    player.rupees = player.rupees + 40
                    sell_return["sold"] = True
                    drawing_functions.sell_info_window.clear()
                if current_sell_item.name == "oscura pluma":
                    sell_return["info 1"] = "Sold Oscura Pluma for 45 rupees."
                    sell_return["info 2"] = "Oscura Pluma removed from inventory."
                    player.items.remove(current_sell_item)
                    drawing_functions.player_items.remove(current_sell_item)
                    pygame.mixer.find_channel(True).play(sfx_sell)
                    player.rupees = player.rupees + 45
                    sell_return["sold"] = True
                    drawing_functions.sell_info_window.clear()
                if current_sell_item.name == "basic armor":
                    sell_return["info 1"] = "Sold Basic Armor for 25 rupees."
                    sell_return["info 2"] = "Basic Armor removed from inventory."
                    player.items.remove(current_sell_item)
                    drawing_functions.player_items.remove(current_sell_item)
                    pygame.mixer.find_channel(True).play(sfx_sell)
                    player.rupees = player.rupees + 25
                    sell_return["sold"] = True
                    drawing_functions.sell_info_window.clear()
                if current_sell_item.name == "forged armor":
                    sell_return["info 1"] = "Sold Forged Armor for 100 rupees."
                    sell_return["info 2"] = "Forged Armor removed from inventory."
                    player.items.remove(current_sell_item)
                    drawing_functions.player_items.remove(current_sell_item)
                    pygame.mixer.find_channel(True).play(sfx_sell)
                    player.rupees = player.rupees + 100
                    sell_return["sold"] = True
                    drawing_functions.sell_info_window.clear()
                if current_sell_item.name == "mythical armor":
                    sell_return["info 1"] = "Sold Mythical Armor for 250 rupees."
                    sell_return["info 2"] = "Mythical Armor removed from inventory."
                    player.items.remove(current_sell_item)
                    drawing_functions.player_items.remove(current_sell_item)
                    pygame.mixer.find_channel(True).play(sfx_sell)
                    player.rupees = player.rupees + 250
                    sell_return["sold"] = True
                    drawing_functions.sell_info_window.clear()
                if current_sell_item.name == "pet cookie":
                    sell_return["info 1"] = "Sold Blueberry Cookie for 10 rupees."
                    sell_return["info 2"] = "Blueberry Cookie removed from inventory."
                    player.items.remove(current_sell_item)
                    drawing_functions.player_items.remove(current_sell_item)
                    pygame.mixer.find_channel(True).play(sfx_sell)
                    player.rupees = player.rupees + 10
                    sell_return["sold"] = True
                    drawing_functions.sell_info_window.clear()
                if current_sell_item.name == "pet candy":
                    sell_return["info 1"] = "Sold Rock Candy for 10 rupees."
                    sell_return["info 2"] = "Rock Candy removed from inventory."
                    player.items.remove(current_sell_item)
                    drawing_functions.player_items.remove(current_sell_item)
                    pygame.mixer.find_channel(True).play(sfx_sell)
                    player.rupees = player.rupees + 10
                    sell_return["sold"] = True
                    drawing_functions.sell_info_window.clear()
                if current_sell_item.name == "pet tart":
                    sell_return["info 1"] = "Sold Peach Tart for 10 rupees."
                    sell_return["info 2"] = "Peach Tart removed from inventory."
                    player.items.remove(current_sell_item)
                    drawing_functions.player_items.remove(current_sell_item)
                    pygame.mixer.find_channel(True).play(sfx_sell)
                    player.rupees = player.rupees + 10
                    sell_return["sold"] = True
                    drawing_functions.sell_info_window.clear()
                if current_sell_item.name == "bone shard":
                    sell_return["info 1"] = "Sold Bone Shard for 60 rupees."
                    sell_return["info 2"] = "Bone Shard removed from inventory."
                    player.items.remove(current_sell_item)
                    drawing_functions.player_items.remove(current_sell_item)
                    pygame.mixer.find_channel(True).play(sfx_sell)
                    player.rupees = player.rupees + 60
                    sell_return["sold"] = True
                    drawing_functions.sell_info_window.clear()
                if current_sell_item.name == "seldon firework":
                    sell_return["info 1"] = "Sold Firework for 10 rupees."
                    sell_return["info 2"] = "Firework removed from inventory."
                    player.items.remove(current_sell_item)
                    drawing_functions.player_items.remove(current_sell_item)
                    pygame.mixer.find_channel(True).play(sfx_sell)
                    player.rupees = player.rupees + 10
                    sell_return["sold"] = True
                    drawing_functions.sell_info_window.clear()
                if current_sell_item.name == "korlok firework":
                    sell_return["info 1"] = "Sold Firework for 10 rupees."
                    sell_return["info 2"] = "Firework removed from inventory."
                    player.items.remove(current_sell_item)
                    drawing_functions.player_items.remove(current_sell_item)
                    pygame.mixer.find_channel(True).play(sfx_sell)
                    player.rupees = player.rupees + 10
                    sell_return["sold"] = True
                    drawing_functions.sell_info_window.clear()
                if current_sell_item.name == "eldream firework":
                    sell_return["info 1"] = "Sold Firework for 10 rupees."
                    sell_return["info 2"] = "Firework removed from inventory."
                    player.items.remove(current_sell_item)
                    drawing_functions.player_items.remove(current_sell_item)
                    pygame.mixer.find_channel(True).play(sfx_sell)
                    player.rupees = player.rupees + 10
                    sell_return["sold"] = True
                    drawing_functions.sell_info_window.clear()
                if current_sell_item.name == "seldon bait":
                    sell_return["info 1"] = "Sold Bait for 5 rupees."
                    sell_return["info 2"] = "Bait removed from inventory."
                    player.items.remove(current_sell_item)
                    drawing_functions.player_items.remove(current_sell_item)
                    pygame.mixer.find_channel(True).play(sfx_sell)
                    player.rupees = player.rupees + 5
                    sell_return["sold"] = True
                    drawing_functions.sell_info_window.clear()
                if current_sell_item.name == "korlok bait":
                    sell_return["info 1"] = "Sold Bait for 5 rupees."
                    sell_return["info 2"] = "Bait removed from inventory."
                    player.items.remove(current_sell_item)
                    drawing_functions.player_items.remove(current_sell_item)
                    pygame.mixer.find_channel(True).play(sfx_sell)
                    player.rupees = player.rupees + 5
                    sell_return["sold"] = True
                    drawing_functions.sell_info_window.clear()
                if current_sell_item.name == "eldream bait":
                    sell_return["info 1"] = "Sold Bait for 5 rupees."
                    sell_return["info 2"] = "Bait removed from inventory."
                    player.items.remove(current_sell_item)
                    drawing_functions.player_items.remove(current_sell_item)
                    pygame.mixer.find_channel(True).play(sfx_sell)
                    player.rupees = player.rupees + 5
                    sell_return["sold"] = True
                    drawing_functions.sell_info_window.clear()
                if current_sell_item.name == "marrow bait":
                    sell_return["info 1"] = "Sold Bait for 75 rupees."
                    sell_return["info 2"] = "Bait removed from inventory."
                    player.items.remove(current_sell_item)
                    drawing_functions.player_items.remove(current_sell_item)
                    pygame.mixer.find_channel(True).play(sfx_sell)
                    player.rupees = player.rupees + 75
                    sell_return["sold"] = True
                    drawing_functions.sell_info_window.clear()
            except AttributeError:
                pass
    if sell_choice == "no":
        drawing_functions.sell_info_window.clear()

    return sell_return


def buy_items(pygame, player, buy_choice, current_buy_item, Item, health_pot_img, energy_pot_img, basic_armor,
              forged_armor, mythical_armor, cookie, candy, tart, sfx_buy, seldon_firework, korlok_firework,
              eldream_firework, seldon_bait, korlok_bait, eldream_bait):
    buy_return = {"info 1": "", "info 2": "", "bought": False}

    if buy_choice == "yes":
        if current_buy_item.name == "small health potion":
            if len(player.items) < 16:
                if player.rupees > 9:
                    buy_return["info 1"] = "You Bought Small Health Potion for 10 rupees."
                    buy_return["info 2"] = "Small Health Potion added to inventory."
                    player.items.append(Item("small health potion", "potion", 200, 200, health_pot_img, 0))
                    player.rupees = player.rupees - 10
                    pygame.mixer.find_channel(True).play(sfx_buy)
                    buy_return["bought"] = True
                else:
                    buy_return["info 1"] = "You do not have enough rupees."
                    buy_return["info 2"] = "Small Health Potion cost 10 rupees."
            else:
                buy_return["info 1"] = "Your inventory is full."
                buy_return["info 2"] = ""

        if current_buy_item.name == "small energy potion":
            if len(player.items) < 16:
                if player.rupees > 9:
                    buy_return["info 1"] = "Bought Small Energy Potion for 10 rupees."
                    buy_return["info 2"] = "Small Energy Potion added to inventory."
                    player.items.append(Item("small energy potion", "potion", 200, 200, energy_pot_img, 0))
                    player.rupees = player.rupees - 10
                    pygame.mixer.find_channel(True).play(sfx_buy)
                    buy_return["bought"] = True
                else:
                    buy_return["info 1"] = "You do not have enough rupees."
                    buy_return["info 2"] = "Small Energy Potion cost 10 rupees."
            else:
                buy_return["info 1"] = "Your inventory is full."
                buy_return["info 2"] = ""

        if current_buy_item.name == "basic armor":
            if len(player.items) < 16:
                if player.rupees > 49:
                    buy_return["info 1"] = "Bought Basic Armor for 50 rupees."
                    buy_return["info 2"] = "Basic Armor added to inventory."
                    player.items.append(Item("basic armor", "armor", 200, 200, basic_armor, 1))
                    player.rupees = player.rupees - 50
                    pygame.mixer.find_channel(True).play(sfx_buy)
                    buy_return["bought"] = True
                else:
                    buy_return["info 1"] = "You do not have enough rupees."
                    buy_return["info 2"] = "Basic Armor cost 50 rupees."
            else:
                buy_return["info 1"] = "Your inventory is full."
                buy_return["info 2"] = ""

        if current_buy_item.name == "forged armor":
            if len(player.items) < 16:
                if player.rupees > 149:
                    buy_return["info 1"] = "Bought Forged Armor for 150 rupees."
                    buy_return["info 2"] = "Forged Armor added to inventory."
                    player.items.append(Item("forged armor", "armor", 200, 200, forged_armor, 2))
                    player.rupees = player.rupees - 150
                    pygame.mixer.find_channel(True).play(sfx_buy)
                    buy_return["bought"] = True
                else:
                    buy_return["info 1"] = "You do not have enough rupees."
                    buy_return["info 2"] = "Forged Armor cost 200 rupees."
            else:
                buy_return["info 1"] = "Your inventory is full."
                buy_return["info 2"] = ""

        if current_buy_item.name == "mythical armor":
            if len(player.items) < 16:
                if player.rupees > 299:
                    buy_return["info 1"] = "Bought Mythical Armor for 300 rupees."
                    buy_return["info 2"] = "Mythical Armor added to inventory."
                    player.items.append(Item("mythical armor", "armor", 200, 200, mythical_armor, 3))
                    player.rupees = player.rupees - 300
                    pygame.mixer.find_channel(True).play(sfx_buy)
                    buy_return["bought"] = True
                else:
                    buy_return["info 1"] = "You do not have enough rupees."
                    buy_return["info 2"] = "Mythical Armor cost 300 rupees."
            else:
                buy_return["info 1"] = "Your inventory is full."
                buy_return["info 2"] = ""

        if current_buy_item.name == "pet cookie":
            if len(player.items) < 16:
                if player.rupees > 19:
                    buy_return["info 1"] = "Bought Blueberry Cookie for 20 rupees."
                    buy_return["info 2"] = "Blueberry Cookie added to inventory."
                    player.items.append(Item("pet cookie", "cookie", 1078, 197, cookie, 1))
                    player.rupees = player.rupees - 20
                    pygame.mixer.find_channel(True).play(sfx_buy)
                    buy_return["bought"] = True
                else:
                    buy_return["info 1"] = "You do not have enough rupees."
                    buy_return["info 2"] = "Blueberry Cookie cost 20 rupees."
            else:
                buy_return["info 1"] = "Your inventory is full."
                buy_return["info 2"] = ""

        if current_buy_item.name == "pet candy":
            if len(player.items) < 16:
                if player.rupees > 19:
                    buy_return["info 1"] = "Bought Rock Candy for 20 rupees."
                    buy_return["info 2"] = "Rock Candy added to inventory."
                    player.items.append(Item("pet candy", "candy", 1078, 197, candy, 1))
                    player.rupees = player.rupees - 20
                    pygame.mixer.find_channel(True).play(sfx_buy)
                    buy_return["bought"] = True
                else:
                    buy_return["info 1"] = "You do not have enough rupees."
                    buy_return["info 2"] = "Rock Candy cost 20 rupees."
            else:
                buy_return["info 1"] = "Your inventory is full."
                buy_return["info 2"] = ""

        if current_buy_item.name == "pet tart":
            if len(player.items) < 16:
                if player.rupees > 19:
                    buy_return["info 1"] = "Bought Peach Tart for 20 rupees."
                    buy_return["info 2"] = "Peach Tart added to inventory."
                    player.items.append(Item("pet tart", "tart", 1078, 197, tart, 1))
                    player.rupees = player.rupees - 20
                    pygame.mixer.find_channel(True).play(sfx_buy)
                    buy_return["bought"] = True
                else:
                    buy_return["info 1"] = "You do not have enough rupees."
                    buy_return["info 2"] = "Peach Tart cost 20 rupees."
            else:
                buy_return["info 1"] = "Your inventory is full."
                buy_return["info 2"] = ""

        if current_buy_item.name == "seldon firework":
            if len(player.items) < 16:
                if player.rupees > 24:
                    if player.reputation["amuna"] >= 20:
                        buy_return["info 1"] = "Bought Firework for 25 rupees."
                        buy_return["info 2"] = "Firework added to inventory."
                        player.items.append(Item("seldon firework", "firework", 200, 200, seldon_firework, 0))
                        player.rupees = player.rupees - 25
                        pygame.mixer.find_channel(True).play(sfx_buy)
                        buy_return["bought"] = True
                    else:
                        buy_return["info 1"] = "You need more reputation."
                        buy_return["info 2"] = "20 Reputation with Amuna required."
                else:
                    buy_return["info 1"] = "You do not have enough rupees."
                    buy_return["info 2"] = "Firework cost 25 rupees."
            else:
                buy_return["info 1"] = "Your inventory is full."
                buy_return["info 2"] = ""

        if current_buy_item.name == "korlok firework":
            if len(player.items) < 16:
                if player.rupees > 24:
                    if player.reputation["nuldar"] >= 20:
                        buy_return["info 1"] = "Bought Firework for 25 rupees."
                        buy_return["info 2"] = "Firework added to inventory."
                        player.items.append(Item("korlok firework", "firework", 200, 200, korlok_firework, 0))
                        player.rupees = player.rupees - 25
                        pygame.mixer.find_channel(True).play(sfx_buy)
                        buy_return["bought"] = True
                    else:
                        buy_return["info 1"] = "You need more reputation."
                        buy_return["info 2"] = "20 Reputation with Nuldar required."
                else:
                    buy_return["info 1"] = "You do not have enough rupees."
                    buy_return["info 2"] = "Firework cost 25 rupees."
            else:
                buy_return["info 1"] = "Your inventory is full."
                buy_return["info 2"] = ""

        if current_buy_item.name == "eldream firework":
            if len(player.items) < 16:
                if player.rupees > 24:
                    if player.reputation["sorae"] >= 20:
                        buy_return["info 1"] = "Bought Firework for 25 rupees."
                        buy_return["info 2"] = "Firework added to inventory."
                        player.items.append(Item("eldream firework", "firework", 200, 200, eldream_firework, 0))
                        player.rupees = player.rupees - 25
                        pygame.mixer.find_channel(True).play(sfx_buy)
                        buy_return["bought"] = True
                    else:
                        buy_return["info 1"] = "You need more reputation."
                        buy_return["info 2"] = "20 Reputation with Sorae required."
                else:
                    buy_return["info 1"] = "You do not have enough rupees."
                    buy_return["info 2"] = "Firework cost 25 rupees."
            else:
                buy_return["info 1"] = "Your inventory is full."
                buy_return["info 2"] = ""

        if current_buy_item.name == "seldon bait":
            if len(player.items) < 16:
                if player.rupees > 9:
                    if player.reputation["amuna"] >= 30:
                        buy_return["info 1"] = "Bought Bait for 10 rupees."
                        buy_return["info 2"] = "Bait added to inventory."
                        player.items.append(Item("seldon bait", "bait", 200, 200, seldon_bait, 0))
                        player.rupees = player.rupees - 10
                        pygame.mixer.find_channel(True).play(sfx_buy)
                        buy_return["bought"] = True
                    else:
                        buy_return["info 1"] = "You need more reputation."
                        buy_return["info 2"] = "30 Reputation with Amuna required."
                else:
                    buy_return["info 1"] = "You do not have enough rupees."
                    buy_return["info 2"] = "Bait cost 10 rupees."
            else:
                buy_return["info 1"] = "Your inventory is full."
                buy_return["info 2"] = ""

        if current_buy_item.name == "korlok bait":
            if len(player.items) < 16:
                if player.rupees > 9:
                    if player.reputation["nuldar"] >= 30:
                        buy_return["info 1"] = "Bought Bait for 10 rupees."
                        buy_return["info 2"] = "Bait added to inventory."
                        player.items.append(Item("korlok bait", "bait", 200, 200, korlok_bait, 0))
                        player.rupees = player.rupees - 10
                        pygame.mixer.find_channel(True).play(sfx_buy)
                        buy_return["bought"] = True
                    else:
                        buy_return["info 1"] = "You need more reputation."
                        buy_return["info 2"] = "30 Reputation with Nuldar required."
                else:
                    buy_return["info 1"] = "You do not have enough rupees."
                    buy_return["info 2"] = "Bait cost 10 rupees."
            else:
                buy_return["info 1"] = "Your inventory is full."
                buy_return["info 2"] = ""

        if current_buy_item.name == "eldream bait":
            if len(player.items) < 16:
                if player.rupees > 9:
                    if player.reputation["sorae"] >= 30:
                        buy_return["info 1"] = "Bought Bait for 10 rupees."
                        buy_return["info 2"] = "Bait added to inventory."
                        player.items.append(Item("eldream bait", "bait", 200, 200, eldream_bait, 0))
                        player.rupees = player.rupees - 10
                        pygame.mixer.find_channel(True).play(sfx_buy)
                        buy_return["bought"] = True
                    else:
                        buy_return["info 1"] = "You need more reputation."
                        buy_return["info 2"] = "30 Reputation with Sorae required."
                else:
                    buy_return["info 1"] = "You do not have enough rupees."
                    buy_return["info 2"] = "Bait cost 10 rupees."
            else:
                buy_return["info 1"] = "Your inventory is full."
                buy_return["info 2"] = ""

    if buy_choice == "no":
        drawing_functions.buy_info_window.clear()

    return buy_return
