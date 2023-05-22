from mergedeep import merge, Strategy
import requests
import secrets
import pprint
import yaml
import json
import hashlib
import os

propulsion = "¶"
ship = ":>"

# Load configuration files from disk
# with open("/vtx/default.yml", "r") as config_file:
#     default_config = yaml.load(config_file, Loader=yaml.FullLoader)

# try:
#     with open("/lab/config.yml", "r") as config_file:
#         user_config = yaml.load(config_file, Loader=yaml.FullLoader)
#         config = merge({}, default_config, user_config, strategy=Strategy.REPLACE)
# except:
#     config = default_config

# pprint.pprint(config)


# Color codes before
class bc:
    FOLD = "\033[94m"
    ROOT = "\033[92m"
    CORE = "\033[91m"


# Color codes after
class ad:
    TEXT = "\033[0m"


# Generate a pseudo-identity, in the Discord ID format
def get_identity():
    count = secrets.choice([17, 18])
    leading = secrets.choice("123456789")
    identity = leading + "".join(secrets.choice("0123456789") for i in range(count))
    return identity


# Generate a deterministic daemon name from a string
def get_daemon(seed):
    obj = {"seed": str(seed)}
    response = requests.get("http://ctx:9666/daemon", json=obj)
    daemon = json.loads(response.text)
    response.close()
    return daemon


# Get a hash value for an entire directory
def hash_directory(path):
    sha1 = hashlib.sha1()
    for root, dirs, files in os.walk(path):
        for file in sorted(files):
            filename = os.path.join(root, file)
            with open(filename, "rb") as f:
                while True:
                    data = f.read(65536)
                    if not data:
                        break
                    sha1.update(data)
    return sha1.hexdigest()


bullets = {
    "⠠",
    "⠏",
    "⠲",
    "⠢",
    "⠐",
    "⠕",
    "⠥",
    "⠭",
    "⠞",
    "⠱",
    "⠟",
    "⠒",
    "⠇",
    "⠙",
    "⠮",
    "⠪",
    "⠑",
    "⠷",
    "⠿",
    "⠊",
    "⠂",
    "⠅",
    "⠡",
    "⠬",
    "⠝",
    "⠰",
    "⠽",
    "⠻",
    "⠧",
    "⠃",
    "⠼",
    "⠹",
    "⠌",
    "⠵",
    "⠄",
    "⠎",
    "⠫",
    "⠳",
    "⠯",
    "⠗",
    "⠉",
    "⠁",
    "⠛",
    "⠸",
    "⠋",
    "⠺",
    "⠔",
    "⠓",
    "⠜",
    "⠆",
    "⠍",
    " ",
    "\n",
}
