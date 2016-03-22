import os, sys, time, inspect

src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
arch_dir = '../../motion-leap/lib/x64' if sys.maxsize > 2 ** 32 else '../../motion-leap/lib/x86'
leap_dir = '../../motion-leap/lib'
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, leap_dir)))
import Leap


def main():
    listener = Leap.Listener()
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
