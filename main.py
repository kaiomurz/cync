import hashlib
import os
import subprocess
import time
from datetime import datetime
from typing import Tuple

from dotenv import load_dotenv


def load_old_hash(hashfile: str) -> str:
    with open(hashfile, "r") as f:
        old_hash = f.read()
    return old_hash


def save_hash(hash_string: str, hashfile: str) -> None:
    with open(hashfile, "w") as f:
        f.write(hash_string)


def get_new_hash(source_path: str) -> str:
    listing = subprocess.Popen(
        f"tree -s {source_path}", shell=True, stdout=subprocess.PIPE
    ).stdout.read()
    new_hash = hashlib.sha256(str(listing).encode("utf-8")).hexdigest()
    return new_hash


def get_env_vars() -> Tuple[str]:
    try:
        del os.environ["HASHFILE"]
        del os.environ["LOCAL"]
        del os.environ["REMOTE"]
    except KeyError:
        pass
    except Exception as e:
        print(e)
        raise e
    load_dotenv()
    hashfile = os.environ["HASHFILE"]
    local = os.environ["LOCAL"]
    remote = os.environ["REMOTE"]
    return hashfile, local, remote


if __name__ == "__main__":
    hashfile, local, remote = get_env_vars()
    print(local, remote)

    old_hash = load_old_hash(hashfile=hashfile)

    while True:
        new_hash = get_new_hash(source_path=local)
        if new_hash != old_hash:
            print(f"rclone sync {local} {remote}")
            subprocess.run(
                f"rclone sync {local} {remote}",
                shell=True,
            )
            print(datetime.now())
            old_hash = new_hash
            save_hash(old_hash, hashfile=hashfile)
        time.sleep(5)
