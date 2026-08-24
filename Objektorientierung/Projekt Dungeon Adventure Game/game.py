"""
Dungeon Adventure Game - Basis-Level VOLLSTÄNDIGE Musterlösung (Python)
Zielgruppe: Jahrgang 10, Fachinformatiker Anwendungsentwicklung
DIESER CODE IST 100% FERTIG UND LAUFFÄHIG!
"""

from abc import ABC, abstractmethod
import random


# ============================================================================
# KLASSE 1: Abstrakte Klasse Character (Basis für alle Charaktere)
# ============================================================================
class Character(ABC):
    """Abstrakte Klasse für alle Charaktere."""
    
    def __init__(self, name, health, damage):
        self._name = name
        self._max_health = health
        self._health = health
        self._damage = damage
    
    def get_name(self):
        return self._name
    
    def get_health(self):
        return self._health
    
    def get_max_health(self):
        return self._max_health
    
    def get_damage(self):
        return self._damage
    
    def set_health(self, value):
        if value < 0:
            self._health = 0
        elif value > self._max_health:
            self._health = self._max_health
        else:
            self._health = value
    
    def set_damage(self, value):
        if value < 0:
            self._damage = 0
        else:
            self._damage = value
    
    def take_damage(self, amount):
        self.set_health(self._health - amount)
    
    def heal(self, amount):
        old_health = self._health
        self.set_health(self._health + amount)
        actual_heal = self._health - old_health
        print(f"💚 {self._name} heilt sich um {actual_heal} Punkte. "
              f"(HP: {self._health}/{self._max_health})")
    
    def is_alive(self):
        return self._health > 0
    
    def show_status(self):
        health_bar = "█" * (self._health // 10) + "░" * ((self._max_health - self._health) // 10)
        print(f"{self._name:15} | HP: [{health_bar}] {self._health}/{self._max_health}")
    
    @abstractmethod
    def attack(self, target):
        pass


# ============================================================================
# KLASSE 2: Warrior (Krieger) - Unterklasse von Character
# ============================================================================
class Warrior(Character):
    """Krieger: Hohe Health, normaler Schaden."""
    
    def __init__(self, name="Krieger"):
        super().__init__(name, health=120, damage=12)
    
    def attack(self, target):
        damage = self._damage + random.randint(-2, 3)
        print(f"⚔️  {self._name} schlägt {target.get_name()} mit dem Schwert! ({damage} Schaden)")
        target.take_damage(damage)


# ============================================================================
# KLASSE 3: Mage (Magier) - Unterklasse von Character
# ============================================================================
class Mage(Character):
    """Magier: Niedrige Health, hoher Schaden."""
    
    def __init__(self, name="Magier"):
        super().__init__(name, health=80, damage=18)
    
    def attack(self, target):
        damage = self._damage + random.randint(0, 5)
        print(f"🔥 {self._name} wirft einen Feuerball auf {target.get_name()}! ({damage} Schaden)")
        target.take_damage(damage)


# ============================================================================
# KLASSE 4: Archer (Bogenschütze) - Unterklasse von Character
# ============================================================================
class Archer(Character):
    """Bogenschütze: Mittlere Health, mittlerer Schaden."""
    
    def __init__(self, name="Bogenschütze"):
        super().__init__(name, health=100, damage=14)
        self._arrows = 15
    
    def attack(self, target):
        if self._arrows > 0:
            self._arrows -= 1
            damage = self._damage + random.randint(-1, 2)
            print(f"🏹 {self._name} schießt einen Pfeil auf {target.get_name()}! "
                  f"({damage} Schaden, Pfeile: {self._arrows})")
            target.take_damage(damage)
        else:
            damage = 3
            print(f"⚠️  {self._name} hat keine Pfeile mehr und schlägt notdürftig zu! ({damage} Schaden)")
            target.take_damage(damage)
    
    def get_arrows(self):
        return self._arrows


# ============================================================================
# KLASSE 5: Enemy (Gegner)
# ============================================================================
class Enemy:
    """Klasse für Gegner."""
    
    def __init__(self, name, health, damage):
        self._name = name
        self._health = health
        self._max_health = health
        self._damage = damage
    
    def get_name(self):
        return self._name
    
    def get_health(self):
        return self._health
    
    def get_max_health(self):
        return self._max_health
    
    def get_damage(self):
        return self._damage
    
    def set_health(self, value):
        if value < 0:
            self._health = 0
        elif value > self._max_health:
            self._health = self._max_health
        else:
            self._health = value
    
    def take_damage(self, amount):
        self.set_health(self._health - amount)
    
    def is_alive(self):
        return self._health > 0
    
    def attack(self, target):
        damage = self._damage + random.randint(-2, 2)
        print(f"👹 {self._name} greift {target.get_name()} an! ({damage} Schaden)")
        target.take_damage(damage)
    
    def show_status(self):
        health_bar = "█" * (self._health // 10) + "░" * ((self._max_health - self._health) // 10)
        print(f"{self._name:15} | HP: [{health_bar}] {self._health}/{self._max_health}")


# ============================================================================
# GEGNER-VORLAGEN
# ============================================================================
ENEMY_TEMPLATES = [
    ("Goblin", 40, 8),
    ("Orc", 70, 12),
    ("Skeleton", 50, 10),
    ("Troll", 100, 14),
    ("Dark Knight", 80, 15),
]


def create_random_enemy():
    """Erstellt einen zufälligen Gegner."""
    name, health, damage = random.choice(ENEMY_TEMPLATES)
    return Enemy(name, health, damage)


# ============================================================================
# KLASSE 6: Battle (Kampf-System)
# ============================================================================
class Battle:
    """Verwaltet den Kampf zwischen Charakter und Gegner."""
    
    def __init__(self, player, enemy):
        self._player = player
        self._enemy = enemy
        self._round = 0
    
    def show_battle_status(self):
        print("\n" + "="*50)
        self._player.show_status()
        self._enemy.show_status()
        print("="*50)
    
    def player_turn(self):
        """Spieler-Zug."""
        while True:
            print("\nDeine Aktion:")
            print("1. Angreifen")
            print("2. Heilen")
            print("3. Flucht versuchen")
            
            choice = input("Wähle (1-3): ").strip()
            
            if choice == "1":
                self._player.attack(self._enemy)
                return True
            elif choice == "2":
                self._player.heal(30)
                return True
            elif choice == "3":
                if random.random() < 0.5:
                    print("✅ Du bist erfolgreich geflohen!")
                    return False
                else:
                    print("❌ Flucht fehlgeschlagen! Der Gegner greift an!")
                    self._enemy.attack(self._player)
                    return True
            else:
                print("❌ Ungültige Eingabe! Versuche es erneut.")
    
    def enemy_turn(self):
        """Gegner-Zug."""
        self._enemy.attack(self._player)
    
    def start(self):
        """Startet den Kampf."""
        print(f"\n{'='*50}")
        print(f"🎮 KAMPF BEGINNT!")
        print(f"{'='*50}")
        print(f"Du kämpfst gegen: {self._enemy.get_name()}")
        print(f"{'='*50}\n")
        
        while self._player.is_alive() and self._enemy.is_alive():
            self._round += 1
            print(f"\n--- RUNDE {self._round} ---")
            
            player_continues = self.player_turn()
            if not player_continues:
                return False
            
            self.show_battle_status()
            
            if not self._enemy.is_alive():
                break
            
            self.enemy_turn()
            self.show_battle_status()
            
            if not self._player.is_alive():
                break
        
        print(f"\n{'='*50}")
        if self._player.is_alive():
            print(f"🎉 DU HAST GEWONNEN!")
            print(f"Der {self._enemy.get_name()} wurde besiegt!")
            print(f"{'='*50}\n")
            return True
        else:
            print(f"💀 DU HAST VERLOREN!")
            print(f"Der {self._enemy.get_name()} hat dich besiegt!")
            print(f"{'='*50}\n")
            return False


# ============================================================================
# KLASSE 7: Game (Hauptprogramm)
# ============================================================================
class Game:
    """Hauptklasse für das Spiel."""
    
    def __init__(self):
        self._player = None
        self._running = True
        self._victories = 0
        self._defeats = 0
    
    def show_welcome(self):
        """Zeigt die Willkommensnachricht."""
        print("\n" + "="*50)
        print("🎮 WILLKOMMEN ZUM DUNGEON ADVENTURE GAME! 🎮")
        print("="*50)
        print("\nBesiege Monster und werde zum Helden!")
        print("="*50 + "\n")
    
    def choose_character(self):
        """Spieler wählt seinen Charakter-Typ."""
        print("Wähle deinen Charakter-Typ:")
        print("1. Krieger (⚔️  Hohe Health, normaler Schaden)")
        print("2. Magier (🔥 Niedrige Health, hoher Schaden)")
        print("3. Bogenschütze (🏹 Mittlere Health, Pfeile-System)")
        
        while True:
            choice = input("\nWähle (1-3): ").strip()
            
            if choice == "1":
                name = input("Gib deinen Namen ein: ").strip()
                if not name:
                    name = "Krieger"
                self._player = Warrior(name)
                print(f"\n✅ Du hast den Krieger gewählt! Willkommen, {name}!")
                break
            elif choice == "2":
                name = input("Gib deinen Namen ein: ").strip()
                if not name:
                    name = "Magier"
                self._player = Mage(name)
                print(f"\n✅ Du hast den Magier gewählt! Willkommen, {name}!")
                break
            elif choice == "3":
                name = input("Gib deinen Namen ein: ").strip()
                if not name:
                    name = "Bogenschütze"
                self._player = Archer(name)
                print(f"\n✅ Du hast den Bogenschütze gewählt! Willkommen, {name}!")
                break
            else:
                print("❌ Ungültige Eingabe! Versuche es erneut.")
    
    def show_player_status(self):
        """Zeigt den Status des Spielers."""
        print("\n" + "="*50)
        print("DEIN STATUS:")
        self._player.show_status()
        print(f"Siege: {self._victories} | Niederlagen: {self._defeats}")
        print("="*50 + "\n")
    
    def play_battle(self):
        """Spielt einen Kampf."""
        enemy = create_random_enemy()
        battle = Battle(self._player, enemy)
        
        if battle.start():
            self._victories += 1
            print(f"✅ Gesamtsiege: {self._victories}")
        else:
            self._defeats += 1
            print(f"❌ Gesamtniederlage: {self._defeats}")
    
    def show_main_menu(self):
        """Zeigt das Hauptmenü."""
        print("\n" + "="*50)
        print("HAUPTMENÜ")
        print("="*50)
        print("1. Kampf starten")
        print("2. Status anzeigen")
        print("3. Spiel beenden")
        print("="*50)
    
    def run(self):
        """Hauptspiel-Schleife."""
        self.show_welcome()
        self.choose_character()
        
        while self._running:
            self.show_main_menu()
            choice = input("Wähle (1-3): ").strip()
            
            if choice == "1":
                self.play_battle()
            elif choice == "2":
                self.show_player_status()
            elif choice == "3":
                print("\n" + "="*50)
                print("🎮 DANKE FÜR'S SPIELEN!")
                print(f"Deine Statistik: {self._victories} Siege, {self._defeats} Niederlagen")
                print("="*50 + "\n")
                self._running = False
            else:
                print("❌ Ungültige Eingabe! Versuche es erneut.")


# ============================================================================
# MAIN - EINSTIEGSPUNKT DES PROGRAMMS
# ============================================================================
def main():
    """Startet das Spiel."""
    game = Game()
    game.run()


if __name__ == "__main__":
    main()
