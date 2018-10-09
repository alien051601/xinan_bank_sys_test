from configs import LocalConfig


def config_prepare(test_env):
    return  test_env

env = config_prepare(LocalConfig)

# print(env.mobile_login)