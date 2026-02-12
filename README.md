## GamesDevelopment – Card Games Collection

This repository contains a small collection of card games implemented as part of a game development project: a **Blackjack** game and a **Poker** game.  
The goal of this project is to demonstrate clean, object‑oriented design, separation of concerns, and readable, maintainable code that can be extended with new rules or additional games.

---

## Overview

- **Technology**: (Python 3.13.1)
- **Focus areas**:
  - Clean game flow and turn management
  - Clear modelling of cards, decks, and players
  - Encapsulated game rules for Blackjack and Poker
  - Simple but user‑friendly input/output (CLI or GUI – update as appropriate)

> **Tip for reviewers**: The codebase is structured so that both games share common card/deck abstractions, while game‑specific rules live in separate modules. This keeps the codebase easy to navigate and extend.

---

## Project Structure

_Adjust this section to match your actual folders and filenames._

- **`cards/` or core module**: Shared card and deck logic.
  - `Card` – represents a single playing card (suit, rank, value).
  - `Deck` – creates, shuffles, and deals cards.
- **`blackjack/`**: Blackjack‑specific logic.
  - Game loop / controller (e.g. `blackjack_game.py`)
  - Player and Dealer hands
  - Blackjack rules and scoring
- **`poker/`**: Poker‑specific logic.
  - Game loop / controller (e.g. `poker_game.py`)
  - Player hands and community cards (if Texas Hold’em)
  - Hand ranking and winner evaluation
- **`main` or launcher**: Entry point that lets you choose which game to run.

If your structure differs, you can quickly update the names in this section, but the intent is to make it easy for a hiring manager to find the relevant code.

---

## Blackjack Game

### Game Concept

Blackjack is implemented as a **turn‑based card game** between a **Player** and the **Dealer**:

- A standard 52‑card deck is used.
- Each round, both the player and dealer are dealt initial cards.
- The player chooses to **Hit** (take another card) or **Stand** (end their turn).
- The dealer then plays according to fixed rules (e.g. must hit until reaching 17 or more).
- The goal is to get as close to 21 as possible **without going over**.

### Rules / Implementation Details

- **Card values**:
  - Number cards (2–10) count as their face value.
  - Face cards (J, Q, K) count as 10.
  - Aces can count as 1 or 11, whichever is more beneficial without busting.
- **Blackjack**:
  - An initial hand of an Ace + a 10‑value card is treated as “Blackjack”.
  - The game detects and resolves this case immediately (win/lose/push).
- **Player actions**:
  - `Hit`: draw an additional card.
  - `Stand`: end the turn and let the dealer play.
  - (Optional extensions: `Double`, `Split`, etc. – mention if implemented.)
- **Dealer behavior**:
  - Follows standard casino rules – typically:
    - Hits until reaching a total of 17 or more.
    - Stands on 17+ (configurable depending on your rules).
- **Round outcome**:
  - If the player busts (\> 21), the dealer wins.
  - If the dealer busts and the player has not, the player wins.
  - Otherwise, the highest total (≤ 21) wins; equal totals result in a push (tie).

### Design Highlights

- **Encapsulated scoring logic**: Hand evaluation is kept in a dedicated function/class so the Ace logic is easy to understand and adjust.
- **Clear separation of concerns**:
  - Deck and card management are reused by both Blackjack and Poker.
  - Game loop handles user interaction and turn sequencing.
  - Rule evaluation functions/classes handle scoring and win/lose logic.
- **Extensibility**: The design leaves room to add betting, multiple players, or additional actions without rewriting the core.

---

## Poker Game

### Game Concept

The Poker implementation (for example **Texas Hold’em** – adjust if you implemented a different variant) simulates a simplified poker round:

- A standard 52‑card deck is used.
- Each player receives a set of **hole cards**.
- Community cards are revealed in stages (Flop, Turn, River) if Texas Hold’em is used.
- The best five‑card hand out of the available cards determines the winner.

### Rules / Implementation Details

- **Game flow** (Texas Hold’em example):
  1. **Deal** two hole cards to each player.
  2. **Flop**: reveal three community cards.
  3. **Turn**: reveal a fourth community card.
  4. **River**: reveal a fifth community card.
  5. **Showdown**: evaluate and compare final hands.
- **Hand ranking** (from highest to lowest):
  - Royal Flush
  - Straight Flush
  - Four of a Kind
  - Full House
  - Flush
  - Straight
  - Three of a Kind
  - Two Pair
  - One Pair
  - High Card
- **Hand evaluation**:
  - The implementation computes the best possible hand each player can form from their cards (and community cards, if present).
  - Hand comparison is encapsulated in a ranking / scoring module or function.
  - Ties are broken using standard poker rules (e.g. highest card within the hand, then kickers).

### Design Highlights

- **Reusable core models**: Uses the same `Card` and `Deck` abstractions as Blackjack.
- **Isolated ranking logic**:
  - Hand evaluation is implemented in a dedicated component.
  - The code is structured to make unit testing of each hand type straightforward.
- **Configurable number of players**: Designed so the number of players can be adjusted (within practical limits).
- **Extendable rules**:
  - Betting, blinds, and multiple rounds can be layered on top of the existing structure.

### Prerequisites

- **Language runtime**: Python 3.10+ 

### Running from the Command Line

```bash
python3 basics/BlackJackGame.py
python3 basics/TexasPokerGame.py
```

## Possible Future Enhancements

- **User Interface**:
  - Add a graphical UI (desktop or web) on top of the existing game engine.
  - Improve the command‑line experience with clearer prompts and colored output.
- **Game Features**:
  - Betting system with chips and balance tracking.
  - Multiple players and multiplayer rounds.
  - Additional Blackjack rules (splits, insurance, surrender).
  - More Poker variants or tournament mode.
- **Technical Improvements**:
  - Add formal unit tests for hand evaluation and scoring.
  - Introduce logging for debugging and game replay analysis.
  - Package the project so games can be installed and run as a CLI tool.

---

## How to Review the Code

For a quick understanding of the implementation:

1. **Start with the core models** (`Card`, `Deck`) to see how cards and decks are represented.
2. **Review Blackjack**:
   - Open the BlackJackGame.py file.
   - Look at how the game loop manages turns and applies scoring.
3. **Review Poker**:
   - Open the TexasPokerGame.py file.
   - Focus on the hand evaluation and ranking logic.
4. **Consider extensibility**:
   - Note how easy it would be to add a new game or additional rules by reusing the core abstractions.

This structure is intentional to reflect how I design game systems: reusable cores, clear separation of concerns, and room to grow in complexity without sacrificing readability.

