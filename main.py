import hashlib
import os
import subprocess
import time
from datetime import datetime
from typing import Tuple

from dotenv import load_dotenv

REMOTE_TO_LOCAL_TIME = 10 * 60
LOCAL_TO_REMOTE_TIME = 5


def load_old_hash(hashfile: str) -> str:
    with open(hashfile, "r") as f:
        old_hash = f.read()
    return old_hash


def save_hash(hash_string: str, hashfile: str) -> None:
    with open(hashfile, "w") as f:
        f.write(hash_string)


def get_new_hash(source_path: str) -> str:
    output = subprocess.Popen(
        f"tree -s {source_path}", shell=True, stdout=subprocess.PIPE
    ).stdout
    if output is None:
        raise ValueError
    listing = output.read()
    new_hash = hashlib.sha256(str(listing).encode("utf-8")).hexdigest()
    return new_hash


def get_env_vars() -> Tuple[str, str, str]:
    try:
        del os.environ["HASHFILE"]
        del os.environ["LOCAL"]
        del os.environ["REMOTE"]
    except KeyError:
        print(
            "make sure you have added the HASHFILE, LOCAL, and REMOTE variables in .env"
        )
    except Exception as e:
        print(e)
        raise e
    load_dotenv()
    hashfile = os.environ["HASHFILE"]
    local = os.environ["LOCAL"]
    remote = os.environ["REMOTE"]
    return hashfile, local, remote


def _cync(source: str, dest: str) -> None:
    """Syncs source to destination using rclone"""
    print(f"syncing {source} to {dest}")
    subprocess.run(
        f"rclone sync {source} {dest}",
        shell=True,
    )
    print("sync complete:", datetime.now())


if __name__ == "__main__":
    hashfile, local, remote = get_env_vars()
    print(f"local: {local}, remote: {remote}")
    remote_local_counter = 0

    old_hash = load_old_hash(hashfile=hashfile)

    while True:
        new_hash = get_new_hash(source_path=local)

        if new_hash != old_hash:
            _cync(local, remote)
            old_hash = new_hash
            save_hash(old_hash, hashfile=hashfile)

        if remote_local_counter % REMOTE_TO_LOCAL_TIME == 0:
            _cync(remote, local)
        remote_local_counter += LOCAL_TO_REMOTE_TIME

        time.sleep(LOCAL_TO_REMOTE_TIME)
