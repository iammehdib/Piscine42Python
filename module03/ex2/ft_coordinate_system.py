import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        raw = input("Enter new coordinates as "
                    "floats in format 'x,y,z': ")
        loc_parts = raw.split(',')

        try:
            x_str, y_str, z_str = loc_parts
        except ValueError:
            print('Invalid syntax')
            continue

        try:
            return (float(x_str), float(y_str), float(z_str))
        except ValueError:
            for part in loc_parts:
                try:
                    float(part)
                except ValueError as e:
                    print(f"Error on parameter "
                          f"'{part.strip()}': {e}")


if __name__ == '__main__':
    print('=== Game Coordinate System ===')
    print()
    print('Get a first set of coordinates')
    first_loc = get_player_pos()
    print(f'Got a first tuple: {first_loc}')
    print(f'It includes: X={first_loc[0]}, '
          f'Y={first_loc[1]}, Z={first_loc[2]}')
    dist_from_center = round(
        math.sqrt((0 - first_loc[0]) ** 2
                  + (0 - first_loc[1]) ** 2
                  + (0 - first_loc[2]) ** 2), 4)
    print(f'Distance to center: {dist_from_center}')
    print()
    print('Get a second set of coordinates')
    second_loc = get_player_pos()
    dist_from_second_loc = round(
        math.sqrt((second_loc[0] - first_loc[0]) ** 2
                  + (second_loc[1] - first_loc[1]) ** 2
                  + (second_loc[2] - first_loc[2]) ** 2), 4)
    print(f'Distance between the '
          f'2 sets of coordinates: {dist_from_second_loc}')
