"""Hiragana g2p rules."""

from pynini import accep, union, cdrewrite, cross, string_map
from pynini.lib import rewrite

monographs = union("あ","い","う","え","お",
				   "か","き","く","け","こ",
				   "さ","し","す","せ","そ",
				   "た","ち","つ","て","と",
				   "な","に","ぬ","ね","の",
				   "は","ひ","ふ","へ","ほ",
				   "ま","み","む","め","も",
				   "や",     "ゆ",     "よ",
				   "ら","り","る","れ","ろ",
				   "ら","り","る","れ","ろ",
				   "わ",               "を",
				   "ん")

graphemes = monographs.optimize()


monograph_phonemes = union("a",	"i", "ɯ", "e", "o",
				   		   "k", "s", "ɕ", "t", "n",
						   "ɲ", "h", "ç", "ɸ", "m",
				   		   "j", "ɾ", "ɰ", "ɴ", "ŋ",
						   "ɰ̃")

phonemes = monograph_phonemes.optimize()

SIGMA_STAR = union(graphemes, phonemes).closure().optimize()

G2P = (
    cdrewrite(cross("は", "ɰa"), "[BOS]", "[EOS]", SIGMA_STAR)
    @ cdrewrite(cross("あ", "a"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("い", "i"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("う", "ɯ"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("え", "e"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("お", "o"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("か", "ka"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("き", "ki"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("く", "kɯ"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("け", "ke"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("こ", "ko"), "", "", SIGMA_STAR)
	@ cdrewrite(cross("さ", "sa"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("し", "ɕi"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("す", "sɯ"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("せ", "se"), "", "", SIGMA_STAR)
    @ cdrewrite(cross("そ", "so"), "", "", SIGMA_STAR)
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
