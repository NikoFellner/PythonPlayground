🧠 Aufgabe 1 – Q‑Learning Agent in einem einfachen GridWorld‑Environment
Diese Aufgabe führt dich Schritt für Schritt durch die Implementierung eines einfachen Reinforcement‑Learning‑Szenarios.
Du entwickelst:
1. Ein Environment (z. B. GridWorld)
2. Einen Q‑Learning‑Agenten
3. Eine Trainingsschleife, die Agent und Environment verbindet
Dabei sollen grundlegende Softwarearchitektur‑Prinzipien wie Single Responsibility, Separation of Concerns, Testbarkeit, Erweiterbarkeit und Kapselung berücksichtigt werden.
---
🎯 Ziel der Aufgabe
Implementiere ein RL‑System, in dem ein Agent in einer kleinen Grid‑Welt lernt, ein Ziel zu erreichen.
Der Agent soll Q‑Learning verwenden.
---
📦 Projektstruktur (Vorschlag)
/src
  /environment
    grid_world.py
  /agent
    q_learning_agent.py
  /training
    trainer.py
main.py
README.md
---
🧩 Teil 1 – Environment: GridWorld
Erstelle eine Klasse:
class GridWorld: …
Anforderungen
• Das Environment repräsentiert ein 2D‑Grid (z.B. 5×5).
• Es gibt:
	◦ eine Startposition
	◦ eine Zielposition
• Der Agent kann Aktionen ausführen:
	◦ “up”, “down”, “left”, “right”
• Das Environment liefert:
	◦ state (z.B. (x, y))
	◦ reward
	◦ done
Methoden
• reset() # liefert ein neues environment mit final und start position
• step(action) → (next_state, reward, done)
• get_available_actions(state) → list[str]
Architekturhinweise
• Keine RL‑Logik im Environment.
• Deterministisches Verhalten.
• Kleine, klar abgegrenzte Methoden.
Tipp
Reward‑Struktur (Vorschlag):
• +1 für Ziel erreicht
• –1 für ungültige Aktion
• –0.1 pro Schritt
---
🤖 Teil 2 – Q‑Learning Agent: QLearningAgent
Erstelle eine Klasse:
class QLearningAgent: …
Anforderungen
Der Agent soll:
• eine Q‑Tabelle verwalten
• eine ε‑greedy Policy nutzen
• Q‑Werte nach der klassischen Formel updaten
Q‑Learning‑Updateformel
Q(s,a) ← Q(s,a) + α * ( r + γ * max_a’ Q(s’,a’) – Q(s,a) )
Methoden
• select_action(state) → action
• update(state, action, reward, next_state)
• get_q_value(state, action)
• set_q_value(state, action, value)
Parameter
• alpha (Lernrate)
• gamma (Discount‑Faktor)
• epsilon (Exploration‑Rate)
• optional: epsilon_decay
Architekturhinweise
• Keine Environment‑Logik im Agent.
• Q‑Tabelle kapseln.
• Agent soll austauschbar sein (z.B. später SARSA, DQN).
---
🔁 Teil 3 – Training: Trainer
Erstelle eine Klasse:
class Trainer: …
Anforderungen
Diese Klasse verbindet Agent und Environment.
Sie soll:
• Episoden ausführen
• pro Episode:
	◦ Environment resetten
	◦ Agent Aktionen wählen lassen
	◦ Q‑Updates durchführen
	◦ Episode beenden, wenn done == True
• Trainingsmetriken sammeln (z. B. Episodenlänge, Gesamt‑Reward)
Methoden
• run_episode() → total_reward
• train(num_episodes) → list[float]
Architekturhinweise
• Trainer kennt Agent und Environment.
• Agent und Environment kennen sich nicht gegenseitig.
• Trainer ist zuständig für Ablaufsteuerung und Logging.
---
🚀 Teil 4 – main.py
Implementiere ein Skript, das:
• das Environment erstellt
• den Agenten erstellt
• den Trainer erstellt
• das Training startet
• Ergebnisse ausgibt (z. B. durchschnittliche Rewards)
---
📈 Optional: Visualisierung
Mögliche Erweiterungen:
• Pfad des Agenten visualisieren
• Q‑Tabelle plotten
• Rewards über Episoden darstellen
Hilfreiche Libraries:
• matplotlib
• numpy
• tqdm
---
🧪 Optional: Tests
Schreibe Unit‑Tests für:
• Environment‑Grenzfälle
• Q‑Value‑Updates
• Action‑Selection‑Logik
---
🎉 Abschluss
Wenn du diese Aufgabe gelöst hast, hast du:
• ein vollständiges RL‑System gebaut
• saubere Architekturprinzipien angewendet
• Q‑Learning praktisch verstanden
