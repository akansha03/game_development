import random
class PokerCard:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return f'{self.rank['rank']} of {self.suit}'

class PokerDeck:
    def __init__(self):
        self.cards = []
        suits = ['hearts', 'spades', 'clubs', 'diamonds']
        ranks = [
            {'rank': 'A', 'value': 11},
            {'rank': '2', 'value': 2},
            {'rank': '3', 'value': 3},
            {'rank': '4', 'value': 4},
            {'rank': '5', 'value': 5},
            {'rank': '6', 'value': 6},
            {'rank': '7', 'value': 7},
            {'rank': '8', 'value': 8},
            {'rank': '9', 'value': 9},
            {'rank': '10', 'value': 10},
            {'rank': 'J', 'value': 10},
            {'rank': 'Q', 'value': 10},
            {'rank': 'K', 'value': 10}
        ]
        for suit in suits:
            for rank in ranks:
                self.cards.append(PokerCard(suit, rank))

    def get_card_rank(self, card):
        return card.rank['value']

    def shuffle_cards(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    def burn_card(self):
        if len(self.cards) > 1:
            self.cards.pop()

    def deal_community_card(self, stage):
        community_cards = []
        if stage == 'flop':
            for i in range(3):
                community_cards.append(self.cards.pop())
        elif stage in ['turn', 'river']:
            community_cards.append(self.cards.pop())
        return community_cards

    def distribute_two_hole_cards(self):
        hole_cards = []
        if len(self.cards) > 2:
            for i in range(2):
                hole_cards.append(self.cards.pop())
        return hole_cards

class Pot:
    def __init__(self):
        self.total = 0

    def calculate_pot_value(self, bet_value):
        self.total += bet_value

class PokerHand:
    def __init__(self):
        self.rank = 0
    '''
    def sort_hand(self, cards):
        sorted_cards = sorted(cards, key=lambda card: self.rank_order[card], reverse=True)
        return sorted_cards

    def evaluate_hand_ranking(self, card_list):

        if len(card_list) == 5:
            c1, c2, c3, c4, c5 = card_list[0], card_list[1], card_list[2], card_list[3], card_list[4]

            # Check all the conditions when suit is same
            if c1.suit == c2.suit and c2.suit == c3.suit and c3.suit == c4.suit and c4.suit == c5.suit:
                if c1.card == 'A' and c2.card == 'K' and c3.card == 'Q' and c4.card == 'J' and c5.card == '10':
                    print(f'Royal Flush - Unbeatable')
                    self.rank = 1
                elif self.get_card_rank(c1.card)-1 == self.get_card_rank(c2.card) and self.get_card_rank(c2.card)-1 == self.get_card_rank(c3.card) and self.get_card_rank(c3.card)-1 == self.get_card_rank(c4.card) and self.get_card_rank(c4.card)-1 == self.get_card_rank(c5.card):
                    print(f'Straight Flush')
                    self.rank = 2
                else:
                    print(f'Flush - five cards of the same suit')
                    self.rank = 5
            else:
                countF = defaultdict(int)
                maxF = 0
                for card, suit in card_list:
                    countF[card] += 1
                    maxF = max(maxF, countF[card])
                if maxF == 4:
                    print(f'Four of a kind : ')
                    self.rank = 3
                elif maxF == 3:
                    if len(countF) == 2:
                        print(f'Full House : ')
                        self.rank = 4
                    else:
                        print(f'Three of a Kind (Trips/Set)')
                        self.rank = 7
                elif maxF == 2:
                    print(f'Two Pair')
                    self.rank = 8
                elif maxF == 1:
                    print(f'One Pair')
                    self.rank = 9
                else:
                    if self.get_card_rank(c1.card)-1 == self.get_card_rank(c2.card) and self.get_card_rank(c2.card)-1 == self.get_card_rank(c3.card) and self.get_card_rank(c3.card)-1 == self.get_card_rank(c4.card) and self.get_card_rank(c4.card)-1 == self.get_card_rank(c5.card):
                        print(f'Straight')
                        self.rank = 6
                    else:
                        print('High Card')
                        self.rank = 10
            return self.rank
        return 0
        '''

class Player:
    def __init__(self, name, seat_pos, player_status, current_bet_in_round, has_acted_this_round=False,stacks=100, hole_cards=None):
        if hole_cards is None:
            hole_cards = []
        self.name = name
        self.seat_pos = seat_pos
        self.player_status = player_status
        self.current_bet_in_round = current_bet_in_round

        self.stacks = stacks
        self.hole_cards = hole_cards
        self.has_acted_this_round = has_acted_this_round
        self.total_invested_in_pot = 0


    def receive_hole_cards(self, hole_cards):
        self.hole_cards = hole_cards

    def player_betting_actions(self, action, highest_bet_in_round, raise_to_amount=0):

        if action == 'fold':
            self.player_status = 'Folded'
            return 0

        elif action == 'check' and highest_bet_in_round == self.current_bet_in_round:
            self.player_status = 'Active'
            return 0

        if self.stacks > self.current_bet_in_round:
            if action == 'call':
                amount_added = (highest_bet_in_round - self.current_bet_in_round)
                self.stacks -= amount_added
                self.current_bet_in_round = highest_bet_in_round
                self.total_invested_in_pot += amount_added
                self.player_status = 'Active'
                return amount_added
            elif action == 'raise' and raise_to_amount > highest_bet_in_round:
                amount_added = (raise_to_amount - self.current_bet_in_round)
                self.stacks -= amount_added
                self.current_bet_in_round = raise_to_amount
                self.total_invested_in_pot += amount_added
                self.player_status = 'Active'
                return amount_added
        elif self.stacks <= self.current_bet_in_round or action == 'all-in':
            amount_added = self.stacks

            self.current_bet_in_round += amount_added
            self.total_invested_in_pot += amount_added
            self.stacks = 0
            self.player_status = 'All-in'
            return amount_added
        return 0


class PokerGame:
    SMALL_BLIND = 5
    BIG_BLIND = 10
    def __init__(self):
        self.computer = Player('P1', 0, 'Active', 0)
        self.me = Player('P2', 1, 'Active', 0)

        self.deck = PokerDeck()
        self.pot = Pot()
        self.highest_bet_in_round = 0
        self.raise_to_amount = 0

        self.stages = ['preflop', 'flop', 'turn', 'river']
        self.current_in_stage = 'preflop'

        self.is_hand_over = False
        self.community_cards = []
        self.dealer_pos = 0

    def post_blinds(self):

        small_blind = self.computer if self.dealer_pos == 0 else self.me
        big_blind = self.me if self.dealer_pos == 0 else self.computer

        small_blind.current_bet_in_round = PokerGame.SMALL_BLIND
        small_blind.stacks -= PokerGame.SMALL_BLIND
        small_blind.total_invested_in_pot = PokerGame.SMALL_BLIND

        big_blind.current_bet_in_round = PokerGame.BIG_BLIND
        big_blind.stacks -= PokerGame.BIG_BLIND
        big_blind.total_invested_in_pot = PokerGame.BIG_BLIND

        self.pot.total += (PokerGame.SMALL_BLIND + PokerGame.BIG_BLIND)
        self.highest_bet_in_round = PokerGame.BIG_BLIND

    def start_new_hand(self):
        # reset the hand
        self.is_hand_over = False
        self.current_in_stage = 'preflop'
        self.community_cards = []
        self.pot.total = 0
        self.highest_bet_in_round = 0

        self.deck = PokerDeck()
        self.deck.shuffle_cards()
        self.computer.hole_cards = self.me.hole_cards = []
        self.computer.player_status = self.me.player_status = 'Active'

        self.computer.current_bet_in_round = self.me.current_bet_in_round = 0
        self.computer.has_acted_this_round = self.me.has_acted_this_round = False
        self.computer.total_invested_in_pot = self.me.total_invested_in_pot = 0

        self.post_blinds()
        self.computer.receive_hole_cards(self.deck.distribute_two_hole_cards())
        self.me.receive_hole_cards(self.deck.distribute_two_hole_cards())

    def is_betting_round_complete(self):

        #Betting will keep on happening until there is an active user, others have not folded and current_bets are matched

        # Check for the number of active users
        active_users = 0
        if self.computer.player_status == 'Active':
            active_users += 1
        if self.me.player_status == 'Active':
            active_users += 1

        # If there are no active users or just one that means we have a winner and no need to go further in the round
        if active_users <=1:
            return True

        has_acted = self.computer.has_acted_this_round and self.me.has_acted_this_round
        match_current_bet = self.computer.current_bet_in_round == self.me.current_bet_in_round
        return has_acted and match_current_bet

    def get_computer_actions(self):

        if self.highest_bet_in_round == self.computer.current_bet_in_round:
            return 'check', 0

        # If bet is smaller
        amount_to_call = self.highest_bet_in_round - self.computer.current_bet_in_round
        if amount_to_call<=20:
            return 'call', 0
        else:
            return 'fold', 0

    def get_player_actions(self):

        # Check for the valid actions
        valid_actions = []

        if self.highest_bet_in_round == self.me.current_bet_in_round:
            valid_actions = ['check', 'raise', 'fold']
        else:
            valid_actions = ['call', 'raise', 'fold']

        print(f'Valid actions : ${valid_actions}')
        print(f'Your current bet : ${self.me.current_bet_in_round}')
        print(f'Highest Bet : ${self.highest_bet_in_round}')
        print(f'Your chips : ${self.me.stacks}')

        action = input("Your action : ").lower()

        # Check if the action is a valid action or not - if not then keep it in a loop
        while action not in valid_actions:
            action = input(f'Invalid action : Please re-enter based on these ${valid_actions}').lower()

        raise_to_amount = 0
        if action == 'raise':
            min_raise = self.highest_bet_in_round + 10
            raise_to_amount = int(input(f'Enter the amount to raise : '))
            while raise_to_amount<min_raise:
                raise_to_amount = int(input(f'Re-enter the amount to raise - should be more than ${min_raise}'))
            self.highest_bet_in_round = raise_to_amount
        return action, raise_to_amount


    def conduct_betting_round(self, stage):

        # Get the position of the players - In case of the preflop dealer will always make the first move
        if self.current_in_stage == stage:
            current_pos  = self.dealer_pos
        else:
            current_pos = (self.dealer_pos + 1) % 2

        while not self.is_betting_round_complete():
            current_player = self.computer if current_pos == 0 else self.me
            # Check if the current player is Active or not, if not then move to the next player
            if current_player.player_status not in ['Active']:
                current_pos = (current_pos + 1) % 2
                continue

            if current_player == self.computer:
                action, raise_amount = self.get_computer_actions()
            else:
                action, raise_amount = self.get_player_actions()

            amount_added = current_player.player_betting_actions(action, self.highest_bet_in_round, raise_amount)
            self.pot.total += amount_added

            # update the highest bet
            current_player.has_acted_this_round = True
            current_pos = (current_pos + 1) % 2

    def is_player_status_active(self, player):
        return player.player_status == 'Active'

    # Code for the Flop round
    def is_hand_over_early(self):
        # Check if there is just one active player - if yes then we can move to showdown
        players = [self.computer, self.me]
        return sum(1 for p in players if p.player_status in ['Active' or 'All-in']) <= 1

    def reset_to_next_betting_round(self, stage):
        players = [self.computer, self.me]
        for player in players:
            player.current_bet_in_round = 0
            if self.is_player_status_active(player):
                player.has_acted_this_round = False
        self.highest_bet_in_round = 0
        self.current_in_stage = stage

    def deal_post_flop_stages(self, stage):
        self.deck.burn_card()
        self.community_cards.extend(self.deck.deal_community_card(stage))

    def can_continue_betting(self):
        players = [self.computer, self.me]
        active = 0
        for player in players:
            if self.is_player_status_active(player):
                active += 1
        return active>=2

    def display_game_state(self):

        """Display the current state of the game"""

        print(f"\n{'='*50}")
        print(f"\nCurrent State of the Game is : ")

        print(f"\nChips with Player 1 is : {self.computer.stacks}")
        print(f"\nChips with Player 2 is : {self.me.stacks}")

        print(f"\nPot : {self.pot.total}")
        print(f"\n Your cards : {self.me.hole_cards[0]} and  {self.me.hole_cards[1]}")
        if self.community_cards:
            print(f"Community Cards: {', '.join(str(card) for card in self.community_cards)}")

        print(f"\n{'='*50}")

    def award_pot_to_winner(self):

        """Award pot to the winner"""
        print(f"\n{'=' * 50}")
        print(f"\n Award Pot to the Winner")
        if self.computer.player_status in ['Active', 'All-in']:
            winner = self.computer
        else:
            winner = self.me
        winner.stacks += self.pot.total
        print(f"\n Winner is : {winner.name} and price is : {winner.stacks} ")
        print(f"\n{'='* 50}")

    def showdown_winner(self):

        """Compare hands at showdown"""
        print(f"\n{'=' * 50}")
        print(f"\n Time for show down winner : ")
        computer_high_card = max(self.computer.hole_cards , key=lambda c : self.deck.get_card_rank(c))
        player_high_card = max(self.me.hole_cards, key=lambda c: self.deck.get_card_rank(c))

        computer_high_value = self.deck.get_card_rank(computer_high_card)
        player_high_value = self.deck.get_card_rank(player_high_card)

        if computer_high_value > player_high_value:
            winner = self.computer
        else:
            winner = self.me

        if computer_high_value == player_high_value:
            # Adding half pot total in the computer stacks
            print(f"\nTie! Pot split: ${self.pot.total // 2} each")
            self.computer.stacks += (self.pot.total//2)
            self.me.stacks += (self.pot.total // 2)
            return

        winner.stacks += self.pot.total
        print(f"\n Winner is : {winner.name} and total is : {winner.stacks}")
        print(f"\n{'=' * 50}")

    def play_game(self):

        print("\nWelcome to the Texas Poker Game : ")
        hands_to_play = int(input("Enter the number of hands to be played"))
        for hand_num in range(1, hands_to_play + 1):

            if self.computer.stacks <=0:
                print("Computer is out of chips ! You win")
                break
            if self.me.stacks <=0:
                print("You are out of chips ! Computer wins")
                break


            print(f"\n{'=' * 50}")
            print(f"Hand {hand_num} of {hands_to_play}")
            print(f"\n{'=' * 50}")

            self.start_new_hand()
            self.display_game_state()

            # Preflop betting round

            print(f"\n Preflop Betting Round : ")
            self.conduct_betting_round('preflop')
            if self.is_hand_over_early():
                self.award_pot_to_winner()
                continue

            # Flop Betting Round

            print(f"\n Flop Betting Round : ")
            self.deal_post_flop_stages('flop')
            self.display_game_state()
            self.reset_to_next_betting_round('flop')
            if self.can_continue_betting():
                self.conduct_betting_round('flop')
                if self.is_hand_over_early():
                    self.award_pot_to_winner()
                    continue

            # Turn Betting Round

            print(f"\n Turn Betting Round : ")
            self.deal_post_flop_stages('turn')
            self.display_game_state()
            self.reset_to_next_betting_round('turn')
            if self.can_continue_betting():
                self.conduct_betting_round('turn')
                if self.is_hand_over_early():
                    self.award_pot_to_winner()
                    continue

            # River Betting Round
            print(f"\n River Betting Round : ")
            self.deal_post_flop_stages('river')
            self.display_game_state()
            self.reset_to_next_betting_round('river')
            if self.can_continue_betting():
                self.conduct_betting_round('river')
                if self.is_hand_over_early():
                    self.award_pot_to_winner()
                    continue

            # showdown winner
            print(f"\n -------Showdown Winner------")
            self.showdown_winner()

        print("\n Game Over! Thanks for playing!")


play_game = PokerGame()
play_game.play_game()











































































