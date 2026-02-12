"""
Night City Theme - Showcase Datei
===================================
Diese Datei zeigt alle Syntax-Highlights des Themes.
Perfekt für Screenshots und Demos! 🌃
"""

import asyncio
import json
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


# === KONSTANTEN & GLOBALS ===
VERSION: str = "2.077"
MAX_CONNECTIONS: int = 100
PI: float = 3.14159
IS_PRODUCTION: bool = True
NONE_VALUE: None = None


# === DATACLASS - Klassen-Definition ===
@dataclass
class Netrunner:
    """Repräsentiert einen Netrunner in Night City"""
    name: str
    level: int
    cyberware: List[str]
    credits: float = 0.0
    is_online: bool = False
    
    def __post_init__(self):
        """Initialisierung nach der Erstellung"""
        if self.level < 1:
            raise ValueError("Level muss mindestens 1 sein")
    
    def __repr__(self) -> str:
        return f"<Netrunner: {self.name} (Lvl {self.level})>"


# === KLASSE mit Vererbung ===
class CyberDeck:
    """Basis-Klasse für Cyberdecks"""
    
    def __init__(self, model: str, ram: int):
        self.model = model
        self.ram = ram
        self._access_key: Optional[str] = None
    
    @property
    def access_key(self) -> Optional[str]:
        """Getter für Access Key"""
        return self._access_key
    
    @access_key.setter
    def access_key(self, key: str) -> None:
        """Setter mit Validierung"""
        if len(key) < 8:
            raise ValueError("Access Key zu kurz!")
        self._access_key = key
    
    def hack(self, target: str) -> Dict[str, any]:
        """Simuliert einen Hack-Versuch"""
        return {
            "target": target,
            "success": True,
            "timestamp": datetime.now().isoformat()
        }

class MilitechDeck(CyberDeck):
    """Spezielles Militech Cyberdeck"""
    
    def __init__(self, model: str, ram: int, military_grade: bool = True):
        super().__init__(model, ram)
        self.military_grade = military_grade
    
    def secure_hack(self, target: str, password: str) -> bool:
        """Militech-spezifischer Secure Hack"""
        result = self.hack(target)
        return result["success"] and self.military_grade


# === ASYNC FUNKTIONEN ===
async def connect_to_net(netrunner: Netrunner, timeout: int = 30) -> bool:
    """
    Verbindet einen Netrunner mit dem Net.
    
    Args:
        netrunner: Der Netrunner der sich verbinden will
        timeout: Timeout in Sekunden
    
    Returns:
        True wenn erfolgreich, sonst False
    """
    print(f"[INFO] {netrunner.name} verbindet sich mit dem Net...")
    await asyncio.sleep(1)  # Simuliere Verbindungsaufbau
    
    if netrunner.level >= 10:
        netrunner.is_online = True
        return True
    return False


async def breach_protocol(targets: List[str]) -> Dict[str, int]:
    """Führt Breach Protocol auf mehrere Targets aus"""
    results = {}
    
    for target in targets:
        print(f"[BREACH] Breaching {target}...")
        await asyncio.sleep(0.5)
        results[target] = 1 if target != "ICE" else 0
    
    return results


# === STANDARD FUNKTIONEN ===
def calculate_damage(base_dmg: float, crit_chance: float = 0.15) -> Tuple[float, bool]:
    """
    Berechnet Schaden mit Crit-Chance.
    
    Returns:
        Tuple mit (Schaden, War es ein Crit?)
    """
    import random
    
    is_crit: bool = random.random() < crit_chance
    damage: float = base_dmg * (2.0 if is_crit else 1.0)
    
    return (damage, is_crit)


def parse_config(filepath: str) -> Dict:
    """Liest eine Config-Datei und parst JSON"""
    try:
        path = Path(filepath)
        
        if not path.exists():
            raise FileNotFoundError(f"Config nicht gefunden: {filepath}")
        
        with open(path, 'r', encoding='utf-8') as file:
            config = json.load(file)
        
        # Validierung
        required_keys = ['version', 'host', 'port']
        for key in required_keys:
            if key not in config:
                raise KeyError(f"Missing required key: {key}")
        
        return config
    
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"[ERROR] Config parsing failed: {e}")
        return {}
    except Exception as ex:
        print(f"[CRITICAL] Unexpected error: {ex}")
        raise


def format_credits(amount: float) -> str:
    """Formatiert Credits mit Tausender-Trennung"""
    return f"€${amount:,.2f}"


# === LIST COMPREHENSIONS & LAMBDA ===
def filter_high_level_runners(netrunners: List[Netrunner]) -> List[Netrunner]:
    """Filtert Netrunner mit Level >= 20"""
    # List Comprehension
    high_level = [runner for runner in netrunners if runner.level >= 20]
    
    # Lambda Sort
    sorted_runners = sorted(high_level, key=lambda r: r.level, reverse=True)
    
    return sorted_runners


def process_data(numbers: List[int]) -> Dict[str, any]:
    """Demonstriert verschiedene List Operations"""
    # Map mit Lambda
    squared = list(map(lambda x: x ** 2, numbers))
    
    # Filter mit Lambda
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    
    # Reduce (sum)
    total = sum(numbers)
    
    return {
        "squared": squared,
        "even": even_numbers,
        "sum": total,
        "max": max(numbers) if numbers else 0,
        "min": min(numbers) if numbers else 0
    }


# === DEKORATOREN ===
def log_execution(func):
    """Decorator zum Loggen von Funktionsaufrufen"""
    def wrapper(*args, **kwargs):
        print(f"[LOG] Executing: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"[LOG] Completed: {func.__name__}")
        return result
    return wrapper


@log_execution
def important_operation(data: str) -> str:
    """Eine wichtige Operation"""
    return data.upper()


# === CONTEXT MANAGER ===
class DatabaseConnection:
    """Simpler Context Manager für DB-Verbindungen"""
    
    def __init__(self, db_name: str):
        self.db_name = db_name
        self.connection = None
    
    def __enter__(self):
        print(f"[DB] Connecting to {self.db_name}...")
        self.connection = f"Connection<{self.db_name}>"
        return self.connection
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"[DB] Closing connection to {self.db_name}")
        self.connection = None
        return False


# === GENERATOR ===
def cyberdeck_generator(count: int):
    """Generator für Cyberdeck-Namen"""
    models = ["Militech", "Arasaka", "Zetatech", "Kang Tao"]
    
    for i in range(count):
        model = models[i % len(models)]
        yield f"{model}-{1000 + i}"


# === MATCH-CASE (Python 3.10+) ===
def process_netrunner_action(action: str) -> str:
    """Verarbeitet Netrunner-Aktionen"""
    match action:
        case "hack":
            return "🔓 Initiating breach protocol..."
        case "scan":
            return "👁️ Scanning network..."
        case "upload":
            return "⬆️ Uploading daemon..."
        case "disconnect":
            return "❌ Disconnecting from net..."
        case _:
            return "❓ Unknown action"


# === MAIN EXECUTION ===
async def main():
    """Hauptfunktion mit Demo-Code"""
    print("=" * 60)
    print("    NIGHT CITY THEME - SYNTAX SHOWCASE")
    print("=" * 60)
    print()
    
    # Netrunner erstellen
    runner = Netrunner(
        name="V",
        level=30,
        cyberware=["Cyberdeck", "Sandevistan", "Mantis Blades"],
        credits=125_000.50
    )
    print(f"Netrunner created: {runner}")
    print(f"Credits: {format_credits(runner.credits)}")
    print()
    
    # Cyberdeck
    deck = MilitechDeck("M-76", ram=64, military_grade=True)
    deck.access_key = "NightCity2077"
    print(f"Cyberdeck: {deck.model} ({deck.ram} GB RAM)")
    print()
    
    # Net-Verbindung
    connected = await connect_to_net(runner, timeout=30)
    print(f"Connection status: {'✅ ONLINE' if connected else '❌ OFFLINE'}")
    print()
    
    # Breach Protocol
    targets = ["Corporate Server", "Security Node", "ICE", "Database"]
    results = await breach_protocol(targets)
    print(f"Breach results: {results}")
    print()
    
    # Damage Calculation
    dmg, is_crit = calculate_damage(100.0, crit_chance=0.25)
    print(f"Damage: {dmg:.1f} {'💥 CRIT!' if is_crit else ''}")
    print()
    
    # List Operations
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    data = process_data(numbers)
    print(f"Data processing: {data}")
    print()
    
    # Generator
    print("Cyberdecks:")
    for deck_name in cyberdeck_generator(6):
        print(f"  - {deck_name}")
    print()
    
    # Match-Case
    actions = ["hack", "scan", "upload", "reboot"]
    for action in actions:
        result = process_netrunner_action(action)
        print(f"{action:12} -> {result}")
    print()
    
    # Context Manager
    with DatabaseConnection("NightCityDB") as conn:
        print(f"Using connection: {conn}")
    print()
    
    # String Operations
    message = "Wake up, Samurai. We have a city to burn."
    print(f"Original: {message}")
    print(f"Upper: {message.upper()}")
    print(f"Words: {message.split()}")
    print(f"Contains 'city': {'city' in message.lower()}")
    print()
    
    # F-Strings & Formatting
    name, age, level = "Johnny Silverhand", 34, 50
    print(f"{name:30} Age: {age:3d} | Level: {level:3d}")
    print(f"Hex Level: {level:#06x}")
    print(f"Binary: {level:08b}")
    print()
    
    # Dictionary Operations
    inventory = {
        "weapons": ["Mantis Blades", "Comrade's Hammer"],
        "quickhacks": ["Breach Protocol", "Ping", "Overheat"],
        "consumables": ["MaxDoc Mk.3", "Bounce Back"]
    }
    
    for category, items in inventory.items():
        print(f"{category.capitalize()}:")
        for item in items:
            print(f"  • {item}")
    print()
    
    # Regular Expressions
    import re
    pattern = r'\b[A-Z][a-z]+\b'
    text = "Night City is the Place to Be for Edgerunners"
    matches = re.findall(pattern, text)
    print(f"Regex matches: {matches}")
    print()
    
    # Error Handling
    try:
        risky_value = 100 / 0  # Division by zero
    except ZeroDivisionError as e:
        print(f"⚠️ Caught error: {e}")
    except Exception as ex:
        print(f"❌ Unexpected error: {ex}")
    else:
        print("✅ No errors")
    finally:
        print("🏁 Cleanup completed")
    print()
    
    print("=" * 60)
    print("    END OF SHOWCASE - THEME LOOKS PREEM!")
    print("=" * 60)


# === ENTRY POINT ===
if __name__ == "__main__":
    # Run async main
    asyncio.run(main())
    
    # Deprecated warning example
    import warnings
    warnings.warn("This is a deprecated feature", DeprecationWarning)
