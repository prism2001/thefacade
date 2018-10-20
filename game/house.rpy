# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define g = Character("Gonzalo")
define t = Character("Trip")
define gr = Character("Grace")
define narrator = nvl_narrator


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene door

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show eileen happy

    # These display lines of dialogue.

    play music "sound/music/flute.mp3"

    voice "sound/voice/trip/00753.wav"
    t "Where are the new wine glasses?"

    voice "sound/voice/grace/00753.wav"
    gr "What for?"

    voice "sound/voice/trip/00754.wav"
    t "That should be obvious!"

    voice "sound/voice/grace/00754.wav"
    gr "Oh god, Trip, don't turn this into a big production, please!"

    voice "sound/voice/trip/00755.wav"
    t "Jesus, Grace, come on, I'm not asking a lot here."

    voice "sound/voice/grace/00755.wav"
    gr "What, Trip, don't give me that look!"

    voice "sound/voice/grace/00756.wav"
    gr "You're going to drive me crazy!"

    narrator "It looks like they're arguing. What a bunch of stupid niggers!"
    narrator "Should I knock?"
    menu:
        "Knock.":
            $ knock = "1"
        "Don't knock.":
            $ knock = "0"

    jump apt_check
    # This ends the game.

    return
