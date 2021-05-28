"""Hiragana g2p rules."""

from pynini import accep, union, cdrewrite, cross, string_map
from pynini.lib import rewrite

monographs = union("あ","い","う","え","お",
				   "か","き","く","け","こ",
				   "が","ぎ","ぐ","げ","ご",
				   "さ","し","す","せ","そ",
				   "ざ","じ","ず","ぜ","ぞ",
				   "た","ち","つ","て","と",
				   "だ","ぢ",     "で","ど",
				   "な","に","ぬ","ね","の",
				   "は","ひ","ふ","へ","ほ",
				   "ば","び","ぶ","べ","ぼ",
				   "ぱ","ぴ","ぷ","ぺ","ぽ",
				   "ま","み","む","め","も",
				   "や",     "ゆ",     "よ",
				   "ら","り","る","れ","ろ",
				   "わ",               "を",
				   "ん")

sokuon = accep("っ")

yoon = union("ゃ", "ゅ", "ょ")

graphemes = union(monographs, sokuon, yoon).optimize()

voiced_consonants = union("b","d","ɡ","g",
						  "m","n","ɲ","ŋ",
						  "ɴ","p","ɾ","j",
						  "ɰ","ɰ̃","z","ʑ",
						  "ʲ","t")

voiceless_consonants = union("ç","ɕ","ɸ","h","k","t","s")

glottal_stop = accep("ʔ")

consonants = union(voiceless_consonants, voiced_consonants, glottal_stop)

vowels = union("a","ɑ","i","i̥","ɯ","ɯ̥","e","ẽ","o")

suprasegmentals = accep("ː")

phonemes = union(consonants, vowels, suprasegmentals)

SIGMA_STAR = union(graphemes, phonemes).closure().optimize()


digraph_map = [
	("きゃ", "kʲa"),
	("きゅ", "kʲɯ"),
	("きょ", "kʲo"),
	
	("しゃ", "ɕa"),
	("しゅ", "ɕɯ"),
	("しょ", "ɕo"),

	("ちゃ", "tɕa"),
	("ちゅ", "tɕɯ"),
	("ちょ", "tɕo"),

	("にゃ", "ŋa"),
	("にゅ", "ŋɯ"),
	("にょ", "ŋo"),

	("ひゃ", "ça"),
	("ひゅ", "çɯ"),
	("ひょ", "ço"),

	("みゃ", "mʲa"),
	("みゅ", "mʲɯ"),
	("みょ", "mʲo"),

	("りゃ", "ɾʲa"),
	("りゅ", "ɾʲɯ"),
	("りょ", "ɾʲo"),

	("ぎゃ", "ɡʲa"),
	("ぎゅ", "ɡʲɯ"),
	("ぎょ", "ɡʲo"),

	("じゃ", "ʑa"),
	("じゅ", "ʑɯ"),
	("じょ", "ʑo"),

	("びゃ", "bʲa"),
	("びゅ", "bʲɯ"),
	("びょ", "bʲo"),

	("ぴゃ", "pʲa"),
	("ぴゅ", "pʲɯ"),
	("ぴょ", "pʲo"),
]

foo_map = [
	("ɯう","ɯː"),
]

context_free_map = [
	("あ", "ɑ"),
	("い", "i"),
	("う", "ɯ"),
	("え", "e"),
	("お", "o"),

	("か", "kɑ"),
	("き", "ki"),
	("く", "kɯ"),
	("け", "ke"),
	("こ", "ko"),

	("が", "gɑ"),
	("ぎ", "gi"),
	("ぐ", "gɯ"),
	("げ", "ge"),
	("ご", "go"),

	("さ", "sɑ"),
	("し", "ɕi"),
	("す", "sɯ"),
	("せ", "se"),
	("そ", "so"),

	("ざ", "zɑ"),
	("じ", "ʑi"),
	("ず", "zɯ"),
	("ぜ", "ze"),
	("ぞ", "zo"),

	("た", "tɑ"),
	("ち", "tɕi"),
	("つ", "tsɯ"),
	("て", "te"),
	("と", "to"),

	("だ", "dɑ"),
	("で", "de"),
	("ど", "do"),

	("な", "nɑ"),
	("に", "ɲi"),
	("ぬ", "nɯ"),
	("ね", "ne"),
	("の", "no"),

	("は", "hɑ"),
	("ひ", "çi"),
	("ふ", "ɸɯ"),
	("へ", "he"),
	("ほ", "ho"),

	("ば", "ba"),
	("び", "bi"),
	("ぶ", "bɯ"),
	("べ", "be"),
	("ぼ", "bo"),

	("ぱ", "pɑ"),
	("ぴ", "pi"),
	("ぷ", "pɯ"),
	("ぺ", "pe"),
	("ぽ", "po"),

	("ま", "mɑ"),
	("み", "mi"),
	("む", "mɯ"),
	("め", "me"),
	("も", "mo"),

	("や", "jɑ"),
	("ゆ", "jɯ"),
	("よ", "jo"),

	("ら", "ɾɑ"),
	("り", "ɾi"),
	("る", "ɾɯ"),
	("れ", "ɾe"),
	("ろ", "ɾo"),

	("わ", "ɰɑ"),
]

long_vowel_map = [
	("おお", "oː"),
	("おう", "oː"),
	("こう", "koː"),
	("ごう", "goː"),
	("そう", "soː"),
	("ぞう", "zoː"),
	("とう", "toː"),
	("どう", "doː"),
	("のう", "noː"),
	("ほう", "hoː"),
	("ぼう", "boː"),
	("ぽう", "poː"),
	("もう", "moː"),
	("ぽう", "poː"),
	("よう", "yoː"),
	("ろう", "ɾoː"),

	("えい", "eː"),
	("けい", "keː"),
	("げい", "geː"),
	("せい", "seː"),
	("ぜい", "zeː"),
	("てい", "teː"),
	("でい", "deː"),
	("ねい", "neː"),
	("へい", "heː"),
	("べい", "beː"),
	("ぺい", "peː"),
	("れい", "reː"),

	("ええ", "eː"),
	("けえ", "keː"),
	("げえ", "geː"),
	("せえ", "seː"),
	("ぜえ", "zeː"),
	("てえ", "teː"),
	("でえ", "deː"),
	("ねえ", "neː"),
	("へえ", "heː"),
	("べえ", "beː"),
	("ぺえ", "peː"),
	("れえ", "reː"),

	("いい", "iː"),
	("きい", "kiː"),
	("ぎい", "giː"),
	("しい", "siː"),
	("じい", "ziː"),
	("にい", "niː"),
	("ひい", "hiː"),
	("びい", "biː"),
	("ぴい", "piː"),
	("りい", "riː"),
	
	("oɯ", "oː"),
]

devoicing_map = [
	("i", "i̥"),
	("ɯ", "ɯ̥"),
]

nasalization_map = [
	("e", "ẽ")
]

gemination_map = [
	("s", "ss"),
	("k", "kk"),
	("t", "tt"),
]

bos_map = [
	("じゃ", "dʑɑ"),
	("じゅ", "dʑɯ"),
	("じょ", "dʑo"),
	("ざ", "dzɑ"),
	("じ", "dʑi"),
	("ず", "dzɯ"),
	("ぜ", "dze"),
	("ぞ", "dzo"),
]
	
G2P = (
    cdrewrite(cross("は", "ɰɑ"), "[BOS]", "[EOS]", SIGMA_STAR)
    @ cdrewrite(string_map(bos_map), "[BOS]", "", SIGMA_STAR)
    @ cdrewrite(cross("ん", "ɴ"), "", "[EOS]", SIGMA_STAR)
	@ cdrewrite(cross("ん", "n"), "", "", SIGMA_STAR)
	@ cdrewrite(string_map(digraph_map), "", "", SIGMA_STAR)
	@ cdrewrite(cross("う","ː"), "ɯ", "", SIGMA_STAR)
	@ cdrewrite(string_map(long_vowel_map), "", "", SIGMA_STAR)
	@ cdrewrite(string_map(context_free_map), "", "", SIGMA_STAR)
	@ cdrewrite(
		string_map(nasalization_map), 
		"",
		"ɴ",
		SIGMA_STAR
	)
	@ cdrewrite(
		string_map(devoicing_map),
		union(voiceless_consonants),
		union(voiceless_consonants, "[EOS]"),
		SIGMA_STAR
	)
	@ cdrewrite(
		string_map(gemination_map),
		sokuon,
		"",
		SIGMA_STAR
	)
	@ cdrewrite(cross(sokuon, ""), "", "", SIGMA_STAR)
	@ cdrewrite(
		cross("g", "ŋ"),
		union(vowels, suprasegmentals),
		vowels,
		SIGMA_STAR)
).optimize()


def g2p(istring: str) -> str:
    """Applies the G2P rule.

    Args:
      istring: the graphemic input string.

    Returns:
      The phonemic output string.

    Raises.
      rewrite.Error: composition failure.
    """
    return rewrite.one_top_rewrite(istring, G2P)
