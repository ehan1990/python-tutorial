

__author__ = 'ehan'

if __name__ == "__main__":

    water_temperature = 20
    freezing_point = 0
    boiling_point = 100

    # if water temperature is greater or equal to 100
    if water_temperature >= boiling_point:
        print "water is evaporating, turning into air"
    # else if water temperature is greater than 0, and smaller than 100
    elif water_temperature > freezing_point and water_temperature < boiling_point:
        print "water is not turning into ice or air. it is in its liquid form"
    # if it doesn't satisfy the previous two conditions (i.e. water temperature is smaller or equal to 0)
    else:
        print "water is turning into ice"
