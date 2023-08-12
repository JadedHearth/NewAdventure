# NewAdventure

A ***better*** adaptation of my old [*Adventure*](https://github.com/WoodenMaxim/adventure) python game that I made in 2020.
This time, with *curses*!
And *a map*!

Or, at least, it will soon be an adapatation...

## Requirements and Dependencies

* a python3 install with *curses*
* numpy
* Pillow
* A terminal application that supports the usage of resize escape codes, for example iTerm2 or Apple Terminal (Both are supported, though they display slightly differently).
  * For iTerm2, however, you need to enable window resizing with escape codes by going to Preferences > Profiles > Default > Terminal > and uncheck "Disable session-initiated window resizing".
  * You could also just comment out those escape code lines and manually resize to 204x46 characters if using Windows or an unsupported terminal.
* A "big enough" screen (though this might be fixed later)
