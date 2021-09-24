# CONVERT = {'direct_family': ['father', 'mother', 'sister', 'brother', 'son', 'daughter', 'spouse'],
#            'distant_family': ['grandmother', 'grandson', 'granddaughter'],
#            'close': ['date', 'family friend', 'friend', 'girlfriend', 'boyfriend'],
#            'moderate': ['roommate', 'neighbor'],
#            'professional_sensitive': ['doctor', 'patient', 'lawyer', 'nanny', 'contact tracer', 'prosecutor'],
#            'professional': ['manager', 'coworker', 'vice president', 'bailiff', 'supervisor', 'assistant', 'trainer', 'employee', 'student'],
#            'distant': ['acquaintance', 'cashier', 'librarian']}

CONVERT = {'father': 'direct_family', 'mother': 'direct_family', 'sister': 'direct_family', 'brother': 'direct_family', 'son': 'direct_family', 'daughter': 'direct_family', 'spouse': 'direct_family',
           'grandmother': 'distant_family', 'grandson': 'distant_family', 'granddaughter': 'distant_family', 
           'date': 'close', 'family friend': 'close', 'friend': 'close', 'girlfriend': 'close', 'boyfriend': 'close',
           'roommate': 'moderate', 'neighbor': 'moderate',
           'doctor': 'professional_sensitive', 'patient': 'professional_sensitive', 'lawyer': 'professional_sensitive', 'nanny': 'professional_sensitive', 'contact tracer': 'professional_sensitive', 'prosecutor': 'professional_sensitive', 
           'manager': 'professional', 'coworker': 'professional', 'vice president': 'professional', 'bailiff': 'professional', 'supervisor': 'professional', 'assistant': 'professional', 'trainer': 'professional', 'employee': 'professional', 'student': 'professional', 
           'acquaintance': 'distant', 'cashier': 'distant', 'librarian': 'distant'}