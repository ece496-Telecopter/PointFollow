# Purpose
The project is a very simple demonstration of following spheres in an unreal simulation using the airsim drone plugin. The entire code is written using only AirSim APIs and no access to UE4 code.

The drone follows 4 spheres one after the other based on commands from the user.

# Instructions

## How to Run

1. Clone the repository
2. Run the vs solution (in DebugGameEditor mode), and build it in debug mode. If you run into errors, close the vs solution, open the solution file and edit the path to point to the correct UE4 engine directory.
3. Once UE4 is open, play the project
4. Run the following command:
```
python3 FollowBasicWaypoints.py
```

## Commands to control the python script

`h` is `previous` 

`l` is `next` 

`q` is `quit` 

### Tips and Warnings
1. Don't spam commands, this will 100% cause the script to lag and freeze output on the UE4 engine. The script is very basic and does not handle any spam protection or any sort of colision on the actual engine
2. Wait for a previous command to finish (there will be a output on the console and there ill be visual cues to indicate) before you enter a new command 
3. You can only go next when the drone is on the ground, don't try to go previous this will do weird things and might crash AirSim, and only previous at the last ring since there is no rings.
4. You can go next a total of 4 times, since there are 4 points to go to.
5. The commands take a small amount of time to respond so please be patient.

<3
