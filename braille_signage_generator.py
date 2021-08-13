import cadquery as cq

# Change the text inside the quotes and a plate
# with the appropriate dots will be generated.
text = "cadquery"

# Braille dot geometry (do not change unless you understand the consequences)
horizontal_interdot = 2.5
vertical_interdot = 2.5
horizontal_intercell = 7.6
vertical_interline = 10.2
dot_height = 0.9
dot_diameter = 1.6

# The base plate thickness
base_thickness = 1.5

# Make sure that only lowercase letters are processed
text = text.lower()

# Map from character to positions.
# Based on https://en.wikipedia.org/wiki/Braille_Patterns
# The positions are
# as follows:
# 1  4
# 2  5
# 3  6
# 7  8
char_point_map = {
    " ": "",
    "a": "1",
    "b": "1,2",
    "c": "1,4",
    "d": "1,4,5",
    "e": "1,5",
    "f": "1,2,4",
    "g": "1,2,4,5",
    "h": "1,2,5",
    "i": "2,4",
    "j": "2,4,5",
    "k": "1,3",
    "l": "1,2,3",
    "m": "1,3,4",
    "n": "1,3,4,5",
    "o": "1,3,5",
    "p": "1,2,3,4",
    "q": "1,2,3,4,5",
    "r": "1,2,3,5",
    "s": "2,3,4",
    "t": "2,3,4,5",
    "u": "1,3,6",
    "v": "1,2,3,6",
    "w": "2,4,5,6",
    "x": "1,4,3,6",
    "y": "1,3,4,5,6",
    "z": "1,3,5,6"
}


def get_plate_width(text):
    """
    Determines the height of the plate based on the number of characters.
    """
    return (len(text) * (horizontal_interdot + horizontal_intercell))


def get_plate_height(text):
    """
    Determines the width of the plate based on the number of characters.
    """
    max_len = max([len(t) for t in text])
    return (2 * horizontal_interdot +
            horizontal_interdot +
            (max_len - 1) * horizontal_intercell)


# Generate the braille plate
plate = (cq.Workplane().rect(get_plate_width(text), get_plate_height(text) + vertical_interdot * 2.0, centered=False)
                       .extrude(base_thickness))

# Add the dot points to the plate
pnts = []
i = 1
offset = 0
for char in text:
    locs = char_point_map[char]
    loc_list = locs.split(",")

    for loc in loc_list:
        if loc == "1":
            pnts.append((horizontal_interdot * i + offset, vertical_interdot * 4))
        elif loc == "2":
            pnts.append((horizontal_interdot * i + offset, vertical_interdot * 3))
        elif loc == "3":
            pnts.append((horizontal_interdot * i + offset, vertical_interdot * 2))
        elif loc == "7":
            pnts.append((horizontal_interdot * i + offset, vertical_interdot * 1))
        elif loc == "4":
            pnts.append((horizontal_interdot * i + horizontal_interdot + offset, vertical_interdot * 4))
        elif loc == "5":
            pnts.append((horizontal_interdot * i + horizontal_interdot + offset, vertical_interdot * 3))
        elif loc == "6":
            pnts.append((horizontal_interdot * i + horizontal_interdot + offset, vertical_interdot * 2))
        elif loc == "8":
            pnts.append((horizontal_interdot * i + horizontal_interdot + offset, vertical_interdot * 1))

    offset += horizontal_intercell
    i += 1
    
plate = plate.faces(">Z").workplane().pushPoints(pnts).circle(dot_diameter / 2.0).extrude(dot_height).faces(">Z").fillet(dot_diameter / 2.0 - 0.151)

show_object(plate)
