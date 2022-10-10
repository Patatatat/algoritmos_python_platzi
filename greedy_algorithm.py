states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])
arr = [1, 2, 2, 3, 3, 3]

print(set(arr))

stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

final_stations = set()

while states_needed:
    best_station = None
    states_covered = set()
    for station, states in stations.items():
        covered = states_needed and states
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered

states_needed -= states_covered
final_stations.add(best_station)

print(set(final_stations))