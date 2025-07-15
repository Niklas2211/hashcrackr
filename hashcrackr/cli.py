import click
import rich_click
from hashcrackr.core import brute_force_crack, wordlist_crack
from hashcrackr.logger import console


@click.group(cls=rich_click.RichGroup)
def cli():
    """HashCrackr CLI Tool"""
    pass

@cli.command()
@click.option('--hash', 'target_hash', required=True, help='The hash value to crack')
@click.option('--algorithm', default='md5', help='Hash algorithm to use (e.g., md5, sha1, sha256)')
@click.option('--min-length', default=1, type=int, help='Minimum password length')
@click.option('--max-length', default=4, type=int, help='Maximum password length')
@click.option('--lowercase/--no-lowercase', default=True, help='Include lowercase letters')
@click.option('--uppercase/--no-uppercase', default=False, help='Include uppercase letters')
@click.option('--digits/--no-digits', default=False, help='Include digits (0–9)')
@click.option('--symbols/--no-symbols', default=False, help='Include special characters')
def brute(target_hash, algorithm, min_length, max_length, lowercase, uppercase, digits, symbols):
    """Perform a brute-force attack to crack a hash"""
    charset = ''
    if lowercase:
        charset += 'abcdefghijklmnopqrstuvwxyz'
    if uppercase:
        charset += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if digits:
        charset += '0123456789'
    if symbols:
        charset += '!@#$%^&*()_-+=[]{}|;:,.<>?/~`'

    if not charset:
        click.secho("⚠️ No character set selected. Brute force cannot proceed.", fg="red")
        return

    result = brute_force_crack(target_hash, algorithm, min_length, max_length, charset)

    if result:
        console.log(f"[success] ✅ Password cracked: {result}")
    else:
        console.log("[error] ❌ No matching password found within the selected character set.")

@cli.command()
@click.option('--hash', 'target_hash', required=True, help='The hash value to crack')
@click.option('--algorithm', default='md5', help='Hash algorithm to use (e.g., md5, sha1, sha256)')
@click.option('--wordlist', required=True, type=click.Path(exists=True), help='Path to the wordlist file')
def wordlist(target_hash, algorithm, wordlist):
    """Perform a wordlist attack to crack a hash"""
    result = wordlist_crack(target_hash, algorithm, wordlist)

    if result:
        console.log(f"[success] ✅ Password cracked: {result}")
    else:
        console.log("[error] ❌ No match found in wordlist.")

if __name__ == "__main__":
    cli()
