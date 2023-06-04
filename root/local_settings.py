"""
2020 Black
Application settings configuration
developer : #ABS
"""

# LOCAL ACCOUNT USERNAME BLACKLIST
LOCAL_ACCOUNT_USERNAME_BLACKLIST = ["admin", 'security', 'secure', 'protection', 'safeguard',
 'privacy', 'confidential', 'shield', 'lock', 'encrypted', 'defender', 'guard', 'safety',
  'firewall', 'securex', 'sentinel', 'secureguard', 'securetech', 'cyber', 'hacker',
   'securecode', 'protect', 'securenet', 'securezone', 'securelock', 'securedata', 'securecloud',
    'securelink', 'secureaccess', 'securelogin', 'secureweb', 'accesscontrol', 'authentication',
     'authorization', 'biometric', 'cryptography', 'cybersecurity', 'dataprotection',
      'digitalcertificate', 'digitalsignature', 'end-to-endencryption', 'forensics',
       'identitymanagement', 'informationsecurity', 'integrity', 'intrusiondetection', 'malware',
        'networksecurity', 'password', 'phishing', 'ransomware', 'riskmanagement',
         'securityaudit', 'securitybreach', 'securityclearance', 'securitypolicy',
          'socialengineering','spyware', 'threatintelligence',
           'virus', 'vulnerabilityassessment', 'zeroday', "god"]

# CSRF LOCAL TRUSTED ORIGINS :
CSRF_LOCAL_TRUSTED_ORIGINS = ['https://8000-irabs175-black-uhfaqk26yl6.ws-eu98.gitpod.io']

# ALLOWED LOCAL HOSTS :
ALLOWED_LOCAL_HOSTS = ['8000-irabs175-black-uhfaqk26yl6.ws-eu98.gitpod.io', '127.0.0.1', 'localhost']

# SECRET KEY
SEC_KEY = 'django-insecure-38n_&5$5ga9)#!-r$&jcyk3^v^673x0u3%f8)*4ekxrd$)=ujs'

# LOCAL HOST IP :
LOCAL_HOST = ('127.0.0.1', '10.0.2.2')

# LOCAL SITE NAME :
LOCAL_SITE_NAME = 'YOUR_DOMIN'

# LOGIN_URL :
LOCAL_LOGIN_URL = '/login/'

# USERNAME MIN LENGTH :
USERNAME_MIN_LENGTH = 6

# ADMINS_PANEL :
ADMINS_PANEL = 'UNIQUEADMINISTRATOR174/'

# DEVELOPERS PANEL :
DEVELOPERS_PANEL = 'UNIQUEDEVELOPER174/'

# BASE_SITE
BASE_ACTIVE_SITE = '8000-irabs175-black-uhfaqk26yl6.ws-eu98.gitpod.io/'

# SITE DEBUG
SITE_DEBIG = True




