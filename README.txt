☐==========================================================================☐
||      ████  ███  █   █ █████    ███  █████   █     █████ █████ █████     ||
||     █     █   █ ██ ██ █       █   █ █       █       █   █     █         ||
||     █  ██ █████ █ █ █ ████    █   █ ████    █       █   ████  ████      ||
||     █   █ █   █ █   █ █       █   █ █       █       █   █     █         ||
||      ███  █   █ █   █ █████    ███  █       █████ █████ █     █████     ||
☐==========================================================================☐
-Description of game
This a recreation of the classic Game of Life made by John Conway. It is a zero-player game
where dots on a grid using a very basic ruleset try to simulate intelligence similar to human life.
A dot on the grid represents life that changes depending on the environment around it: that being other 
lives.

The 4 rules that dicate the game are:
-Any live cell with fewer than two live neighbours dies, as if by underpopulation.
-Any live cell with two or three live neighbours lives on to the next generation.
-Any live cell with more than three live neighbours dies, as if by overpopulation.
-Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

With the 1.1.2 patch "God Mode", the game can now shift into a single player game as the player now
has agency to add or destory lives on the grid.

☐===========================================☐
||     █▀▀ █▀█ █▄ █ ▀█▀ █▀█ █▀█ █   █▀▀     ||
||     █▄▄ █▄█ █ ▀█  █  █▀▄ █▄█ █▄▄ ▄██     ||
☐===========================================☐
-CONTROLS
'q' = Exit game
's' = Pauses continuous updates
'd' = Update game by single generation at a time
mouseLeftClick = During pause, can click on window to revive ot kill a specified cell 

☐===============================================☐
||     █▀▀ █▄█ ▄▀▄ █▄ █ █▀▀ █▀▀ █   █▀█ █▀▀     ||
||     █▄▄ █ █ █▀█ █ ▀█ █▄█ ██▄ █▄▄ █▄█ █▄█     || 
☐===============================================☐

*1.1.0 Initial release
-Base game

*1.1.1 Controls
-Added controls to game
-Ability to exit the game using 'q' key
-Ability to stop the game using 's' key
-Ability to step game one update using 'd' key

1.1.2 God Mode
-Adds the ability for the user to propogate and destory cells actively on the board
-While game is stopped, player can use MouseLeftClick on window to select specified cell to change its status

1.1.3 Application
-Used Pyinstaller to create executable application of game
-Can not dynamically change settings when using executable file
-Changed main.py to main.pyw to hide console window when opened

