import numpy as np
import random
import math

class Ship:
    def __init__(self):

        # Dynamic states
        self.position    = 0.0
        self.velocity    = 0.0
        self.disturbance = 20 #random.randint(-15, 15)
        
        # Vessel parameters
        self.mass              = 10
        self.CD0               = 0.25
        self.Area              = 0.04 
        self.propellerDiameter = 0.08
        self.KT0               = 0.4
        self.rho               = 1025

        # User inputs
        self.control_active = False
        self.setpoint       = 0
        self.rps            = 0
        self.max_rps        = 15000 / 60
        self.max_thrust     = 0.5 * self.rho * self.KT0 * self.propellerDiameter ** 4 * abs(self.max_rps) * self.max_rps
        self.s              = 0
        self.q_i            = 0
        self.v              = 0
        self.e              = 1
        self.eps            = 0.5

    def PID(self, dt):

        omega = 1.8
        zeta = 1
        m = self.mass
        d_stjerne = 1/2 * self.rho * self.CD0 * self.Area * 0.5

        error = self.setpoint - self.position
        error_dot = 0 - self.velocity

        k_p = m * omega ** 2
        k_d = m * 2 * zeta * omega - d_stjerne
        k_i = k_p / (5 + error ** 2)

        if error > 1:
            self.e = 1
        elif error < -1:
            self.e = -1
        else:
            self.e = error

        #if self.q_i > -self.eps * self.max_thrust and self.e < 0:
        #    self.q_i += k_i * dt * self.e

        #elif self.q_i < self.eps * self.max_thrust and self.e > 0:
        #    self.q_i += k_i * dt * self.e
        
        if (self.q_i > self.eps * self.max_thrust) and (self.e > 0) or (self.q_i < - self.eps * self.max_thrust) and (self.e < 0):
            self.q_i += 0

        else:
            self.q_i += self.e * dt

        P_ledd = k_d * error
        D_ledd = k_d * error_dot
        I_ledd = k_i * self.q_i


        u = P_ledd + D_ledd + I_ledd

        if (self.s < 1):

            A = np.array([[0, 1],
              [-k_p / m, -(k_d + d_stjerne) / m]])
    
            eigen = np.linalg.eigvals(A)
            print("eigenverdier: ", eigen)
            self.s += 1
        
        print(f'P leddet: {P_ledd: .2f}, D leddet: {D_ledd: .2f}, og I leddet: {I_ledd: .2f}. u blir da {u: .2f}')
        
        return u


    
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
            U = self.PID(dt)
            # self.super_twist(dt)
            self.rps = np.sign(U) * np.sqrt((2 * np.abs(U)) / ( self.rho * self.KT0 * (self.propellerDiameter ** 4)))

        if self.rps > self.max_rps:
            self.rps = self.max_rps
        elif self.rps < -self.max_rps:
            self.rps = -self.max_rps
        
        thrust = 0.5 * self.rho * self.KT0 * self.propellerDiameter ** 4 * abs(self.rps) * self.rps
        drag = -0.5 * self.rho * self.CD0 * self.Area * abs(self.velocity) * self.velocity

        self.velocity = self.velocity + dt * ((1 / self.mass) * (thrust + drag + self.disturbance))
        self.position = self.position + dt * self.velocity

        return 0.0
    
