

from television import Television


def test_initial_state():
    tv = Television()
    # TV should start OFF, channel 0, volume 0
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"


def test_power_toggle():
    tv = Television()

    # Turn on
    tv.power()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

    # Turn off again
    tv.power()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"


def test_channel_changes_only_when_on():
    tv = Television()

    # TV is off, channel should not change
    tv.channel_up()
    tv.channel_down()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

    # Turn on and then change channel
    tv.power()
    tv.channel_up()
    assert str(tv) == "Power = True, Channel = 1, Volume = 0"


def test_channel_up_wrap_around():
    tv = Television()
    tv.power()

    # Go from 0 → 1 → 2 → 3
    tv.channel_up()
    tv.channel_up()
    tv.channel_up()
    assert str(tv) == "Power = True, Channel = 3, Volume = 0"

    # One more up should wrap to 0
    tv.channel_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"


def test_channel_down_wrap_around():
    tv = Television()
    tv.power()

    # Start at 0, going down should wrap to 3
    tv.channel_down()
    assert str(tv) == "Power = True, Channel = 3, Volume = 0"

    # Down again: 3 → 2
    tv.channel_down()
    assert str(tv) == "Power = True, Channel = 2, Volume = 0"


def test_volume_changes_only_when_on():
    tv = Television()

    # TV is off, volume should not change
    tv.volume_up()
    tv.volume_down()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

    # Turn on and then change volume
    tv.power()
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"


def test_volume_limits():
    tv = Television()
    tv.power()

    # Raise volume above max on purpose
    for _ in range(10):
        tv.volume_up()
    # MAX_VOLUME = 2
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"

    # Try to go higher, should stay at 2
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"

    # Now go down below min on purpose
    for _ in range(10):
        tv.volume_down()
    # MIN_VOLUME = 0
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

    # One more down, still 0 (this is the “past minimum value” case)
    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"


def test_mute_toggle_basic():
    tv = Television()
    tv.power()

    # Turn volume up to 2
    tv.volume_up()
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"

    # Mute: volume should go to 0
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

    # Unmute: volume should go back to 2
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"


def test_mute_with_volume_change():

    tv = Television()
    tv.power()

    # Raise volume to 2
    tv.volume_up()
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"

    # Mute: 2 → 0
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

    # Change volume while muted: should unmute and change correctly
    tv.volume_down()
    # Previous volume was 2, then restore to 2 and go down to 1
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"

    # Mute again from volume 1: 1 → 0
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

    # Volume up while muted: restore to 1 and then up to 2
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"


def test_str_matches_main_example_sequences():

    tv_1 = Television()
    tv_1.power()
    assert str(tv_1) == "Power = True, Channel = 0, Volume = 0"

    tv_1.channel_up()
    tv_1.channel_up()
    tv_1.volume_up()
    assert str(tv_1) == "Power = True, Channel = 2, Volume = 1"

    tv_1.channel_up()
    tv_1.channel_up()
    tv_1.channel_up()
    tv_1.volume_down()
    tv_1.volume_down()
    assert str(tv_1) == "Power = True, Channel = 1, Volume = 0"

    tv_1.power()
    tv_1.volume_up()
    tv_1.channel_down()
    # TV off, so no effect from volume_up and channel_down
    assert str(tv_1) == "Power = False, Channel = 1, Volume = 0"
