
import json
import random

# Определение URL изображений для каждой редкости
image_urls = {
    "Common": "https://github.com/loonynvi/Lmaooff/blob/main/common.png",
    "Uncommon": "https://github.com/loonynvi/Lmaooff/blob/main/uncommon.png",
    "Rare": "https://github.com/loonynvi/Lmaooff/blob/main/rare.png",
    "Epic": "https://github.com/loonynvi/Lmaooff/blob/main/epic.png",
    "Legendary": "https://github.com/loonynvi/Lmaooff/blob/main/legendary.png"
}

# Создание списка rarities, где каждый элемент — это кортеж (редкость, URL)
rarities = (
    [("Common", image_urls["Common"])] * 250 +
    [("Uncommon", image_urls["Uncommon"])] * 150 +
    [("Rare", image_urls["Rare"])] * 50 +
    [("Epic", image_urls["Epic"])] * 30 +
    [("Legendary", image_urls["Legendary"])] * 20
)

# Убедимся, что каждый элемент в списке — это кортеж
rarities_flat = []
for rarity, url in rarities:
    rarities_flat.append((rarity, url))

# Перемешивание списка для рандомизации
random.shuffle(rarities_flat)

# Вывод первых 10 элементов для проверки
print("Sample rarities:", rarities_flat[:10])

# Основные данные для NFT
nft_base = {
    "description": "Explore unique digital assets each with its own story and rarity."
}

# Количество NFTs
nft_count = 500

# Генерация JSON файлов
for i in range(nft_count):
    rarity, image_url = rarities_flat[i]
    nft = nft_base.copy()
    nft['name'] = f"Treasury Chest #{i+1}"
    nft['image'] = image_url
    nft['attributes'] = [
        {"trait_type": "Rarity", "value": rarity}
    ]

    # Сохранение JSON файла
    with open(f'{i}.json', 'w') as f:
        json.dump(nft, f, indent=4)


