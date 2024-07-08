# import os
# import time
# import chime
# import sys
# import select
#
# from exercise_list.exercise_with_rom import exercise_with_rom
#
#
# def beep(times, exercise):
#     chime.theme('big-sur')
#     for _ in range(times):
#         chime.success()
#         pause_and_resume(1, exercise)
#
#
# def say(sentence, sleep=2, opt_message=False):
#     if opt_message:
#         print(sentence)
#     os.system(f"say {sentence}")
#     pause_and_resume(sleep, '')
#
#
# def wait_for_input_or_carry_on(timeout, char_inputs: list):
#     user_input, _, _ = select.select([sys.stdin], [], [], timeout)
#     if user_input:
#         char_input = sys.stdin.readline().strip()
#         return char_input in char_inputs
#     return False
#
#
# def pause_and_resume(timeout, exercise):
#     for sec in range(timeout):
#         if wait_for_input_or_carry_on(1, ['p', 'P']):
#             say(f"{exercise} exercise paused. Press  r to resume.", opt_message=True)
#             while True:
#                 ipt = sys.stdin.readline().strip()
#                 if ipt in ['r', 'R']:
#                     say(f"Resuming exercise {exercise}.", opt_message=True)
#                     break
#                 else:
#                     say(f'Unrecognized input. You pressed {ipt}.', sleep=1)
#                     say('Press r to resume.')
#
#
# def start_exercise(exercise_list, reps=5):
#     for exercise in exercise_list:
#         say(f"Now starting exercise {exercise}", sleep=0, opt_message=True)
#         if wait_for_input_or_carry_on(3, ['s', 'S']):
#             say(f"Skipping exercise {exercise}.", opt_message=True)
#             continue
#         for count in range(1, reps + 1):
#             say(f"Round {count}", sleep=0)
#             pause_and_resume(2, exercise)
#             say("Start now!", sleep=0)
#             pause_and_resume(2, exercise)
#             beep(14 , exercise)
#             say("Stop. Rest for 10 seconds", 10)
#         say(f"Done exercise {exercise}.")
#
#
# def main():
#     exercises = [
#         'shrugs', 'wall push front', 'wall push back', 'wall push side', 'back shrugs',
#         'wrist push front', 'wrist push back'
#     ]
#     start_time = time.time()
#     say("Welcome Kundan")
#     start_exercise(exercises)
#     end_time = time.time()
#     minutes, seconds = divmod(round(end_time - start_time), 60)
#     message = f"Congratulations Kundan. You are awesome. You took {minutes} minutes and {seconds} seconds to complete"
#     say(message, opt_message=True)
#
#
# if __name__ == '__main__':
#     exercise_with_rom()
#     # main()


import asyncio

from exercise_list.exercise_with_rom import exercise_with_rom


class Exercise:
    def __init__(self, repetitions, wait_time):
        self.repetitions = repetitions
        self.wait_time = wait_time
        self.paused = False

    async def exercise_loop(self):
        for i in range(self.repetitions):
            while self.paused:
                print("Paused. Press 'r' to resume.")
                await asyncio.sleep(1)
            print(f"Exercise {i + 1}")
            await asyncio.sleep(self.wait_time)  # Simulate exercise with wait
            if i < self.repetitions - 1:
                print(f"Completed {i + 1}/{self.repetitions} exercises. Press 'p' to pause.")

    async def handle_input(self):
        while True:
            command = await asyncio.to_thread(input)
            if command.lower() == 'p':
                self.paused = True
            elif command.lower() == 'r':
                self.paused = False
                print("Resumed")


async def main():
    repetitions = 10
    wait_time = 2  # seconds

    exercise = Exercise(repetitions, wait_time)
    await asyncio.gather(exercise.exercise_loop(), exercise.handle_input())


if __name__ == "__main__":
    # asyncio.run(main())
    exercise_with_rom()