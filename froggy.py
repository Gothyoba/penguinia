#code by koifly aka publickey
"""Generate random numbers using Fibonacci LFSRs."""
import numpy as np
import math
import time

MAX_ROUNDS = 100

#SEED
SEED_SEED = np.array([0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0])


#INTERNAL STRUCTURES
POLLY_SEED = np.array([0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1])
POLLY_FROG = np.array([0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1])

#HELPER FUNCTIONS

def decimal_to_binary(num):
	"""Return the binary representation of num, as a numpy array."""
	binary_string = np.binary_repr(num)
	binary_arr = np.array([int(bit) for bit in binary_string])

	# Make sure array is exactly 12 bits long
	if binary_arr.size > 13:
		binary_arr = binary_arr[:13]
	elif binary_arr.size < 13:
		zeros = np.array([0]*(13 - binary_arr.size))
		binary_arr = np.insert(binary_arr, 0, zeros)
	return binary_arr

def binary_to_decimal(num):
	"""Convert binary numpy array to integer."""
	decimal = 0
	for (i, bit) in enumerate(num):
		decimal = decimal + bit * 2 ** ((num.size -1) - i)

	return decimal

def update(iv, polly, rounds):
	"""Linear feedback shift register."""
	state = iv
	rounds = rounds % 100
	while rounds != 0:
		shift = state[:11]
		tapped = np.sum(np.array([(c + x) % 2 for (c, x) in zip(polly, state)])) % 2
		state = np.insert(shift,0, tapped)

		rounds = rounds - 1
	return state

def filter(state, start, end):
	"""Filter state to an n-bit number."""
	decimal_state = binary_to_decimal(state)
	return start + (decimal_state % (end - start))

def get_seed():
	return update(SEED_SEED, POLLY_SEED, int(time.time()))

#start is minimum value, end is maximum value seed is optional form: forg(start, end, seed)
def frog(start, end, seed=None):
	"""Get a random number in the range."""
	seed_arr = np.array([])

    # Get seed array (a 12 bit array)
	if seed is None:
		seed_arr = get_seed()
	else:
		seed_arr = decimal_to_binary(seed)

	rounds = binary_to_decimal(seed_arr)

	final_state = update(seed_arr, POLLY_FROG, rounds)

	froggy_random = filter(final_state, start, end)

	return froggy_random
