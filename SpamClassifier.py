
from TrainingSetsUtil import *

# c is an experimentally obtained value- minimum valye for word not found in training set
def classify(message, training_set, prior = 0.2, c = 3.7e-4):
    
    """
    Returns the probability that the given message is of the given type of
    the training set.
    """
    
    msg_terms = get_words(message)
    
    msg_probability = 1
    
    for term in msg_terms:        
        if term in training_set:
            msg_probability *= training_set[term]
        else:
            msg_probability *= c
            
    return msg_probability * prior

# uncomment this to provide input to the program
  
# mail_msg = raw_input('Enter the message to be classified:')
mail_msg = 'Recipient address'
print('')
#
## 0.3 and 0.6 because the ratio of samples for blacklisted and non-blocked
spam_probability = classify(mail_msg, spam_training_set, 0.3)
ham_probability = classify(mail_msg, ham_training_set, 0.6)
if spam_probability > ham_probability:
   print('Your mail has been classified as SPAM.')
else:
   print('Your mail has been classified as HAM.')
print('')
