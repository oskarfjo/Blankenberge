import numpy as np
import random
import math

class Ship:
    def __init__(self):

        # Dynamic states
        self.position    = 0.0
        self.velocity    = 0.0
        self.disturbance = 1.0
        
        # Vessel parameters
        self.mass              = 10
        self.CD0               = 0.25
        self.Area              = 0.04 
        self.propellerDiameter = 0.08
        self.KT0               = 0.4
        
        # User inputs
        self.control_active = False
        self.setpoint       = 0
        self.rps            = 0
        self.max_rps        = 15000 / 60
        self.s = 0

        self.q_i = 0

    def PID(self, dt):

        w_o = 1.8
        w_r = 1.8
        m = self.mass
        d_stjerne = 1/2 * 1000 * self.CD0 * self.Area * 0.5

        error = self.setpoint - self.position
        error_a = error
        error_dot = 0 - self.velocity

        k_p = m * w_o ** 2
        k_d = 2 * m * w_r - d_stjerne
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
              [-k_p / m, -k_d / m]])
    
            eigen = np.linalg.eigvals(A)
            print("eigenverdier", eigen)
            self.s += 1

    def update_dynamics(self, dt):
        
        # Implement the dynamic model of the ship here

        if self.control_active:
            self.PID(dt)




        thrust = 0.5 * 1025 * self.KT0 * self.propellerDiameter ** 4 * abs(self.rps) * self.rps
        drag = -0.5 * 1025 * self.CD0 * self.Area * abs(self.velocity) * self.velocity

        
        self.velocity = self.velocity + dt * ((1 / self.mass) * (self.disturbance + (1/2) * 1000 * self.KT0 * self.propellerDiameter ** 4 * abs(self.rps) * self.rps - (1/2) * 1000 * self.CD0 * self.Area * abs(self.velocity) * self.velocity ))
        self.position = self.position + dt * self.velocity

        return 0.0
    