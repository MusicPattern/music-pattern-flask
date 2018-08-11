def get_chromatic_scale_name(scale_indexes):

    # triades
    if scale_indexes == [0,4,7]:
        return "M"
    if scale_indexes == [0,3,7]:
        return "m"

    # tetrades
    if scale_indexes == [0,4,7,11]:
        return "Maj"
    if scale_indexes == [0,3,7,10]:
        return "min"
    if scale_indexes == [0,4,7,10]:
        return "7"
    if scale_indexes == [0,3,6,10]:
        return "half"

    # pentatonics
    if scale_indexes == [0,4,7,11]:
        return "Major"
    if scale_indexes == [0,3,7,10]:
        return "Minor"
    if scale_indexes == [0,4,7,10]:
        return "7"
    if scale_indexes == [0,3,6,10]:
        return "half"

    # modes
    if scale_indexes == [0,2,4,5,7,9,11]:
        return "Ionian"
    if scale_indexes == [0,2,3,5,7,9,10]:
        return "Dorian"
    if scale_indexes == [0,1,3,5,7,8,10]:
        return "Phrygian"
    if scale_indexes == [0,2,4,6,7,9,11]:
        return "Lydian"
    if scale_indexes == [0,2,4,5,7,9,10]:
        return "Mixolydian"
    if scale_indexes == [0,2,3,5,7,8,10]:
        return "Eolian"
    if scale_indexes == [0,1,3,5,6,8,10]:
        return "Locrian"

    return "-".join(scale_indexes)

def get_chromatic_scale_tags(scale_indexes):
    tags = []
    if 3 in scale_indexes:
        tags.append('isMinor')
    if 4 in scale_indexes:
        tags.append('isMajor')
        if 10 in scale_indexes:
            tags.append('isDominant')
    return tags
