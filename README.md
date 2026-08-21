# HA Brand Icons

Набор иконок (brand images) для кастомных интеграций Home Assistant, у которых нет иконок в [официальном brands-репозитории](https://github.com/home-assistant/brands).

Иконки сгенерированы программно (Python + Pillow), формат — как требует HA для локальных brand-изображений (HA 2026.3+): каталог `brand/` внутри интеграции с `icon.png` (1024×1024) и `icon@2x.png` (2048×2048).

## Состав

| Интеграция | Домен | Иконка |
|---|---|---|
| Время света | `time_of_light` | 🕐 часы с лучами (янтарная) |
| Свет по движению | `off_light` | 💡 лампочка + волны движения (синяя) |
| Управление рамкой | `frame_control` | 🖼️ планшет/рамка с пейзажем (фиолетовая) |
| Programmable Thermostat | `programmable_thermostat` | 🌡️ термометр + расписание (оранжевая) |
| SmartLife | `smartlife` | 🔌 розетка на синей плашке |
| YandexDiskBackup | `yabackup` | ☁️ облако с загрузкой (красная, Яндекс) |

## Установка

Для каждой интеграции скопируйте каталог `icons/<domain>/` в `custom_components/<domain>/brand/`:

```bash
# пример для time_of_light
mkdir -p custom_components/time_of_light/brand
cp icons/time_of_light/icon.png icons/time_of_light/icon@2x.png custom_components/time_of_light/brand/
```

Затем перезапустите Home Assistant. Иконка появится в «Устройства и службы» и в диалоге добавления интеграции.

> Требуется Home Assistant Core 2026.3+ (поддержка локальных brand-изображений). На более старых версиях интеграции показывают иконку из brands-репозитория или стандартную заглушку.

## Генерация

Скрипт `scripts/generate_icons.py` создаёт все иконки из SVG-описаний на Python/Pillow:

```bash
pip install pillow
python3 scripts/generate_icons.py
```

## Лицензия

MIT
