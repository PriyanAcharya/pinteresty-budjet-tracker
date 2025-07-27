from categories import CATEGORIES

def auto_category(item):
    item = item.lower()
    for cat, keywords in CATEGORIES.items():
        if any(word in item for word in keywords):
            return cat
    return "Uncategorized"

def should_treat_or_chill(total_spent):
    if total_spent < 500:
        return "✨ You can treat yourself!"
    elif total_spent < 1000:
        return "🧘 Chill out, maybe save a little."
    else:
        return "🚨 Girl, chill TF out!"
