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

	def test_ue(self) -> None:
		self.rewrites("うえ", "ɯe")

	def test_aku(self) -> None:
		self.rewrites("あく", "akɯ")

	def test_sushi(self) -> None:
		self.rewrites("すし", "sɯɕi")
	
	def test_tsuchi(self) -> None:
		self.rewrites("つち", "tsɯtɕi")

	def test_tanuki(self) -> None:
		self.rewrites("たぬき", "tanɯki")

	def test_hoshi(self) -> None:
		self.rewrites("ほし", "hoɕi")

	def test_hanami(self) -> None:
		self.rewrites("はなみ", "hanami")
	
	def test_yamato(self) -> None:
		self.rewrites("やまと", "jamato")

	def test_kore(self) -> None:
		self.rewrites("これ", "koɾe")

	def test_o(self) -> None:
		self.rewrites("を", "o")

	def test_wa(self) -> None:
		self.rewrites("は", "ɰa")
	
	def test_gohan(self) -> None:
		self.rewrites("ごはん", "gohaɴ")
	
	def test_futari(self) -> None:
		self.rewrites("ふたり", "ɸɯtaɾi")

	def test_zonjiru(self) -> None:
		self.rewrites("ぞんじる", "dzonʑiɾɯ")

	def test_gyoza(self) -> None:
		self.rewrites("ぎょざ", "ɡʲoza")

	def test_jojo(self) -> None:
		self.rewrites("じょじょ", "dʑoʑo")

	def test_shojo(self) -> None:
		self.rewrites("しょじょ", "ɕoʑo")

	def test_yakuza(self) -> None:
		self.rewrites("やくざ", "jakɯza")

	def test_jinja(self) -> None:
		self.rewrites("じんじゃ", "dʑinʑa")

	def test_kingyo(self) -> None:
		self.rewrites("きんぎょ", "kinɡʲo")

	def test_shirou(self) -> None:
		self.rewrites("しろう", "ɕiɾoɯ")

	def test_ii(self) -> None:
		self.rewrites("いい", "iː")

	'''
	def test_phonetic_db(self) -> None:
		_file = open('jpd.txt', 'r')
		for line in _file:
			kana, ipa = line.split("\t")
			self.rewrites(kana, ipa)
	'''

if __name__ == "__main__":
    unittest.main()


