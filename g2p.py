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

voiced_consonants = union("b","d","ɡ","j",
						  "m","n","ɲ","ŋ",
						  "ɴ","p","ɾ","s",
						  "ɰ","ɰ̃","z","ʑ",
						  "ʲ","t")
voiceless_consonants = union("ç","ɕ","ɸ","h","k","t")
glottal_stop = accep("ʔ")
consonants = union(voiceless_consonants, voiced_consonants, glottal_stop)

vowels = union("ɑ","i","i̥","ɯ","ɯ̥","e","ẽ","o")

suprasegmentals = accep("ː")

'''
monograph_phonemes = union("a",	"i", "ɯ", "e", "o",
				   		   "k", "s", "ɕ", "t", "n",
						   "ɲ", "h", "ç", "ɸ", "m",
				   		   "j", "ɾ", "ɰ", "ɴ", "ŋ",
						   "ɰ̃", "g", "ɡ", "p", "b",
						   "z", "ʑ", "d", "ʲ", "ː",
						   "ɑ", "ɯ̥")
'''
phonemes = union(consonants, vowels, suprasegmentals)

SIGMA_STAR = union(graphemes, phonemes).closure().optimize()

G2P = (
    cdrewrite(cross("は", "ɰɑ"), "[BOS]", "[EOS]", SIGMA_STAR)
    @ cdrewrite(cross("きゃ", "kʲɑ"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("きゃ", "kʲu"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("きゃ", "kʲo"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("ぎゃ", "ɡʲɑ"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("ぎゅ", "ɡʲu"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("ぎょ", "ɡʲo"), "", "", SIGMA_STAR)
	@ cdrewrite(cross("しゃ", "ɕɑ"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("しゅ", "ɕɯ"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("しょ", "ɕo"), "", "", SIGMA_STAR)
	@ cdrewrite(cross("じゃ", "dʑɑ"), "[BOS]", "", SIGMA_STAR)
    @ cdrewrite(cross("じゅ", "dʑɯ"), "[BOS]", "", SIGMA_STAR)
    @ cdrewrite(cross("じょ", "dʑo"), "[BOS]", "", SIGMA_STAR)
	@ cdrewrite(cross("じゃ", "ʑɑ"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("じゅ", "ʑɯ"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("じょ", "ʑo"), "", "", SIGMA_STAR)
	@ cdrewrite(cross("ちゃ", "tɕɑ"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("ちゅ", "tɕɯ"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("ちょ", "tɕo"), "", "", SIGMA_STAR)
	@ cdrewrite(cross("にゃ", "ɲɑ"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("にゅ", "ɲɯ"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("にょ", "ɲo"), "", "", SIGMA_STAR)
	@ cdrewrite(cross("ひゃ", "çɑ"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("ひゅ", "çɯ"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("ひょ", "ço"), "", "", SIGMA_STAR)
	@ cdrewrite(cross("みゃ", "mʲɑ"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("みゅ", "mʲɯ"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("みょ", "mʲo"), "", "", SIGMA_STAR)
	@ cdrewrite(cross("りゃ", "ɾʲɑ"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("りゅ", "ɾʲɯ"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("りょ", "ɾʲo"), "", "", SIGMA_STAR)
	@ cdrewrite(cross("びゃ", "bʲɑ"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("びゅ", "bʲɯ"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("びょ", "bʲo"), "", "", SIGMA_STAR)
	@ cdrewrite(cross("ぴゃ", "pʲɑ"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("ぴゅ", "pʲɯ"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("びょ", "pʲo"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("ん", "ɴ"), "", "[EOS]", SIGMA_STAR)
    @ cdrewrite(cross("ん", "n"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("ざ", "dzɑ"), "[BOS]", "", SIGMA_STAR)
    @ cdrewrite(cross("じ", "dʑi"), "[BOS]", "", SIGMA_STAR)
    @ cdrewrite(cross("ず", "dzɯ"), "[BOS]", "", SIGMA_STAR)
    @ cdrewrite(cross("ぜ", "dze"), "[BOS]", "", SIGMA_STAR)
    @ cdrewrite(cross("ぞ", "dzo"), "[BOS]", "", SIGMA_STAR)
	@ cdrewrite(cross("か", "kɑ"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("き", "ki"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("く", "kɯ"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("け", "ke"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("こ", "ko"), "", "", SIGMA_STAR)
	@ cdrewrite(cross("が", "gɑ"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("ぎ", "gi"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("ぐ", "gɯ"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("げ", "ge"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("ご", "go"), "", "", SIGMA_STAR)
	@ cdrewrite(cross("さ", "sɑ"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("し", "ɕi"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("す", "sɯ"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("せ", "se"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("そ", "so"), "", "", SIGMA_STAR)
	@ cdrewrite(cross("ざ", "zɑ"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("じ", "ʑi"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("ず", "zɯ"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("ぜ", "ze"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("ぞ", "zo"), "", "", SIGMA_STAR)
	@ cdrewrite(cross("た", "tɑ"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("ち", "tɕi"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("つ", "tsɯ"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("て", "te"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("と", "to"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("な", "nɑ"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("に", "ɲi"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("ぬ", "nɯ"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("ね", "ne"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("の", "no"), "", "", SIGMA_STAR)
	@ cdrewrite(cross("は", "hɑ"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("ひ", "çi"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("ふ", "ɸɯ"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("へ", "he"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("ほ", "ho"), "", "", SIGMA_STAR)
	@ cdrewrite(cross("ま", "mɑ"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("み", "mi"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("む", "mɯ"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("め", "me"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("も", "mo"), "", "", SIGMA_STAR)
	@ cdrewrite(cross("や", "jɑ"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("ゆ", "jɯ"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("よ", "jo"), "", "", SIGMA_STAR)
	@ cdrewrite(cross("ら", "ɾɑ"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("り", "ɾi"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("る", "ɾɯ"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("れ", "ɾe"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("ろ", "ɾo"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("わ", "ɰɑ"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("を", "o"), "", "", SIGMA_STAR)
	@ cdrewrite(cross("あ", "ː"), union("あ","a"), "", SIGMA_STAR)
    @ cdrewrite(cross("い", "ː"), union("い","i"), "", SIGMA_STAR)
    @ cdrewrite(cross("う", "ː"), union("う","ɯ"), "", SIGMA_STAR)
    @ cdrewrite(cross("え", "ː"), union("え","e"), "", SIGMA_STAR)
    @ cdrewrite(cross("お", "ː"), union("お","o"), "", SIGMA_STAR)
	@ cdrewrite(cross("あ", "ɑ"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("い", "i"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("う", "ɯ"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("え", "e"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("お", "o"), "", "", SIGMA_STAR)
)


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
