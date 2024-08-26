from datetime import datetime
import time
import subprocess
import hashlib
import sys


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
    print(str(listing))
    return new_hash


if __name__ == "__main__":
    # load environment variables
    old_hash = load_old_hash(hashfile="hashfile.txt")
    while True:
        new_hash = get_new_hash(source_path="~/obdsidian/Kaiomurz/")
        print(new_hash)
        if new_hash != old_hash:
            subprocess.run(
                "rclone sync ~/obdsidian/Kaiomurz/ googledrive:/DriveSyncFiles/Kaiomurz",  # replace with vars
                shell=True,
            )
            print(datetime.now())
            old_hash = new_hash
            save_hash(old_hash, hashfile="hashfile.txt")
        time.sleep(5)
