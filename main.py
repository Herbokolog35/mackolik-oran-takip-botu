from mackolik_scraper import get_mackolik_data
from telegram_bot import send_message

def filtrele_ve_gonder():
    maçlar = get_mackolik_data()
    if not maçlar:
        return
    lines = []
    for m in maçlar:
        oran = m["İY1.5"] * m["MS2.5"]
        prefix = "🔥 +6 Oran" if oran >= 6 else ""
        lines.append(f"{prefix}\n{m['maç']}\nİY1.5: {m['İY1.5']} | MS2.5: {m['MS2.5']} | Toplam: {round(oran,2)}")
    text = "📊 Güncel İddaa Analizi:\n\n" + "\n\n".join(lines)
    send_message(text)

if __name__ == "__main__":
    filtrele_ve_gonder()
