from typing import Tuple

import numpy as np


def delta_phi(ticks: int, prev_ticks: int, resolution: int) -> Tuple[float, float]:
    """
    Args:
        ticks: Current tick count from the encoders.
        prev_ticks: Previous tick count from the encoders.
        resolution: Number of ticks per full wheel rotation returned by the encoder.
    Return:
        rotation_wheel: Rotation of the wheel in radians.
        ticks: current number of ticks.
    """

    # TODO: these are random values, you have to implement your own solution in here
    ticks = ticks - prev_ticks
    dphi = ticks/resolution
    # ---
    return dphi, ticks


def pose_estimation(
    R: float,
    baseline: float,
    x_prev: float,
    y_prev: float,
    theta_prev: float,
    delta_phi_left: float,
    delta_phi_right: float,
) -> Tuple[float, float, float]:

    """
    Calculate the current Duckiebot pose using the dead-reckoning model.

    Args:
        R:                  radius of wheel (both wheels are assumed to have the same size) - this is fixed in simulation,
                            and will be imported from your saved calibration for the real robot
        baseline:           distance from wheel to wheel; 2L of the theory
        x_prev:             previous x estimate - assume given
        y_prev:             previous y estimate - assume given
        theta_prev:         previous orientation estimate - assume given
        delta_phi_left:     left wheel rotation (rad)
        delta_phi_right:    right wheel rotation (rad)

    Return:
        x:                  estimated x coordinate
        y:                  estimated y coordinate
        theta:              estimated heading
    """
    left_wheel_distance = delta_phi_left * R
    right_wheel_distance = delta_phi_right * R
    distance = (right_wheel_distance + left_wheel_distance)/2
    delta_theta = (right_wheel_distance - left_wheel_distance)/baseline
    # These are random values, replace with your own
    x_curr = x_prev + distance*np.cos(theta_prev)
    y_curr = y_prev + distance*np.sin(theta_prev)
    theta_curr = theta_prev + delta_theta
    # ---
    return x_curr, y_curr, theta_curr
