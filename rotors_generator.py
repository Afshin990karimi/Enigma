import random
import pickle

alphabet = 'abcdefghijklmnopqrstuvwxyz'

# Generate random rotor states
rotor1_state = ''.join(random.sample(alphabet, len(alphabet)))
rotor2_state = ''.join(random.sample(alphabet, len(alphabet)))
rotor3_state = ''.join(random.sample(alphabet, len(alphabet)))

# Save the rotor states to a file
with open('today_rotor_state.enigma', 'wb') as f:
    pickle.dump((rotor1_state, rotor2_state, rotor3_state), f)