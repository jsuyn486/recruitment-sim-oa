'''
TO explain the physics behind this code,

I have started with the assumption.

I have assumed that the gravitaional constant is 9.81 m/s^2, and the first moment of inertia for a uniform disk is 1/2 m r^2.


torsion = I * alpha
where I is the moment of inertia, and alpha is the angular acceleration.

torsion = friction force * radius

Friction force = friction coefficient * normal force

Friction force * r = 1/2m * r^2 * a / r
Friction force = 1/2 m * a
m * g * friction coefficient = 1/2 m * a

friction coefficient = a / (2 * g * cos(theta))

F = ma

mg sin(theta) - mg cos(theta) * friction coefficient = ma
plugging in friction coefficient,
g sin(theta) - a/2 = a

a = 2/3 g sin(theta)

v^2 = u^2 + 2 a L

u = 0, as the initial speed is 0

v = sqrt(2 * (2/3 g sin(theta)) * L)
Therefore, v = sqrt(4/3 g h)

This solution was aided by youtube videos and my knowledge of highschoolphysics.
'''

import numpy as np


def final_disk_speed(height: float, length: float, incline: float, mass: float, friction: float, radius: float) -> float:
    """
    Returns the speed of a uniform disk after it reaches the bottom of an inclined slope.

    :param height: the height of the incline (meters)
    :param length: the length of the slope (meters)
    :param incline: the angle of the slope (degrees)
    :param mass: the mass of the ball (kilograms)
    :param friction: kinetic friction coefficient of the slope's surface (0.0 - 1.0)
    :param radius: the radius of the disk (meters)
    :return: the speed of the disk (m/s)
    """

    g = 9.81  # gravitational constant (m/s^2)

    if (np.abs(height - length*np.sin(incline*np.pi/180)) > 0.01):
        raise ValueError("Wrong geometry.") # to prevent geometrically inconsistent inputs
    if (friction < 0 or friction > 1):
        raise ValueError("Friction must be between 0.0 and 1.0.") # to prevent invalid friction inputs
    if (mass <= 0):
        raise ValueError("Mass must be positive.") # to prevent invalid mass inputs
    if (radius <= 0 or radius >= length):
        raise ValueError("invalid radius.") # to prevent invalid radius inputs

    speed = np.sqrt(4/3*g*height) 
    ''' I got this equation from dynamics and kinematics equations. 
    I have simplified sin(theta) L = h, and added the if statement above to prevent inconsistent outputs.
    Since the question assumes that the disk rolls without slipping and no air friction, friction does not affect the final speed.
    '''
    return speed


#Case 1
v = final_disk_speed(5, 10, 30, 2, 0.1, 0.5)
print(v)

#Case 2
v = final_disk_speed(2, 4, 30, 1, 0.5, 0.2)
print(v)
