# hashcrackr/logger.py
from rich.console import Console
from rich.theme import Theme

custom_theme = Theme({
    "info": "dim cyan",
    "success": "bold green",
    "error": "bold red",
    "warning": "yellow"
})

console = Console(theme=custom_theme)