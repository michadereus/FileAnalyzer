#%%
import util.config as config

def validate_api_key(api_key):
    if api_key == config.API_KEY:
        return True
    else:
        return False

# %%
