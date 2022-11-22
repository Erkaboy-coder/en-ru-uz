from googletrans import Translator
translator = Translator()
results = {}
means = []
class TranslateLangs(word):
    def lang_uz(word):
        uz = translator.translate(word, 'uz').text
        means.append('🇺🇿 ' + uz + '\n')

    def lang_ru(word):
        ru = translator.translate(word, 'ru').text
        means.append('🇸🇮 ' + ru + '\n')

    def lang_en(word):
        en = translator.translate(word, 'en').text
        means.append('🏴󠁧󠁢󠁥󠁮󠁧󠁿 ' + en + '\n')