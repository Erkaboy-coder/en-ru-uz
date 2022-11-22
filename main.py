from connections import *
from googletrans import Translator
# from langs import TranslateLangs
translator = Translator()


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
	await message.reply("🔎 Qidiriladigan so'zni yoki gapni kiriting! Ingliz, o'zbek  yoki rus tillarida!")

@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
	await message.reply("👨‍💻 Bu bot test rejimida muhandis dasturchi erkaboy tamonidan yaratilidi.")

@dp.message_handler()
async def tarjimon(message: types.Message):
	lang = translator.detect(message.text).lang
	results = {}
	means = []

	new_text = message.text

	if lang == 'uz':
		ru = translator.translate(new_text, 'ru').text
		means.append('🇸🇮 ' + ru)

		en = translator.translate(new_text, 'en').text
		means.append('🏴󠁧󠁢󠁥󠁮󠁧󠁿 ' + en)

	elif lang == 'ru':
		uz = translator.translate(new_text, 'uz').text
		means.append('🇺🇿 ' + uz)

		en = translator.translate(new_text, 'en').text
		means.append('🏴󠁧󠁢󠁥󠁮󠁧󠁿 ' + en)

	elif lang == 'en':
		uz = translator.translate(new_text, 'uz').text
		means.append('🇺🇿 ' + uz)

		ru = translator.translate(new_text, 'ru').text
		means.append('🇸🇮 ' + ru)
	else:
		means.append('⛔️ Kechirasiz siz tizimda mavjud bo\'lmagan tildagi so\'zni kiritdingiz !')


	results['words'] = "\n".join(means)
	await message.reply(results['words'])



if __name__ == '__main__':
	executor.start_polling(dp, skip_updates=True)