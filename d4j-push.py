#!/usr/bin/env python
import subprocess
import os.path

# consts
HR = '---------------------------'
BUGID = '1'
PATH_FAILING_TEST = 'failing_tests'
PATH_DEFECTS4J = '/media/devel/defects4j/defects4j'
PATH_COMMIT_DB = PATH_DEFECTS4J + '/framework/projects/Sandbox/commit-db'
PATH_DIR_MAP = PATH_DEFECTS4J + '/framework/projects/Sandbox/dir_map.csv'
PATH_TRIGGER_TESTS = PATH_DEFECTS4J + '/framework/projects/Sandbox/trigger_tests/'

def overwrite_file(file_path, content):
    with open(file_path,'w') as f:
        f.seek(0)
        f.write(content)
        f.truncate()

commits = subprocess.check_output('git log | grep commit', shell=True)
#commits = subprocess.check_output('git log')

#for commit in commits.splitlines():
#	print commit.split()[1]

commit_fix = commits.splitlines()[0].split()[1]
commit_bug = commits.splitlines()[1].split()[1]

commit_db = '%s,%s,%s' % (BUGID, commit_bug, commit_fix)
print HR
print 'generating %s:\n%s' % (PATH_COMMIT_DB, commit_db)
overwrite_file(PATH_COMMIT_DB, commit_db + '\n')

dir_map = '%s,src/main/java,src/test/java\n%s,src/main/java,src/test/java' % (commit_bug, commit_fix)
print HR
print 'generating dir_map.csv:\n%s' % dir_map
overwrite_file(PATH_DIR_MAP, dir_map + '\n')

print HR
print 'run defects4j test to generate %s...' % PATH_FAILING_TEST
# subprocess.check_call('defects4j test', shell=True)

try:
	os.remove(PATH_FAILING_TEST)
except OSError:
	pass

result = subprocess.check_output('defects4j test', shell=True)

if os.path.isfile(PATH_FAILING_TEST_FILE):	
	subprocess.check_call('cp %s %s' % (PATH_FAILING_TEST, PATH_TRIGGER_TESTS + BUGID))
	print 'succeed'
else:
	print 'generating %s failed.' % PATH_FAILING_TEST
