#!/usr/bin/env python

import kmsauth
import sys
import os

validator = kmsauth.KMSTokenValidator(
    # KMS keys to use for service authentication
    [sys.argv[1]],
    # KMS keys to use for user authentication
    [sys.argv[1]],
    # The context of this validation (the "to" context to validate against)
    sys.argv[2],
    # Find the KMS keys in this region
    os.environ.get('AWS_REGION',os.environ.get('AWS_DEFAULT_REGION','us-east-1'))
)

print "%s" % validator.decrypt_token(sys.argv[3], sys.argv[4])
