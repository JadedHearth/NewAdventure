""" The status window. """

import curses
from config import *

class StatusManager:
    """
    Class for the status window.
    """
    def __init__(self) -> None:
        possibleHealthStatuses = ["Good", "Ok", "Poor", "Broken", "Gone"]
        
        healthWindowWidth = len("   Right Hand Health: ") + len(max(possibleHealthStatuses)) + 4 # Hackjob way of making it fit the largest entry

        self.statusWindow = curses.newwin(int(Config.HEIGHT/2 + 2), int(Config.WIDTH / 2 - 1), 0, 0)
        self.statusWindow.border()

        self.health = self.HealthDescription(healthWindowWidth, possibleHealthStatuses)

    class HealthDescription:
        def __init__(self, healthWindowWidth, possibleHealthStatuses) -> None:

            self.healthDescriptionWindow = curses.newwin(int(Config.HEIGHT/2 + 2), healthWindowWidth, 0, 0)

            # TODO: Manage this in a "currentState" class or the like so it can be saved.
            self.health = [possibleHealthStatuses[0], # Overall
                           possibleHealthStatuses[0], # Skull
                           possibleHealthStatuses[0], # Brain
                           possibleHealthStatuses[0], # Throat
                           possibleHealthStatuses[0], # Neck
                           possibleHealthStatuses[0], # Left Arm
                           possibleHealthStatuses[0], # Left Hand
                           possibleHealthStatuses[0], # Right Arm
                           possibleHealthStatuses[0], # Right Hand
                           possibleHealthStatuses[0], # Left Leg
                           possibleHealthStatuses[0], # Right Leg
                           possibleHealthStatuses[0], # Ribcage
                           possibleHealthStatuses[0], # Heart
                           possibleHealthStatuses[0], # Lung
                           possibleHealthStatuses[0], # Digestive
                           possibleHealthStatuses[0], # Liver
                           possibleHealthStatuses[0], # Immune
                           possibleHealthStatuses[0], # Spine
                           possibleHealthStatuses[0]] # Hip
        

        def noutrefresh(self) -> None:
            self.healthDescriptionWindow.border()

            self.healthDescriptionWindow.addstr(1,2, f"Overall Health: {self.health[0]}")

            self.healthDescriptionWindow.addstr(3,2, f"Skull Health: {self.health[1]}")
            self.healthDescriptionWindow.addstr(4,4, f"Brain Health: {self.health[2]}")
            self.healthDescriptionWindow.addstr(5,4, f"Throat Health: {self.health[3]}")
            self.healthDescriptionWindow.addstr(6,4, f"Neck Health: {self.health[4]}")

            self.healthDescriptionWindow.addstr(8,2, f"Left Arm Health: {self.health[5]}")
            self.healthDescriptionWindow.addstr(9,4, f"Left Hand Health: {self.health[6]}")
            self.healthDescriptionWindow.addstr(10,2, f"Right Arm Health: {self.health[7]}")
            self.healthDescriptionWindow.addstr(11,4, f"Right Hand Health: {self.health[8]}")

            self.healthDescriptionWindow.addstr(13,2, f"Left Leg Health: {self.health[9]}")
            self.healthDescriptionWindow.addstr(14,2, f"Right Leg Health: {self.health[10]}")

            self.healthDescriptionWindow.addstr(16,2, f"Ribcage Health: {self.health[11]}")
            self.healthDescriptionWindow.addstr(17,4, f"Heart Health: {self.health[12]}")
            self.healthDescriptionWindow.addstr(18,4, f"Lung Health: {self.health[13]}")
            self.healthDescriptionWindow.addstr(19,4, f"Digestive Health: {self.health[14]}")
            self.healthDescriptionWindow.addstr(20,6, f"Liver Health: {self.health[15]}")

            self.healthDescriptionWindow.addstr(21,2, f"Immune Health: {self.health[16]}")
            self.healthDescriptionWindow.addstr(22,4, f"Spine Health: {self.health[17]}")
            self.healthDescriptionWindow.addstr(23,2, f"Hip Health: {self.health[18]}")

            self.healthDescriptionWindow.noutrefresh()

    def prerefresh(self) -> None:
        self.statusWindow.noutrefresh()
        self.health.noutrefresh()