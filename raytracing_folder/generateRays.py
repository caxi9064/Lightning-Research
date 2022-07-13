import itertools
import json

step = 5
lat = list(range(-90,90+step,step))
lon = list(range(-180,180+step,step))
pairs = list(itertools.product(lat, lon)) # gets the cartesian product of lat and lon

freq = 5e3
alt = 500e3
alpha = 180
phi = 0
rays = [ { "freq": freq, "alt": alt, "lat": pair[0], "lon": pair[1], "alpha": alpha, "phi": phi } for pair in pairs ] 

config = {
    "rayfile_directory": "/projects/caxi9064",

    "date_time_iso_utc":"2021-09-21T14:12:0.0Z",
    "minalt": 1000e3,
    "mode": "DE",
    "Kp": 1,
    "AE": 1.6,
    "Pdyn": 4,
    "Dst": 1.0,
    "ByIMF": 0.0,
    "BzIMF": -5,
    "W": [0.132, 0.303, 0.083, 0.070, 0.211, 0.308],
    "use_tsyg": 1,
    "use_IGRF": 1,

    "t_max": 10,    
    "dt0": 1e-3,
    "dtmax": 0.1,
    "root": 2,
    "fixedstep": 0,
    "maxerr": 5.0e-3,
    "maxsteps": 5e3,
    "outputper": 1,

    "rays": rays
}

# # Creating JSON file: 
# with open('generatedRays.json', 'w') as json_file:
#    print('dump')
#    json.dump(config, json_file, indent=4, separators=(',', ': '))
