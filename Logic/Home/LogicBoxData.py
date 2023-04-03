import random

class LogicBoxData:

    def randomize(self, type):
        self.box_rewards = { 'Rewards': [] }

        if (type == 10):
            check = False
            pon = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,34,35,36,37,38,39,40,41,42,43,44,45,46,47]
            srawl = random.choice(pon)

            if (random.randint(0,100) < 20):
                locked_brawlers = sorted(set(self.player.brawlers_id) - set(self.player.brawlers_unlocked))
                if (locked_brawlers):
                    brawler = random.choice(locked_brawlers)
                    brawler_reward = {'Amount': 1, 'DataRef': [16, srawl], 'Value': 1}
                    self.box_rewards['Rewards'].append(brawler_reward)
                    if srawl not in self.player.brawlers_unlocked:
                        self.player.brawlers_unlocked.append(srawl)
                        self.player.db.update_player_account(self.player.token, 'UnlockedBrawlers',self.player.brawlers_unlocked)
                    check = True

            if (random.randint(0,100) < 100) and not check:
                gold_value = random.randint(20, 100)
                gold_reward = {'Amount': gold_value, 'DataRef': [0, 0], 'Value': 7}
                self.box_rewards['Rewards'].append(gold_reward)
                self.player.resources[1]['Amount'] = self.player.resources[1]['Amount'] + gold_value
                self.player.db.update_player_account(self.player.token, 'Resources', self.player.resources)
                rewarded = []
                for x in range(1):
                    pp_value = random.randint(5, 30)
                    brawler = random.choice(sorted(set(self.player.brawlers_unlocked) - set(rewarded)))
                    if (self.player.brawlers_level[str(srawl)] < 8):
 
                         
                        self.player.brawlers_powerpoints[str(srawl)] = self.player.brawlers_powerpoints[ str(srawl)] + pp_value
                        self.player.db.update_player_account(self.player.token, 'BrawlersPowerPoints', self.player.brawlers_powerpoints)
                        rewarded.append(srawl)

            if (random.randint(0,100) < 30):
                bonus = random.choice([2, 8])
                if (bonus == 8):
                    bonus_value = random.randint(5, 15)
                    self.player.gems = self.player.gems + bonus_value
                    self.player.db.update_player_account(self.player.token, 'Gems', self.player.gems)
                else:
                    bonus_value = random.randint(20, 50)
                    self.player.token_doubler = self.player.token_doubler + bonus_value
                    self.player.db.update_player_account(self.player.token, 'TokenDoubler', self.player.token_doubler)
 



        elif (type == 12):
            check = False
            pon = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,34,35,36,37,38,39,40,41,42,43,44,45,46,47]
            srawl = random.choice(pon)

            if (random.randint(0,100) < 20):
                locked_brawlers = sorted(set(self.player.brawlers_id) - set(self.player.brawlers_unlocked))
                if (locked_brawlers):
                    brawler = random.choice(locked_brawlers)
                    brawler_reward = {'Amount': 1, 'DataRef': [16, srawl], 'Value': 1}
                    self.box_rewards['Rewards'].append(brawler_reward)
                    if srawl not in self.player.brawlers_unlocked:
                        self.player.brawlers_unlocked.append(srawl)
                        self.player.db.update_player_account(self.player.token, 'UnlockedBrawlers',self.player.brawlers_unlocked)
                    check = True

            if (random.randint(0,100) < 100) and not check:
                gold_value = random.randint(50, 150)
                gold_reward = {'Amount': gold_value, 'DataRef': [0, 0], 'Value': 7}
                self.box_rewards['Rewards'].append(gold_reward)
                self.player.resources[1]['Amount'] = self.player.resources[1]['Amount'] + gold_value
                self.player.db.update_player_account(self.player.token, 'Resources', self.player.resources)
                rewarded = []
                for x in range(1):
                    pp_value = random.randint(30, 50)
                    brawler = random.choice(sorted(set(self.player.brawlers_unlocked) - set(rewarded)))
                    if (self.player.brawlers_level[str(srawl)] < 8):
 
                         
                        self.player.brawlers_powerpoints[str(srawl)] = self.player.brawlers_powerpoints[ str(srawl)] + pp_value
                        self.player.db.update_player_account(self.player.token, 'BrawlersPowerPoints', self.player.brawlers_powerpoints)
                        rewarded.append(srawl)

            if (random.randint(0,100) < 35):
                bonus = random.choice([2, 8])
                if (bonus == 8):
                    bonus_value = random.randint(10, 20)
                    self.player.gems = self.player.gems + bonus_value
                    self.player.db.update_player_account(self.player.token, 'Gems', self.player.gems)
                else:
                    bonus_value = random.randint(20, 50)
                    self.player.token_doubler = self.player.token_doubler + bonus_value
                    self.player.db.update_player_account(self.player.token, 'TokenDoubler', self.player.token_doubler)
 


        elif (type == 11):
            srawl = random.randint(1, 48)
            if (random.randint(0,100) < 100):
                gold_value = random.randint(100, 500)
                gold_reward = {'Amount': gold_value, 'DataRef': [0, 0], 'Value': 7}
                self.box_rewards['Rewards'].append(gold_reward)

                self.player.resources[1]['Amount'] = self.player.resources[1]['Amount'] + gold_value
                self.player.db.update_player_account(self.player.token, 'Resources', self.player.resources)

                if len(self.player.brawlers_unlocked) in [1, 2, 3, 4]:
                    rewarded = []
                    for x in range(len(self.player.brawlers_unlocked)):
                        pp_value = random.randint(50, 150)
                        brawler = random.choice(sorted(set(self.player.brawlers_unlocked) - set(rewarded)))
                        if (self.player.brawlers_level[str(srawl)] < 8):
     
                             
                            self.player.brawlers_powerpoints[str(srawl)] = self.player.brawlers_powerpoints[ str(srawl)] + pp_value
                            self.player.db.update_player_account(self.player.token, 'BrawlersPowerPoints', self.player.brawlers_powerpoints)
                            rewarded.append(brawler)
                else:
                    rewarded = []
                    for x in range(random.choice([4, 5])):
                        pp_value = random.randint(50, 150)
                        brawler = random.choice(sorted(set(self.player.brawlers_unlocked) - set(rewarded)))
                        if (self.player.brawlers_level[str(srawl)] < 8):
     
                             
                            self.player.brawlers_powerpoints[str(srawl)] = self.player.brawlers_powerpoints[ str(srawl)] + pp_value
                            self.player.db.update_player_account(self.player.token, 'BrawlersPowerPoints', self.player.brawlers_powerpoints)
                            rewarded.append(brawler)

            if (random.randint(0,100) < 55):
                locked_brawlers = sorted(set(self.player.brawlers_id) - set(self.player.brawlers_unlocked))
                if (locked_brawlers):
                    brawler = random.choice(locked_brawlers)
                    brawler_reward = {'Amount': 1, 'DataRef': [16, srawl], 'Value': 1}
                    self.box_rewards['Rewards'].append(brawler_reward)
                    if srawl not in self.player.brawlers_unlocked:
                        self.player.brawlers_unlocked.append(srawl)
                        self.player.db.update_player_account(self.player.token, 'UnlockedBrawlers', self.player.brawlers_unlocked)

            if (random.randint(0,100) < 50):
                bonus = random.choice([2, 8])
                if (bonus == 8):
                    bonus_value = random.randint(10, 50)
                    self.player.gems = self.player.gems + bonus_value
                    self.player.db.update_player_account(self.player.token, 'Gems', self.player.gems)
                else:
                    bonus_value = random.randint(100, 400)
                    self.player.token_doubler = self.player.token_doubler + bonus_value
                    self.player.db.update_player_account(self.player.token, 'TokenDoubler', self.player.token_doubler)
 


        return self.box_rewards


