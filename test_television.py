from television import Television


def test_power(self):
    """Toggle the power status of the TV."""
    self.__status = not self.__status


def test_mute(self):
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


def test_channel_up(self):
    """Increase channel by 1 when TV is on, wrap after MAX_CHANNEL."""
    if self.__status:
        if self.__channel >= Television.MAX_CHANNEL:
            self.__channel = Television.MIN_CHANNEL
        else:
            self.__channel += 1


def test_channel_down(self):
    """Decrease channel by 1 when TV is on, wrap below MIN_CHANNEL."""
    if self.__status:
        if self.__channel <= Television.MIN_CHANNEL:
            self.__channel = Television.MAX_CHANNEL
        else:
            self.__channel -= 1


def test_volume_up(self):
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


def test_volume_down(self):
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
