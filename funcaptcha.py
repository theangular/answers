import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from twocaptcha import TwoCaptcha

config = {
'apiKey':           'YOUR_API_KEY',
'defaultTimeout':    300,
}

solver = TwoCaptcha(**config)

try:
  result = solver.funcaptcha(sitekey='747B83EC-2CA3-43AD-A7DF-701F286FBABA',
							url='https://octocaptcha.com/?origin_page=github_signup_redesign&responsive=true&require_ack=true&version=2',
							surl='https://github-api.arkoselabs.com'
							)

except Exception as e:
  sys.exit(e)

else:
  sys.exit('result: ' + str(result))
