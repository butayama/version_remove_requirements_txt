from scripts.edit_requirements import strip_version_numbers
from shutil import copy2
from os.path import join

def test_strip_version_numbers(requirements_test_env):
    copy2('requirements_test.txt', join(requirements_test_env, 'requirements.txt'))
    copy2('requirements_result.txt', join(requirements_test_env, 'requirements_result.txt'))
    strip_version_numbers(join(requirements_test_env, 'requirements.txt'), join(requirements_test_env, 'requirements_old.txt'))
    with open(join(requirements_test_env, 'requirements.txt'), "r") as gen:
        with open(join(requirements_test_env, 'requirements_result.txt'), "r") as res:
            for l_gen, l_res in zip(gen, res):
                assert l_gen == l_res

