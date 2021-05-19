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

vowels = union("あ","い","う","え","お")

monograph_phonemes = union("a",	"i", "ɯ", "e", "o",
				   		   "k", "s", "ɕ", "t", "n",
						   "ɲ", "h", "ç", "ɸ", "m",
				   		   "j", "ɾ", "ɰ", "ɴ", "ŋ",
						   "ɰ̃", "g", "ɡ", "p", "b",
						   "z", "ʑ", "d", "ʲ", "ː")

phonemes = monograph_phonemes.optimize()

SIGMA_STAR = union(graphemes, phonemes).closure().optimize()

G2P = (
    cdrewrite(cross("は", "ɰa"), "[BOS]", "[EOS]", SIGMA_STAR)
    @ cdrewrite(cross("きゃ", "kʲa"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("きゃ", "kʲu"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("きゃ", "kʲo"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("ぎゃ", "ɡʲa"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("ぎゅ", "ɡʲu"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("ぎょ", "ɡʲo"), "", "", SIGMA_STAR)
	@ cdrewrite(cross("しゃ", "ɕa"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("しゅ", "ɕɯ"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("しょ", "ɕo"), "", "", SIGMA_STAR)
	@ cdrewrite(cross("じゃ", "dʑa"), "[BOS]", "", SIGMA_STAR)
    @ cdrewrite(cross("じゅ", "dʑɯ"), "[BOS]", "", SIGMA_STAR)
    @ cdrewrite(cross("じょ", "dʑo"), "[BOS]", "", SIGMA_STAR)
	@ cdrewrite(cross("じゃ", "ʑa"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("じゅ", "ʑɯ"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("じょ", "ʑo"), "", "", SIGMA_STAR)
	@ cdrewrite(cross("ちゃ", "tɕa"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("ちゅ", "tɕɯ"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("ちょ", "tɕo"), "", "", SIGMA_STAR)
	@ cdrewrite(cross("にゃ", "ɲa"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("にゅ", "ɲɯ"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("にょ", "ɲo"), "", "", SIGMA_STAR)
	@ cdrewrite(cross("ひゃ", "ça"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("ひゅ", "çɯ"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("ひょ", "ço"), "", "", SIGMA_STAR)
	@ cdrewrite(cross("みゃ", "mʲa"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("みゅ", "mʲɯ"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("みょ", "mʲo"), "", "", SIGMA_STAR)
	@ cdrewrite(cross("りゃ", "ɾʲa"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("りゅ", "ɾʲɯ"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("りょ", "ɾʲo"), "", "", SIGMA_STAR)
	@ cdrewrite(cross("びゃ", "bʲa"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("びゅ", "bʲɯ"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("びょ", "bʲo"), "", "", SIGMA_STAR)
	@ cdrewrite(cross("ぴゃ", "pʲa"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("ぴゅ", "pʲɯ"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("びょ", "pʲo"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("ん", "ɴ"), "", "[EOS]", SIGMA_STAR)
    @ cdrewrite(cross("ん", "n"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("ざ", "dza"), "[BOS]", "", SIGMA_STAR)
    @ cdrewrite(cross("じ", "dʑi"), "[BOS]", "", SIGMA_STAR)
    @ cdrewrite(cross("ず", "dzɯ"), "[BOS]", "", SIGMA_STAR)
    @ cdrewrite(cross("ぜ", "dze"), "[BOS]", "", SIGMA_STAR)
    @ cdrewrite(cross("ぞ", "dzo"), "[BOS]", "", SIGMA_STAR)
	@ cdrewrite(cross("か", "ka"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("き", "ki"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("く", "kɯ"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("け", "ke"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("こ", "ko"), "", "", SIGMA_STAR)
	@ cdrewrite(cross("が", "ga"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("ぎ", "gi"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("ぐ", "gɯ"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("げ", "ge"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("ご", "go"), "", "", SIGMA_STAR)
	@ cdrewrite(cross("さ", "sa"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("し", "ɕi"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("す", "sɯ"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("せ", "se"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("そ", "so"), "", "", SIGMA_STAR)
	@ cdrewrite(cross("ざ", "za"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("じ", "ʑi"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("ず", "zɯ"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("ぜ", "ze"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("ぞ", "zo"), "", "", SIGMA_STAR)
	@ cdrewrite(cross("た", "ta"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("ち", "tɕi"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("つ", "tsɯ"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("て", "te"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("と", "to"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("な", "na"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("に", "ɲi"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("ぬ", "nɯ"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("ね", "ne"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("の", "no"), "", "", SIGMA_STAR)
	@ cdrewrite(cross("は", "ha"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("ひ", "çi"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("ふ", "ɸɯ"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("へ", "he"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("ほ", "ho"), "", "", SIGMA_STAR)
	@ cdrewrite(cross("ま", "ma"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("み", "mi"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("む", "mɯ"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("め", "me"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("も", "mo"), "", "", SIGMA_STAR)
	@ cdrewrite(cross("や", "ja"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("ゆ", "jɯ"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("よ", "jo"), "", "", SIGMA_STAR)
	@ cdrewrite(cross("ら", "ɾa"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("り", "ɾi"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("る", "ɾɯ"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("れ", "ɾe"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("ろ", "ɾo"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("わ", "ɰa"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("を", "o"), "", "", SIGMA_STAR)
	@ cdrewrite(cross("あ", "ː"), union("あ","a"), "", SIGMA_STAR)
    @ cdrewrite(cross("い", "ː"), union("い","i"), "", SIGMA_STAR)
    @ cdrewrite(cross("う", "ː"), union("う","ɯ"), "", SIGMA_STAR)
    @ cdrewrite(cross("え", "ː"), union("え","e"), "", SIGMA_STAR)
    @ cdrewrite(cross("お", "ː"), union("お","o"), "", SIGMA_STAR)
	@ cdrewrite(cross("あ", "a"), "", "", SIGMA_STAR)
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
