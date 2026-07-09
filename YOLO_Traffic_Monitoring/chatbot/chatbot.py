knowledge = {
    "red signal": "🚦 Stop your vehicle immediately.",
    "yellow signal": "🟡 Slow down and prepare to stop.",
    "green signal": "🟢 You may proceed if the road is clear.",
    "speed limit": "🚗 Always obey the speed limit displayed on road signs.",
    "helmet": "🪖 Wearing a helmet is compulsory for two-wheeler riders.",
    "seat belt": "🔒 Seat belts are mandatory for drivers and passengers.",
    "no parking": "🚫 Parking is prohibited in the marked area.",
    "school zone": "🏫 Drive slowly and watch for children crossing.",
    "zebra crossing": "🚶 Give priority to pedestrians at zebra crossings.",
    "u-turn": "↩️ Take a U-turn only where it is permitted."
}

def get_answer(question):
    question = question.lower()

    for key in knowledge:
        if key in question:
            return knowledge[key]

    return "❌ Sorry, I don't know the answer. Please ask about traffic rules or road signs."