# Alchemy Saga
Alchemy Saga is a Turn-Based Python Battle Showdown Game inspired by *Pokémon Showdown*. Developed as my final project for CIT1C18 Computational Thinking, it blends strategic gameplay with an intuitive graphical interface.

<p align="center"> <img src="https://github.com/sofiaamihan/alchemy-saga/blob/main/data/home-screen.png" alt="Home Screen" width="45%" /> <img src="https://github.com/sofiaamihan/alchemy-saga/blob/main/data/battle-screen.png" alt="Battle Screen" width="45%" /> </p>

## Basic Game Mechanics
Full Gameplay Guide can be found [here (PDF)](https://github.com/sofiaamihan/alchemy-saga/blob/main/guide/alchemy-saga-game-mechanics.pdf).
- **Net Attack**: Character’s `Attack` minus Opponent's `Defence`
- **Net Defence**: Buffs the Character’s DP by 10%
- **Skill**: Varies based on Chosen Job Class
- **Speed**: Faster Character(s) will go first

## Features
- Engaging turn-based combat system
- Multiple game modes (1v1 and 2v2)
- Unique character job classes with distinct abilities
- Skill manipulation and strategic gameplay
- Intuitive user interface built with Tkinter

  > Settings page is static to fit the requirements of the subject.

## Packages
| Package     | Purpose                                                                 |
|-------------|-------------------------------------------------------------------------|
| `tkinter`   | Used for creating the **graphical user interface (GUI)**, including windows, buttons, and layout logic. |
| `PIL` *(from Pillow)* | Used to **load and display images** such as sprites, backgrounds, and screen elements in the Tkinter interface. |
| `random`    | Powers the **randomised elements** in battle, such as damage variation and skill outcomes. Adds unpredictability to gameplay. |

