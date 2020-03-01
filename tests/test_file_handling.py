from os.path import join, exists
import file_handling as fh


def test_verify_path(pickle_test_env):
    # is verify_path creating a directory if directory does not exist yet?
    assert not exists(join(pickle_test_env, 'not_yet_there'))
    fh.verify_path(join(pickle_test_env, 'not_yet_there'))
    assert exists(join(pickle_test_env, 'not_yet_there'))


def test_overwrite_file(pickle_test_env):
    # is verify_path returning a valid filename if filename doesn't exist?
    assert not exists(join(pickle_test_env, 'not_yet_there.pkl'))
    assert fh.overwrite_file(join(pickle_test_env, 'not_yet_there.pkl')) == \
           join(pickle_test_env, 'not_yet_there.pkl')


def test_overwrite_file_exists(pickle_test_env, monkeypatch):
    # is verify_path returning a valid filename if filename exists
    # and file should be overwritten?
    filename = 'pickle/already_there.pkl'
    assert exists(join(pickle_test_env, filename))
    monkeypatch.setattr('builtins.input', lambda overwrite: "y")
    assert fh.overwrite_file(join(pickle_test_env, filename)) == join(pickle_test_env, filename)

