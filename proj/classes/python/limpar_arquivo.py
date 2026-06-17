import unicodedata

def _remove_format_chars(s):
	return ''.join(ch for ch in s if unicodedata.category(ch) != 'Cf')

def limpar_arquivo(origem, destino):
	entrada = open(origem, "r", encoding="utf-8")
	saida = open(destino, "w", encoding="utf-8")
	for line in entrada:
		cleaned = _remove_format_chars(line)
		if cleaned.strip() != '':
			saida.write(cleaned)
				