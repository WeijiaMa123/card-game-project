## card-game-project
My project is a video game. It will be a game about cards. 
In this game, there are 2 players. The goal of this game is to kill the opponent. There are different characters with different abilities. Different characters also has different health. Players need to choose a character. You need to have cards to attack.  First, I need to break this project into many parts.
Create a deck with different cards that perform different thing. We need to make sure that the cards are random. Some cards should be more common than the other cards, because this game is killing the opponent. If you can’t attack so often, the game will be boring and extremely long. For this game, each player have 4 random cards initially. They needs to gain 2 more cards from the deck after each term. The deck will never run out of cards because this game never ends until one of the player dies.
Make the game work by creating the system of terms. We need to make players move in a order repeatedly. For example, every player need to gain 2 cards from the deck before they use any cards. The player will move after his opponent finished and gained his 2 new cards.
We need to create characters. We need to set the player’s health first, because you can do nothing without health points.  After that we can use functions to define many characters’ abilities. Character’s ability can make the game more fun and playable. For example, a character’s ability can be losing 1 health point and gain 3 cards. It also could be using some common cards as other rare cards that are more helpful. It also could be doing more damage using only a normal “attack” card. 
Now we need to define card’s functions. Right now I have designed 5 cards. The red coding below is what I have already done. 
For “attack” cards, it can make opponent lose 1 health if the opponent does not have a “block” card. 
The “block” card can help you avoid losing 1 health. 
The “heart” card makes you gain 1 health. 
The “alien invasion” card force your opponent to use a “attack” card that is not toward you. If your opponent doesn't have a “attack” card, he will lose 1 health point. 
The “peace” card makes you and your opponent both gain 1 health point. For each character, their maximum health is how many health points they had at beginning of the game. 
 	5. Every player can keep their cards if they decide not to use the cards. 
6. The end of the game is when one of the player’s health goes to 0.
7. Now I have many functions and many parts of the game. I need to add these functions, such as effects of cards, abilities of characters, into the whole system. 
8. Make the graphics of the game and run the game in a server so people can find opponents online. 


These 8 parts are extremely hard for a programmer like me, but I can do some parts of it. I can create the deck, define some cards and some characters’ abilities. The graphics, servers and making the game work is too hard. 








#Testing 
I will end up with 2 decks. One is for player 1 and the other one is for player 2.
I also need to check the five different cards to see if they work.
The “attack” cards can make opponent lose 1 health if the opponent does not have a “block” card. 
The “block” card can help you avoid losing 1 health from the attack card. 
The “heart” card makes you gain 1 health. 
The “alien invasion” card force your opponent to use a “attack” card that is not toward you. If your opponent doesn't have a “attack” card, he will lose 2 health point. 
The “peace” card makes you and your opponent both gain 1 health point. 

I also need to check that the player will die if the health is below 0. I also need to check the player will have a maximum health of 5.
