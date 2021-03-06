Program: Armada (Armada.py)
Karissa Bowser
knb@csu.fullerton.edu
CPSC 386 Game Design - Final Project


Intro: 
	This program is a single player top-down space themed shooter game. 
	The player is tasked with defending Earth and eliminating the aliens. 
	The goal of the game is to kill the mothership that will spawn randomly somewhere between levels 5 and 10.


External Requirements:
	There are no external requirements.


Setup and Installation:
	1. Run the Python installer downloaded from: ProgramArcadeGames.com/python-3.4.3.msi
	2. Run the Pygame installer downloaded from: ProgramArcadeGames.com/pygame-1.9.2a0.win32-py3.4.msi 
	3. Download zip file "386-p5_Bowser-K.zip", unzip, and run the program 


General Rules:

	1. You only have one life per game.
	2. You have 100 HP to start the game, and each hit taken reduces that by 5.
	3. The player can shoot at the enemies and move around the game display.
	4. The player can kill the smaller alien ships with a single shot, but the mothership has 100 HP, and takes multiple shots to kill. 
	5. Each time an alien reaches Earth, the Earth's defense drops 5 percent.


Win/Lose Conditions:
	The player will lose the game if they do any of the following (Lose State): 
		1. Collide into an alien (Be careful, they get faster as the levels increase)
		2. Allow Earth's Defense to drop to 0 (Each time an alien reaches Earth, the Earth's defense drops 5 percent).
		3. Allow their own HP to drop to zero (Player has 100 HP, each shot from the AI reduces HP by 5)
		4. Let the mothership reach Earth.
	The player will win if they do the following (Win State):
		1. Kill the mothership that will spawn randomly somewhere between levels 5 and 10, before it reaches Earth.
		   The mothership has 100 HP, each shot reduces HP by 5


Features:
	Features include but are not limited to: sound (music and sound effects), graphics, keyboard input, user interface, level 0 brain AI, and so on.


Bugs: 
	There are no known bugs at this point in time, although the program was not extensively tested.
	
ART CREDITS:
•	Enemy Art: (alien1.png, alien2.png, boss.png) https://opengameart.org/content/spaceship-6 by wubitog and Skorpio (https://opengameart.org/users/skorpio)
•	Player Art: (player_ship.png) this work has been released under the Creative Commons License: https://creativecommons.org/licenses/by/4.0/ By MillionthVector (https://millionthvector.blogspot.de)
•	Explosion Art: (big_explosion.png, explosion.png) by Retimer at https://opengameart.org/content/wgstudio-explosion-animation
•	Title Screen Art: https://www.reddit.com/r/wallpaper/comments/1oljxk/the_sun_behind_the_earth_1920_x_1080/
•	In-game Background Art: https://www.gunnars.com/space/
•	Instructions Screen Art: https://www.jpl.nasa.gov/assets/images/content/tmp/home/missions_bg_image.jpg

MUSIC CREDITS:
•	Non in-game music: (death.mid) by Jan125 https://opengameart.org/content/stereotypical-90s-space-shooter-music 
•	In-game music: (boss.mid) by Jan125 https://opengameart.org/content/stereotypical-90s-space-shooter-music 
•	Laser Fire Sound Effect: (laser_fire.wav) by dklon https://opengameart.org/content/laser-fire

CODE REFERENCES:
•	https://www.cs.rutgers.edu/~biglars/pycs4hs/pydemo4.html

