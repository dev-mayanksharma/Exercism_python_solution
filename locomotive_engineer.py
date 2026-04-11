def get_list_of_wagons(*args):
    return list(args)


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    misplaced_wagon1, misplaced_wagon2, locomotive, *remaining_wagons = each_wagons_id      
    return [locomotive, *missing_wagons, *remaining_wagons, misplaced_wagon1, misplaced_wagon2]


def add_missing_stops(route, **kwargs):
    stops = []

    
    for value in kwargs.values():
        if isinstance(value, dict):
            stops.extend(value.values())

    # stop_1, stop_2 sorted
    numbered = [(k, v) for k, v in kwargs.items() if k.startswith("stop_")]
    numbered.sort(key=lambda x: int(x[0].split("_")[1]))

    stops.extend([v for k, v in numbered])

    route["stops"] = stops
    return route


def extend_route_information(route, more_route_information):
    return {**route, **more_route_information}


def fix_wagon_depot(wagons):
    return [list(row) for row in zip(*wagons)]