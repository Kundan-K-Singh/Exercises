from exercise_config import EXERCISES, ExerciseType
from utils import Utils


def _prompt_executor_t1(prompts):
    for prompt in prompts:
        Utils.say(prompt['SAY'])
        beep = prompt.get('BEEP', False)
        wait = prompt['WAIT']
        if beep:
            Utils.beep(wait)
        else:
            Utils.wait_without_beep(wait)


def _prompt_executor_t2(prompts):
    for prompt in prompts:
        Utils.say(prompt['SAY'])
        beep = prompt.get('BEEP', False)
        wait = prompt['WAIT']
        if beep:
            Utils.beep(wait)
        else:
            Utils.wait_without_beep(wait)


def _start_next_round(rep, exercise):
    Utils.say(f'Round {rep}.')
    prompts = exercise['PROMPTS'].values()
    if exercise['TYPE'] in [ExerciseType.TIMED, ExerciseType.PROMPTED]:
        _prompt_executor_t1(prompts)
    elif exercise['TYPE'] == ExerciseType.COUNTED:
        _prompt_executor_t2(prompts)


def exercise_with_rom():
    for exercise_group_name, exercises in EXERCISES.items():
        Utils.say(f'Starting {exercise_group_name.value}.')
        for _, exercise in exercises.items():
            Utils.say(f"Start {exercise['NAME']}.")
            reps = exercise['REPS']
            for count in range(1, reps + 1):
                _start_next_round(count, exercise)
