#!/usr/bin/env python

import kmsauth
import sys
import os

# user to service authentication
generator = kmsauth.KMSTokenGenerator(
    # KMS key to use for authentication
    sys.argv[1],
    # Encryption context to use
    {
        # We're authenticating to this service
        'to': sys.argv[2],
        # It's from this user
        'from':sys.argv[3],
        # This token is for a user
        'user_type': 'user'
    },
    # Find the KMS key in this region
    os.environ.get('AWS_REGION',os.environ.get('AWS_DEFAULT_REGION','us-east-1'))
)
username = generator.get_username()
token = generator.get_token()

print "%s %s" % (username, token)
