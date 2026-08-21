import random
chaos_factor = 5
categorias = [
    "Acción remota de PNJ",
    "Acción ambigua",
    "PNJ actúa contra el PJ",
    "PNJ actúa a favor del PJ",
    "Avance de una trama actual",
    "Trama inesperada",
    "PNJ se aleja",
    "PNJ negativo",
    "PNJ positivo",
    "Nueva trama",
    "PNJ atrapado/comprometido",
    "Cambio de ubicación actual",
    "Se acerca algo importante",
    "El escenario cambia",
    "Introducir nuevo PNJ",
    "Cambio de trama",
    "Cierre de trama",
    "Refuerzo positivo",
    "Refuerzo negativo",
    "Giro totalmente inesperado",
]
action_1 = [
    "Abandon", "Accompany", "Activate", "Agree", "Ambush",
    "Arrive", "Assist", "Attack", "Attain", "Bargain",
    "Befriend", "Bestow", "Betray", "Block", "Break",
    "Carry", "Celebrate", "Change", "Close", "Combine",
    "Communicate", "Conceal", "Continue", "Control", "Create",
    "Deceive", "Decrease", "Defend", "Delay", "Deny",
    "Depart", "Deposit", "Destroy", "Dispute", "Disrupt",
    "Distrust", "Divide", "Drop", "Easy", "Energize",
    "Escape", "Expose", "Fail", "Fight", "Flee",
    "Free", "Guide", "Harm", "Heal", "Hinder",
    "Imitate", "Imprison", "Increase", "Indulge", "Inform",
    "Inquire", "Inspect", "Invade", "Leave", "Lure",
    "Misuse", "Move", "Neglect", "Observe", "Open",
    "Oppose", "Overthrow", "Praise", "Proceed", "Protect",
    "Punish", "Pursue", "Recruit", "Refuse", "Release",
    "Relinquish", "Repair", "Repulse", "Return", "Reward",
    "Ruin", "Separate", "Start", "Stop", "Strange",
    "Struggle", "Succeed", "Support", "Suppress", "Take",
    "Threaten", "Transform", "Trap", "Travel", "Triumph",
    "Truce", "Trust", "Use", "Usurp", "Waste"
]

action_2 = [
    "Advantage", "Adversity", "Agreement", "Animal", "Attention",
    "Balance", "Battle", "Benefits", "Building", "Burden",
    "Bureaucracy", "Business", "Chaos", "Comfort", "Completion",
    "Conflict", "Cooperation", "Danger", "Defense", "Depletion",
    "Disadvantage", "Distraction", "Elements", "Emotion", "Enemy",
    "Energy", "Environment", "Expectation", "Exterior", "Extravagance",
    "Failure", "Fame", "Fear", "Freedom", "Friend",
    "Goal", "Group", "Health", "Hindrance", "Home",
    "Hope", "Idea", "Illness", "Illusion", "Individual",
    "Information", "Innocent", "Intellect", "Interior", "Investment",
    "Leadership", "Legal", "Location", "Military", "Misfortune",
    "Mundane", "Nature", "Needs", "News", "Normal",
    "Object", "Obscurity", "Official", "Opposition", "Outside",
    "Pain", "Path", "Peace", "People", "Personal",
    "Physical", "Plot", "Portal", "Possessions", "Poverty",
    "Power", "Prison", "Project", "Protection", "Reassurance",
    "Representative", "Riches", "Safety", "Strength", "Success",
    "Suffering", "Surprise", "Tactic", "Technology", "Tension",
    "Time", "Trial", "Value", "Vehicle", "Victory",
    "Vulnerability", "Weapon", "Weather", "Work", "Wound"
]
descriptor_1 = [
    "Adventurously", "Aggressively", "Anxiously", "Awkwardly", "Beautifully",
    "Bleakly", "Boldly", "Bravely", "Busily", "Calmly",
    "Carefully", "Carelessly", "Cautiously", "Ceaselessly", "Cheerfully",
    "Combatively", "Coolly", "Crazily", "Curiously", "Dangerously",
    "Defiantly", "Deliberately", "Delicately", "Delightfully", "Dimly",
    "Efficiently", "Emotionally", "Energetically", "Enormously", "Enthusiastically",
    "Excitedly", "Fearfully", "Ferociously", "Fiercely", "Foolishly",
    "Fortunately", "Frantically", "Freely", "Frighteningly", "Fully",
    "Generously", "Gently", "Gladly", "Gracefully", "Gratefully",
    "Happily", "Hastily", "Healthily", "Helpfully", "Helplessly",
    "Hopelessly", "Innocently", "Intensely", "Interestingly", "Irritatingly",
    "Joyfully", "Kindly", "Lazily", "Lightly", "Loosely",
    "Loudly", "Lovingly", "Loyally", "Majestically", "Meaningfully",
    "Mechanically", "Mildly", "Miserably", "Mockingly", "Mysteriously",
    "Naturally", "Neatly", "Nicely", "Oddly", "Offensively",
    "Officially", "Partially", "Passively", "Peacefully", "Perfectly",
    "Playfully", "Politely", "Positively", "Powerfully", "Quaintly",
    "Quarrelsomely", "Quietly", "Roughly", "Rudely", "Ruthlessly",
    "Slowly", "Softly", "Strangely", "Swiftly", "Threateningly",
    "Timidly", "Very", "Violently", "Wildly", "Yieldingly"
]

descriptor_2 = [
    "Abnormal", "Amusing", "Artificial", "Average", "Beautiful",
    "Bizarre", "Boring", "Bright", "Broken", "Clean",
    "Cold", "Colorful", "Colorless", "Comforting", "Creepy",
    "Cute", "Damaged", "Dark", "Defeated", "Dirty",
    "Disagreeable", "Dry", "Dull", "Empty", "Enormous",
    "Extraordinary", "Extravagant", "Faded", "Familiar", "Fancy",
    "Feeble", "Festive", "Flawless", "Forlorn", "Fragile",
    "Fragrant", "Fresh", "Full", "Glorious", "Graceful",
    "Hard", "Harsh", "Healthy", "Heavy", "Historical",
    "Horrible", "Important", "Interesting", "Juvenile", "Lacking",
    "Large", "Lavish", "Lean", "Less", "Lethal",
    "Lively", "Lonely", "Lovely", "Magnificent", "Mature",
    "Messy", "Mighty", "Military", "Modern", "Mundane",
    "Mysterious", "Natural", "Normal", "Odd", "Old",
    "Pale", "Peaceful", "Petite", "Plain", "Poor",
    "Powerful", "Protective", "Quaint", "Rare", "Reassuring",
    "Remarkable", "Rotten", "Rough", "Ruined", "Rustic",
    "Scary", "Shocking", "Simple", "Small", "Smooth",
    "Soft", "Strong", "Stylish", "Unpleasant", "Valuable",
    "Vibrant", "Warm", "Watery", "Weak", "Young"
]
locations = [
    "Abandoned", "Active", "Artistic", "Atmosphere", "Beautiful",
    "Bleak", "Bright", "Business", "Calm", "Charming",
    "Clean", "Cluttered", "Cold", "Colorful", "Colorless",
    "Confusing", "Cramped", "Creepy", "Crude", "Cute",
    "Damaged", "Dangerous", "Dark", "Delightful", "Dirty",
    "Domestic", "Empty", "Enclosed", "Enormous", "Entrance",
    "Exclusive", "Exposed", "Extravagant", "Familiar", "Fancy",
    "Festive", "Foreboding", "Fortunate", "Fragrant", "Frantic",
    "Frightening", "Full", "Harmful", "Helpful", "Horrible",
    "Important", "Impressive", "Inactive", "Intense", "Intriguing",
    "Lively", "Lonely", "Long", "Loud", "Meaningful",
    "Messy", "Mobile", "Modern", "Mundane", "Mysterious",
    "Natural", "New", "Occupied", "Odd", "Official",
    "Old", "Open", "Peaceful", "Personal", "Plain",
    "Portal", "Protected", "Protection", "Powerful", "Quiet",
    "Reassuring", "Remote", "Resourceful", "Ruined", "Rustic",
    "Safe", "Services", "Simple", "Small", "Spacious",
    "Storage", "Strange", "Stylish", "Suspicious", "Tall",
    "Threatening", "Tranquil", "Unexpected", "Unpleasant", "Unusual",
    "Useful", "Warm", "Warning", "Watery", "Welcoming"
]

characters = [
    "Accompanied", "Active", "Aggressive", "Ambush", "Animal",
    "Anxious", "Armed", "Beautiful", "Bold", "Busy",
    "Calm", "Careless", "Casual", "Cautious", "Classy",
    "Colorful", "Combative", "Crazy", "Creepy", "Curious",
    "Dangerous", "Deceitful", "Delightful", "Defeated", "Delightful",
    "Emotional", "Energetic", "Equipped", "Excited", "Expected",
    "Familiar", "Fast", "Feeble", "Feminine", "Ferocious",
    "Foe", "Foolish", "Fortunate", "Fragrant", "Frantic",
    "Friend", "Frightened", "Frightening", "Generous", "Glad",
    "Happy", "Harmful", "Helpful", "Helpless", "Hurt",
    "Important", "Inactive", "Influential", "Innocent", "Intense",
    "Knowledgeable", "Large", "Lonely", "Loud", "Loyal",
    "Masculine", "Mighty", "Miserable", "Miserable", "Multiple",
    "Mundane", "Mysterious", "Natural", "Odd", "Official",
    "Old", "Passive", "Peaceful", "Playful", "Powerful",
    "Professional", "Protected", "Protecting", "Questioning", "Quiet",
    "Reassuring", "Resourceful", "Seeking", "Skilled", "Slow",
    "Small", "Stealthy", "Strange", "Strong", "Tall",
    "Thieving", "Threatening", "Triumphant", "Unexpected", "Unnatural",
    "Unusual", "Violent", "Vocal", "Weak", "Wild", "Young"
]

objects = [
    "Active", "Artistic", "Average", "Beautiful", "Bizarre",
    "Bright", "Cloth", "Clue", "Cold", "Colorful",
    "Communication", "Construction", "Confusing", "Consumable", "Container",
    "Creepy", "Crude", "Cute", "Damaged", "Dangerous",
    "Dark", "Deliberate", "Delightful", "Desired", "Domestic",
    "Empty", "Energy", "Enormous", "Equipment", "Expected",
    "Expanded", "Extravagant", "Faded", "Familiar", "Fancy",
    "Flora", "Fortunate", "Fragile", "Fragrant", "Frightening",
    "Garbage", "Guidance", "Hard", "Harmful", "Healing",
    "Heavy", "Helpful", "Horrible", "Important", "Inactive",
    "Information", "Intriguing", "Large", "Lethal", "Light",
    "Liquid", "Loud", "Majestic", "Meaningful", "Mechanical",
    "Modern", "Moving", "Multiple", "Mundane", "Mysterious",
    "Natural", "New", "Odd", "Official", "Old",
    "Ornamental", "Ornamental", "Personal", "Powerful", "Priced",
    "Protection", "Rare", "Ready", "Reassuring", "Resource",
    "Ruined", "Small", "Soft", "Solitary", "Stolen",
    "Strange", "Stylish", "Threatening", "Tool", "Travel",
    "Unexpected", "Unpleasant", "Unusual", "Useful", "Useless",
    "Valuable", "Warm", "Weapon", "Wet", "Worn"
]
listas_elementos = {
    "1": action_1,
    "2": action_2,
    "3": descriptor_1,
    "4": descriptor_2,
    "5": locations,
    "6": characters,
    "7": objects,
}
fate_chart = {
    "Imposible":       {1: 1,  2: 2,  3: 3,  4: 4,  5: 5,  6: 6,  7: 7,  8: 8,  9: 9},
    "Casi imposible":  {1: 5,  2: 7,  3: 10, 4: 13, 5: 15, 6: 18, 7: 21, 8: 24, 9: 28},
    "Muy improbable":  {1: 10, 2: 14, 3: 18, 4: 21, 5: 25, 6: 29, 7: 33, 8: 38, 9: 42},
    "Improbable":      {1: 15, 2: 20, 3: 27, 4: 31, 5: 35, 6: 39, 7: 44, 8: 50, 9: 55},
    "50/50":           {1: 15, 2: 25, 3: 35, 4: 42, 5: 50, 6: 58, 7: 65, 8: 75, 9: 85},
    "Probable":        {1: 45, 2: 50, 3: 56, 4: 61, 5: 65, 6: 69, 7: 73, 8: 80, 9: 85},
    "Muy probable":    {1: 58, 2: 62, 3: 67, 4: 71, 5: 75, 6: 79, 7: 82, 8: 86, 9: 90},
    "Casi seguro":     {1: 72, 2: 76, 3: 80, 4: 85, 5: 90, 6: 92, 7: 94, 8: 96, 9: 98},
    "Seguro":          {1: 91, 2: 92, 3: 93, 4: 94, 5: 95, 6: 96, 7: 97, 8: 98, 9: 99}
}
def oraculo():
        print(f"""
    ===Oraculo===\n
    ===Chaos Factor: {chaos_factor} ===\n
    1. Imposible\n
    2. Casi Imposible\n
    3. Muy Improbable\n
    4. Improbable\n
    5. 50/50\n
    6. Probable\n
    7. Muy Probable\n
    8. Casi Seguro\n
    9. Seguro""")
        respuesta  = input()
        niveles = ["Imposible", "Casi imposible", "Muy improbable", "Improbable", "50/50", "Probable", "Muy probable", "Casi seguro", "Seguro"]
        nivel = niveles[int(respuesta) - 1]
        
        umbral = fate_chart[nivel][chaos_factor]
        numero = random.randint(1, 100)
        print(f"""
            Numero: {numero}\n
            Umbral:{umbral}""")
        if numero <= umbral and numero in range(11,100,11):
            print("Si excepcional")
            if (numero // 10) <= chaos_factor:
                evento_aleatorio()
            return
        elif numero > umbral and numero in range(11,100,11):
            print("No excepcional")
            if (numero // 10) <= chaos_factor:
                evento_aleatorio()
            return
        elif numero <= umbral:
            print("Si")
            return
        else:
            print("No")
            return
        

def evento_aleatorio():
        numero = random.randint(1,100)
        evento = (numero - 1) // 5
        print(numero)
        print(categorias[evento])
        print("""Elige 1 o 2 listas separado por espacios:\n
        1: action_1,\n
        2: action_2,\n
        3: descriptor_1,\n
        4: descriptor_2,\n
        5: locations,\n
        6: characters,\n
        7: objects,  \n
        """)
        respuesta = input()
        partes = respuesta.split()
        numero1 = random.randint(1,100)
        try:
            if len(partes) == 2:
                numero2 = random.randint(1, 100)
                lista1 = listas_elementos[partes[0]]
                lista2 = listas_elementos[partes[1]]
                palabra1 = lista1[numero1 - 1]
                palabra2 = lista2[numero2 - 1]
                print(palabra1)
                print(palabra2)
            elif len(partes) == 1:
                lista = listas_elementos[partes[0]]
                palabra1 = lista[numero1 - 1]
                print(palabra1)
        except KeyError:
            print("Elige una lista de 1 al 7")
        return
def main():
  while True:
    print(f"""===Chaos Factor: {chaos_factor} ===\n
    1. Preguntar al Oraculo\n
    2. Generar Evento Aleatorio\n
    3. Salir""")
    respuesta = input()
    if respuesta == "3":
        return exit()
    if respuesta == "1":
         print(oraculo())
    if respuesta == "2":
        print(evento_aleatorio())

main()
#"Este proyecto usa contenido de Mythic Game Master Emulator Second Edition, de Tana Pigeon, publicado por Word Mill Games, y licenciado bajo Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0). Más información en www.wordmillgames.com."
