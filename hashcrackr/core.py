from rich.progress import Progress
import hashlib
import itertools
import time

from hashcrackr.logger import console


def brute_force_crack(target_hash, algorithm, min_length, max_length, charset):
    console.log(f"[info] Trying to decode hash with charset: {charset}")
    try:
        hash_func = getattr(hashlib, algorithm)
    except AttributeError:
        console.log(f"[warning] ⚠️  Algorithm '{algorithm}' is not supported.")
        return None
    
    total_combinations = sum(len(charset) ** length for length in range(min_length, max_length + 1))
    if total_combinations > 1e8:
        console.log(f"[warning] ⚠️  Caution: {total_combinations:,} combinations to try — this may take a very long time!")
    
    checked = 0
    start_time = time.time()

    with Progress() as progress:
        task = progress.add_task("[info]Running brute force...", total=total_combinations)

        for length in range(min_length, max_length + 1):
            for candidate_tuple in itertools.product(charset, repeat=length):
                candidate = ''.join(candidate_tuple)
                hashed_candidate = hash_func(candidate.encode()).hexdigest()
                checked += 1
                progress.update(task, advance=1)

                if hashed_candidate == target_hash:
                    elapsed = time.time() - start_time
                    progress.stop()
                    console.log(f"[success] Password found after {checked} attempts in {elapsed:.2f} seconds")
                    return candidate

    console.log("\n[error]❌ No password found.")
    return None

def wordlist_crack(target_hash, algorithm, wordlist_path):
    try:
        hash_func = getattr(hashlib, algorithm)
    except AttributeError:
        console.log(f"[error] Algorithm '{algorithm}' is not supported.")
        return None

    try:
        with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as f:
            passwords = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        console.log(f"[error] Wordlist file not found: {wordlist_path}")
        return None

    total = len(passwords)
    start_time = time.time()

    with Progress() as progress:
        task = progress.add_task("[cyan]Running wordlist attack...", total=total)

        for idx, password in enumerate(passwords):
            hashed_candidate = hash_func(password.encode()).hexdigest()
            progress.update(task, advance=1)

            if hashed_candidate == target_hash:
                elapsed = time.time() - start_time
                console.log(f"[success] Password found  after {idx + 1} attempts in {elapsed:.2f}s")
                return password

    console.log("[error] ❌ No password match found in wordlist.")
    return None
