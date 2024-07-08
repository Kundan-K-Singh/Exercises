from enum import Enum


class ExerciseType(Enum):
    PROMPTED = 'PROMPTED'
    COUNTED = 'COUNTED'
    TIMED = 'TIMED'


class ExerciseGroupNameMap(Enum):
    ROM_EXERCISES = 'Range of Motion Exercises'
    STRENGTH_EXERCISES = 'Strength Exercises'
    ISOMETRIC_EXERCISES = 'Isometric Exercises'
    PENDULAR_EXERCISE = 'Pendular Exercises'


EXERCISES = {
    ExerciseGroupNameMap.ROM_EXERCISES: {
        'FLEXION_AND_EXTENSION': {
            'NAME': 'Lift above head',
            'TYPE': ExerciseType.PROMPTED,
            'PROMPTS': {
                'LIFT_UP': {'SAY': 'Lift Up', 'WAIT': 1},
                'WAIT': {'SAY': 'Wait', 'WAIT': 12, 'BEEP': True},
                'LIFT_DOWN': {'SAY': 'Go Down and relax', 'WAIT': 8}
            },
            'REPS': 10
        },
        'HORIZONTAL_ABDUCTION_ADDUCTION': {  # Modify round count
            'NAME': 'Side to Side Abduction and Adduction',
            'TYPE': ExerciseType.PROMPTED,
            'PROMPTS': {
                'MOVE_RIGHT': {'SAY': 'Move Right', 'WAIT': 2},
                'WAIT_1': {'SAY': 'Wait', 'WAIT': 7, 'BEEP': True},
                # Need rest here
                'MOVE_LEFT': {'SAY': 'Move Left', 'WAIT': 2},
                'WAIT': {'SAY': 'Wait', 'WAIT': 5, 'BEEP': True},
            },
            'REPS': 10
        },
        'ABDUCTION_ADDUCTION': {  # Modify round count
            'NAME': 'Abduction and Adduction',
            'TYPE': ExerciseType.PROMPTED,
            'PROMPTS': {
                'MOVE_RIGHT': {'SAY': 'Move Right', 'WAIT': 1},
                'WAIT_1': {'SAY': 'Wait', 'WAIT': 5, 'BEEP': True},
                'MOVE_LEFT': {'SAY': 'Move Left', 'WAIT': 1},
                'WAIT_2': {'SAY': 'Wait', 'WAIT': 9, 'BEEP': True}
            },
            'REPS': 10
        },
        'SIDE_TO_SIDE_ROTATION': {
            'NAME': 'Side to Side Rotation',
            'TYPE': ExerciseType.PROMPTED,
            'PROMPTS': {
                'PUSH_RIGHT': {'SAY': 'Push Right', 'WAIT': 4},
                'RELAX': {'SAY': 'Relax', 'WAIT': 1}
            },
            'REPS': 20
        },
        "WALL_CLIMB_SIDE": {
            'NAME': 'Wall Climb Side',
            'TYPE': ExerciseType.PROMPTED,
            'PROMPTS': {
                'GO_UP': {'SAY': 'Go Up', 'WAIT': 3},
                'WAIT_1': {'SAY': 'Wait', 'WAIT': 15, 'BEEP': True},
                'GO_DOWN': {'SAY': 'Go Down', 'WAIT': 1},
                'RELAX': {'SAY': 'Relax', 'WAIT': 10}
            },
            'REPS': 10
        },
        "WALL_CLIMB_FRONT": {
            'NAME': 'Wall Climb Front',
            'TYPE': ExerciseType.PROMPTED,
            'PROMPTS': {
                'GO_UP': {'SAY': 'Go Up', 'WAIT': 3},
                'WAIT_1': {'SAY': 'Wait', 'WAIT': 15, 'BEEP': True},
                'GO_DOWN': {'SAY': 'Go Down', 'WAIT': 1},
                'RELAX': {'SAY': 'Relax', 'WAIT': 10}
            },
            'REPS': 10
        }
    },
    ExerciseGroupNameMap.STRENGTH_EXERCISES: {
        'SIDE_ARM_PRESS': {
            'NAME': 'Side Arm Press',
            'TYPE': ExerciseType.TIMED,
            'PROMPTS': {
                'START': {'SAY': 'Press down', 'WAIT': 0},
                'WAIT_1': {'SAY': 'Hold', 'WAIT': 7, 'BEEP': True},
                'MOVE_OTHER_SIDE': {'SAY': 'Move to other side', 'WAIT': 2},
                'WAIT_2': {'SAY': 'Hold', 'WAIT': 6, 'BEEP': True},
                'RELAX': {'SAY': 'Relax', 'WAIT': 5}
            },
            'REPS': 20
        },
        'RISE_FRONT': {
            'NAME': 'Raise Front',
            'TYPE': ExerciseType.TIMED,
            'PROMPTS': {
                'START': {'SAY': 'Raise Up', 'WAIT': 0},
                'WAIT_1': {'SAY': 'Hold', 'WAIT': 5, 'BEEP': True},
                'RELAX': {'SAY': 'Relax', 'WAIT': 3}
            },
            'REPS': 10
        },
        'RISE_MID': {
            'NAME': 'Rise Mid',
            'TYPE': ExerciseType.TIMED,
            'PROMPTS': {
                'START': {'SAY': 'Raise Up', 'WAIT': 0},
                'WAIT_1': {'SAY': 'Hold', 'WAIT': 6, 'BEEP': True},
                'RELAX': {'SAY': 'Relax', 'WAIT': 3}
            },
            'REPS': 10
        },
        'RISE_SIDE': {
            'NAME': 'Raise Side',
            'TYPE': ExerciseType.TIMED,
            'PROMPTS': {
                'START': {'SAY': 'Raise Up', 'WAIT': 0},
                'WAIT_1': {'SAY': 'Hold', 'WAIT': 8, 'BEEP': True},
                'RELAX': {'SAY': 'Relax', 'WAIT': 2}
            },
            'REPS': 10
        },
        'W_UP': {
            'NAME': 'W Up',
            'TYPE': ExerciseType.TIMED,
            'PROMPTS': {
                'START': {'SAY': 'Raise Up', 'WAIT': 0},
                'WAIT_1': {'SAY': 'Hold', 'WAIT': 5, 'BEEP': True},
                'RELAX': {'SAY': 'Relax', 'WAIT': 2}
            },
            'REPS': 10
        }
    },
    ExerciseGroupNameMap.ISOMETRIC_EXERCISES: {
        'HAND_PUSH_OUT': {
            'NAME': 'Push Wrist Out',
            'TYPE': ExerciseType.TIMED,
            'PROMPTS': {
                'PUSH_RIGHT': {'SAY': 'Start now', 'WAIT': 12, 'BEEP': True},
                'RELAX': {'SAY': 'Relax', 'WAIT': 6}
            },
            'REPS': 10
        },
        'HAND_PUSH_IN': {
            'NAME': 'Push Wrist In',
            'TYPE': ExerciseType.TIMED,
            'PROMPTS': {
                'PUSH_RIGHT': {'SAY': 'Start now', 'WAIT': 12, 'BEEP': True},
                'RELAX': {'SAY': 'Relax', 'WAIT': 6}
            },
            'REPS': 10
        },
        'ELBOW_PUSH_BACK': {
            'NAME': 'Elbow Push Back',
            'TYPE': ExerciseType.TIMED,
            'PROMPTS': {
                'PUSH_RIGHT': {'SAY': 'Start now', 'WAIT': 12, 'BEEP': True},
                'RELAX': {'SAY': 'Relax', 'WAIT': 5}
            },
            'REPS': 10
        },
        'WALL_PUSH_BACK': {
            'NAME': 'Wall Push Back',
            'TYPE': ExerciseType.TIMED,
            'PROMPTS': {
                'PUSH_RIGHT': {'SAY': 'Start now', 'WAIT': 12, 'BEEP': True},
                'RELAX': {'SAY': 'Relax', 'WAIT': 8}
            },
            'REPS': 10
        },
        'WALL_PUSH_FRONT': {
            'NAME': 'Wall Push Front',
            'TYPE': ExerciseType.TIMED,
            'PROMPTS': {
                'PUSH_RIGHT': {'SAY': 'Start now', 'WAIT': 12, 'BEEP': True},
                'RELAX': {'SAY': 'Relax', 'WAIT': 8}
            },
            'REPS': 10
        },
        'WALL_PUSH_SIDE': {
            'NAME': 'Wall Push SIDE',
            'TYPE': ExerciseType.TIMED,
            'PROMPTS': {
                'PUSH_RIGHT': {'SAY': 'Start now', 'WAIT': 12, 'BEEP': True},
                'RELAX': {'SAY': 'Relax', 'WAIT': 8}
            },
            'REPS': 10
        },
    },
    ExerciseGroupNameMap.PENDULAR_EXERCISE: {
        # TODO Check this
        'PENDULAR_EXERCISE': {
            'NAME': 'Hand Swing',
            'TYPE': ExerciseType.COUNTED,
            'PROMPTS': {
                'START': {'SAY': 'Start now', 'WAIT': 2},
                'CONTINUE': {'SAY': '', 'WAIT': 30, 'BEEP': True}
            },
            'REPS': 1
        }
    }
}
