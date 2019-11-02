from time import sleep,  time
import RPi.GPIO as GPIO

TRIG_PORT = 27
ECHO_PORT = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG_PORT , GPIO.OUT)
GPIO.setup(ECHO_PORT , GPIO.IN)

def read_distance():
    GPIO.output(TRIG_PORT, GPIO.LOW)
    sleep(0.001)
    GPIO.output(TRIG_PORT, GPIO.HIGH)
    sleep(0.011)
    GPIO.output(TRIG_PORT, GPIO.LOW)

    sig_start = sig_end=0
    while GPIO.input(ECHO_PORT) == GPIO.LOW:
        sig_start = time()
    while GPIO.input(ECHO_PORT) == GPIO.HIGH:
        sig_end = time()

    duration = sig_end - sig_start
    distance = duration * 17000
    return distance

if __name__ == '__main__':
    try:
        while True:
            cm = read_distance()
            print("distance=",cm)
            sleep(0.01)
    except KeyboardInterrupt:
        pass
    GPIO.cleanup()
