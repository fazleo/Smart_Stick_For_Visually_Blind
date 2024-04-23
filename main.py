from machine import Pin, PWM, time_pulse_us
import time

# Pin assignments
trigger_pin = 5
echo_pin = 4
buzzer_pin = 0
vibrator_pin = 14

# Initialize ultrasonic sensor
trigger = Pin(trigger_pin, Pin.OUT)
echo = Pin(echo_pin, Pin.IN)

# Initialize buzzer
buzzer = PWM(Pin(buzzer_pin))
buzzer.freq(2000)  # Set initial frequency

# Initialize vibrator
vibrator = PWM(Pin(vibrator_pin))
vibrator.freq(2000)  # Set initial frequency


# Function to measure distance using ultrasonic sensor
def get_distance():
    trigger.value(0)
    time.sleep_us(2)
    trigger.value(1)
    time.sleep_us(10)
    trigger.value(0)
    pulse_duration = time_pulse_us(echo, 1)
    distance = (pulse_duration / 2) / 29.1
    # Divide by 29.1 to convert to centimeters
    return distance

# Function to control the buzzer sound based on distance
def control_buzzer(distance):
    if distance <= 30:
        buzzer.duty(1023)  # Max duty cycle, maximum sound
    elif distance <= 60:
        buzzer.duty(700)  # Medium duty cycle, medium sound
    else:
        buzzer.duty(0)  # No sound

# Function to control the vibrator based on distance
def control_vibrator(distance):
    if distance <= 30:
        vibrator.duty(1023)  # Max duty cycle, maximum vibration
    elif distance <= 60:
        vibrator.duty(700)  # Medium duty cycle, medium vibration
    else:
        vibrator.duty(0)  # No vibration

# Main loop
while True:
    distance = get_distance()
    print("Distance : ", distance)
    control_buzzer(distance)
    control_vibrator(distance)
    time.sleep(0.1)  # Delay between distance measurements