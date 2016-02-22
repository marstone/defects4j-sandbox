#!/usr/bin/env python
import subprocess
import os.path

# consts
HR = '---------------------------'
BUGID = '1'

PATH_FAILING_TEST = 'failing_tests'
PATH_DEFECTS4J = '/media/devel/defects4j/defects4j/'
PATH_DEFECTS4J_PROJECT = PATH_DEFECTS4J + 'framework/projects/Sandbox/'
PATH_COMMIT_DB = PATH_DEFECTS4J_PROJECT + 'commit-db'
PATH_DIR_MAP = PATH_DEFECTS4J_PROJECT + 'dir_map.csv'
PATH_TRIGGER_TESTS = PATH_DEFECTS4J_PROJECT + 'trigger_tests/'
PATH_PATCH = PATH_DEFECTS4J_PROJECT + 'patches/' + BUGID + '.src.patch'


def overwrite_file(file_path, content):
    with open(file_path,'w') as f:
        f.seek(0)
        f.write(content)
        f.truncate()

commits = subprocess.check_output('git log | grep -E FIX -B4 | grep commit', shell=True)
commit_fix = commits.split()[1]
commits = subprocess.check_output('git log | grep -E BUG -B4 | grep commit', shell=True)
commit_bug = commits.split()[1]

commit_db = '%s,%s,%s' % (BUGID, commit_bug, commit_fix)
print HR
print 'generating %s:\n%s' % (PATH_COMMIT_DB, commit_db)
overwrite_file(PATH_COMMIT_DB, commit_db + '\n')

dir_map = '%s,src/main/java,src/test/java\n%s,src/main/java,src/test/java' % (commit_bug, commit_fix)
print HR
print 'generating dir_map.csv:\n%s' % dir_map
overwrite_file(PATH_DIR_MAP, dir_map + '\n')

print HR
print 'generating patch..'
patch_cmd = 'git diff %s %s' % (commit_fix, commit_bug) 
subprocess.check_call(patch_cmd, shell=True)
subprocess.check_call('%s > %s' % (patch_cmd, PATH_PATCH), shell=True)
