import numpy as np
import matplotlib.pyplot as plt
g=9.8

def motion_of_pendulum(time_simulation, time_step, mass, damping, length, 
                       initial_angular_vel, initial_angular_pos):
    
    k1 = 0.5*(-damping/mass + np.sqrt((damping/mass)**2 - 4.0*g/length + 0.0j))
    k2 = 0.5*(-damping/mass - np.sqrt((damping/mass)**2 - 4.0*g/length + 0.0j))
    c1 = (initial_angular_vel - k2*initial_angular_pos)/(k1 - k2)
    c2 = (k1*initial_angular_pos - initial_angular_vel)/(k1 - k2)
    
    t = 0.0
    time = [t]
    position = [initial_angular_pos]
    velocity = [initial_angular_vel]

    while t <= time_simulation:
        t += time_step
        time.append(t)
        ang_pos = c1*np.exp(k1*t) + c2*np.exp(k2*t)
        ang_vel = c1*k1*np.exp(k1*t) + c2*k2*np.exp(k2*t)
        position.append(ang_pos.real)
        velocity.append(ang_vel.real)
    return position, velocity, time

def plot(time_simulation=10.0, time_step=0.1, mass=0.1, damping=0.06, length=1.0, 
         initial_angular_vel=0.0, initial_angular_pos=0.15):
    
    ang_pos, ang_vel, time = motion_of_pendulum(time_simulation, time_step, mass, damping, length, 
                                                initial_angular_vel, initial_angular_pos)

    plt.ioff()
    plt.figure(figsize=(17.0, 9.0))
    plt.plot(time, ang_pos, label='Angular position $\\theta$')
    plt.plot(time, ang_vel, label='Angular velocity $\dot{\\theta}$')
    plt.legend()
    plt.title("Rollno: 130010057", fontweight='bold', fontsize=28)
    plt.xlabel("Time in s", fontweight='bold', fontsize=22)
    plt.savefig('../output/pendulum.png')
    plt.close()
    plt.clf

def test():
    ang_pos, ang_vel, time = motion_of_pendulum(10.0, 1.0, 1.0, 0.1, 1.0, 0.0, 0.0)
    for i in range(len(ang_pos)):
        assert ang_pos[i] == 0.0
        assert ang_vel[i] == 0.0

if __name__ == '__main__':
    test()
    plot()