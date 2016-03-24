import os, sys, time, inspect, datetime, json

src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
arch_dir = '../../motion-leap/lib/x64' if sys.maxsize > 2 ** 32 else '../../motion-leap/lib/x86'
leap_dir = '../../motion-leap/lib'
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, leap_dir)))
import Leap

with open(os.getcwd()+'/config.json', 'r') as config_file:
    config = json.load(config_file)

class Listener(Leap.Listener):
    def on_init(self, controller):
        print str(datetime.datetime.now())+" Initialized"

    def on_connect(self, controller):
        print str(datetime.datetime.now())+" Connected"

    def on_disconnect(self, controller):
        print str(datetime.datetime.now())+" Disconnected"

    def on_exit(self, controller):
        print str(datetime.datetime.now())+" Exited"

    def on_frame(self, controller):
        #right most hand speed
        hand_speed = controller.frame().hands.rightmost.palm_velocity

        #output
        print str(datetime.datetime.now())+" x: "+str(hand_speed.x)+" y: "+str(hand_speed.y)+" z: "+str(hand_speed.z)

        #output while it over threshold
        if hand_speed.x > config["threshold"]["x"]:
            print str(datetime.datetime.now())+" right over threshold:"+str(hand_speed.x)
        elif hand_speed.x < config["threshold"]["-x"]:
            print str(datetime.datetime.now())+" left over threshold:"+str(hand_speed.x)
        
        if hand_speed.y > config["threshold"]["y"]:
            print str(datetime.datetime.now())+" up over threshold:"+str(hand_speed.y)
        elif hand_speed.y < config["threshold"]["-y"]:
            print str(datetime.datetime.now())+" down over threshold:"+str(hand_speed.y)

        if hand_speed.z > config["threshold"]["z"]:
            print str(datetime.datetime.now())+" front over threshold:"+str(hand_speed.z)
        elif hand_speed.z < config["threshold"]["-z"]:
            print str(datetime.datetime.now())+" back over threshold:"+str(hand_speed.z)

        time.sleep(config["sleep"])

def main():
    listener = Listener()
    controller = Leap.Controller()
    controller.add_listener(listener)

    print "Press Enter to quit..."
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        controller.remove_listener(listener)

if __name__ == "__main__":
    main()
