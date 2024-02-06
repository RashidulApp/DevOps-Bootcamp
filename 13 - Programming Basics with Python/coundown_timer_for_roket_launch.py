import time 


def countdown_timer_for_roket_launch(total_time):
    secound_left = total_time

    while secound_left >= 0:
        time.sleep(1)
        print(f"Time left {secound_left}s")
        secound_left = secound_left - 1
    print("Roket has Launch! 🚀")

countdown_time = 10

countdown_timer_for_roket_launch(countdown_time)