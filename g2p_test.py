#!/usr/bin/env python
"""Unit tests for Hiragana G2P."""

import unittest
import g2p


class G2PTest(unittest.TestCase):
    def rewrites(self, istring: str, expected_ostring: str) -> None:
        """Asserts that the g2p rule produces the correct output.

        Note that this itself is not a unit test because its name does not
        begin with `test_`; but it can be used to implement other unit tests.

        Args:
            istring: the input string
            expected_ostring: the expected output string.
        """
        ostring = g2p.g2p(istring)
        self.assertEqual(ostring, expected_ostring)

    def test_げんじてん(self) -> None:
        self.rewrites("げんじてん", "ɡẽɴʑitẽɴ")

    def test_じか(self) -> None:
        self.rewrites("じか", "dʑikɑ")

    def test_げんか(self) -> None:
        self.rewrites("げんか", "ɡẽɴkɑ")

    def test_とうせい(self) -> None:
        self.rewrites("とうせい", "toːseː")

    def test_とうせつ(self) -> None:
        self.rewrites("とうせつ", "toːsetsɯ̥")

    def test_きょうび(self) -> None:
        self.rewrites("きょうび", "kjoːbi")

    def test_とうだい(self) -> None:
        self.rewrites("とうだい", "toːdɑi")

    def test_げんせ(self) -> None:
        self.rewrites("げんせ", "ɡẽɴse")

    def test_げんせい(self) -> None:
        self.rewrites("げんせい", "ɡẽɴseː")

    def test_こんじょう(self) -> None:
        self.rewrites("こんじょう", "kõɴʑoː")

    def test_そっこん(self) -> None:
        self.rewrites("そっこん", "sokkõɴ")

    def test_きょうあす(self) -> None:
        self.rewrites("きょうあす", "kjoːɑsɯ̥")

    def test_ことし(self) -> None:
        self.rewrites("ことし", "kotoɕi")

    def test_こんねん(self) -> None:
        self.rewrites("こんねん", "kõɴnẽɴ")

    def test_こんじ(self) -> None:
        self.rewrites("こんじ", "kõɴʑi")

    def test_ほんねん(self) -> None:
        self.rewrites("ほんねん", "hõɴnẽɴ")

    def test_とうねん(self) -> None:
        self.rewrites("とうねん", "toːnẽɴ")

    def test_こんき(self) -> None:
        self.rewrites("こんき", "kõɴki̥")

    def test_こんしいずん(self) -> None:
        self.rewrites("こんしいずん", "kõɴɕiːzɯ̃ɴ")

    def test_こんしゅん(self) -> None:
        self.rewrites("こんしゅん", "kõɴɕɯ̃ɴ")

    def test_こんげつ(self) -> None:
        self.rewrites("こんげつ", "kõɴŋetsɯ̥")

    def test_ほんげつ(self) -> None:
        self.rewrites("ほんげつ", "hõɴŋetsɯ̥")

    def test_とうげつ(self) -> None:
        self.rewrites("とうげつ", "toːŋetsɯ̥")

    def test_こんしゅう(self) -> None:
        self.rewrites("こんしゅう", "kõɴɕɯː")

    def test_きょう(self) -> None:
        self.rewrites("きょう", "kjoː")

    def test_こんにち(self) -> None:
        self.rewrites("こんにち", "kõɴnʲitɕi̥")

    def test_ほんじつ(self) -> None:
        self.rewrites("ほんじつ", "hõɴʑitsɯ̥")

    def test_けさ(self) -> None:
        self.rewrites("けさ", "kesɑ")

    def test_こんぎょう(self) -> None:
        self.rewrites("こんぎょう", "kõɴŋjoː")

    def test_こんばん(self) -> None:
        self.rewrites("こんばん", "kõmbãɴ")

    def test_こんせき(self) -> None:
        self.rewrites("こんせき", "kõɴseki̥")

    def test_こんゆう(self) -> None:
        self.rewrites("こんゆう", "kõɴyɯː")

    def test_こよい(self) -> None:
        self.rewrites("こよい", "koyoi")

    def test_こんや(self) -> None:
        self.rewrites("こんや", "kõɴyɑ")

    def test_こんど(self) -> None:
        self.rewrites("こんど", "kõɴdo")

    def test_こんぱん(self) -> None:
        self.rewrites("こんぱん", "kõɴpãɴ")

    def test_こんかい(self) -> None:
        self.rewrites("こんかい", "kõɴkɑi")

    def test_こんじ(self) -> None:
        self.rewrites("こんじ", "kõɴʑi")

    def test_このたび(self) -> None:
        self.rewrites("このたび", "konotɑbi")

    def test_とうめん(self) -> None:
        self.rewrites("とうめん", "toːmẽɴ")

    def test_とうざ(self) -> None:
        self.rewrites("とうざ", "toːzɑ")

    def test_ここ(self) -> None:
        self.rewrites("ここ", "koko")

    def test_かこ(self) -> None:
        self.rewrites("かこ", "kɑko")

    def test_きおう(self) -> None:
        self.rewrites("きおう", "kioː")

    def test_むかし(self) -> None:
        self.rewrites("むかし", "mɯkɑɕi")

    def test_そのむかし(self) -> None:
        self.rewrites("そのむかし", "sonomɯkɑɕi")

    def test_むかしむかし(self) -> None:
        self.rewrites("むかしむかし", "mɯkɑɕimɯkɑɕi")

    def test_おおむかし(self) -> None:
        self.rewrites("おおむかし", "oːmɯkɑɕi̥")

    def test_ひとむかし(self) -> None:
        self.rewrites("ひとむかし", "çi̥tomɯkɑɕi̥")

    def test_せきねん(self) -> None:
        self.rewrites("せきねん", "sekinẽɴ")

    def test_せきじつ(self) -> None:
        self.rewrites("せきじつ", "sekiʑitsɯ̥")

    def test_せきじ(self) -> None:
        self.rewrites("せきじ", "sekiʑi")

    def test_おうせき(self) -> None:
        self.rewrites("おうせき", "oːseki")

    def test_そのかみ(self) -> None:
        self.rewrites("そのかみ", "sonokɑmi")

    def test_いにしえ(self) -> None:
        self.rewrites("いにしえ", "inʲiɕie")

    def test_おうこ(self) -> None:
        self.rewrites("おうこ", "oːko")

    def test_おうじ(self) -> None:
        self.rewrites("おうじ", "oːʑi")

    def test_こしかた(self) -> None:
        self.rewrites("こしかた", "koɕi̥kɑtɑ")

    def test_きしかた(self) -> None:
        self.rewrites("きしかた", "ki̥ɕi̥kɑtɑ")

    def test_おうねん(self) -> None:
        self.rewrites("おうねん", "oːnẽɴ")

    def test_とうねん(self) -> None:
        self.rewrites("とうねん", "toːnẽɴ")

    def test_せんねん(self) -> None:
        self.rewrites("せんねん", "sẽɴnẽɴ")

    def test_ひところ(self) -> None:
        self.rewrites("ひところ", "çi̥tokoɾo")

    def test_ひときり(self) -> None:
        self.rewrites("ひときり", "çi̥tokiɾi")

    def test_ぜんせ(self) -> None:
        self.rewrites("ぜんせ", "zẽɴse")

    def test_ぜんせい(self) -> None:
        self.rewrites("ぜんせい", "zẽɴseː")

    def test_しゅくせ(self) -> None:
        self.rewrites("しゅくせ", "ɕɯ̥kɯse")

    def test_すくせ(self) -> None:
        self.rewrites("すくせ", "sɯ̥kɯse")

    def test_ありしひ(self) -> None:
        self.rewrites("ありしひ", "ɑɾiɕi̥çi")

    def test_もと(self) -> None:
        self.rewrites("もと", "moto")

    def test_きゅう(self) -> None:
        self.rewrites("きゅう", "kjɯː")

    def test_せん(self) -> None:
        self.rewrites("せん", "sẽɴ")

    def test_いましがた(self) -> None:
        self.rewrites("いましがた", "imɑɕiŋɑtɑ")

    def test_せんこく(self) -> None:
        self.rewrites("せんこく", "sẽɴkokɯ̥")

    def test_さいぜん(self) -> None:
        self.rewrites("さいぜん", "sɑizẽɴ")

    def test_さき(self) -> None:
        self.rewrites("さき", "sɑki")

    def test_さっき(self) -> None:
        self.rewrites("さっき", "sɑk̚ki̥")

    def test_さきほど(self) -> None:
        self.rewrites("さきほど", "sɑki̥hodo")

    def test_このまえ(self) -> None:
        self.rewrites("このまえ", "konomɑe")

    def test_このあいだ(self) -> None:
        self.rewrites("このあいだ", "konoɑidɑ")

    def test_こないだ(self) -> None:
        self.rewrites("こないだ", "konɑidɑ")

    def test_せんだって(self) -> None:
        self.rewrites("せんだって", "sẽɴdɑt̚te")

    def test_せんじつ(self) -> None:
        self.rewrites("せんじつ", "sẽɴʑitsɯ̥")

    def test_かじつ(self) -> None:
        self.rewrites("かじつ", "kɑʑitsɯ̥")

    def test_きのうきょう(self) -> None:
        self.rewrites("きのうきょう", "kinoːkjoː")

    def test_さきごろ(self) -> None:
        self.rewrites("さきごろ", "sɑkiŋoɾo")

    def test_せんぱん(self) -> None:
        self.rewrites("せんぱん", "sẽɴpãɴ")

    def test_せんど(self) -> None:
        self.rewrites("せんど", "sẽɴdo")

    def test_かはん(self) -> None:
        self.rewrites("かはん", "kɑhãɴ")

    def test_いつぞや(self) -> None:
        self.rewrites("いつぞや", "itsɯzoyɑ")

    def test_さっこん(self) -> None:
        self.rewrites("さっこん", "sɑkkõɴ")

    def test_さいきん(self) -> None:
        self.rewrites("さいきん", "sɑikĩɴ")

    def test_ちょっきん(self) -> None:
        self.rewrites("ちょっきん", "tɕok̚kĩɴ")

    def test_ちかごろ(self) -> None:
        self.rewrites("ちかごろ", "tɕi̥kɑŋoɾo")

    def test_このほど(self) -> None:
        self.rewrites("このほど", "konohodo")

    def test_きんねん(self) -> None:
        self.rewrites("きんねん", "kĩɴnẽɴ")

    def test_きんらい(self) -> None:
        self.rewrites("きんらい", "kĩɴɾɑi")

    def test_きんじ(self) -> None:
        self.rewrites("きんじ", "kĩɴʑi")

    def test_きょねん(self) -> None:
        self.rewrites("きょねん", "kjonẽɴ")

    def test_さくねん(self) -> None:
        self.rewrites("さくねん", "sɑkɯnẽɴ")

    def test_かくねん(self) -> None:
        self.rewrites("かくねん", "kɑkɯnẽɴ")

    def test_きゅうねん(self) -> None:
        self.rewrites("きゅうねん", "kjɯːnẽɴ")

    def test_こぞ(self) -> None:
        self.rewrites("こぞ", "kozo")

    def test_おととし(self) -> None:
        self.rewrites("おととし", "ototoɕi̥")

    def test_いっさくねん(self) -> None:
        self.rewrites("いっさくねん", "issakɯnẽɴ")

    def test_さきおととし(self) -> None:
        self.rewrites("さきおととし", "sɑkiototoɕi̥")

    def test_いっさくさくねん(self) -> None:
        self.rewrites("いっさくさくねん", "issakɯ̥sɑkɯnẽɴ")

    def test_せんげつ(self) -> None:
        self.rewrites("せんげつ", "sẽɴŋetsɯ̥")

    def test_せんせんげつ(self) -> None:
        self.rewrites("せんせんげつ", "sẽɴsẽɴŋetsɯ̥")

    def test_きゅうろう(self) -> None:
        self.rewrites("きゅうろう", "kjɯːɾoː")

    def test_きゅうとう(self) -> None:
        self.rewrites("きゅうとう", "kjɯːtoː")

    def test_せんしゅう(self) -> None:
        self.rewrites("せんしゅう", "sẽɴɕɯː")

    def test_せんせんしゅう(self) -> None:
        self.rewrites("せんせんしゅう", "sẽɴsẽɴɕɯː")

    def test_きのう(self) -> None:
        self.rewrites("きのう", "kinoː")

    def test_さくじつ(self) -> None:
        self.rewrites("さくじつ", "sɑkɯʑitsɯ̥")

    def test_いえすたでえ(self) -> None:
        self.rewrites("いえすたでえ", "iesɯ̥tɑdeː")

    def test_きぞ(self) -> None:
        self.rewrites("きぞ", "kizo")

    def test_おととい(self) -> None:
        self.rewrites("おととい", "ototoi")

    def test_いっさくじつ(self) -> None:
        self.rewrites("いっさくじつ", "issakɯʑitsɯ̥")

    def test_さきおととい(self) -> None:
        self.rewrites("さきおととい", "sɑkiototoi")

    def test_せんせんじつ(self) -> None:
        self.rewrites("せんせんじつ", "sẽɴsẽɴʑitsɯ̥")

    def test_いっさくさくじつ(self) -> None:
        self.rewrites("いっさくさくじつ", "issakɯ̥sɑkɯʑitsɯ̥")

    def test_ゆうべ(self) -> None:
        self.rewrites("ゆうべ", "yɯːbe")

    def test_さくばん(self) -> None:
        self.rewrites("さくばん", "sɑkɯbãɴ")

    def test_さくゆう(self) -> None:
        self.rewrites("さくゆう", "sɑkɯyɯː")

    def test_さくや(self) -> None:
        self.rewrites("さくや", "sɑkɯyɑ")

    def test_やぜん(self) -> None:
        self.rewrites("やぜん", "yɑzẽɴ")

    def test_いっさくばん(self) -> None:
        self.rewrites("いっさくばん", "issakɯbãɴ")

    def test_せんばん(self) -> None:
        self.rewrites("せんばん", "sẽɴbãɴ")

    def test_せんや(self) -> None:
        self.rewrites("せんや", "sẽɴyɑ")

    def test_やらい(self) -> None:
        self.rewrites("やらい", "yɑɾɑi")

    def test_これまで(self) -> None:
        self.rewrites("これまで", "koɾemɑde")

    def test_じゅうらい(self) -> None:
        self.rewrites("じゅうらい", "dʑɯːɾɑi")

    def test_じゅうぜん(self) -> None:
        self.rewrites("じゅうぜん", "dʑɯːzẽɴ")

    def test_きゅうらい(self) -> None:
        self.rewrites("きゅうらい", "kjɯːɾɑi")

    def test_ざいらい(self) -> None:
        self.rewrites("ざいらい", "zɑiɾɑi")

    def test_ねんらい(self) -> None:
        self.rewrites("ねんらい", "nẽɴɾɑi")

    def test_こらい(self) -> None:
        self.rewrites("こらい", "koɾɑi")

    def test_えいねん(self) -> None:
        self.rewrites("えいねん", "eːnẽɴ")

    def test_ながねん(self) -> None:
        self.rewrites("ながねん", "nɑŋɑnẽɴ")

    def test_ながねん(self) -> None:
        self.rewrites("ながねん", "nɑŋɑnẽɴ")

    def test_たねん(self) -> None:
        self.rewrites("たねん", "tɑnẽɴ")

    def test_いぜん(self) -> None:
        self.rewrites("いぜん", "izẽɴ")

    def test_とう(self) -> None:
        self.rewrites("とう", "toː")

    def test_とっく(self) -> None:
        self.rewrites("とっく", "tokkɯ")

    def test_とうのむかし(self) -> None:
        self.rewrites("とうのむかし", "toːnomɯkɑɕi̥")

    def test_とっくのむかし(self) -> None:
        self.rewrites("とっくのむかし", "tokkɯnomɯkɑɕi̥")

    def test_しょうらい(self) -> None:
        self.rewrites("しょうらい", "ɕoːɾɑi")

    def test_みらい(self) -> None:
        self.rewrites("みらい", "miɾɑi")

    def test_みぜん(self) -> None:
        self.rewrites("みぜん", "mizẽɴ")

    def test_こんご(self) -> None:
        self.rewrites("こんご", "kõɴŋo")

    def test_こうご(self) -> None:
        self.rewrites("こうご", "koːŋo")

    def test_これから(self) -> None:
        self.rewrites("これから", "koɾekɑɾɑ")

    def test_このあと(self) -> None:
        self.rewrites("このあと", "konoɑto")

    def test_さき(self) -> None:
        self.rewrites("さき", "sɑki")

    def test_さきざき(self) -> None:
        self.rewrites("さきざき", "sɑkizɑki̥")

    def test_ゆくゆく(self) -> None:
        self.rewrites("ゆくゆく", "yɯkɯyɯkɯ")

    def test_あとあと(self) -> None:
        self.rewrites("あとあと", "ɑtoɑto")

    def test_のちのち(self) -> None:
        self.rewrites("のちのち", "notɕinotɕi")

    def test_さきゆき(self) -> None:
        self.rewrites("さきゆき", "sɑkiyɯki")

    def test_ゆくすえ(self) -> None:
        self.rewrites("ゆくすえ", "yɯkɯ̥sɯe")

    def test_ぜんと(self) -> None:
        self.rewrites("ぜんと", "zẽɴto")

    def test_いっすんさき(self) -> None:
        self.rewrites("いっすんさき", "issɯ̃ɴsɑki̥")

    def test_おいさき(self) -> None:
        self.rewrites("おいさき", "oisɑki")

    def test_おいさき(self) -> None:
        self.rewrites("おいさき", "oisɑki")

    def test_らいせ(self) -> None:
        self.rewrites("らいせ", "ɾɑise")

    def test_こうせい(self) -> None:
        self.rewrites("こうせい", "koːseː")

    def test_ごしょう(self) -> None:
        self.rewrites("ごしょう", "ɡoɕoː")

    def test_こうだい(self) -> None:
        self.rewrites("こうだい", "koːdɑi")

    def test_のちのよ(self) -> None:
        self.rewrites("のちのよ", "notɕinoyo")

    def test_いご(self) -> None:
        self.rewrites("いご", "iŋo")

    def test_すえ(self) -> None:
        self.rewrites("すえ", "sɯe")

    def test_のち(self) -> None:
        self.rewrites("のち", "notɕi")

    def test_むこう(self) -> None:
        self.rewrites("むこう", "mɯkoː")

    def test_ゆくえ(self) -> None:
        self.rewrites("ゆくえ", "yɯkɯe")

    def test_ゆくさき(self) -> None:
        self.rewrites("ゆくさき", "yɯkɯ̥sɑki")

    def test_いくさき(self) -> None:
        self.rewrites("いくさき", "ikɯ̥sɑki")

    def test_ごこく(self) -> None:
        self.rewrites("ごこく", "ɡokokɯ̥")

    def test_きんじつ(self) -> None:
        self.rewrites("きんじつ", "kĩɴʑitsɯ̥")

    def test_ごじつ(self) -> None:
        self.rewrites("ごじつ", "ɡoʑitsɯ̥")

    def test_こうねん(self) -> None:
        self.rewrites("こうねん", "koːnẽɴ")

    def test_そうばん(self) -> None:
        self.rewrites("そうばん", "soːbãɴ")

    def test_たじつ(self) -> None:
        self.rewrites("たじつ", "tɑʑitsɯ̥")

    def test_たねん(self) -> None:
        self.rewrites("たねん", "tɑnẽɴ")

    def test_やがて(self) -> None:
        self.rewrites("やがて", "yɑŋɑte")

    def test_もくしょうのかん(self) -> None:
        self.rewrites("もくしょうのかん", "mokɯ̥ɕoːnokãɴ")

    def test_もくぜん(self) -> None:
        self.rewrites("もくぜん", "mokɯzẽɴ")

    def test_まぢか(self) -> None:
        self.rewrites("まぢか", "mɑʑikɑ")

    def test_みょうねん(self) -> None:
        self.rewrites("みょうねん", "mjoːnẽɴ")

    def test_らいねん(self) -> None:
        self.rewrites("らいねん", "ɾɑinẽɴ")

    def test_みょうしゅん(self) -> None:
        self.rewrites("みょうしゅん", "mjoːɕɯ̃ɴ")

    def test_らいしゅん(self) -> None:
        self.rewrites("らいしゅん", "ɾɑiɕɯ̃ɴ")

    def test_らいはる(self) -> None:
        self.rewrites("らいはる", "ɾɑihɑɾɯ")

    def test_さらいねん(self) -> None:
        self.rewrites("さらいねん", "sɑɾɑinẽɴ")

    def test_みょうごねん(self) -> None:
        self.rewrites("みょうごねん", "mjoːŋonẽɴ")

    def test_らいがくねん(self) -> None:
        self.rewrites("らいがくねん", "ɾɑiŋɑkɯnẽɴ")

    def test_らいがっき(self) -> None:
        self.rewrites("らいがっき", "ɾɑiŋɑk̚ki̥")

    def test_らいき(self) -> None:
        self.rewrites("らいき", "ɾɑiki̥")


if __name__ == "__main__":
    log_file = "test_log.txt"
    with open(log_file, "w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)
