## card-game-project
**Big Picture:**

My project is a video game. It will be a game about cards. In this game, there are 2 players. The goal of this game is to kill the opponent.There are different kinds of cards with different functions. There could be different character with different skills. I can even make the winner earn some money in the game. The winner can use it to buy new characters.

**Plan:**

Create a deck with different cards that perform different thing. We need to make sure that the cards are random. Some cards should be more common than the other cards. For this game, each player gains 2 cards from the deck after each term. The deck will never run out of cards because this game never ends until one of the player dies.

Make the game work by creating the system of terms. Each player needs to gain 2 cards from the deck before they use any cards. The player will move after his opponent finished and gained his 2 new cards.


**Now we need to define card’s functions. I have designed 5 cards.**

-For the “attack” card, it can make the opponent lose 1 health if the opponent does not have a “block” card.

-The “block” card can help you avoid losing 1 health. 

-The “heart” card makes you gain 1 health. 

-The “alien invasion” card forces your opponent to use a “attack” card that is not toward you. If your opponent doesn't use an “attack” card, he will lose 1 health point. 

-The “peace” card makes you and your opponent both gain 1 health point. If you reach 3 health points, you can't add more health.

-Every player can keep block cards,peace cards and attack cards if they decide not to use the cards.
The end of the game is when one of the player’s health goes to 0.

**Problems**

I can’t check if the players have the block cards because my deck is a random function that keeps going on. I am unable to monitor the situation as it is happening.  
 
**Testing**

I will end up with 2 decks. One is for player 1 and the other one is for player 2. I also need to check the five different cards to see if they work. The “attack” cards can make opponent lose 1 health if the opponent does not have a “block” card. The “block” card can help you avoid losing 1 health from the attack card. The “heart” card makes you gain 1 health. The “alien invasion” card force your opponent to use a “attack” card that is not toward you. If your opponent doesn't have a “attack” card, he will lose 1 health point. The “peace” card makes you and your opponent both recover 1 health point.



:+1: 






## Second Round 

**Use of pygame**

Use pygame to add graphics to the game. For every card, I can define a function like a button. When the player click on the card, he will use it. I can add some images, words on the card by using the features of Pygame such as drawing and loading images. I can also add some sound effects to make the game cooler. I can make a "game intro" and "try again" pages. 

**Changes about codes in my first round**

I will make some major changes about the code and the game I designed. I will change my game loop because my player can't really play my old game. I should make players pick what card they use and what card they keep. At the first round, my codes are really sloppy because I made only two functions which are the engine function and the deck function. I also used many global varibles which are very confusing. I should define more functions.

**About making the game playable**

My old design for the game is boring because your opponent can see your card. It is also a two people game on one computer. I have ideas of make my game for only one player. I wants to make bosses and the goal is to kill. The bosses are not smart, they do something same for all the rounds. Maybe make you lose one health every round and can block once every round. The boss can't control any cards. The bosses could also make some special effect such as poisoning, healing and immune to some cards. 
- Poisoning can make the player die in 20 rounds instantly. 
- The healing can heal the boss once when he is dead.
- Some bosses can be immune to some cards. 

**What contents I may add to the game**

If I did other codes pretty easily, I may add some more cards in the game. I can also make this game for more players. But it is still just some thoughts.

