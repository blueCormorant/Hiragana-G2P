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

phonemes = union(consonants, vowels, suprasegmentals)

SIGMA_STAR = union(graphemes, phonemes).closure().optimize()

context_free_map = [
	("か", "kɑ"),
	("き", "ki"),
	("く", "kɯ"),
	("け", "ke"),
	("こ", "ko"),
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

G2P = (
    cdrewrite(cross("は", "ɰɑ"), "[BOS]", "[EOS]", SIGMA_STAR)
	@ cdrewrite(cross("じゃ", "dʑɑ"), "[BOS]", "", SIGMA_STAR)
    @ cdrewrite(cross("じゅ", "dʑɯ"), "[BOS]", "", SIGMA_STAR)
    @ cdrewrite(cross("じょ", "dʑo"), "[BOS]", "", SIGMA_STAR)
    @ cdrewrite(cross("ん", "ɴ"), "", "[EOS]", SIGMA_STAR)
    @ cdrewrite(cross("ん", "n"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("ざ", "dzɑ"), "[BOS]", "", SIGMA_STAR)
    @ cdrewrite(cross("じ", "dʑi"), "[BOS]", "", SIGMA_STAR)
    @ cdrewrite(cross("ず", "dzɯ"), "[BOS]", "", SIGMA_STAR)
    @ cdrewrite(cross("ぜ", "dze"), "[BOS]", "", SIGMA_STAR)
    @ cdrewrite(cross("ぞ", "dzo"), "[BOS]", "", SIGMA_STAR)
    @ cdrewrite(cross("ご", "go"), "", "", SIGMA_STAR)
    @ cdrewrite(string_map(context_free_map), "", "", SIGMA_STAR)
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
