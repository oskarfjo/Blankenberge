import numpy as np
import random
import math

class Ship:
    def __init__(self):

        # Dynamic states
        self.position    = 0.0
        self.velocity    = 0.0
        self.disturbance = random.randint(-15, 15)
        
        # Vessel parameters
        self.mass              = 10
        self.CD0               = 0.25
        self.Area              = 0.04 
        self.propellerDiameter = 0.08
        self.KT0               = 0.4
        self.rho               = 1000

        # User inputs
        self.control_active = False
        self.setpoint       = 0
        self.rps            = 0
        self.max_rps        = 15000 / 60
        self.s              = 0

        self.q_i            = 0
        self.v              = 0

    def PID(self, dt):

        omega = 1.5
        zeta = 1
        m = self.mass
        d_stjerne = 1/2 * self.rho * self.CD0 * self.Area * 0.5

        error = self.setpoint - self.position
        error_a = error
        error_dot = 0 - self.velocity

        k_p = m * omega ** 2
        k_d = m * 2 * zeta * omega - d_stjerne
        k_i = k_p / 10

        if error_a > 1:
            error_a = 1
        elif error_a < -1:
            error_a = -1

        self.q_i = self.q_i + dt * error_a 

        u = k_p * error + k_d * error_dot + k_i * self.q_i

        if u > self.max_rps:
            u = self.max_rps
        elif u < -self.max_rps:
            u = -self.max_rps

        self.rps = u   

        if (self.s < 1):

            A = np.array([[0, 1],
              [-k_p / m, -(k_d + 2 * d_stjerne) / m]])
    
            eigen = np.linalg.eigvals(A)
            print("eigenverdier", eigen)
            self.s += 1



    
    def super_twist(self, dt):

        k_a = -100
        k_b = -1

        error = self.setpoint - self.position

        v_dot = - k_b * np.sign(error)   

        self.v = self.v + v_dot * dt 

        u = -k_a * math.sqrt(abs(error)) * np.sign(error) + self.v

        self.rps = u




    def update_dynamics(self, dt):

        if self.control_active:
            self.PID(dt)
            # self.super_twist(dt)

        # thrust = 0.5 * self.rho * self.KT0 * self.propellerDiameter ** 4 * abs(self.rps) * self.rps
        # drag = -0.5 * self.rho * self.CD0 * self.Area * abs(self.velocity) * self.velocity

        self.velocity = self.velocity + dt * ((1 / self.mass) * (self.disturbance + (1/2) * self.rho * self.KT0 * self.propellerDiameter ** 4 * abs(self.rps) * self.rps - (1/2) * self.rho * self.CD0 * self.Area * abs(self.velocity) * self.velocity ))
        self.position = self.position + dt * self.velocity

        return 0.0
    
