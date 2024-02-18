#!/usr/bin/env python3

class Remote:
    """
    Represents a TV remote control.

    Attributes:
        is_on (bool): Indicates if the TV is turned on.
        MAX_VOLUME (int): Maximum volume level.
        MIN_VOLUME (int): Minimum volume level.
        volume (int): Current volume level.
        channel_list (list): List of available channels.
        channel_index (int): Index of the current channel in the channel list.
        is_muted (bool): Indicates if the TV is muted.
        location (str): Indictates the location of the TV
        brand (str): Specifies the brand of the TV
    """

    def __init__(self, brand, location):
        """Initializes a Remote object with default settings."""
        self.is_on: bool = False
        self.MAX_VOLUME: int = 15
        self.MIN_VOLUME: int = 0
        self.volume: int = self.MAX_VOLUME // 5
        self.channel_list: list = list(range(2, 69, 3))
        self.channel_index: int = 0
        self.is_muted: bool = False
        self.location: str = location
        self.brand: str = brand

    def activate_power(self):
        """Toggles the power state of the TV."""
        self.is_on = not self.is_on

    def volume_up(self):
        """Increases the volume by one level."""
        if not self.is_on:
            return None
        elif self.volume < self.MAX_VOLUME:
            if self.is_muted:  # if TV is muted, changing volume unmutes TV
                self.is_muted = not self.is_muted
            self.volume += 1

    def volume_down(self):
        """Decreases the volume by one level."""
        if not self.is_on:
            return None
        elif self.volume > self.MIN_VOLUME:
            if self.is_muted:  # if TV is muted, changing volume unmutes TV
                self.is_muted = not self.is_muted
            self.volume -= 1

    def channel_up(self):
        """Switches to the next channel in the channel list."""
        if not self.is_on:
            return None

        # if channel_index is at the end of the list,
        # switch to the beginning of the channel_list
        elif self.channel_index == len(self.channel_list) - 1:
            self.channel_index = 0

        else:
            self.channel_index += 1

    def channel_down(self):
        """Switches to the previous channel in the channel list."""
        if not self.is_on:
            return None

        # if channel_index is at the beginning of the list,
        # switch to the end of the channel_list
        elif self.channel_index == 0:
            self.channel_index = len(self.channel_list) - 1

        else:
            self.channel_index -= 1

    def activate_mute(self):
        """Toggles the mute state of the TV."""
        self.is_muted = not self.is_muted

    def select_channel(self, user_input: int):
        """
        Selects a channel based on user input.

        Args:
            user_input (int): The channel number to select.
        """
        try:
            if user_input in self.channel_list:
                self.channel_index = self.channel_list.index(user_input)
        except ValueError:
            print(f'Channel {user_input} is not available')

    def get_info(self):
        """Prints the current status of the TV."""
        if self.is_on:
            print(
                f"{self.brand} TV in the {self.location} is: On\n"
                f"Channel: {self.channel_list[self.channel_index]}\n"
                f"Volume Level: {self.volume} {"(Muted)\n" if self.is_muted else "\n"}"
            )
        else:
            print(f"The {self.brand} TV in the {self.location} is off")


# first Remote object
tv1 = Remote('Samsung', 'theater')
tv1.activate_power()
tv1.get_info()
tv1.channel_down()
tv1.get_info()
tv1.channel_down()
tv1.get_info()
tv1.channel_down()
tv1.get_info()
tv1.volume_up()
tv1.get_info()
tv1.volume_up()
tv1.get_info()
tv1.volume_up()
tv1.get_info()
tv1.volume_up()
tv1.get_info()
tv1.activate_mute()
tv1.get_info()
tv1.volume_down()
tv1.get_info()
tv1.volume_down()
tv1.get_info()
tv1.channel_up()
tv1.get_info()
tv1.channel_up()
tv1.get_info()
tv1.channel_up()
tv1.get_info()
tv1.channel_up()
tv1.get_info()
tv1.activate_power()
tv1.get_info()

# Second Remote object
tv2 = Remote('Sony', 'game room')
tv2.get_info()
tv2.channel_up()
tv2.get_info()
tv2.volume_down()
tv2.get_info()
