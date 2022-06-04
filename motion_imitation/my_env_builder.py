import os
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(os.path.dirname(currentdir))
os.sys.path.insert(0, parentdir)

from motion_imitation.robots import laikago
from motion_imitation.envs.env_wrappers import simple_openloop


def build_imitation_env(motion_files, num_parallel_envs, mode,
                        enable_randomizer, enable_rendering,
                        robot_class=laikago.Laikago,
                        trajectory_generator=simple_openloop.LaikagoPoseOffsetGenerator(action_limit=laikago.UPPER_BOUND)):
        assert len(motion_files) > 0
        curriculum_episode_length_start = 20
        curriculum_episode_length_end = 600
        