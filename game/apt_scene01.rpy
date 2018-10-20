label apt_check:

    if knock == "1":
        jump apt01
    elif knock == "0":
        jump apt01_ALT


label apt01:

    play sound "sound/fx/knock.wav"
    $ renpy.pause(1, hard=True)
    voice "sound/voice/trip/00759.wav"
    t "Oh, he's here!"

    voice "sound/voice/grace/00764.wav"
    gr "What? You told me it'd be an hour from now!"

    voice "sound/voice/trip/00761.wav"
    t "No, he's right on time!"

    voice "sound/voice/grace/00763.wav"
    gr "Trip!"

label apt01_ALT:

