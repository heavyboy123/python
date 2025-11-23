class Television:
    # ---------- class constants ----------
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        """
        Set default instance values.
        TV starts OFF, not muted, on minimum channel and minimum volume.
        """
        self.__status = False          # False = off, True = on
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL
        self.__prev_volume = Television.MIN_VOLUME  # remembers volume before mute

    def power(self):
        """Toggle the power status of the TV."""
        self.__status = not self.__status

    def mute(self):
        """
        Toggle mute when TV is on.

        When muting: store current volume in __prev_volume and set volume to 0.
        When unmuting: restore the previous volume.
        """
        if self.__status:
            if not self.__muted:
                self.__muted = True
                self.__prev_volume = self.__volume
                self.__volume = Television.MIN_VOLUME
            else:
                self.__muted = False
                self.__volume = self.__prev_volume

    def channel_up(self):
        """Increase channel by 1 when TV is on, wrap after MAX_CHANNEL."""
        if self.__status:
            if self.__channel >= Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self):
        """Decrease channel by 1 when TV is on, wrap below MIN_CHANNEL."""
        if self.__status:
            if self.__channel <= Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self):
        """
        Increase volume when TV is on.

        If muted: unmute, restore previous volume, then increase.
        Volume is limited to MAX_VOLUME.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__prev_volume
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1
            self.__prev_volume = self.__volume

    def volume_down(self):
        """
        Decrease volume when TV is on.

        If muted: unmute, restore previous volume, then decrease.
        Volume is limited to MIN_VOLUME.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__prev_volume
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1
            self.__prev_volume = self.__volume

    def __str__(self):
        """Return TV details in required format."""
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"
