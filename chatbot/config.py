class Config(object):
    DEBUG = True
    TESTING = False


class DevelopmentConfig(Config):
    SECRET_KEY = "this-is-a-super-secret-key"
    OPENAI_KEY = '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'


config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}
