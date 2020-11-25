import airsim
import keyboard

# connect to the AirSim simulator
client = airsim.MultirotorClient()
client.confirmConnection()
client.enableApiControl(True)
client.armDisarm(True)

client.takeoffAsync().join()

print("Take off complete")

i = 0
while True:
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('l'):  # if key 'l' is then move to next waypoint 
            print(f"Starting Move to Waypoint_{i}")
            pos = client.simGetObjectPose(f"Waypoint_{i}").position
            client.moveToPositionAsync(pos.x_val, pos.y_val, pos.z_val, 5).join()
            print(f"Finished Move to Waypoint_{i}")
            i += 1
            continue # finishing the loop
        if keyboard.is_pressed('h'):  # if key 'l' is then move to next waypoint 
            print(f"Starting Move to Waypoint_{i}")
            i -= 1
            pos = client.simGetObjectPose(f"Waypoint_{i}").position
            client.moveToPositionAsync(pos.x_val, pos.y_val, pos.z_val, 5).join()
            print(f"Finished Move to Waypoint_{i}")
            continue # finishing the loop
 
        if keyboard.is_pressed('r'):
            print(f"Reseting to position")
            client.reset()
            continue
        if keyboard.is_pressed('q'):
            break
    except:
        break  # if user pressed a key other than the given key the loop will break

print("All complete")