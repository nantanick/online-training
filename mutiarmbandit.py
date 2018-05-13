import numpy as np
import math
import random


class ucb1:
    """
    A multi arm bandit class that uses the UCB1 algorithm
    """
    def __init__(self, arms):
        """
        Parameters
        arms = a list of the arms
        """
        self.arms = arms 
        self.arm_counts = np.array([0]*len(self.arms))
        self.arm_sums = np.array([0.]*len(self.arms))
    def pick_arm(self):
        """
        Picks an arm using the UCB1 algorithm
        
        Returns
         Tuple of the best arm and the index
        """
        n = np.sum(self.arm_counts)
        if n < len(self.arms):
            print('#')
            return (self.arms[n], n)
        else:
            average = self.arm_sums/self.arm_counts
            root = np.sqrt(np.array([2*math.log(n)]*len(self.arms))/self.arm_counts)
            index = np.argmax(average+root)
            return (self.arms[index], index)
    
    def update(self, arm_index, feedback):
        """
        Give feedback to the system.
        Use this function after each call of pick_arm or the algorithm will not
        update.
        
        arm_index = index of the arm
        feedback = an interger signifying the success/failure
        """
        self.arm_sums[arm_index] += feedback
        self.arm_counts[arm_index] += 1

class egreedy:
    """
    e-greedy algorithm
    """
    def __init__(self, arms, e):
        """
        Parameters
        arms = a list of the arms
        e = epsilon value
        """
        self.e = e
        self.arms = arms #
        self.arm_counts = np.array([0]*len(self.arms))
        self.arm_sums = np.array([0.]*len(self.arms))
    
    def pick_arm(self):
        """
        Picks an arm using the e-greedy algorithm
        
        Returns
         Tuple of the best arm and the index
        """
        if random.random() < self.e:
            index = random.randint(0,len(self.arms))
            return (self.arms[index], index)
        else:
            best = np.argmax(self.arm_sums/self.arm_counts)
            return (self.arms[best], best)

    def update(self, arm_index, feedback):
        """
        Give feedback to the system.
        Use this function after each call of pick_arm or the algorithm will not
        update.
        
        arm_index = index of the arm
        feedback = an interger signifying the success/failure
        """
        self.arm_sums[arm_index] += feedback
        self.arm_counts[arm_index] += 1




		
