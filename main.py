import subprocess

# execute_type = 'Smoke test'
execute_type = 'Regression test'
subprocess.call(['python', 'Screen\\login_page\\testSuite.py', execute_type])
